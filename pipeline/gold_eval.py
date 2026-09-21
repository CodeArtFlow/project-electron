"""Score the TypeSafe semantic audit against the labelled gold set (reference/gold/).

WHY THIS EXISTS. The audit's review thresholds (0.9 confidence, 0.1 adverse) were set with no
data behind them, and on the first live run they flagged 12 of 12 publication documents, 7 of 7
extracted claims and 10 of 10 reconciliation pairs. A check that flags everything cannot tell a
defect from a clean page. docs/typesafe.md says a labelled semiconductor set must exist before the
thresholds are interpreted; this is the harness that uses it, and reference/semantic_policy.yaml
says the gate stays advisory until it can vouch for the numbers.

WHAT IT MEASURES. For each gold case the model's answers are compared with the labels, and two
detection rules are scored as classifiers of "does this case contain a real defect?":

    current       the audit exactly as shipped (any flag at all)
    confident     flag only if the model CONFIDENTLY gives an adverse answer at threshold tau,
                  swept from 0.5 to 0.95 - the middle ground between advisory and blocking

HONEST LIMITS, printed on every run:
  * The seed set is small. With n this low a single case moves a rate by 10-20 points.
  * The labels were written by the agent that made the extractions being judged, and have not been
    reviewed by anyone else.
  * Labels are relative to the evidence the audit is shown. It sees the record, never the paper,
    so a record that faithfully repeats a wrong abstract cannot be caught (see `blind_spot`).
  * The publication set has NO defective examples, so recall cannot be measured there and no
    threshold for those checks can be validated. That is the gap to close before `blocking`.

Usage:
    python pipeline/gold_eval.py --status
    python pipeline/gold_eval.py --score run/typesafe-all.json       # an existing audit report
    python pipeline/gold_eval.py --run                               # preview: build the requests
    python pipeline/gold_eval.py --run --live                        # spend API credits, then score
"""

import argparse
import json
import os
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

ROOT = Path(__file__).resolve().parent.parent
GOLD = ROOT / "reference" / "gold"
TAUS = (0.5, 0.6, 0.7, 0.8, 0.9, 0.95)
SMALL_N = 30

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

# noul answers are P(yes). For these, "yes" is the GOOD answer; every other noul is bad-if-yes.
YES_IS_GOOD = {"atomic", "gap_visible"}


def load_gold(root=ROOT, kinds=("extraction", "publication")):
    cases, provenance = [], None
    for kind in kinds:
        path = Path(root) / "reference" / "gold" / f"{kind}.yaml"
        if path.exists():
            doc = yaml.safe_load(path.read_text(encoding="utf-8"))
            provenance = provenance or doc.get("provenance")
            cases += doc.get("cases", [])
    return cases, provenance


def is_defective(case):
    """Does the gold say this case contains a real defect?"""
    L = case["labels"]
    if case["stage"] == "extraction":
        recorded = ((case.get("state") or {}).get("claim") or {}).get("evidence_type")
        return bool(L.get("support") in ("unsupported", "contradicts")
                    or L.get("conditions") == "unsupported"
                    or L.get("numbers") == "distorted"
                    or L.get("atomic") is False
                    or (recorded and L.get("evidence_type") not in (recorded, "unknown")))
    return bool(L.get("faithful") != "supports" or L.get("overstates") is True
                or L.get("gap_visible") is False)


def match(report, cases, check_fingerprint=True):
    """Pair gold cases with usable audit records. Returns (pairs, skipped-with-reasons)."""
    by_id = {r["id"]: r for r in report.get("records", [])}
    pairs, skipped = [], []
    for case in cases:
        rec = by_id.get(case["audit_id"])
        if rec is None:
            skipped.append((case["id"], "not in the report"))
        elif not rec.get("response"):
            skipped.append((case["id"], f"no model response (status {rec.get('status')})"))
        elif check_fingerprint and rec.get("fingerprint") != case.get("fingerprint"):
            skipped.append((case["id"], "input changed since it was labelled; the label no longer applies"))
        else:
            pairs.append((case, rec))
    return pairs, skipped


def current_flags(rec):
    """The flags the audit as shipped raises for this record (same routing code, same thresholds)."""
    from semantic_checks import route
    job = {"stage": rec["stage"], "request": rec["request"], "required": rec.get("required", False),
           "missing": rec.get("missing", [])}
    return route(job, rec["response"])["flags"]


