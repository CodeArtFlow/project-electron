"""Check sources/registry.yaml against its own stated rules.

This validates internal consistency, not external truth - verify_registry.py does the latter.
It exists because the registry states rules in its own header comments, and a rule stated but
not enforced drifts silently. On its first run it found nine conference entries marked
`verified: true` while carrying `oa_status: hybrid`, contradicting the registry's own
"hybrid is permanently review" rule.

Exit code is non-zero when any check fails, so this can gate a commit or a harvest.

Usage:  python pipeline/validate_registry.py
"""

import collections
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "sources" / "registry.yaml"

VALID_VERIFIED = (True, "review", False)
VALID_OA = ("full", "hybrid", "preprint", "open_spec", "public_corp", "open_news")
VALID_GRADES = ("A", "B", "C", "D", "E")
# Per CLAUDE.md. `ALL` is a registry-only wildcard, not a topic code.
VALID_TOPICS = ("MAT", "DEV", "LITHO", "PROC", "PKG", "MEM", "ARCH", "PHOT", "EDA", "ECON", "ALL")

BOOKKEEPING = ("removed", "excluded_paywalled")
# Harvest scope. `specialist` skips the topic filter; absent means `broad` (filter applied).
VALID_SCOPE = ("specialist", "broad")


def main():
    reg = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    problems = []
    ids = []

    for section, rows in reg.items():
        if not isinstance(rows, list):
            continue
        for e in rows:
            if not isinstance(e, dict):
                continue
            eid = e.get("id")
            ids.append(eid)
            where = f"{section}/{eid}"

            if not eid:
                problems.append((where, "entry has no id"))
            if section in BOOKKEEPING:
                continue

            v = e.get("verified")
            oa = e.get("oa_status")
            grade = e.get("grade_default")

            if v not in VALID_VERIFIED:
                problems.append((where, f"verified must be true/review/false, got {v!r}"))
            if oa not in VALID_OA:
                problems.append((where, f"oa_status invalid: {oa!r}"))
            if grade is not None and grade not in VALID_GRADES:
                problems.append((where, f"grade_default invalid: {grade!r}"))

            scope = e.get("scope")
            if scope is not None and scope not in VALID_SCOPE:
                problems.append((where, f"scope must be one of {VALID_SCOPE}, got {scope!r}"))

            for t in e.get("topics", []) or []:
                if t not in VALID_TOPICS:
                    problems.append((where, f"unknown topic code {t!r}"))

            # A source we cannot reach must say why, or the registry silently loses the reason.
            if v is False and not e.get("blocker"):
                problems.append((where, "verified:false requires a blocker explaining why"))

            # OA is an article-level property for hybrid venues, so they can never be `true`.
            if oa == "hybrid" and v is True:
                problems.append((where, "oa_status:hybrid cannot be verified:true - must be review"))

            # `true` asserts the venue is active; a zero activity count contradicts that.
            if v is True and e.get("recent") == 0:
                problems.append((where, "verified:true contradicted by recent:0"))

            # Journals are identified by ISSN; without one, verification cannot be deterministic.
            if section.startswith("journals_") and not e.get("issn"):
                problems.append((where, "journal entry has no issn"))

            # Everything we reach over the web needs an address to reach it at.
            if section in ("preprints", "conferences", "institutional", "standards",
                           "vendor", "trade_press") and not e.get("url"):
                problems.append((where, "web entry has no url"))

    for eid, count in collections.Counter(ids).items():
        if count > 1:
            problems.append((f"id:{eid}", f"duplicate id used {count} times"))

    counts = collections.Counter(
        e.get("verified") for s, r in reg.items() if isinstance(r, list) and s not in BOOKKEEPING
        for e in r if isinstance(e, dict))

    print(f"entries: {len(ids)}")
    print(f"sections: { {s: len(r) for s, r in reg.items() if isinstance(r, list)} }")
    print(f"verified: { {str(k): v for k, v in counts.items()} }")

    if problems:
        print(f"\nFAILED - {len(problems)} problem(s):")
        for where, msg in problems:
            print(f"  {where}: {msg}")
        return 1
    print("\nOK - registry is internally consistent with its own rules")
    return 0


if __name__ == "__main__":
    sys.exit(main())
