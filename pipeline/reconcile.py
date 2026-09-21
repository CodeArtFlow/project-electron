"""Stage 4: detect contradictions, hold their state, regenerate the open register.

Split the same way harvest is, and for the same reason. DETECTION is mechanical: two claims about
the same quantity under overlapping conditions whose si_base values disagree is arithmetic.
CLASSIFICATION is not: deciding whether that disagreement is a unit mismatch (D), a scopable
difference (C1), an unadjudicable one (C2), a supersession (B) or our own error (A) requires
reading both sources. So this module opens conflicts in `live:unexamined` - the error state - and
the `reconcile` skill classifies them.

A detector that also classified would be guessing, and CLAUDE.md rule 6 says guessing is the
failure mode this project exists to prevent.

Comparisons happen ONLY in si_base. Two claims are comparable when they share a quantity type and
their stated conditions do not conflict; claims measured under different conditions are not in
disagreement, they are about different things.

Usage:
    python pipeline/reconcile.py --detect      # open CFL records for new contradictions
    python pipeline/reconcile.py --register    # regenerate ledger/open-contradictions.md
    python pipeline/reconcile.py --check       # validate every CFL record's state
"""

import argparse
import re
import sys
from datetime import date, datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CLAIMS = ROOT / "ledger" / "claims"
CONFLICTS = ROOT / "ledger" / "conflicts"
REGISTER = ROOT / "ledger" / "open-contradictions.md"
PAPERS = ROOT / "corpus" / "papers"

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

RELATIVE_TOLERANCE = 0.05          # 5%: below this, two measurements agree for our purposes
MISSING_DATA = ("not-yet-measured", "undisclosed-method", "awaiting-confirmation", "access-blocked")
RESOLVED_REASONS = ("normalized", "scoped", "superseded", "our-error")
STATES = ("resolved", "live:data-absent", "live:unexamined")


def load_claims():
    out = {}
    for p in sorted(CLAIMS.glob("*.yaml")):
        doc = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        for c in doc.get("claims", []) or []:
            if c.get("id"):
                out[c["id"]] = c
    return out


def load_conflicts():
    out = []
    for p in sorted(CONFLICTS.glob("CFL-*.md")):
        text = p.read_text(encoding="utf-8")
        fm = {}
        if text.startswith("---"):
            parsed = yaml.safe_load(text.split("---")[1])
            if isinstance(parsed, dict):
                fm = parsed
        fm["__path__"] = p
        out.append(fm)
    return out


def next_conflict_id():
    highest = 0
    for p in CONFLICTS.glob("CFL-*.md"):
        try:
            highest = max(highest, int(p.stem.split("-")[1]))
        except (IndexError, ValueError):
            continue
    return f"CFL-{highest + 1:04d}"


# ------------------------------------------------------------------ comparability
def conditions_conflict(a, b):
    """True when two claims state DIFFERENT values for a condition they both name.

    Claims measured at different temperatures are not in disagreement - they are separate
    results. Only shared conditions with different values make a comparison invalid.
    """
    ca, cb = (a.get("conditions") or {}), (b.get("conditions") or {})
    for key in set(ca) & set(cb):
        if str(ca[key]).strip().lower() != str(cb[key]).strip().lower():
            return True
    return False


def comparable(a, b):
    qa, qb = a.get("quantity") or {}, b.get("quantity") or {}
    if not qa or not qb:
        return False
    if qa.get("quantity") != qb.get("quantity"):
        return False
    if (qa.get("si_base") or {}).get("unit") != (qb.get("si_base") or {}).get("unit"):
        return False
    return not conditions_conflict(a, b)


def disagree(a, b, tol=RELATIVE_TOLERANCE):
    va = (a["quantity"]["si_base"] or {}).get("value")
    vb = (b["quantity"]["si_base"] or {}).get("value")
    if va is None or vb is None:
        return False, None
    scale = max(abs(va), abs(vb)) or 1.0
    rel = abs(va - vb) / scale
    return rel > tol, rel


def independent(a, b, sources_meta):
    """Per CLAUDE.md: no shared corresponding author, no shared lead institution."""
    def meta(claim):
        auth, aff = set(), set()
        for sid in claim.get("sources", []) or []:
            m = sources_meta.get(sid, {})
            if not m.get("authors") or not m.get("affiliations"): return set(), set()
            auth |= set(m.get("authors", []))
            aff |= set(m.get("affiliations", []))
        return auth, aff
    aa, fa = meta(a)
    ab, fb = meta(b)
    return bool(aa and ab and fa and fb) and not (aa & ab) and not (fa & fb)


