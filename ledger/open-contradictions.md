# Open Contradictions Register

**Generated artifact — do not edit by hand.** Derived from `ledger/conflicts/CFL-*.md` by the
`reconcile` skill on every cycle. Editing this file directly creates a second source of truth and
is itself the defect the project exists to prevent.

Per CLAUDE.md, a contradiction appears here if and only if the data to resolve it is absent, and
that absence is named. Everything below is a live disagreement we have examined and cannot close
with available evidence — not a backlog of unfinished work.

---

## Status — 2026-09-20

**0 live contradictions.** The corpus is empty; no claims have been made yet.

This is an honest zero, not a clean bill of health. Nothing has been harvested, so nothing could
contradict anything. The first non-trivial reading of this register comes after the first harvest.

**The generator does not exist yet.** `reconcile` has not been built, so this file is a
hand-written placeholder standing in for a derived artifact — a temporary violation of the rule
at the top of this page. It is recorded here rather than left implicit, and it closes when
`reconcile` lands.

---

## Register format

Once populated, each entry carries:

| Field | Meaning |
|---|---|
| `id` | `CFL-nnnn` |
| `opened` | Date the contradiction was detected |
| `age` | Days open — displayed, never hidden |
| `topic` | Topic code |
| `claims` | The competing claim IDs, with grade and credibility tier for each |
| `type` | `C2` (unadjudicable) or `B-single` (awaiting confirmation) |
| `missing_data` | `not-yet-measured` · `undisclosed-method` · `awaiting-confirmation` · `access-blocked` |
| `gap` | The absent evidence, in plain language |
| `resolution_trigger` | What would close this |
| `last_reviewed` | Date of last re-examination |

---

## Ageing summary

| Bucket | Count |
|---|---|
| Under 7 days | 0 |
| 7–30 days | 0 |
| 30–90 days | 0 |
| Over 90 days | 0 |

## By gap category

| Category | Count | Reading |
|---|---|---|
| `not-yet-measured` | 0 | The field hasn't run the experiment |
| `undisclosed-method` | 0 | Sources withhold what's needed to compare |
| `awaiting-confirmation` | 0 | One source unreplicated |
| `access-blocked` | 0 | Evidence likely exists behind a paywall — the cost of open-access-only |
