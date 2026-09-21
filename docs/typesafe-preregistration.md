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

First live run: 2026-09-21, workflow run 35657438542, answers committed in `e89b20b`. 9 papers, 23 claims,
**0 errors**, 64,285 input tokens, about $0.003 at the documented price. Every request fit at the widest
context (1,500 characters either side of a quote). This section was written after the answers existed;
everything above it was committed before (`968421d`).

**A correction to this file, left visible.** The text above says "14 claims with a stated expectation". Its own
tables list **15** (8 expected low, 7 expected high). The count was my error. It matters for one thing: the
bar "12 or more right" was written for 14.

### Expectation 1: `is_result` (p that the excerpts show a reported result)

| Claim | Expected | TypeSafe p | |
|---|---|---|---|
| `CLM-MAT-0001` | low | 0.35 | right |
| `CLM-MAT-0002` | low | 0.25 | right |
| `CLM-MAT-0003` | low | 0.41 | right |
| `CLM-MAT-0004` | low | 0.37 | right |
| `CLM-DEV-0002` | low | 0.84 | **wrong** |
| `CLM-DEV-0003` | low | 0.66 | **wrong** |
| `CLM-DEV-0004` | low | 0.81 | **wrong** |
| `CLM-PROC-0001` | low | 0.44 | right |
| `CLM-ARCH-0007/0008/0009` | high | 0.89 / 0.93 / 0.88 | right |
| `CLM-ARCH-0012/0013/0014` | high | 0.93 / 0.94 / 0.95 | right |
| `CLM-MAT-0005` | high | 0.97 | right |

**12 of 15 right.** Against the bars as written: "12 or more" is **met by the letter**. The proportional
equivalent of 12 of 14 is 86%, which would be 13 of 15; 12 of 15 is 80%, so it is **short of the
proportion**. I am not choosing whichever reading flatters the result. It is a smoke test of 15 items and
it says the check is not at chance, nothing more.

The three misses are all the QLED paper. Reading its excerpt: the Methods say "QLEDs were fabricated on ITO
glass substrates with a sheet resistance of ∽20 Ω sq-1" and "custom high vacuum deposition chamber
(background pressure, ∽3 × 10 -7 torr)". These are fabrication conditions, so **the expectation was right
and TypeSafe was wrong.** One caution: "a result reported by the authors" can fairly be read to include
anything the authors state in Methods, so part of this miss may be the wording of my question, not only
TypeSafe. That is unresolved and is a reason to sharpen the question before phase 3.

### Expectation 2: the reader's evidence-type labels

- **`CLM-ARCH-0007/0008/0009` (labelled `measured`). Our label was wrong, and so was TypeSafe.** The excerpt's
  table caption reads "AREA AND POWER ARE SYNTHESIS RESULTS", from Synopsys Design Compiler on RTL: an
  EDA estimate, not silicon. The reader said `measured` and TypeSafe also said `measured` (0.54 to 0.77).
  **The expectation was right; TypeSafe did not catch this. A person reading the excerpt did.** Corrected to
  `simulated` on the three claims and on `SRC-00005`, non-public (never published), each with the paper's
  sentence as the reason.
- **`CLM-DEV-0002/0003/0004` (labelled `simulated`). The reader's label is wrong.** They come from the Methods
  of an experimental device paper. TypeSafe said `measured` (0.57 to 0.73), closer but not obviously right:
  a fabrication condition is neither a measurement nor a simulation. **Not corrected**, because the real
  question is whether fabrication-recipe details belong in the ledger at all, which is the user's decision
  (`TODO.md` D7).

### Expectation 3: unverified words

- `BLG` (`CLM-MAT-0002`) p=0.91, `QLEDs` (`CLM-DEV-0002`) p=0.94: established, as expected.
- **`CMOS` (`CLM-ARCH-0007`) p=0.18: TypeSafe was right and my expectation was wrong.** The excerpts contain
  no "CMOS" at all; the reading model supplied it (the paper says TSMC28HPC). This is the defect class the
  check exists for, found. Removed from the statement, non-public.
- `CLM-MAT-0003/0004` `support`: TypeSafe said `supports` at 0.97. I had pre-registered "uncertain" with no
  direction, so this is not a miss, but the guess that the definitions would fall outside the windows was
  not borne out.

### Other observations

- **13 of 23 claims flagged** (not the "flags everything" failure of the older audit's thresholds). By kind:
  not a reported result 5, "more than one thing" 5, evidence type 3, term 1, condition 1.
- The **`atomic` question is noisy.** `CLM-ARCH-0007` ("consumes 40.4 mW ... in 28nm at 500 MHz") is one
  assertion with its conditions, and it was flagged (p=0.26). What counts as one assertion needs a sharper
  definition before any threshold means anything.
- The **`unit` question worked** on the case that motivated it: the MiX `mW` is in a table header outside
  the quoted row, and TypeSafe answered 0.96 to 0.97 that the excerpts show it.

### What this run does and does not establish

- **Found:** one defect in the ledger by TypeSafe (`CMOS`), one by reading only (the synthesis label, where
  the reader and TypeSafe were wrong together), and evidence that the reader mislabels evidence type for
  claims from Methods sections.
- **A concrete instance of a principle in the plan:** two models agreeing is weak evidence. The reader and
  TypeSafe both said `measured` and both were wrong. Agreement can lower a claim's priority for review; it
  can never clear it.
- **Not established:** accuracy. 15 items on 6 papers, one at a time, is a smoke test. Nothing was
  calibrated and no threshold was tuned. The 0.5 cut is still a provisional line, not a measured one.
- **Next:** sharpen `is_result` and `atomic`, make the reader's evidence-type guidance explicit (synthesis and
  other EDA results are `simulated`), then phase 3 (a gold set) before anything is trusted quantitatively
  (`TODO.md` N10, N11, A1).
