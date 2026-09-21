"""Run the pipeline end to end, timing every stage.

Two kinds of stage, and the distinction is the whole architecture:

  AUTOMATIC  deterministic code. Runs here.
  READING    requires comprehension - reading a paper, classifying a contradiction. A script
             cannot do these without fabricating, so they run as skills in a Claude session.
             This orchestrator does not fake them: it reports what is waiting and why.

The run record lands in run/timings.json and is rendered on the site, so the published page shows
how long each stage took and which stages were blocked on a human.

Usage:
    python pipeline/run_pipeline.py            # full run
    python pipeline/run_pipeline.py --no-sweep # skip the network sweep
"""

import argparse
import json
import subprocess
import sys
import time
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUN = ROOT / "run"

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass


sys.path.insert(0, str(Path(__file__).resolve().parent))
from candidates import load as load_candidate  # noqa: E402
from candidates import unread_candidates  # noqa: E402


def count(pattern, root=ROOT):
    return len(list(root.glob(pattern)))


def unread_by_lane():
    """Unread candidates split by who can read them: the automated arXiv lane, or a human."""
    lane = {"arxiv": 0, "other": 0}
    for p in unread_candidates(ROOT / "corpus" / "candidates"):
        lane["arxiv" if load_candidate(p).get("source") == "arxiv" else "other"] += 1
    return lane


