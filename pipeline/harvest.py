"""Stage 1 of harvest: the deterministic sweep. Finds candidates. Reads nothing.

WHAT THIS DOES NOT DO, deliberately: it never writes a source record to corpus/papers/.

A source record carries `reported` (what the source says in its own terms), `method_summary`,
`limitations`, and `access` - what we ACTUALLY read. None of those can be produced by a script.
A script that filled them in would be fabricating, and one that wrote `access: full_text` without
anything having read the text would bake a falsehood into an immutable artifact. So this stage
writes CANDIDATES: metadata, verified OA location, and nothing about content. Turning a candidate
into a source record requires reading it, which is the `harvest` skill's job.

This split is what makes the sweep safe to automate on a schedule.

Venue scope:
  specialist  - semiconductor-dedicated; every article is in scope
  broad       - multidisciplinary; a topic filter is applied (Nature Communications publishes
                ~200 papers a week, of which ~13 are on-topic)
Default is broad. Missing a few papers from a specialist venue is recoverable; flooding the
corpus with off-topic material is not.

Usage:
    python pipeline/harvest.py [--days 3] [--limit-per-venue 25] [--dry-run]
"""

import argparse
from collections import Counter
import json
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta
from pathlib import Path

import requests
import yaml

# Paper titles carry typographic characters (U+2010 hyphen, en dashes, Greek letters) that the
# default Windows console codec cannot encode, which crashed a local --dry-run. The daily job
# runs on Linux, but a human running this on Windows is exactly who needs the dry run to work.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "sources" / "registry.yaml"
CANDIDATES = ROOT / "corpus" / "candidates"
PAPERS = ROOT / "corpus" / "papers"

UA = {"User-Agent": "ProjectElectron/0.1 (semiconductor research agent; harvest)"}
TIMEOUT = 40
PAUSE = 0.2

# Broad venues are gated by sources/topics.yaml - a verified allowlist of OpenAlex topic IDs.
# Keyword matching was removed: OpenAlex's own topic search returns "Memory and Neural
# Mechanisms" for "memory" and "Meat and Animal Product Quality" for "packaging", and no keyword
# list can separate those from DRAM and flip-chip packaging. Structured topic ids can, because
# the work has already been classified. Specialist venues skip this filter entirely.
TOPICS_FILE = ROOT / "sources" / "topics.yaml"


def load_topic_allowlist(path=TOPICS_FILE):
    """Return (all_ids_to_query, relevance_by_id).

    Core and adjacent are queried together - both are harvested. The tier is stamped on each
    candidate as `relevance`, so adjacency is visible to the reading stage rather than being
    silently decided here.
    """
    doc = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    core = [e["id"] for e in doc.get("allow", [])]
    adjacent = [e["id"] for e in doc.get("adjacent", [])]
    if not core:
        raise ValueError("topic core list is empty - refusing to sweep broad venues unfiltered")
    relevance = {i: "core" for i in core}
    relevance.update({i: "adjacent" for i in adjacent})
    return core + adjacent, relevance


# OpenAlex primary_topic.field -> our topic codes. Advisory only: the reading stage assigns the
# real code. Recorded so a human can triage without re-deriving it.
FIELD_HINT = {
    "Materials Science": "MAT",
    "Physics and Astronomy": "MAT",
    "Engineering": "DEV",
    "Computer Science": "ARCH",
    "Chemistry": "MAT",
    "Economics, Econometrics and Finance": "ECON",
}

ARXIV_TOPIC = {
    "cond-mat.mtrl-sci": "MAT", "cond-mat.mes-hall": "MAT", "physics.app-ph": "DEV",
    "physics.optics": "PHOT", "cs.AR": "ARCH", "cs.ET": "DEV", "eess.SP": "ARCH",
}


def load_registry():
    return yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))


def harvestable_journals(reg):
    """Venues we may legitimately read from, per CLAUDE.md's three verification states."""
    out = []
    for section in ("journals_full_oa", "journals_hybrid"):
        for e in reg.get(section, []) or []:
            if e.get("verified") is False or not e.get("issn"):
                continue
            out.append({
                "id": e["id"], "name": e["name"], "issn": e["issn"],
                "verified": e.get("verified"), "oa_status": e.get("oa_status"),
                "grade_default": e.get("grade_default", "A"),
                "scope": e.get("scope", "broad"),
                "topics": e.get("topics", []),
            })
    return out


def existing_ids():
    """Everything already seen, so a re-run is idempotent."""
    seen = set()
    for d in (PAPERS, CANDIDATES):
        for p in d.glob("*.yaml") if d.exists() else []:
            try:
                doc = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
            except yaml.YAMLError:
                continue
            for key in ("doi", "arxiv_id", "openalex_id"):
                if doc.get(key):
                    seen.add(str(doc[key]).lower())
    return seen


