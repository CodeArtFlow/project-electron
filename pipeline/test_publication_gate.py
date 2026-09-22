"""Prove every publication-gate check actually fires.

A gate that has only ever run against an empty corpus is not a gate - it is eight functions that
have never returned False. (Check 9, the TypeSafe audit, is tested in test_semantic_checks.py.) This builds a deliberately broken fixture tree for each check and
asserts the gate catches it, then builds a clean tree and asserts it passes.

Fixtures are written to a temporary directory, never into the project's real ledger.

Usage:  python pipeline/test_publication_gate.py
"""

import shutil
import sys
import tempfile
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from publication_gate import run_gate  # noqa: E402


def tree(root):
    for d in ("ledger/claims", "ledger/conflicts", "digests", "corpus/papers"):
        (root / d).mkdir(parents=True, exist_ok=True)
    return root


def write_claim(root, **over):
    claim = {
        "id": "CLM-DEV-0001", "topic": "DEV",
        "statement": "Electron mobility of 1000 cm2/(V*s) at 300 K.",
        "sources": ["SRC-00001"], "grade": "A", "credibility": "unknown",
        "evidence_type": "measured", "status": "active",
        "as_of": "2026-03-11", "created": "2026-09-20",
        "quantity": {"quantity": "mobility",
                     "as_published": {"value": 1000, "unit": "cm**2/(V*s)"},
                     "si_base": {"value": 0.1, "unit": "m^2/(V*s)"},
                     "display": {"value": 1000.0, "unit": "cm^2/(V*s)"}},
    }
    claim.update(over)
    (root / "ledger/claims/DEV.yaml").write_text(
        yaml.safe_dump({"claims": [claim]}), encoding="utf-8")
    return claim


def write_source(root, sid="SRC-00001", **over):
    rec = {"id": sid, "venue_id": "nat_comms", "access": "full_text_figures",
           "oa_evidence": "registry oa_status: full, DOAJ-confirmed",
           "published_date": "2026-03-11", "evidence_type": "measured", "grade": "A"}
    rec.update(over)
    (root / f"corpus/papers/{sid}.yaml").write_text(yaml.safe_dump(rec), encoding="utf-8")


def write_conflict(root, name="CFL-0001.md", **fm):
    body = "---\n" + yaml.safe_dump(fm) + "---\n\nBody.\n"
    (root / "ledger/conflicts" / name).write_text(body, encoding="utf-8")


def failed_checks(root):
    results, _ = run_gate(root)
    return {r["check"] for r in results if not r["passed"]}


def case(label, build, expect_fail):
    tmp = Path(tempfile.mkdtemp(prefix="gate-"))
    try:
        tree(tmp)
        build(tmp)
        got = failed_checks(tmp)
        ok = expect_fail in got if expect_fail else not got
        detail = f"failed={sorted(got)}"
        print(f"  [{'OK ' if ok else 'BAD'}] {label}  ({detail})")
        return ok
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    print("publication gate - each check must fire on a broken fixture\n")
    results = []

    # clean baseline must pass
    def clean(r):
        write_source(r)
        write_claim(r)
        (r / "digests/2026-09-20.md").write_text("Digest citing CLM-DEV-0001.\n", encoding="utf-8")
    results.append(case("clean tree passes every check", clean, None))

    # 1 - live:unexamined blocks
    def c1(r):
        clean(r)
        write_conflict(r, state="live:unexamined", claims=["CLM-DEV-0001"])
    results.append(case("1. live:unexamined blocks publication", c1, 1))

    # 2 - data-absent without a named gap
    def c2(r):
        clean(r)
        write_conflict(r, state="live:data-absent", claims=["CLM-DEV-0001"],
                       missing_data="because-i-said-so")
    results.append(case("2. unnamed/invalid gap is caught", c2, 2))

    # 3 - digest cites a claim that does not exist
    def c3(r):
        clean(r)
        (r / "digests/2026-09-20.md").write_text("Cites CLM-DEV-9999.\n", encoding="utf-8")
    results.append(case("3. digest citing a nonexistent claim", c3, 3))

    # 3b - digest cites a retracted claim
    def c3b(r):
        write_source(r)
        write_claim(r, status="retracted")
        (r / "digests/2026-09-20.md").write_text("Cites CLM-DEV-0001.\n", encoding="utf-8")
    results.append(case("3. digest citing a retracted claim", c3b, 3))

    # 3c - the SAME mistake, but a later digest's '## Corrections' section names the claim. A
    # published digest is never rewritten (AGENTS.md), so this is how a citation mistake already
    # committed gets to stop blocking every future gate run forever.
    def c3c(r):
        write_source(r)
        write_claim(r, status="retracted", correction_published_in="2026-09-21")
        (r / "digests/2026-09-20.md").write_text("Cites CLM-DEV-0001.\n", encoding="utf-8")
        (r / "digests/2026-09-21.md").write_text(
            "# Digest\n\n## Corrections\n\n- `CLM-DEV-0001` was retracted before this digest; "
            "the 2026-09-20 digest should not have cited it.\n\n## Open contradictions\n\n_None._\n",
            encoding="utf-8")
    results.append(case("3. a retracted-claim citation is resolved once a later digest corrects it", c3c, None))

    # 4 - claim under a live contradiction cited without its flag
    def c4(r):
        write_source(r)
        write_claim(r)
        (r / "digests/2026-09-20.md").write_text("Cites CLM-DEV-0001.\n", encoding="utf-8")
        write_conflict(r, state="live:data-absent", claims=["CLM-DEV-0001"],
                       missing_data="awaiting-confirmation",
                       resolution_trigger="an independent replication",
                       gap="no second group has measured this")
    results.append(case("4. unflagged claim under live contradiction", c4, 4))

    # 5 - cited source has no corpus record
    def c5(r):
        write_claim(r)  # no write_source
        (r / "digests/2026-09-20.md").write_text("Cites CLM-DEV-0001.\n", encoding="utf-8")
    results.append(case("5. cited source with no corpus record", c5, 5))

    # 5b - source from a verified:false venue
    def c5b(r):
        write_source(r, venue_id="techrxiv")
        write_claim(r)
    results.append(case("5. source from a verified:false venue", c5b, 5))

    # 6 - quantity missing si_base
    def c6(r):
        write_source(r)
        write_claim(r, quantity={"quantity": "mobility",
                                 "as_published": {"value": 1000, "unit": "cm**2/(V*s)"}})
    results.append(case("6. quantity missing si_base", c6, 6))

    # 7 - grade E asserted as fact
    def c7(r):
        write_source(r)
        write_claim(r, grade="E", statement="The process achieves 30% higher density.")
    results.append(case("7. grade E asserted as fact", c7, 7))

    # 8 - published claim retracted with no correction recorded
    def c8(r):
        write_source(r)
        write_claim(r, status="superseded")
        (r / "digests/2026-09-20.md").write_text("Cites CLM-DEV-0001.\n", encoding="utf-8")
    results.append(case("8. published claim changed without a correction", c8, 8))

    print()
    if all(results):
        print(f"OK - all {len(results)} gate scenarios behaved correctly")
        return 0
    print(f"FAILED - {results.count(False)} of {len(results)} scenarios misbehaved")
    return 1


if __name__ == "__main__":
    sys.exit(main())
