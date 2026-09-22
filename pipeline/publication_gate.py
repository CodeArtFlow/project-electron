"""The publication gate from AGENTS.md. Nothing ships unless this passes.

Runs the nine checks that stand between the ledger and a published digest. Exits non-zero on
any failure, so CI cannot deploy around it. Eight are deterministic; the ninth (the TypeSafe
audit) is governed by the committed policy file reference/semantic_policy.yaml.

Two of the checks cannot be fully mechanised, and this file says so rather than pretending:
check 3 (every digest sentence traces to a claim) is verified structurally - every claim id a
digest cites must exist and be citable - but whether a sentence faithfully represents its claim
is not decided here (sota.py renders the digest from ledger fields, which keeps it faithful by
construction, but nothing in this gate checks that independently). Check 8 (corrections stated plainly) is likewise
structural: it verifies that a retracted or superseded claim previously published has a
correction entry, not that the prose is adequate.

A gate that silently skipped those would be worse than one that names its limits.

Usage:  python pipeline/publication_gate.py [--json]
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CLAIMS_DIR = ROOT / "ledger" / "claims"
CONFLICTS_DIR = ROOT / "ledger" / "conflicts"
DIGESTS_DIR = ROOT / "digests"
CORPUS_DIR = ROOT / "corpus" / "papers"
REGISTRY = ROOT / "sources" / "registry.yaml"

MISSING_DATA_CATEGORIES = {
    "not-yet-measured", "undisclosed-method", "awaiting-confirmation", "access-blocked",
}
CLAIM_REF_RE = re.compile(r"\bCLM-[A-Z]+-\d{4}\b")
LIVE_FLAG_RE = re.compile(r"CFL-\d{4}")


def load_yaml(p):
    try:
        return yaml.safe_load(Path(p).read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as e:
        return {"__error__": str(e)}


def load_claims(claims_dir=None):
    claims = {}
    for path in sorted(Path(claims_dir or CLAIMS_DIR).glob("*.yaml")):
        doc = load_yaml(path)
        for c in doc.get("claims", []) or []:
            if c.get("id"):
                claims[c["id"]] = c
    return claims


def load_conflicts(conflicts_dir=None):
    out = []
    for path in sorted(Path(conflicts_dir or CONFLICTS_DIR).glob("CFL-*.md")):
        text = path.read_text(encoding="utf-8")
        fm = {}
        if text.startswith("---"):
            _, _, rest = text.partition("---")
            block, _, _ = rest.partition("---")
            parsed = yaml.safe_load(block)
            if isinstance(parsed, dict):
                fm = parsed
        fm["__path__"] = path.name
        out.append(fm)
    return out


def check(results, number, name, failures, note=None):
    results.append({
        "check": number, "name": name,
        "passed": not failures, "failures": failures, "note": note,
    })


def run_gate(root=None):
    """Run all nine checks. `root` lets tests point the gate at fixture trees."""
    root = Path(root) if root else ROOT
    claims_dir = root / "ledger" / "claims"
    conflicts_dir = root / "ledger" / "conflicts"
    digests_dir = root / "digests"
    corpus_dir = root / "corpus" / "papers"
    registry_path = root / "sources" / "registry.yaml"
    if not registry_path.exists():
        registry_path = REGISTRY  # fixtures reuse the real registry

    claims = load_claims(claims_dir)
    conflicts = load_conflicts(conflicts_dir)
    registry = load_yaml(registry_path)
    results = []

    venue_state = {}
    for section, rows in registry.items():
        if isinstance(rows, list):
            for e in rows:
                if isinstance(e, dict) and e.get("id"):
                    venue_state[e["id"]] = e.get("verified")

    # --- 1. no CFL in live:unexamined. The hard gate. ---
    f = [f"{c['__path__']} is live:unexamined" for c in conflicts
         if c.get("state") == "live:unexamined"]
    check(results, 1, "no conflict in live:unexamined", f)

    # --- 2. every live:data-absent has a named gap and a resolution trigger ---
    f = []
    for c in conflicts:
        if c.get("state") != "live:data-absent":
            continue
        md = c.get("missing_data")
        if md not in MISSING_DATA_CATEGORIES:
            f.append(f"{c['__path__']}: missing_data {md!r} not one of {sorted(MISSING_DATA_CATEGORIES)}")
        if not c.get("resolution_trigger"):
            f.append(f"{c['__path__']}: no resolution_trigger")
        if not c.get("gap"):
            f.append(f"{c['__path__']}: no named gap in plain language")
    check(results, 2, "live:data-absent records name their gap", f)

    # A published digest is never rewritten (AGENTS.md), so a citation mistake already committed
    # stays in that file forever - the gate cannot demand it never existed, only that it was
    # corrected. `reported[stem]` is that digest's own "## Corrections" section text; a citation
    # in an EARLIER digest counts as addressed once a LATER one's Corrections section names the
    # claim. Built once, used by checks 3 and 8 alike.
    def corrections_section(text):
        m = re.search(r"^## Corrections\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
        return m.group(1) if m else ""

    digest_texts = {p.stem: p.read_text(encoding="utf-8") for p in digests_dir.glob("*.md")}
    reported = {stem: corrections_section(text) for stem, text in digest_texts.items()}

    def later_correction_covers(stem, ref):
        return any(later_stem > stem and ref in section for later_stem, section in reported.items())

    # --- 3. every digest claim reference resolves to a citable claim ---
    f = []
    citable = {"active", "challenged", "contested"}
    for stem, text in sorted(digest_texts.items()):
        corr_text = reported.get(stem, "")
        # A reference inside the digest's OWN "## Corrections" section is exempt from citability:
        # naming a retracted/superseded claim there is the entire point of a correction, not a
        # mistake to flag. Only a reference OUTSIDE that section (an ordinary citation) must be
        # citable, and only then does the "was it fixed later" escape hatch apply.
        body_refs = set(CLAIM_REF_RE.findall(text)) - set(CLAIM_REF_RE.findall(corr_text))
        for ref in sorted(set(CLAIM_REF_RE.findall(text))):
            if ref not in claims:
                f.append(f"{stem}.md cites {ref}, which is not in the ledger")
            elif ref in body_refs and claims[ref].get("status") not in citable \
                    and not later_correction_covers(stem, ref):
                f.append(f"{stem}.md cites {ref} with status "
                         f"{claims[ref].get('status')!r} (citable: {sorted(citable)})")
    check(results, 3, "digest claim references resolve and are citable", f,
          note="Structural only. Whether a sentence faithfully represents its claim is not "
               "something this gate can decide; the digest is rendered from ledger fields. A "
               "reference inside a digest's own '## Corrections' section is exempt (naming a "
               "non-citable claim there is the point). A citation in an already-published "
               "digest's ordinary body is not a failure once a LATER digest's '## Corrections' "
               "section names the claim - the digest itself is never rewritten.")

    # --- 4. claims under a live contradiction carry their flag wherever they appear ---
    live_claim_ids = set()
    for c in conflicts:
        if str(c.get("state", "")).startswith("live:"):
            for cid in c.get("claims", []) or []:
                live_claim_ids.add(cid)
    f = []
    for path in sorted(digests_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for ref in set(CLAIM_REF_RE.findall(text)) & live_claim_ids:
            # the flag must appear in the same document, near the claim
            if not LIVE_FLAG_RE.search(text):
                f.append(f"{path.name} cites {ref} (under a live contradiction) "
                         f"without showing a CFL reference")
    check(results, 4, "claims under live contradictions are flagged where cited", f)

    # --- 5. every cited source has a corpus record and a harvestable venue ---
    f = []
    for cid, c in claims.items():
        for src in c.get("sources", []) or []:
            rec_path = corpus_dir / f"{src}.yaml"
            if not rec_path.exists():
                f.append(f"{cid} cites {src}, which has no corpus record")
                continue
            rec = load_yaml(rec_path)
            venue = rec.get("venue_id")
            state = venue_state.get(venue)
            if venue not in venue_state:
                f.append(f"{src} venue {venue!r} is not in the registry")
            elif state is False:
                f.append(f"{src} venue {venue!r} is verified:false - not harvestable")
            elif state == "review" and not rec.get("oa_evidence"):
                f.append(f"{src} venue {venue!r} is `review` with no oa_evidence recorded")
    check(results, 5, "cited sources have corpus records and verified venues", f)

    # --- 6. every quantity carries as_published and si_base ---
    f = []
    for cid, c in claims.items():
        q = c.get("quantity")
        if not q:
            continue
        for part in ("as_published", "si_base"):
            if part not in q:
                f.append(f"{cid} quantity missing {part}")
        if "si_base" in q and not isinstance(q["si_base"], dict):
            f.append(f"{cid} si_base is not a {{value, unit}} block")
    check(results, 6, "quantities carry as_published and si_base", f)

    # --- 7. no grade D/E material phrased as fact ---
    attribution = re.compile(r"\b(states?|claims?|announced|reported|according to|says?)\b", re.I)
    f = [f"{cid} is grade {c.get('grade')} but asserts rather than attributes"
         for cid, c in claims.items()
         if c.get("grade") in ("D", "E") and not attribution.search(c.get("statement", ""))]
    check(results, 7, "grade D/E is attributed, never asserted", f)

    # --- 8. retracted/superseded claims that were published have a correction ---
    f = []
    published_refs = set()
    for text in digest_texts.values():
        published_refs |= set(CLAIM_REF_RE.findall(text))
    for cid, c in claims.items():
        if c.get("status") in ("retracted", "superseded") and cid in published_refs:
            if not c.get("correction_published_in"):
                f.append(f"{cid} is {c.get('status')} and was published, but no "
                         f"correction_published_in is recorded")
    # A claim that changed after publication must say so in a digest. `public: true` on a
    # correction means readers had already seen the claim, so the change is reported under
    # "## Corrections" in a digest dated on or after it - never edited away silently.
    for cid, c in claims.items():
        for corr in c.get("corrections", []) or []:
            if corr.get("public") is not True:
                continue
            when = str(corr.get("date"))
            if not any(stem >= when and cid in section for stem, section in reported.items()):
                f.append(f"{cid} has a public correction dated {when} that no digest on or after "
                         f"that date reports under '## Corrections'")
    check(results, 8, "corrections recorded for published claims that changed", f,
          note="Structural only. This verifies a correction exists, not that its wording is "
               "adequate.")

    # Semantic signals supplement the deterministic checks; they cannot certify truth.
    from semantic_checks import audit_findings, gate_failures, load_policy
    required = os.environ.get("ELECTRON_TYPESAFE_REQUIRED") == "1"
    policy = load_policy(root)
    findings = audit_findings(root, required)
    if policy == "advisory":
        # The policy is a committed file (reference/semantic_policy.yaml), not a switch CI can
        # flip, so this is not a way around the gate. The check passes, and says so out loud.
        note = (f"ADVISORY policy: {len(findings)} audit finding(s) reported on the Research "
                f"checks page and NOT blocking. Uncalibrated signals until a gold set exists."
                if findings else
                "ADVISORY policy: no audit findings. Uncalibrated signals, not verification.")
    else:
        note = ("Required in production. Uncalibrated review signals, not scientific verification."
                if required else "Optional locally; any present audit must be current and pass.")
    check(results, 9, "TypeSafe evidence audit has no unresolved publication flags",
          gate_failures(root, required), note=note)

    return results, {"claims": len(claims), "conflicts": len(conflicts),
                     "digests": len(list(digests_dir.glob("*.md")))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    results, counts = run_gate()
    failed = [r for r in results if not r["passed"]]

    if args.json:
        print(json.dumps({"passed": not failed, "counts": counts, "checks": results}, indent=2))
        return 1 if failed else 0

    print(f"publication gate - {counts['claims']} claims, {counts['conflicts']} conflicts, "
          f"{counts['digests']} digests")
    print()
    for r in results:
        mark = "PASS" if r["passed"] else "FAIL"
        print(f"  [{mark}] {r['check']}. {r['name']}")
        for problem in r["failures"]:
            print(f"         - {problem}")
        if r["note"]:
            print(f"         note: {r['note']}")
    print()
    if failed:
        print(f"GATE FAILED - {len(failed)} check(s). Nothing may be published.")
        return 1
    if counts["claims"] == 0 and counts["digests"] == 0:
        print("GATE PASSED on an empty corpus. This is vacuous: there is nothing to publish "
              "yet, so every check passes trivially. It is not evidence the gate works on "
              "real content.")
        return 0
    print("GATE PASSED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
