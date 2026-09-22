"""Measure the automated reader, so a change to its model, thinking level or prompt is judged on data.

    python pipeline/read_report.py                 # the table, from corpus/candidates/_read_runs.jsonl
    python pipeline/read_report.py --backfill-git  # one-off: add the runs already in git history

`read_paper.py` appends one compact record per run to `_read_runs.jsonl` (append-only, committed with
the run, like the spend ledger). This module reads it back and groups runs by the three things that
can be changed: the screening model, the extraction model and the prompt version. Nothing here calls a
model, spends money or writes a record other than that log.

A rejection is bucketed by *why the verifier refused it* (`reason_kind`). The buckets are the point:
"the reader is bad" cannot be fixed, but "44% of rejections are a number the quotes lack" can. A
reason the buckets do not recognise lands in `other`, which is reported, so a new kind of refusal
cannot hide inside the totals.

What this does NOT measure: whether the claims that WERE accepted are true. That needs a person, or the
paper-grounded check (`paper_check.py`) against a gold set (`docs/typesafe-plan.md`, phase 3).
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG_NAME = "_read_runs.jsonl"
LAST_NAME = "_last_read.json"
DECISIONS_WITH_EXTRACTION = ("read", "no_claims")     # papers the extraction model was given in full

# Ordered: the first pattern that matches wins, so the specific ones come before the general ones.
KINDS = [
    ("number_not_in_quotes", r"^the statement contains the number"),
    ("value_not_in_quotes", r"^the value .* does not appear in any of the claim's quotes"),
    ("quote_not_found", r"^anchor quote not found verbatim"),
    ("no_anchor_quote", r"^no anchor quote"),
    ("no_condition", r"^a claim with a number needs at least one verified condition"),
    ("unit_unparsed", r"^unit conversion refused: .*could not parse"),
    ("unit_incompatible", r"^unit conversion refused"),
    ("qualifier_dropped", r"^the quote says"),
    ("statement_length", r"^statement is not between"),
    ("unknown_quantity", r"^unknown quantity"),
    ("duplicate", r"^duplicate of a claim"),
    ("schema_rule", r"^\[[a-z_]+\]"),
]
KIND_NOTES = {
    "number_not_in_quotes": "the statement has a number none of its quotes contain",
    "value_not_in_quotes": "the recorded value is in none of the quotes",
    "quote_not_found": "a quote is not in the paper (or too short)",
    "no_anchor_quote": "no quote at all",
    "no_condition": "a number with nothing saying what it is a value of",
    "unit_unparsed": "a unit we could not parse (recoverable if it is only a spelling)",
    "unit_incompatible": "a unit that does not fit the quantity (usually the model's error)",
    "qualifier_dropped": "'up to' / 'roughly' in the quote but not in the bound",
    "statement_length": "statement outside 30 to 400 characters",
    "unknown_quantity": "a quantity name we do not define",
    "duplicate": "the same result stated twice",
    "schema_rule": "a rule in reference/schemas.yaml refused it",
    "other": "not recognised: add a bucket or look at it",
}


def reason_kind(reason):
    text = str(reason or "").strip()
    for kind, pat in KINDS:
        if re.search(pat, text):
            return kind
    return "other"


# ---------------------------------------------------------------------------------------- the log
def run_record(summary, source="run"):
    """The compact, permanent form of one run's summary. Statements stay in `_last_read.json` and the
    source records; here each rejection keeps only its bucket and its reason."""
    papers = []
    for p in summary.get("papers", []):
        papers.append({
            "candidate": p.get("candidate"), "decision": p.get("decision"), "chars": p.get("chars") or 0,
            "accepted": len(p.get("claims") or []),
            "rejected": [{"kind": reason_kind(r.get("reason")), "reason": str(r.get("reason", ""))[:200]}
                         for r in p.get("rejected") or []]})
    return {"source": source, "date": summary.get("date"), "model": summary.get("model"),
            "extract_model": summary.get("extract_model"), "prompt_version": summary.get("prompt_version"),
            "stop_reason": summary.get("stop_reason"), "seconds": summary.get("seconds"),
            "cost_usd": summary.get("cost_usd", 0.0), "tokens": summary.get("tokens") or {},
            "counts": summary.get("counts") or {}, "claims_accepted": summary.get("claims_accepted", 0),
            "claims_rejected": summary.get("claims_rejected", 0), "papers": papers}


def log_path(candidates_dir):
    return Path(candidates_dir) / LOG_NAME


def load_runs(candidates_dir):
    p = log_path(candidates_dir)
    if not p.exists():
        return []
    return [json.loads(line) for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]


def append_run(candidates_dir, summary, source="run"):
    """Append one run. Append-only: nothing already logged is rewritten."""
    if summary.get("skipped_reason"):
        return None                               # no key, nothing was attempted: not a run
    rec = run_record(summary, source)
    p = log_path(candidates_dir)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(rec, ensure_ascii=False, sort_keys=True) + "\n")
    return rec


def backfill_from_git(candidates_dir, root=ROOT, runner=subprocess.run):
    """One-off: every committed version of `_last_read.json` that the log does not already hold.
    A run is identified by the commit it was committed in, so this can be repeated safely."""
    rel = f"corpus/candidates/{LAST_NAME}"
    done = {r.get("source") for r in load_runs(candidates_dir)}
    shas = runner(["git", "log", "--reverse", "--format=%h", "--", rel], cwd=root, capture_output=True,
                  text=True, encoding="utf-8").stdout.split()
    added = []
    for sha in shas:
        tag = f"git:{sha}"
        if tag in done:
            continue
        blob = runner(["git", "show", f"{sha}:{rel}"], cwd=root, capture_output=True, text=True,
                      encoding="utf-8").stdout
        try:
            summary = json.loads(blob)
        except ValueError:
            continue
        rec = append_run(candidates_dir, summary, source=tag)
        if rec:
            added.append(rec)
    return added


# --------------------------------------------------------------------------------------- the report
def group_key(run):
    return (run.get("model") or "?", run.get("extract_model") or "-", run.get("prompt_version") or "?")


def summarise(runs):
    """Per (screening model, extraction model, prompt version): what the reader did and cost."""
    groups = {}
    for run in runs:
        g = groups.setdefault(group_key(run), {
            "runs": 0, "papers": 0, "decisions": {}, "accepted": 0, "rejected": 0, "cost": 0.0,
            "extracted": 0, "with_claims": 0, "kinds": {}, "dates": set()})
        g["runs"] += 1
        g["cost"] += float(run.get("cost_usd") or 0.0)
        if run.get("date"):
            g["dates"].add(run["date"])
        for p in run.get("papers", []):
            g["papers"] += 1
            d = p.get("decision") or "?"
            g["decisions"][d] = g["decisions"].get(d, 0) + 1
            g["accepted"] += p.get("accepted", 0)
            if d in DECISIONS_WITH_EXTRACTION:
                g["extracted"] += 1
                if p.get("accepted", 0):
                    g["with_claims"] += 1
            for r in p.get("rejected", []):
                g["rejected"] += 1
                g["kinds"][r["kind"]] = g["kinds"].get(r["kind"], 0) + 1
    return groups


def _per(numerator, denominator):
    return f"${numerator / denominator:.4f}" if denominator else "n/a"


def render(runs):
    if not runs:
        return "No reader runs are logged yet.\n"
    groups = summarise(runs)
    out = [f"Reader measurements from {len(runs)} logged run(s). Groups are (screening model, "
           f"extraction model, prompt version); a change to any of them is a new group.", ""]
    for key in sorted(groups, key=lambda k: min(groups[k]["dates"] or {"9999"})):
        g = groups[key]
        model, extract, prompt = key
        proposed = g["accepted"] + g["rejected"]
        rate = f"{100 * g['accepted'] / proposed:.0f}%" if proposed else "n/a"
        out += [f"== screen {model} | extract {extract} | prompt {prompt}",
                f"   runs {g['runs']} on {', '.join(sorted(g['dates'])) or '?'}; papers {g['papers']}; "
                f"decisions {dict(sorted(g['decisions'].items()))}",
                f"   extracted (read in full) {g['extracted']}, of which {g['with_claims']} gave at least one claim",
                f"   claims proposed {proposed}: accepted {g['accepted']}, rejected {g['rejected']} "
                f"(acceptance {rate})",
                f"   cost ${g['cost']:.4f} at paid list price; {_per(g['cost'], g['extracted'])} per paper "
                f"read in full (screening included), {_per(g['cost'], g['accepted'])} per accepted claim"]
        if g["kinds"]:
            out.append("   rejections by why the verifier refused them:")
            for kind, n in sorted(g["kinds"].items(), key=lambda kv: (-kv[1], kv[0])):
                out.append(f"      {n:3d}  {kind:22s} {KIND_NOTES.get(kind, '')}")
        out.append("")
    out.append("Not measured here: whether the ACCEPTED claims are true. Only a reader of the paper, or the "
               "paper-grounded check against a gold set, can say that.")
    return "\n".join(out) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--backfill-git", action="store_true",
                    help="add the runs already committed as _last_read.json (safe to repeat)")
    ap.add_argument("--candidates", default=str(ROOT / "corpus" / "candidates"))
    a = ap.parse_args(argv)
    if a.backfill_git:
        added = backfill_from_git(a.candidates)
        print(f"backfilled {len(added)} run(s) from git history")
    sys.stdout.reconfigure(encoding="utf-8")
    print(render(load_runs(a.candidates)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