def agreement(pairs):
    """Per question: does the model's answer match the label?"""
    stats = {}
    for case, rec in pairs:
        for q, label in case["labels"].items():
            a = rec["response"]["answers"].get(q)
            if a is None:
                continue
            if a["type"] == "noul":
                ok = (a["noul"] >= 0.5) == bool(label)
                conf = a["noul"] if label else 1 - a["noul"]
            else:
                ok = a["choice"] == label
                conf = a["confidence"]
            s = stats.setdefault((case["stage"], q), {"n": 0, "ok": 0, "conf_ok": [], "conf_bad": [],
                                                      "wrong": []})
            s["n"] += 1
            s["ok"] += ok
            (s["conf_ok"] if ok else s["conf_bad"]).append(conf)
            if not ok:
                said = f"{a['noul']:.2f}" if a["type"] == "noul" else a["choice"]
                s["wrong"].append((case["id"], label, said, conf))
    return stats


def confident_adverse(rec, tau):
    """Would a 'block only on confident adverse answers' rule flag this record at threshold tau?"""
    ans = rec["response"]["answers"]
    hit = False
    if rec["stage"] == "extraction":
        claim = (rec["request"]["state"].get("claim") or {})
        for q, bad in (("support", ("unsupported", "contradicts")), ("conditions", ("unsupported",)),
                       ("numbers", ("distorted",))):
            hit |= ans[q]["choice"] in bad and ans[q]["confidence"] >= tau
        e = ans["evidence_type"]
        hit |= e["choice"] not in (claim.get("evidence_type"), "unknown") and e["confidence"] >= tau
        hit |= ans["atomic"]["noul"] <= 1 - tau
    else:
        f = ans["faithful"]
        hit |= f["choice"] in ("unsupported", "contradicts") and f["confidence"] >= tau
        hit |= ans["overstates"]["noul"] >= tau
        hit |= ans["gap_visible"]["noul"] <= 1 - tau
    return hit


def confusion(pairs, rule):
    tp = fp = fn = tn = 0
    for case, rec in pairs:
        flagged, defect = rule(rec), is_defective(case)
        tp += flagged and defect
        fp += flagged and not defect
        fn += (not flagged) and defect
        tn += (not flagged) and not defect
    return tp, fp, fn, tn


def rate(a, b):
    return "  n/a" if b == 0 else f"{100 * a / b:4.0f}%"


def render(pairs, skipped, title):
    out = [f"== {title} ==", ""]
    n_def = sum(is_defective(c) for c, _ in pairs)
    out.append(f"cases scored: {len(pairs)}  ({n_def} with a real defect, {len(pairs) - n_def} clean); "
               f"skipped: {len(skipped)}")
    for cid, why in skipped:
        out.append(f"  skipped {cid}: {why}")
    out += ["", "-- does the model's answer match the label? (ignores confidence) --",
            f"{'stage':<12}{'question':<16}{'n':>3} {'agree':>6}   mean confidence when right / wrong"]
    for (stage, q), s in sorted(agreement(pairs).items()):
        mo = f"{sum(s['conf_ok']) / len(s['conf_ok']):.2f}" if s["conf_ok"] else " - "
        mb = f"{sum(s['conf_bad']) / len(s['conf_bad']):.2f}" if s["conf_bad"] else " - "
        out.append(f"{stage:<12}{q:<16}{s['n']:>3} {rate(s['ok'], s['n']):>6}   {mo} / {mb}")

    wrong = [(stage, q, w) for (stage, q), s in sorted(agreement(pairs).items()) for w in s["wrong"]]
    if wrong:
        out += ["", "-- answers that DISAGREE with the label: either the model or the label is wrong --"]
        for stage, q, (cid, label, said, conf) in wrong:
            out.append(f"  {cid:<18}{q:<14} label={label!s:<12} model={said!s:<12} confidence {conf:.2f}")
        out.append("  An independent reviewer should settle each of these first. A confident model "
                   "answer that contradicts a label is a reason to doubt the LABEL as much as the model.")

    out += ["", "-- as a detector of a real defect --",
            f"{'rule':<26}{'flagged':>8} {'caught':>7} {'false alarm':>12}   (tp fp fn tn)"]
    rows = [("current (any flag)", lambda r: bool(current_flags(r)))]
    rows += [(f"confident adverse >= {t:.2f}", (lambda t: lambda r: confident_adverse(r, t))(t)) for t in TAUS]
    for name, rule in rows:
        tp, fp, fn, tn = confusion(pairs, rule)
        out.append(f"{name:<26}{tp + fp:>8} {rate(tp, tp + fn):>7} {rate(fp, fp + tn):>12}   ({tp} {fp} {fn} {tn})")

    def who(rule):
        miss = [c["id"] for c, r in pairs if is_defective(c) and not rule(r)]
        alarm = [c["id"] for c, r in pairs if not is_defective(c) and rule(r)]
        return miss, alarm
    miss, alarm = who(lambda r: confident_adverse(r, 0.5))
    out += ["", f"at 'confident adverse >= 0.50': missed {miss or 'none'}; false alarms {alarm or 'none'}"]

    out += ["", "-- caveats (always shown) --",
            f"* n = {len(pairs)}: a seed, not a benchmark. Below ~{SMALL_N} a single case moves a rate by 10-20 points.",
            "* Labels are by the agent that made the extractions, and NOT independently reviewed.",
            "* Labels are relative to the record the audit sees, not the paper (see blind_spot notes)."]
    stages = {c["stage"] for c, _ in pairs}
    for stage in sorted(stages):
        if not any(is_defective(c) for c, _ in pairs if c["stage"] == stage):
            out.append(f"* '{stage}' has NO defective examples: recall cannot be measured, so no "
                       f"threshold for it can be validated.")
    blind = [c["id"] for c, _ in pairs if c.get("blind_spot")]
    if blind:
        out.append(f"* Documented blind spots (invisible to a record-only audit): {', '.join(blind)}")
    return "\n".join(out)


