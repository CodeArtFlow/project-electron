"""Verify every entry in sources/registry.yaml against external authorities.

Per CLAUDE.md, an unverified registry entry may not be harvested from. Verification answers
three questions, and records the evidence for each rather than asserting a conclusion:

    (a) does the venue exist?            -> Crossref journals / HTTP probe
    (b) is its OA status as stated?      -> DOAJ (authoritative for journal OA)
    (c) does the access endpoint work?   -> live probe with a real minimal query

Writes a JSON evidence report. It never edits the registry: the human-reviewable diff between
report and registry is the audit trail, and a script that both judges and rewrites the record
would erase it.

Usage:  python pipeline/verify_registry.py [--section aggregators|journals|web|all]
"""

import argparse
import re
import json
import sys
import time
import urllib.parse
from datetime import date, timedelta
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "sources" / "registry.yaml"

# No email in the User-Agent. Crossref's "polite pool" and Unpaywall both want a contact address;
# the operator's personal address is not ours to hand to third-party services, so we run in the
# public pool and accept the lower rate limit. See report note on unpaywall.
UA = {"User-Agent": "ProjectElectron/0.1 (semiconductor research agent; verification)"}
TIMEOUT = 30
PAUSE = 0.35  # public-pool courtesy

# Activity threshold: a venue with no Crossref-indexed output in this window is flagged for
# review rather than auto-failed. Indexing lag is real and varies by publisher.
ACTIVE_WINDOW_DAYS = 400


def get(url, **kw):
    try:
        r = requests.get(url, headers=UA, timeout=TIMEOUT, **kw)
        return r, None
    except Exception as e:  # noqa: BLE001 - any transport failure is evidence, not a crash
        return None, f"{type(e).__name__}: {e}"


# --------------------------------------------------------------------------- journals
def _norm(s):
    return "".join(c for c in (s or "").lower() if c.isalnum())


def _query_variants(title):
    """Crossref's journal search returns nothing for '&' and is sensitive to punctuation.

    Variants are for RETRIEVAL only. Acceptance is still an exact normalized-title match, so a
    loosened query can never loosen the identification.
    """
    seen, out = set(), []
    for v in (title,
              re.sub(r"\s*\([^)]*\)", "", title),          # drop "(MDPI)", "(IOP)"
              title.replace("&", " ").replace(":", " "),
              re.sub(r"\s*\([^)]*\)", "", title).replace("&", " ").replace(":", " ")):
        v = " ".join(v.split())
        if v and v not in seen:
            seen.add(v)
            out.append(v)
    return out


def crossref_by_issn(issn):
    """Deterministic lookup. Preferred whenever the registry carries an ISSN."""
    r, err = get("https://api.crossref.org/journals/" + urllib.parse.quote(issn))
    if err or r.status_code != 200:
        return {"ok": False, "error": err or f"HTTP {r.status_code}"}
    m = r.json()["message"]
    return {"ok": True, "match": "issn", "title": m.get("title"),
            "issn": m.get("ISSN") or [issn], "publisher": m.get("publisher")}


def crossref_journal(title, issn=None):
    """Identify a journal. ISSN first; otherwise EXACT title match only.

    Substring matching is deliberately absent. An earlier version accepted `target in candidate`,
    which silently identified 'NatureJobs' as 'Nature' and then reported the wrong journal as
    inactive. A near-miss must fail loudly and surface candidates for a human, never resolve
    itself to the closest-looking thing.
    """
    if issn:
        res = crossref_by_issn(issn)
        if res.get("ok"):
            if _norm(res["title"]) != _norm(title):
                res["title_mismatch"] = {"registry": title, "crossref": res["title"]}
            return res

    candidates = []
    for variant in _query_variants(title):
        url = "https://api.crossref.org/journals?query=" + urllib.parse.quote(variant) + "&rows=5"
        r, err = get(url)
        time.sleep(PAUSE)
        if err or r.status_code != 200:
            continue
        items = r.json()["message"]["items"]
        candidates.extend(i.get("title") for i in items[:3])
        target = _norm(title)
        # also accept an exact match against the punctuation-stripped registry name
        targets = {target, _norm(re.sub(r"\s*\([^)]*\)", "", title))}
        hit = next((i for i in items if _norm(i.get("title")) in targets), None)
        if hit:
            return {"ok": True, "match": "exact_title", "query_used": variant,
                    "title": hit.get("title"), "issn": hit.get("ISSN") or [],
                    "publisher": hit.get("publisher")}

    return {"ok": False, "error": "no exact title match in Crossref",
            "candidates": sorted(set(c for c in candidates if c))[:5]}