def get(url, attempts=4):
    """Fetch with backoff. Returns (response, error). NEVER conflates a rate-limit with a
    genuine empty result - an earlier version returned None for both, so a throttled venue
    dropped silently out of the sweep and the run still reported success. For a daily job that
    is the worst kind of bug: silent partial coverage that looks like a quiet news day.
    """
    delay = 1.0
    last = None
    for attempt in range(attempts):
        try:
            r = requests.get(url, headers=UA, timeout=TIMEOUT)
            if r.status_code == 200:
                return r, None
            last = f"HTTP {r.status_code}"
            if r.status_code in (429, 500, 502, 503, 504):
                time.sleep(delay)
                delay *= 2
                continue
            return None, last          # 4xx other than 429 will not improve on retry
        except requests.RequestException as e:
            last = f"{type(e).__name__}"
            time.sleep(delay)
            delay *= 2
    return None, f"{last} after {attempts} attempts"


def _work_to_candidate(w, venue):
    oa = w.get("open_access") or {}
    best = w.get("best_oa_location") or {}
    doi = (w.get("doi") or "").replace("https://doi.org/", "") or None
    authors = [{
        "name": (a.get("author") or {}).get("display_name"),
        "openalex_author_id": (a.get("author") or {}).get("id"),
        "affiliation": (a.get("raw_affiliation_strings") or [None])[0],
        "corresponding": bool(a.get("is_corresponding")),
    } for a in (w.get("authorships") or [])]
    pt = w.get("primary_topic") or {}
    field = (pt.get("field") or {}).get("display_name")
    return {
        "source": "openalex",
        "openalex_id": w.get("id"),
        "doi": doi,
        "title": w.get("title"),
        "venue_id": venue["id"],
        "venue_name": venue["name"],
        "published_date": w.get("publication_date"),
        "authors": authors,
        "is_oa": bool(oa.get("is_oa")),
        "oa_status": oa.get("oa_status"),
        "oa_location": {
            "host": ((best.get("source") or {}).get("display_name")),
            "version": best.get("version"),
            "license": best.get("license"),
            "url": best.get("pdf_url") or best.get("landing_page_url"),
        } if best else None,
        "grade_default": venue["grade_default"],
        "topic_hint": FIELD_HINT.get(field) or (venue["topics"] or ["MAT"])[0],
        "primary_topic": pt.get("display_name"),
        "primary_topic_id": (pt.get("id") or "").rsplit("/", 1)[-1] or None,
    }


def sweep_batched(venues, since, topic_ids, relevance=None, chunk=30, per_page=200,
                  max_pages=5, rate_floor=50):
    """Sweep many venues in a FEW requests instead of one request per venue.

    OpenAlex accepts `issn:A|B|C` as OR, so 75 per-venue calls collapse to a handful. This is
    the structural fix for rate limiting: backoff copes with being throttled, batching avoids
    being throttled at all. OpenAlex also reports the remaining budget in response headers, so
    we read it rather than guess - and stop cleanly while the budget is still positive instead
    of hammering until it refuses.

    `topic_ids` gates broad venues by primary_topic; pass None for specialist venues.
    """
    by_issn = {v["issn"]: v for v in venues}
    items, errors, rate = [], [], {}
    issns = list(by_issn)

    for i in range(0, len(issns), chunk):
        group = issns[i:i + chunk]
        filters = ["primary_location.source.issn:" + "|".join(group),
                   f"from_publication_date:{since}"]
        if topic_ids:
            filters.append("primary_topic.id:" + "|".join(topic_ids))
        cursor = "*"
        for _ in range(max_pages):
            url = ("https://api.openalex.org/works?filter=" + ",".join(filters)
                   + f"&per-page={per_page}&cursor={urllib.parse.quote(cursor)}")
            r, err = get(url)
            time.sleep(PAUSE)
            if r is None:
                errors.append(f"issn-batch[{i // chunk}]: {err}")
                break
            remaining = r.headers.get("X-RateLimit-Remaining")
            if remaining is not None:
                try:
                    rate["remaining"] = int(remaining)
                    rate["limit"] = int(r.headers.get("X-RateLimit-Limit", 0)) or None
                except ValueError:
                    pass
            payload = r.json()
            for w in payload.get("results", []):
                src = (w.get("primary_location") or {}).get("source") or {}
                candidate_issns = [s for s in (src.get("issn") or []) if s]
                if src.get("issn_l"):
                    candidate_issns.append(src["issn_l"])
                venue = next((by_issn[s] for s in candidate_issns if s in by_issn), None)
                if venue is None:
                    # Filtered by our own ISSN list, so this should not happen. Record rather
                    # than silently drop - an unattributable work means the mapping is wrong.
                    errors.append(f"unmappable work {w.get('id')} issns={candidate_issns}")
                    continue
                cand = _work_to_candidate(w, venue)
                cand["relevance"] = (relevance.get(cand.get("primary_topic_id"), "core")
                                     if relevance else "core")
                items.append(cand)
            cursor = (payload.get("meta") or {}).get("next_cursor")
            if not cursor or not payload.get("results"):
                break
        if rate.get("remaining") is not None and rate["remaining"] < rate_floor:
            errors.append(f"stopped early: rate budget low "
                          f"({rate['remaining']}/{rate.get('limit')} remaining)")
            break
    return items, errors, rate