def source_meta():
    out = {}
    for p in PAPERS.glob("SRC-*.yaml"):
        rec = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        corr = [a for a in rec.get("authors", []) or [] if a.get("corresponding")]
        out[rec.get("id", p.stem)] = {
            "authors": [str(a.get("name", "")).strip().lower() for a in corr if a.get("name")],
            "affiliations": [str(a.get("affiliation", "")).strip().lower()
                             for a in corr if a.get("affiliation")],
        }
    return out


# ------------------------------------------------------------------ detection
def detect(claims, existing):
    """Open a CFL for every comparable, disagreeing pair not already tracked."""
    covered = set()
    for c in existing:
        ids = tuple(sorted(c.get("claims", []) or []))
        if len(ids) == 2:
            covered.add(ids)

    meta = source_meta()
    live = [c for c in claims.values()
            if c.get("status") in ("active", "challenged", "contested")]
    found = []
    for i, a in enumerate(live):
        for b in live[i + 1:]:
            pair = tuple(sorted([a["id"], b["id"]]))
            if pair in covered or not comparable(a, b):
                continue
            differs, rel = disagree(a, b)
            if not differs:
                continue
            found.append({
                "claims": list(pair), "relative_difference": round(rel, 4),
                "quantity": a["quantity"]["quantity"],
                "values": {a["id"]: a["quantity"]["si_base"], b["id"]: b["quantity"]["si_base"]},
                "independent": independent(a, b, meta),
                "grades": {a["id"]: a.get("grade"), b["id"]: b.get("grade")},
                "as_of": {a["id"]: str(a.get("as_of")), b["id"]: str(b.get("as_of"))},
            })
    return found


def write_conflict(finding):
    cid = next_conflict_id()
    a, b = finding["claims"]
    fm = {
        "id": cid,
        "state": "live:unexamined",
        "opened": date.today().isoformat(),
        "claims": finding["claims"],
        "quantity": finding["quantity"],
        "relative_difference": finding["relative_difference"],
        "independent_sources": finding["independent"],
        "detected_by": "pipeline/reconcile.py --detect",
    }
    body = f"""---
{yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()}
---

# {cid}

Two claims about **{finding['quantity']}** disagree by
{finding['relative_difference'] * 100:.1f}% in `si_base`, under conditions that do not conflict.

| Claim | si_base | grade | as_of |
|---|---|---|---|
| `{a}` | {finding['values'][a]['value']} {finding['values'][a]['unit']} | {finding['grades'][a]} | {finding['as_of'][a]} |
| `{b}` | {finding['values'][b]['value']} {finding['values'][b]['unit']} | {finding['grades'][b]} | {finding['as_of'][b]} |

Sources are {'independent' if finding['independent'] else 'not established independent'} (shared
corresponding author or lead institution collapses them into one source for supersession).

## State: `live:unexamined`

**This is the error state.** Detection is mechanical; classification is not. A human or the
`reconcile` skill must read both sources and classify this as Type D, C1, C2, B or A, then move
it to `resolved` or `live:data-absent` with a named `missing_data` gap. It blocks publication
until then.

## Classification

_Not yet classified._

## Resolution

_None yet._
"""
    (CONFLICTS / f"{cid}.md").write_text(body, encoding="utf-8")
    return cid


