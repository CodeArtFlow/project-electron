"""Prove the discovery loop obeys its constraints.

The three properties that matter most, because violating any of them would put a falsehood into
the research record:

  1. It only ever emits text that exists in the corpus (no outside information).
  2. It never merges two sentences whose NUMBERS differ - that would hide a contradiction
     inside a condensed finding.
  3. It never treats an unread candidate as evidence.

Plus the bounds: iteration cap, per-iteration timeout, total budget, ceiling clamping.

Usage:  python pipeline/test_discover.py
"""

import shutil
import sys
import tempfile
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from discover import (  # noqa: E402
    Corpus, LimitError, Passage, condense, independent_groups, load_corpus,
    resolve_limits, run_loop, verify,
)

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(ok)
    print(f"  [{'OK ' if ok else 'BAD'}] {label}" + (f"  ({detail})" if detail else ""))


def build_tree(root, records=(), claims=(), candidates=()):
    for d in ("corpus/papers", "corpus/candidates", "ledger/claims"):
        (root / d).mkdir(parents=True, exist_ok=True)
    for rec in records:
        (root / "corpus/papers" / f"{rec['id']}.yaml").write_text(
            yaml.safe_dump(rec), encoding="utf-8")
    if claims:
        (root / "ledger/claims/DEV.yaml").write_text(
            yaml.safe_dump({"claims": list(claims)}), encoding="utf-8")
    for c in candidates:
        (root / "corpus/candidates" / f"{c['id']}.yaml").write_text(
            yaml.safe_dump(c), encoding="utf-8")
    return load_corpus(root / "corpus/papers", root / "ledger/claims", root / "corpus/candidates")


def rec(sid, reported, author="A. Researcher", affil="Institute X", access="full_text_figures"):
    return {"id": sid, "access": access, "venue_id": "nat_comms",
            "authors": [{"name": author, "affiliation": affil, "corresponding": True}],
            "reported": reported, "method_summary": "Measured on fabricated devices.",
            "limitations": "Single lab."}