def sweep_arxiv(categories, since, limit):
    """arXiv preprints. Always grade B, always OA by construction."""
    cat_q = "+OR+".join(f"cat:{c}" for c in categories)
    url = ("http://export.arxiv.org/api/query?search_query=" + cat_q
           + f"&start=0&max_results={limit}&sortBy=submittedDate&sortOrder=descending")
    r, err = get(url)
    time.sleep(1.0)  # arXiv asks for a slower cadence than the journals APIs
    if r is None:
        return None, err

    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(r.content)
    out = []
    for entry in root.findall("a:entry", ns):
        published = (entry.findtext("a:published", default="", namespaces=ns) or "")[:10]
        if published and published < since:
            continue
        aid = (entry.findtext("a:id", default="", namespaces=ns) or "").rsplit("/", 1)[-1]
        cats = [c.get("term") for c in entry.findall("a:category", ns)]
        primary = next((c for c in cats if c in ARXIV_TOPIC), None)
        out.append({
            "source": "arxiv",
            "arxiv_id": aid,
            "doi": (entry.findtext("a:doi", default="", namespaces=ns) or None),
            "title": " ".join((entry.findtext("a:title", default="", namespaces=ns) or "").split()),
            "venue_id": "arxiv_api",
            "venue_name": "arXiv",
            "published_date": published,
            "authors": [{"name": a.findtext("a:name", default="", namespaces=ns)}
                        for a in entry.findall("a:author", ns)],
            "is_oa": True,
            "oa_status": "green",
            "oa_location": {"host": "arXiv", "version": "submittedVersion",
                            "license": None,
                            "url": f"https://arxiv.org/abs/{aid}"},
            "grade_default": "B",
            "topic_hint": ARXIV_TOPIC.get(primary, "MAT"),
            "primary_topic": primary,
        })
    return out, None


def next_candidate_seq():
    """Continue today's numbering rather than restarting at 1.

    An earlier version numbered from 1 on every run, so a manual dispatch followed by the
    scheduled run on the same day wrote CAND-<today>-0001 twice and silently overwrote the first
    run's candidate with a different paper. Numbering now continues from the highest existing
    file for today, so every candidate filename is unique across runs.
    """
    prefix = f"CAND-{date.today():%Y%m%d}-"
    highest = 0
    for p in CANDIDATES.glob(f"{prefix}*.yaml"):
        try:
            highest = max(highest, int(p.stem[len(prefix):]))
        except ValueError:
            continue
    return highest + 1