# ------------------------------------------------------------------ register
def regenerate_register(conflicts):
    live = [c for c in conflicts if str(c.get("state", "")).startswith("live:")]
    absent = [c for c in live if c.get("state") == "live:data-absent"]
    unexamined = [c for c in live if c.get("state") == "live:unexamined"]
    today = date.today()

    def age(c):
        try:
            return (today - datetime.fromisoformat(str(c.get("opened"))).date()).days
        except (TypeError, ValueError):
            return None

    lines = ["# Open Contradictions Register", "",
             "**Generated artifact — do not edit by hand.** Produced by "
             "`pipeline/reconcile.py --register` from `ledger/conflicts/`.", "",
             "A contradiction appears here if and only if the data to resolve it is absent, and "
             "that absence is named.", "", "---", "",
             f"## Status — {today.isoformat()}", ""]

    if unexamined:
        lines += [f"> **{len(unexamined)} conflict(s) in `live:unexamined`.** This is an error "
                  "state, not a category of contradiction: it means reconciliation is unfinished. "
                  "Publication is blocked until they are classified.", ""]
        for c in unexamined:
            lines.append(f"- `{c['id']}` opened {c.get('opened')} "
                         f"({age(c)} day(s) ago) — {', '.join(c.get('claims', []))}")
        lines.append("")

    if not absent:
        lines += ["**0 live contradictions with a named data gap.**", ""]
    else:
        lines += [f"**{len(absent)} live contradiction(s).** Each names the evidence that would "
                  "close it.", ""]
        for c in sorted(absent, key=lambda x: -(age(x) or 0)):
            lines += [f"### `{c['id']}` — {c.get('quantity', 'unspecified quantity')}", "",
                      f"- **claims:** {', '.join(c.get('claims', []))}",
                      f"- **gap:** {c.get('gap', '_unnamed — this is a defect_')}",
                      f"- **missing_data:** `{c.get('missing_data', 'UNSET')}`",
                      f"- **would be resolved by:** {c.get('resolution_trigger', '_unset_')}",
                      f"- **open for:** {age(c)} day(s) (since {c.get('opened')})", ""]

    buckets = {"under 7 days": 0, "7-30 days": 0, "30-90 days": 0, "over 90 days": 0}
    for c in absent:
        d = age(c) or 0
        key = ("under 7 days" if d < 7 else "7-30 days" if d < 30
               else "30-90 days" if d < 90 else "over 90 days")
        buckets[key] += 1
    lines += ["## Ageing", "", "| Bucket | Count |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in buckets.items()]

    cats = {m: sum(1 for c in absent if c.get("missing_data") == m) for m in MISSING_DATA}
    lines += ["", "## By gap category", "", "| Category | Count |", "|---|---|"]
    lines += [f"| `{k}` | {v} |" for k, v in cats.items()]
    lines.append("")
    REGISTER.write_text("\n".join(lines), encoding="utf-8")
    return len(absent), len(unexamined)


# ------------------------------------------------------------------ checks
def check(conflicts):
    problems = []
    for c in conflicts:
        cid = c.get("id") or c["__path__"].name
        state = c.get("state")
        if state not in STATES:
            problems.append(f"{cid}: state {state!r} not one of {STATES}")
        if state == "live:data-absent":
            if c.get("missing_data") not in MISSING_DATA:
                problems.append(f"{cid}: missing_data {c.get('missing_data')!r} invalid")
            if not c.get("gap"):
                problems.append(f"{cid}: live:data-absent without a named gap")
            if not c.get("resolution_trigger"):
                problems.append(f"{cid}: live:data-absent without a resolution_trigger")
        if state == "resolved" and c.get("resolution") not in RESOLVED_REASONS:
            problems.append(f"{cid}: resolved with reason {c.get('resolution')!r}, "
                            f"expected one of {RESOLVED_REASONS}")
        if not c.get("claims"):
            problems.append(f"{cid}: no claims referenced")
    return problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--detect", action="store_true")
    ap.add_argument("--register", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    if not any((a.detect, a.register, a.check, a.all)):
        ap.print_help()
        return 0

    CONFLICTS.mkdir(parents=True, exist_ok=True)
    rc = 0

    if a.detect or a.all:
        claims = load_claims()
        existing = load_conflicts()
        findings = detect(claims, existing)
        for f in findings:
            cid = write_conflict(f)
            print(f"  opened {cid}: {f['quantity']} differs by "
                  f"{f['relative_difference'] * 100:.1f}% ({', '.join(f['claims'])})")
        print(f"detect: {len(claims)} claims -> {len(findings)} new conflict(s)")

    if a.register or a.all:
        conflicts = load_conflicts()
        absent, unexamined = regenerate_register(conflicts)
        print(f"register: {absent} live:data-absent, {unexamined} live:unexamined "
              f"-> ledger/open-contradictions.md")

    if a.check or a.all:
        problems = check(load_conflicts())
        if problems:
            print(f"check FAILED - {len(problems)} problem(s):")
            for p in problems:
                print("  " + p)
            rc = 1
        else:
            print("check: every conflict record is well-formed")
    return rc


if __name__ == "__main__":
    sys.exit(main())