def stage(name, description, argv, kind="automatic", allow_fail=False):
    started = time.perf_counter()
    proc = subprocess.run([sys.executable] + argv, capture_output=True, text=True, cwd=ROOT)
    elapsed = time.perf_counter() - started
    ok = proc.returncode == 0
    tail = (proc.stdout or "").strip().splitlines()
    rec = {
        "stage": name, "description": description, "kind": kind,
        "command": "python " + " ".join(argv),
        "seconds": round(elapsed, 3), "exit_code": proc.returncode, "ok": ok,
        "output_tail": tail[-6:],
    }
    if proc.returncode != 0 and (proc.stderr or "").strip():
        rec["stderr_tail"] = (proc.stderr or "").strip().splitlines()[-4:]
    status = "ok" if ok else "FAIL"
    print(f"  [{status:4}] {elapsed:7.2f}s  {name:24} {description}")
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-sweep", action="store_true")
    ap.add_argument("--days", default="7")
    ap.add_argument("--typesafe", choices=("preview","live"), default="preview")
    a = ap.parse_args()

    RUN.mkdir(exist_ok=True)
    steps = []
    t0 = time.perf_counter()
    print(f"Project Electron - full pipeline run {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    before = {
        "candidates": count("corpus/candidates/CAND-*.yaml"),
        "sources": count("corpus/papers/SRC-*.yaml"),
        "claims_files": count("ledger/claims/*.yaml"),
        "conflicts": count("ledger/conflicts/CFL-*.md"),
    }

    print("integrity checks (authorities must be valid before anything runs)")
    for name, desc, argv in [
        ("validate-registry", "registry against its own rules", ["pipeline/validate_registry.py"]),
        ("units", "SI engine vs definitions.yaml", ["pipeline/units.py"]),
        ("authority", "definitions vs the NIST CODATA file", ["pipeline/bounds.py", "--verify"]),
        ("reader-budget", "the reader's spending policy is valid", ["pipeline/budget.py", "--check"]),
        ("claims-selftest", "extraction refusals fire", ["pipeline/claims.py", "--self-test"]),
        ("gate-selftest", "every gate check fires", ["pipeline/test_publication_gate.py"]),
        ("discover-selftest", "discovery loop bounds", ["pipeline/test_discover.py"]),
    ]:
        steps.append(stage(name, desc, argv))

    print("\nstage 1 - harvest")
    if a.no_sweep:
        print("  [skip]           harvest.sweep            --no-sweep")
        steps.append({"stage": "harvest.sweep", "description": "skipped", "kind": "automatic",
                      "seconds": 0.0, "ok": True, "skipped": True, "output_tail": []})
    else:
        steps.append(stage("harvest.sweep", "sweep verified venues for candidates",
                           ["pipeline/harvest.py", "--days", a.days], allow_fail=True))

    print("\nstage 3 - extract (ledger validation)")
    steps.append(stage("claims-validate", "every claim well-formed",
                       ["pipeline/claims.py", "--validate"]))

    steps.append(stage("bounds-scrutiny", "claims outside a derived physical bound (informational)",
                       ["pipeline/bounds.py", "--check-ledger"]))

    print("\nstage 4 - reconcile")
    for name, desc, argv in [
        ("reconcile.detect", "find comparable claims that disagree",
         ["pipeline/reconcile.py", "--detect"]),
        ("reconcile.register", "regenerate the open contradictions register",
         ["pipeline/reconcile.py", "--register"]),
        ("reconcile.check", "every conflict record well-formed",
         ["pipeline/reconcile.py", "--check"]),
    ]:
        steps.append(stage(name, desc, argv, allow_fail=(name == "reconcile.check")))

    print("\nstage 5 - derive")
    steps.append(stage("sota", "per-layer state of the art", ["pipeline/sota.py", "--sota"]))
    steps.append(stage("synthesis", "cross-stack synthesis", ["pipeline/sota.py", "--synthesis"]))
    steps.append(stage("digest", "daily digest from the ledger", ["pipeline/sota.py", "--digest"]))

    argv = ["pipeline/semantic_checks.py", "--scope", "publication"]
    if a.typesafe == "live": argv.append("--live")
    steps.append(stage("typesafe", "evidence-bound semantic audit", argv, kind="model"))

    print("\nstage 6 - publish")
    steps.append(stage("publication-gate", "the nine checks", ["pipeline/publication_gate.py"],
                       allow_fail=True))
    gate_ok = all(s.get("ok") for s in steps)
    if gate_ok:
        steps.append(stage("build-site", "render the static site",
                           ["pipeline/build_site.py", "--out", "_site"]))
    else:
        print("  [BLOCK]           build-site               gate failed; refusing to build")
        steps.append({"stage": "build-site", "description": "blocked by the publication gate",
                      "kind": "automatic", "seconds": 0.0, "ok": False, "blocked": True,
                      "output_tail": ["The gate failed, so nothing was built. This is the gate "
                                      "working."]})

    after = {
        "candidates": count("corpus/candidates/CAND-*.yaml"),
        "sources": count("corpus/papers/SRC-*.yaml"),
        "claims_files": count("ledger/claims/*.yaml"),
        "conflicts": count("ledger/conflicts/CFL-*.md"),
        "sota_docs": count("sota/*.md"),
        "digests": count("digests/*.md"),
        "discoveries": count("discoveries/*.md"),
    }

    # Stages that need comprehension. Reported, never simulated.
    lanes = unread_by_lane()
    after["candidates_unread"] = lanes["arxiv"] + lanes["other"]
    pending = []
    if lanes["arxiv"]:
        pending.append({
            "stage": "harvest.read (automated)", "kind": "reading",
            "why": f"{lanes['arxiv']} arXiv candidate(s) are unread. They are read by "
                   "pipeline/read_paper.py (daily, read.yml, at most $10 a month) once GEMINI_API_KEY is configured. A "
                   "model only proposes quotes; code verifies each one verbatim against the paper.",
            "skill": "read_paper.py",
        })
    if lanes["other"]:
        pending.append({
            "stage": "harvest.read (manual)", "kind": "reading",
            "why": f"{lanes['other']} publisher candidate(s) are unread. About a quarter of these "
                   "can be fetched as full text; the rest are behind bot walls. They need a human "
                   "reader (the harvest skill) or a legitimate full-text route.",
            "skill": "harvest",
        })
    unexamined = 0
    for p in (ROOT / "ledger" / "conflicts").glob("CFL-*.md"):
        if "state: live:unexamined" in p.read_text(encoding="utf-8"):
            unexamined += 1
    if unexamined:
        pending.append({
            "stage": "reconcile.classify", "kind": "reading",
            "why": f"{unexamined} conflict(s) are in live:unexamined. Detection is arithmetic; "
                   "classifying a contradiction requires reading both sources.",
            "skill": "reconcile",
        })

    total = time.perf_counter() - t0
    record = {
        "run_started": datetime.now().isoformat(timespec="seconds"),
        "date": date.today().isoformat(),
        "total_seconds": round(total, 2),
        "automatic_seconds": round(sum(s.get("seconds", 0) for s in steps), 2),
        "steps": steps,
        "before": before, "after": after,
        "pending_reading_stages": pending,
        "all_ok": all(s.get("ok") for s in steps),
    }
    (RUN / "timings.json").write_text(json.dumps(record, indent=2), encoding="utf-8")

    print(f"\ntotal {total:.2f}s across {len(steps)} automatic stage(s)")
    if pending:
        print(f"{len(pending)} stage(s) waiting on reading:")
        for p in pending:
            print(f"  - {p['stage']} (skill: {p['skill']}) - {p['why']}")
    print(f"run record -> run/timings.json")
    return 0 if record["all_ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