def write_candidate(cand, seq):
    """Write a candidate. Explicitly NOT a source record - see module docstring."""
    cid = f"CAND-{date.today():%Y%m%d}-{seq:04d}"
    path = CANDIDATES / f"{cid}.yaml"
    if path.exists():
        # Refuse rather than overwrite. Reaching this means the numbering logic is broken, and
        # clobbering a candidate would lose a paper without any trace.
        raise FileExistsError(f"{path.name} already exists - refusing to overwrite")
    doc = dict(cand)
    doc["id"] = cid
    doc["harvested_date"] = date.today().isoformat()
    doc["status"] = "unread"
    doc["access"] = "metadata_only"
    doc["_note"] = (
        "CANDIDATE, not a source record. Nothing has read this yet, so it carries no "
        "`reported`, `method_summary` or `limitations`. The `harvest` skill reads it and writes "
        "corpus/papers/SRC-nnnnn.yaml. Do not cite this file."
    )
    path.write_text(
        yaml.safe_dump(doc, sort_keys=False, allow_unicode=True), encoding="utf-8")
    return cid


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=3,
                    help="look-back window. Default 3 so a Monday run still covers the "
                         "weekend; dedupe makes the overlap free.")
    ap.add_argument("--limit-per-venue", type=int, default=25)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    CANDIDATES.mkdir(parents=True, exist_ok=True)
    since = (date.today() - timedelta(days=args.days)).isoformat()
    reg = load_registry()
    journals = harvestable_journals(reg)
    seen = existing_ids()

    print(f"harvest sweep - window {since} .. {date.today().isoformat()}")
    print(f"  venues: {len(journals)} journals + arXiv | already known: {len(seen)}")

    topic_ids, relevance = load_topic_allowlist()
    specialist = [v for v in journals if v["scope"] == "specialist"]
    broad = [v for v in journals if v["scope"] != "specialist"]
    n_core = sum(1 for v in relevance.values() if v == "core")
    print(f"  {len(specialist)} specialist (no topic filter), {len(broad)} broad "
          f"(gated by {n_core} core + {len(topic_ids) - n_core} adjacent topics)")

    found, errors = [], []
    rate = {}
    for label, group, topics in (("specialist", specialist, None), ("broad", broad, topic_ids)):
        if not group:
            continue
        items, errs, r = sweep_batched(group, since, topics, relevance)
        errors.extend(errs)
        rate.update(r)
        found.extend(items)
        per_venue = {}
        for c in items:
            per_venue[c["venue_id"]] = per_venue.get(c["venue_id"], 0) + 1
        print(f"    {label:12} {len(items):4} items from {len(per_venue)} venue(s)")
        for vid, n in sorted(per_venue.items(), key=lambda x: -x[1])[:6]:
            print(f"      {vid:22} {n}")
    if rate.get("remaining") is not None:
        print(f"  rate budget: {rate['remaining']}/{rate.get('limit')} remaining")

    arx = next((a for a in reg.get("aggregators", []) if a.get("id") == "arxiv_api"), None)
    if arx and arx.get("verified") is not False:
        items, err = sweep_arxiv(arx.get("categories", []), since, args.limit_per_venue * 4)
        if err:
            errors.append(f"arxiv: {err}")
        else:
            print(f"    {'arxiv':20} {len(items):3} (specialist)")
            found.extend(items)

    # dedupe within this run and against everything previously seen
    new, dupes = [], 0
    run_keys = set()
    for c in found:
        keys = {str(c.get(k)).lower() for k in ("doi", "arxiv_id", "openalex_id") if c.get(k)}
        if keys & seen or keys & run_keys:
            dupes += 1
            continue
        run_keys |= keys
        new.append(c)

    # A closed-access hit is evidence, not noise: it is what makes the cost of the
    # open-access-only policy measurable (CLAUDE.md, `access-blocked`).
    readable = [c for c in new if c["is_oa"] and (c.get("oa_location") or {}).get("url")]
    blocked = [c for c in new if not c["is_oa"]]

    tiers = Counter(c.get("relevance", "core") for c in new)
    print(f"\n  found {len(found)} | new {len(new)} | duplicates skipped {dupes}")
    print(f"  relevance: {dict(tiers)}")
    print(f"  readable (OA copy located): {len(readable)}")
    print(f"  access-blocked (no legal OA copy): {len(blocked)}")
    # Partial coverage is a failure, not a footnote. A venue that errored contributed zero items,
    # so a run reporting "3 new papers" while six journals never answered is indistinguishable
    # from a genuinely quiet day. Say so loudly, and exit non-zero.
    if errors:
        print(f"\n  !! INCOMPLETE SWEEP - {len(errors)} of {len(journals) + 1} venues did not "
              f"answer. Coverage for this window is partial.")
        for e in errors:
            print(f"     - {e}")

    if args.dry_run:
        print("\ndry run - nothing written")
        for c in readable[:10]:
            print(f"    {c['venue_id']:16} {(c['title'] or '')[:64]}")
        # A dry run that hit partial coverage is still partial. An earlier version printed
        # INCOMPLETE SWEEP and then exited 0, so the message and the exit code disagreed.
        return 2 if errors else 0

    start = next_candidate_seq()
    written = [write_candidate(c, start + i) for i, c in enumerate(readable)]

    summary = {
        "date": date.today().isoformat(), "window_days": args.days,
        "venues_swept": len(journals) + 1, "found": len(found), "new": len(new),
        "duplicates": dupes, "written": len(written),
        "access_blocked": len(blocked), "errors": errors,
    }
    (CANDIDATES / "_last_sweep.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"\n  wrote {len(written)} candidates -> corpus/candidates/")
    print("  these are UNREAD. Run the `harvest` skill to turn them into source records.")
    if errors:
        print(f"  exit 2: sweep incomplete ({len(errors)} venue(s) failed)")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