def crossref_activity(issns):
    """Recent indexed output = the venue is live, not merely registered.

    Checks EVERY ISSN, not just the first. Crossref journal records often carry a legacy print
    ISSN alongside the current electronic one, and works are indexed against whichever the
    publisher deposits. Testing only issns[0] reported Physical Review B and Nanophotonics as
    inactive - both false, both caused by an outdated first ISSN.
    """
    if not issns:
        return {"ok": False, "error": "no ISSN"}
    since = (date.today() - timedelta(days=ACTIVE_WINDOW_DAYS)).isoformat()
    per_issn, best = {}, 0
    for issn in issns:
        url = ("https://api.crossref.org/works?filter=issn:" + urllib.parse.quote(issn)
               + ",from-pub-date:" + since + "&rows=0")
        r, err = get(url)
        time.sleep(PAUSE)
        if err or r.status_code != 200:
            per_issn[issn] = None
            continue
        n = r.json()["message"]["total-results"]
        per_issn[issn] = n
        best = max(best, n)
    if all(v is None for v in per_issn.values()):
        return {"ok": False, "error": "all ISSN activity queries failed"}
    return {"ok": True, "recent_works": best, "per_issn": per_issn,
            "since": since, "active": best > 0}


def doaj_by_issn(issns):
    """DOAJ listing is authoritative for FULL open access.

    Absence is NOT evidence of paywall: DOAJ lists journals, and a fully-OA journal can be
    absent for administrative reasons. Absence downgrades a `full` claim to unconfirmed,
    it does not disprove it.
    """
    for issn in issns:
        url = "https://doaj.org/api/search/journals/" + urllib.parse.quote(f"issn:{issn}")
        r, err = get(url)
        time.sleep(PAUSE)
        if err or r.status_code != 200:
            continue
        d = r.json()
        if d.get("total", 0) > 0:
            b = d["results"][0].get("bibjson", {})
            lic = [l.get("type") for l in b.get("license", []) if isinstance(l, dict)]
            return {"ok": True, "in_doaj": True, "issn_matched": issn,
                    "doaj_title": b.get("title"), "license": lic}
    return {"ok": True, "in_doaj": False}


def verify_journal(entry, declared_oa):
    name = entry["name"]
    res = {"id": entry["id"], "name": name, "declared_oa": declared_oa}

    cr = crossref_journal(name, entry.get("issn"))
    time.sleep(PAUSE)
    res["crossref"] = cr
    if not cr.get("ok"):
        res["verdict"] = "FAIL"
        res["reason"] = "not found in Crossref: " + str(cr.get("error"))
        return res

    act = crossref_activity(cr["issn"])
    time.sleep(PAUSE)
    res["activity"] = act

    doaj = doaj_by_issn(cr["issn"])
    res["doaj"] = doaj

    in_doaj = doaj.get("in_doaj")
    active = act.get("active")

    if declared_oa == "full":
        if in_doaj and active:
            res["verdict"] = "PASS"
        elif in_doaj and not active:
            res["verdict"] = "REVIEW"
            res["reason"] = "OA confirmed, but no Crossref output in activity window"
        elif active:
            res["verdict"] = "REVIEW"
            res["reason"] = "active, but full-OA not confirmed by DOAJ"
        else:
            res["verdict"] = "FAIL"
            res["reason"] = "neither OA-confirmed nor recently active"
    else:  # hybrid
        if in_doaj:
            res["verdict"] = "REVIEW"
            res["reason"] = "declared hybrid but DOAJ-listed as full OA - upgrade candidate"
        elif active:
            res["verdict"] = "PASS"
            res["reason"] = "exists and active; hybrid means per-article OA check at harvest"
        else:
            res["verdict"] = "FAIL"
            res["reason"] = "no recent activity"
    return res


