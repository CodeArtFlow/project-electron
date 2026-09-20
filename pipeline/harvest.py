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
import json
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "sources" / "registry.yaml"
CANDIDATES = ROOT / "corpus" / "candidates"
PAPERS = ROOT / "corpus" / "papers"

UA = {"User-Agent": "ProjectElectron/0.1 (semiconductor research agent; harvest)"}
TIMEOUT = 40
PAUSE = 0.2

# Topic filter for broad venues. Generous by design - precision comes from the reading stage,
# and a candidate costs nothing but a file.
TOPIC_TERMS = (
    'semiconductor OR transistor OR lithography OR chiplet OR wafer OR "thin film" OR '
    'photonic OR memristor OR "gate-all-around" OR CMOS OR MOSFET OR "2D material" OR '
    'interconnect OR "high-k" OR epitaxy OR "quantum dot" OR spintronic OR ferroelectric OR '
    '"phase change memory" OR packaging OR "silicon photonics" OR nanowire OR "wide bandgap"'
)

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


def sweep_openalex(venue, since, limit):
    """Recent works from one venue, OA-checked. Returns candidate dicts."""
    filters = [f"primary_location.source.issn:{venue['issn']}",
               f"from_publication_date:{since}"]
    if venue["scope"] != "specialist":
        filters.append("title_and_abstract.search:" + urllib.parse.quote(TOPIC_TERMS))
    url = ("https://api.openalex.org/works?filter=" + ",".join(filters)
           + f"&per-page={min(limit, 200)}&sort=publication_date:desc")
    r, err = get(url)
    time.sleep(PAUSE)
    if r is None:
        return None, err

    out = []
    for w in r.json().get("results", [])[:limit]:
        oa = w.get("open_access") or {}
        best = w.get("best_oa_location") or {}
        doi = (w.get("doi") or "").replace("https://doi.org/", "") or None
        authors = [{
            "name": (a.get("author") or {}).get("display_name"),
            "openalex_author_id": (a.get("author") or {}).get("id"),
            "affiliation": (a.get("raw_affiliation_strings") or [None])[0],
            "corresponding": bool(a.get("is_corresponding")),
        } for a in (w.get("authorships") or [])]
        field = ((w.get("primary_topic") or {}).get("field") or {}).get("display_name")
        out.append({
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
            "primary_topic": (w.get("primary_topic") or {}).get("display_name"),
        })
    return out, None


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

    found, errors = [], []
    for v in journals:
        items, err = sweep_openalex(v, since, args.limit_per_venue)
        if err:
            errors.append(f"{v['id']}: {err}")
            continue
        if items:
            print(f"    {v['id']:20} {len(items):3} ({v['scope']})")
        found.extend(items)

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

    print(f"\n  found {len(found)} | new {len(new)} | duplicates skipped {dupes}")
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