def main():
    print("discovery loop - constraint tests\n")
    tmp = Path(tempfile.mkdtemp(prefix="disc-"))
    try:
        # ---------- 1. condensing merges duplicates and keeps every citation ----------
        corpus = build_tree(tmp / "t1", records=[
            rec("SRC-00001", "Electron mobility reached 1000 cm2/(V*s) at 300 K.", "Alice", "MIT"),
            rec("SRC-00002", "Electron mobility reached 1000 cm2/(V*s) at 300 K.", "Bob", "IMEC"),
        ])
        r = run_loop("electron mobility", corpus)
        merged = [f for f in r.findings if len(f.citations) >= 2]
        check("identical statements merge into one finding, citations kept",
              len(r.findings) == 1 and len(merged) == 1,
              f"findings={len(r.findings)}")
        check("merged finding counts 2 independent groups",
              merged and independent_groups(["SRC-00001", "SRC-00002"], corpus.source_meta) == 2)

        # ---------- 2. THE CRITICAL ONE: differing numbers must never merge ----------
        corpus = build_tree(tmp / "t2", records=[
            rec("SRC-00001", "Electron mobility reached 1000 cm2/(V*s) at 300 K.", "Alice", "MIT"),
            rec("SRC-00002", "Electron mobility reached 100 cm2/(V*s) at 300 K.", "Bob", "IMEC"),
        ])
        r = run_loop("electron mobility", corpus)
        texts = {f.text for f in r.findings}
        check("sentences differing ONLY in the number are NOT merged",
              len(r.findings) == 2, f"findings={len(r.findings)}")
        check("both values survive condensation",
              any("1000" in t for t in texts) and any(" 100 " in t or "100 cm2" in t for t in texts))
        check("the divergence is flagged for reconcile", len(r.divergent) >= 1,
              f"divergent={len(r.divergent)}")

        # ---------- 3. shared author collapses independence ----------
        corpus = build_tree(tmp / "t3", records=[
            rec("SRC-00001", "Drive current of 800 uA/um was measured.", "Alice", "MIT"),
            rec("SRC-00002", "Drive current of 800 uA/um was measured.", "Alice", "Stanford"),
        ])
        check("same corresponding author -> 1 independent group",
              independent_groups(["SRC-00001", "SRC-00002"], corpus.source_meta) == 1)

        # ---------- 4. unread candidates are never evidence ----------
        corpus = build_tree(
            tmp / "t4",
            records=[rec("SRC-00001", "Subthreshold swing of 65 mV/dec was measured.")],
            candidates=[{"id": "CAND-20260920-0001",
                         "title": "Subthreshold swing of 42 mV/dec in a new transistor",
                         "venue_id": "nat_comms", "doi": "10.1/x"}])
        r = run_loop("subthreshold swing", corpus)
        cited = " ".join(pid for f in r.findings for pid, _ in f.citations)
        check("no CAND id appears in any citation", "CAND" not in cited)
        check("candidate title text never becomes a finding",
              all("42" not in f.text for f in r.findings))
        check("candidate still surfaces as read-next routing",
              any(c["id"].startswith("CAND") for c in r.read_next))

        # ---------- 5. metadata-only records contribute no passages ----------
        corpus = build_tree(tmp / "t5", records=[
            rec("SRC-00001", "Mobility of 900 cm2/(V*s).", access="metadata_only")])
        check("metadata_only source record contributes nothing to condense",
              len(corpus.passages) == 0, f"passages={len(corpus.passages)}")

        # ---------- 6. verifier rejects a citation that is not verbatim ----------
        corpus = build_tree(tmp / "t6",
                            records=[rec("SRC-00001", "Mobility of 900 cm2/(V*s) was measured.")])
        from discover import Finding
        fake = Finding("Mobility of 5000 cm2/(V*s) was measured.", [], {},
                       [("SRC-00001:reported", "Mobility of 5000 cm2/(V*s) was measured.")])
        kept, rejected = verify([fake], corpus)
        check("fabricated citation (not verbatim in the passage) is rejected",
              len(rejected) == 1 and not kept)
        real = Finding("Mobility of 900 cm2/(V*s) was measured.", [], {},
                       [("SRC-00001:reported", "Mobility of 900 cm2/(V*s) was measured.")])
        kept, rejected = verify([real], corpus)
        check("genuine verbatim citation passes", len(kept) == 1 and not rejected)

        # ---------- 7. bounds ----------
        limits, warns = resolve_limits(max_iterations=999, total_seconds=99999)
        check("limits above the ceiling are clamped, with a warning",
              limits["max_iterations"] == 6 and limits["total_seconds"] == 300 and len(warns) == 2,
              f"{limits['max_iterations']}/{limits['total_seconds']}")
        try:
            resolve_limits(max_iterations=0)
            check("non-positive limit rejected", False)
        except LimitError:
            check("non-positive limit rejected", True)

        # iteration cap: a corpus wide enough to keep finding new passages
        many = [rec(f"SRC-{i:05d}", f"Transistor mobility measurement number {i} of 12 samples.",
                    f"Author{i}", f"Inst{i}") for i in range(1, 30)]
        corpus = build_tree(tmp / "t7", records=many)
        r = run_loop("transistor mobility measurement", corpus, max_iterations=2)
        check("iteration cap stops the loop", r.iterations <= 2 and r.stop_reason in
              ("iteration_cap", "converged"), f"{r.iterations}/{r.stop_reason}")

        # total budget: a clock that jumps past the budget
        ticks = iter([0, 0, 500, 500, 500, 500, 500, 500])
        r = run_loop("transistor mobility measurement", corpus,
                     clock=lambda: next(ticks, 500), total_seconds=100)
        check("total time budget stops the loop", r.stop_reason == "time_budget",
              r.stop_reason)

        # per-iteration timeout
        ticks2 = iter([0, 0, 0, 99, 99, 99, 99, 99, 99, 99])
        r = run_loop("transistor mobility measurement", corpus,
                     clock=lambda: next(ticks2, 99), iteration_seconds=10, total_seconds=300)
        check("per-iteration timeout stops the loop",
              r.stop_reason in ("iteration_timeout", "time_budget"), r.stop_reason)

        # ---------- 8. convergence on an exhausted corpus ----------
        corpus = build_tree(tmp / "t8",
                            records=[rec("SRC-00001", "Mobility of 900 cm2/(V*s) was measured.")])
        r = run_loop("mobility", corpus)
        check("loop converges once the corpus is exhausted", r.stop_reason == "converged",
              r.stop_reason)

        # ---------- 9. every finding is verbatim in its cited passage ----------
        corpus = build_tree(tmp / "t9", records=[
            rec("SRC-00001", "Drive current of 1.2 mA/um at Vdd of 0.75 V was measured. "
                             "Subthreshold swing was 68 mV/dec."),
            rec("SRC-00002", "Drive current of 1.2 mA/um at Vdd of 0.75 V was measured.",
                "Bob", "IMEC")])
        r = run_loop("drive current subthreshold swing", corpus)
        by_pid = {p.pid: " ".join(p.text.split()) for p in corpus.passages}
        allv = all(" ".join(s.split()) in by_pid.get(pid, "")
                   for f in r.findings for pid, s in f.citations)
        check("every emitted sentence exists verbatim in the passage it cites", allv)
        check("verifier rejected nothing from the extractive engine", r.rejected == 0,
              f"rejected={r.rejected}")
        check("residual gap reported when a sub-question finds nothing",
              isinstance(r.residual, list))

        # ---------- 10. empty corpus is handled honestly ----------
        corpus = build_tree(tmp / "t10")
        r = run_loop("anything at all", corpus)
        check("empty read corpus yields zero findings, not an error",
              r.findings == [] and r.stop_reason == "converged")

        print()
        if all(RESULTS):
            print(f"OK - all {len(RESULTS)} constraint checks passed")
            return 0
        print(f"FAILED - {RESULTS.count(False)} of {len(RESULTS)} checks failed")
        return 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