# --------------------------------------------------------------------------- endpoints
# Live probes: a real minimal query, because a 200 on a landing page proves nothing about
# whether the API answers.
PROBES = {
    "openalex": "https://api.openalex.org/works?per-page=1",
    "arxiv_api": "http://export.arxiv.org/api/query?search_query=cat:cond-mat.mtrl-sci&max_results=1",
    "semantic_scholar": "https://api.semanticscholar.org/graph/v1/paper/search?query=transistor&limit=1",
    "crossref": "https://api.crossref.org/works?rows=1",
    "doaj": "https://doaj.org/api/search/journals/issn:2041-1723",
    "osti": "https://www.osti.gov/api/v1/records?rows=1",
    "unpaywall": None,  # requires an email parameter - see report note
    "retraction_watch": "https://api.labs.crossref.org/data/retractionwatch?rows=1",
}


def verify_endpoint(entry):
    eid = entry["id"]
    res = {"id": eid, "name": entry["name"]}
    probe = PROBES.get(eid, entry.get("endpoint"))
    if probe is None:
        res["verdict"] = "BLOCKED"
        res["reason"] = "requires a contact email we will not supply without the operator's say-so"
        return res
    res["probe"] = probe
    r, err = get(probe)
    if err:
        res["verdict"] = "FAIL"
        res["reason"] = err
        return res
    res["status"] = r.status_code
    res["bytes"] = len(r.content)
    if r.status_code == 200 and len(r.content) > 0:
        res["verdict"] = "PASS"
    else:
        res["verdict"] = "FAIL"
        res["reason"] = f"HTTP {r.status_code}"
    return res


# --------------------------------------------------------------------------- web venues
def verify_url(entry):
    res = {"id": entry["id"], "name": entry["name"], "url": entry.get("url")}
    if not entry.get("url"):
        res["verdict"] = "NO_URL"
        res["reason"] = "registry entry carries no URL to probe"
        return res
    r, err = get(entry["url"], allow_redirects=True)
    if err:
        res["verdict"] = "FAIL"
        res["reason"] = err
        return res
    res["status"] = r.status_code
    res["final_url"] = r.url
    res["bytes"] = len(r.content)
    res["verdict"] = "PASS" if r.status_code < 400 else "FAIL"
    if r.status_code >= 400:
        res["reason"] = f"HTTP {r.status_code}"
    return res


# --------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--section", default="all",
                    choices=["aggregators", "journals", "web", "all"])
    ap.add_argument("--out", default=str(ROOT / "pipeline" / "verification_report.json"))
    args = ap.parse_args()

    reg = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    report = {"run_date": date.today().isoformat(), "sections": {}}

    if args.section in ("aggregators", "all"):
        out = []
        for e in reg.get("aggregators", []):
            r = verify_endpoint(e)
            print(f"[agg ] {r['verdict']:8} {r['name']}", flush=True)
            out.append(r)
        report["sections"]["aggregators"] = out

    if args.section in ("journals", "all"):
        out = []
        for key, declared in (("journals_full_oa", "full"), ("journals_hybrid", "hybrid")):
            for e in reg.get(key, []):
                r = verify_journal(e, declared)
                r["section"] = key
                extra = r.get("reason", "")
                print(f"[jrnl] {r['verdict']:8} {r['name']}  {extra}", flush=True)
                out.append(r)
        report["sections"]["journals"] = out

    if args.section in ("web", "all"):
        out = []
        for key in ("preprints", "conferences", "institutional", "standards",
                    "vendor", "trade_press"):
            for e in reg.get(key, []):
                r = verify_url(e)
                r["section"] = key
                print(f"[web ] {r['verdict']:8} {r['name']}", flush=True)
                out.append(r)
        report["sections"]["web"] = out

    Path(args.out).write_text(json.dumps(report, indent=2), encoding="utf-8")

    print("\n--- summary ---")
    for sec, rows in report["sections"].items():
        counts = {}
        for r in rows:
            counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
        print(f"{sec}: {counts}")
    print(f"report -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
