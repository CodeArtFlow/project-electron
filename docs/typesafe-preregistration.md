# TypeSafe paper-grounded check: expectations, written BEFORE the first live run

Phase 2 of `docs/typesafe-plan.md`. Written 2026-09-21 and committed before any TypeSafe answer exists,
so the run tests TypeSafe (and our reader) and not our reading of the result.

## What these expectations are, and are not

They come from **the wording of the claims and from what such tables usually are.** They do **not** come
from having read the papers, and general knowledge is not a source here (`AGENTS.md`, "Model memory is
not a source"). They are hypotheses. When TypeSafe and an expectation disagree, neither is presumed
right: a person reads the excerpt (the answers file records exactly which positions in the paper were
sent) and decides. That reading, not this file, is what settles any case.

## Expectation 1: input parameters are not results (`is_result`)

Claims that look like inputs, settings or specifications. TypeSafe should judge that the excerpts do
**not** show a reported result (`is_result` below 0.5):

| Claim | Why it looks like an input |
|---|---|
| `CLM-MAT-0001`, `-0002` | Phonon energies: rows of a parameter table |
| `CLM-MAT-0003`, `-0004` | "Temperature used in the calculations": a setting |
| `CLM-DEV-0002`, `-0004` | Base pressure of a deposition chamber: fabrication conditions |
| `CLM-DEV-0003` | Sheet resistance of the ITO-coated glass: a substrate specification |
| `CLM-PROC-0001` | "Thermalized to 300 K" in a simulation: a setting |

Claims that look like reported results. TypeSafe should judge that the excerpts **do** show a result
(`is_result` at or above 0.5):

| Claim | Why it looks like a result |
|---|---|
| `CLM-ARCH-0007`, `-0008`, `-0009` | Power from an RTL synthesis table |
| `CLM-ARCH-0012`, `-0013`, `-0014` | Total latency of three architectures |
| `CLM-MAT-0005` | A computed lifetime |

That is **14 claims with a stated expectation.** Not pre-registered, because I could not judge them from the
wording: the PHOT claims, `CLM-DEV-0005/0006`, `CLM-ARCH-0010/0011`.

## Expectation 2: the reader's evidence-type labels may be wrong (`evidence_type`)

This one is a hypothesis about **our reader**, not about TypeSafe.

- `CLM-DEV-0002/0003/0004` are labelled `simulated`, but they read as fabrication conditions from an
  experimental device paper. If TypeSafe says anything other than `simulated`, the excerpts should be
  read; I expect the reader's label to be wrong.
- `CLM-ARCH-0007/0008/0009` are labelled `measured`, but RTL synthesis reports estimates, not silicon
  measurements. I expect TypeSafe to say `simulated`. If it does, and a reading confirms it, then the
  `evidence_type` on those claims is our error and gets a correction entry.

## Expectation 3: unverified words in statements

- `CLM-MAT-0002` says "in BLG"; `BLG` is not in its verified quote. The excerpts include the paper's
  opening (title and abstract), which probably define it, so I expect `BLG` to be **established**
  (`term` at or above 0.5). If it is not, the abbreviation is defined outside the excerpts, and that
  says something about excerpt coverage as much as about the claim.
- `CLM-ARCH-0007` says "28nm CMOS"; `CMOS` is not in its quote. Expected established. `QLEDs` on
  `CLM-DEV-0002` likewise.
- The acoustic-phonon wording of `CLM-MAT-0003` and "optical phonon and surface polar phonon" of
  `-0004` translate the paper's "AP" and "OP and SPP". The definitions may be outside the windows, so I
  expect `support` on these two to be **uncertain**, and pre-register no direction for them.

## How the run is scored

Per question type, counting only the pre-registered claims:

- `is_result`: a claim counts as right if TypeSafe's side of 0.5 matches the expectation.
  **Of the 14: 12 or more right is encouraging; 9 or fewer right is no better than a coin.** With 14
  items this is a smoke test. It cannot calibrate anything (that is phase 3) and one item moves it by
  seven points.
- Every disagreement is settled by reading the excerpt, and the outcome is recorded here as **TypeSafe
  right, expectation right, or the excerpt could not settle it.** The last is a finding about excerpts.
- Cost, request size and how many questions returned confident answers are recorded. Confidence is
  reported per question as it comes, with no threshold applied until phase 3.

## What would change the plan

- If `is_result` is near chance, the paper-grounded check is not useful as designed, and we stop and
  reconsider before building more (`docs/typesafe-plan.md`, section 9).
- If TypeSafe is right where our reader was wrong (Expectation 2), the labels are corrected through the
  normal `corrections` mechanism, and that is a result for the reader, not only for TypeSafe.
- If the excerpts often cannot settle a case, the windows are too narrow: widen the context steps and
  try again, recording that the first run used the narrower ones.

## Results

_Not yet run. Filled in below after the first live run, whichever way it falls._