def status(cases, provenance):
    by = {}
    for c in cases:
        k = by.setdefault(c["stage"], {"n": 0, "defective": 0})
        k["n"] += 1
        k["defective"] += is_defective(c)
    lines = ["gold set status", ""]
    for stage, k in sorted(by.items()):
        lines.append(f"  {stage:<12} {k['n']:>3} cases, {k['defective']} with a real defect")
    lines += ["", f"labelled by : {(provenance or {}).get('labelled_by')}",
              f"review      : {(provenance or {}).get('independent_review')}",
              "", "Needed before the audit can move from advisory to blocking:",
              f"  * at least {SMALL_N} cases per blocking stage",
              "  * defective examples for every stage that can block (publication has none)",
              "  * independent review of the labels"]
    return "\n".join(lines)


def build_jobs_from_gold(cases):
    """Rebuild audit requests from the gold cases' FROZEN inputs, asking today's questions."""
    from semantic_checks import extraction_questions, job
    return [job(c["audit_id"], "extraction", c["state"], extraction_questions(), True)
            for c in cases if c["stage"] == "extraction" and c.get("state")]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--score", metavar="REPORT.json")
    ap.add_argument("--run", action="store_true", help="re-run the audit on the gold inputs")
    ap.add_argument("--live", action="store_true", help="with --run: call the API (needs TYPESAFE_API_KEY)")
    ap.add_argument("--max-calls", type=int, default=30)
    ap.add_argument("--seconds", type=int, default=120)
    a = ap.parse_args()

    cases, provenance = load_gold()
    if a.status or not (a.score or a.run):
        print(status(cases, provenance))
        return 0

    if a.score:
        report = json.loads(Path(a.score).read_text(encoding="utf-8"))
        pairs, skipped = match(report, cases, check_fingerprint=True)
        print(render(pairs, skipped, f"audit report {Path(a.score).name} ({report.get('version')}, "
                                     f"{report.get('mode')}) vs gold"))
        return 0

    from semantic_checks import run
    if a.live and not os.environ.get("TYPESAFE_API_KEY"):
        sys.exit("--live needs TYPESAFE_API_KEY in the environment (never in a file or in chat)")
    jobs = build_jobs_from_gold(cases)
    report = run(jobs, {"gold_cases": len(jobs)}, ROOT, live=a.live, max_calls=a.max_calls,
                 seconds=a.seconds)
    out = ROOT / "run" / "typesafe-gold.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"built {len(jobs)} requests from frozen gold inputs; mode={report['mode']}; "
          f"calls={report['calls']}; status={report['status_counts']}  -> {out.relative_to(ROOT)}")
    if not a.live:
        print("preview only: no API calls were made. Add --live to score the model on them.")
        return 0
    # The gold inputs are frozen, so match by id: the question wording may have moved on since the
    # cases were first labelled, but the labelled INPUT is the same.
    pairs, skipped = match(report, [c for c in cases if c["stage"] == "extraction"], check_fingerprint=False)
    print()
    print(render(pairs, skipped, "live re-run on frozen gold inputs"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
