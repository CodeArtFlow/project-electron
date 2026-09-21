# TODO — Project Electron

Last updated: 2026-09-21 (UTC), from the repository as it then stood.

**What this file is.** The tracker for *work*: what is blocked, what is in flight, what is next, and
what could bite us. **Rules** live in `AGENTS.md`. **Facts about the current state** (counts, measured
costs, what was learned) live in `AGENTS.md`, "Current state". This file points at them and does not
restate either, because a second copy is a contradiction waiting to happen. When work lands, tick it
here and update "Current state" there. Item ids (`D1`, `F1`, ...) are stable: never reused.

Legend: `[ ]` open · `[~]` in progress · `[x]` done · **BLOCKED** = waiting on a decision only the user can make.

---

## 0. Blocking publication right now

- [x] **B1. (Cleared 2026-09-21.) Six conflicts were `live:unexamined`, so every deploy was blocked** (`CFL-0006..0011`, opened by
  the scheduled reading run on 2026-09-21; the run's deploy failed at check 1 of the gate, and the live
  site is still the last good build, `29a08cd`). This is the doctrine working, not a bug. Read them:
  five are between claims from *different* papers that only share a generic quantity name (`time`,
  `temperature`) and no condition that says they concern the same thing; `CFL-0011` is two different
  mode spacings (Ω1, Ω2) of one photonic molecule with identical structured conditions.
  The cause was fixed first (D1, N1), then all six were closed as `scoped`. Done when the guard is
  deployed and the gate passes on `main`; see B2 for the schedule.
- [x] **B2. The daily reading workflow was paused, and is re-enabled** (paused 2026-09-21 at the user's
  decision so no more false conflicts accumulated; re-enabled once the guard had deployed and the gate
  passed on `main`, `3c551e5`). The next scheduled run is the first under the guard: read its result
  (`corpus/candidates/_last_read.json`, the conflicts it opened, and `ledger/not-compared.md`).

## 1. Needs your decision

- [x] **D1. How should comparability be decided?** Decided 2026-09-21: **a deterministic guard first.**
  Two claims are compared only if they share subject context (at least one condition key that is not an
  operating-point key, with an equal value). Pairs that disagree numerically but share none are logged
  visibly as *not compared*, never dropped. TypeSafe pair triage can refine it later (plan, family D).
  The reading schedule is paused meanwhile (B2).
- [x] **D2. The TypeSafe plan** (`docs/typesafe-plan.md`) is approved, filtered excerpts and numeric
  checks kept in code. **Claims against the paper are built first** (phase 1), after N1.
- [ ] **D3. Independence for arXiv-only sources.** arXiv states no corresponding author, and `reconcile`
  correctly treats missing metadata as not-independent, so no arXiv-only supersession can ever happen
  (`AGENTS.md`, open decisions). Choose a fallback rule, or wait for author records (A3).
- [ ] **D4. Should CI regenerate the SOTA, synthesis and digest after reading?** Today only
  `run_pipeline.py` does, so claims reach the ledger but the site's pages lag (they still say
  "3 source records"). Build it, or keep it a manual step? If built: who may publish a daily digest,
  given that a published digest is never rewritten?
- [ ] **D5. Reading throughput.** 25 papers a run against about 33 arXiv candidates a day
  (`AGENTS.md`); 117 arXiv candidates are unread. A second daily run would keep pace and the money
  allows it (estimate, see `AGENTS.md`). A deliberate edit of `read.yml`.
- [ ] **D7. Do fabrication-recipe details belong in the ledger?** `CLM-DEV-0002..0004` (a deposition
  chamber's base pressure, an ITO substrate's sheet resistance, a device area) are stated in the Methods of
  an experimental paper. They are true of the paper, but they are procedure, not findings, and no
  evidence-type label fits them (`simulated` is wrong; `measured` is not right either). Options: keep them
  with a corrected label, retract them, or tell the reader not to extract procedure parameters. Nothing
  published cites them.
- [ ] **D6. Publisher lane.** 197 candidates are unread and mostly bot-walled (about 25% fetchable).
  Choose a legitimate full-text route, or accept human reading (`harvest` skill).

## 2. Your actions (I cannot do these)

- [ ] **U1. Set Google's own monthly spend cap** (AI Studio > Spend > Monthly spend cap, or prepaid billing
  with auto-reload off). Ours is the second line of defence (`AGENTS.md`, "Reader budget").
- [ ] **U2. Optional: a free Semantic Scholar key**, an enhancement to discovery, not a blocker.

## 3. In flight

- [x] **F1. TypeSafe paper-grounded check, phases 1 and 2: done 2026-09-21.** Built, then run live once on
  9 papers (about $0.003) against expectations committed first: 12 of 15 on `is_result`, one real defect
  found by TypeSafe (`CMOS`), one found only by reading (the MiX synthesis results labelled `measured` by
  both the reader and TypeSafe), corrections applied. Results and caveats:
  `docs/typesafe-preregistration.md`. Next is phase 3 (A1: a gold set).

## 4. Next up, in order

- [x] **N1. Fix comparability (D1).** Done 2026-09-21: `reference/comparability.yaml`, rule 3 in
  `reconcile.py`, the visible `ledger/not-compared.md`, 15 tests including the six real pairs and a
  real contradiction that is still found. `CFL-0006..0011` closed as `scoped` (five by the guard, one by
  hand-scoping `CLM-PHOT-0002/0003`). Its known limit is N3.
- [ ] **N2. Reader: unit parsing costs recall.** Refused so far for units we could parse but do not:
  `˚A`/`Å` spellings, `mm2`, `Ω sq-1`, `me`, `TFLOP...`, and `dB` mapped onto a power quantity. Add
  aliases with tests; refuse everything else as now.
- [ ] **N3. Reader: a distinguishing condition is required, not enforced.** `reader-v3` demands at least
  one verified condition, but `CLM-PHOT-0002/0003` carry identical conditions for different spacings
  (Ω1, Ω2). The verifier cannot tell whether a condition distinguishes. Candidates: ask for the symbol or
  label as a condition; TypeSafe question per claim (plan, family B).
- [ ] **N4. Reader: measure it.** Keep a per-run record of accepted and rejected counts and reasons by
  model and prompt version (the numbers are in `_last_read.json` history) so a change to a model, thinking
  level or prompt is judged on data. First reading: 12 of 25 out of scope, 5 `no_claims`, 2 `too_long`,
  6 read, 13 accepted, 18 rejected.
- [ ] **N5. `no_claims` papers (8) and `too_long` papers (2) are parked, not lost.** Decide who takes
  them: a stronger model, a higher thinking level, or a human. `too_long` skips at 120,000 characters
  and never truncates.
- [ ] **N6. Research checks page** shows the audit's markdown in a `<pre>` (`build_site.py`); render it.
- [ ] **N7. TypeSafe plan, phases 2 to 6** (`docs/typesafe-plan.md`). Approved (D2). Phase 1 is built (F1).
- [ ] **N8. Units are not verified against quotes.** The verifier proves a number is in its quote, not the
  unit: the MiX power figures' `mW` is in a table header, outside the quoted row. Phase 1 asks TypeSafe
  whether the excerpts show the unit; whether code should also check is open.
- [x] **N9. Evidence-type labels on some claims (settled by reading the excerpts).** `CLM-ARCH-0007..0009`
  and `SRC-00005` were `measured`; the paper says the figures are synthesis results, so they are now
  `simulated` (non-public corrections). `CLM-DEV-0002..0004` are `simulated` but are fabrication
  conditions of an experimental paper: **not corrected, waiting on D7.**
- [ ] **N10. Reader: evidence-type guidance.** The model called synthesis results `measured` and
  fabrication conditions `simulated`. Make the rule explicit in the prompt (synthesis and other EDA-tool
  results are `simulated`; a paper's fabrication recipe is not a measurement) and measure it (N4). A
  change to the prompt is a new prompt version.
- [ ] **N11. TypeSafe questions to sharpen before any threshold is set:** `is_result` (TypeSafe read the QLED
  Methods conditions as reported results; part of that may be my wording) and `atomic` (flagged
  `CLM-ARCH-0007`, which is one assertion with its conditions). Phase 3.

## 5. Assurance and calibration

- [ ] **A1. Gold set.** Independent review of the labels (today: labelled by the agent that built the
  pipeline); at least 30 cases per stage that could block; defective *publication* examples (there are
  none); paper-grounded cases for the plan. Until then the semantic audit stays advisory
  (`reference/semantic_policy.yaml`).
- [ ] **A2. Statements can carry words the anchor quotes lack** ("in BLG"; "acoustic phonon" for the
  paper's "AP"). The verifier checks numbers and quotes, not every word. Noted in the corrections of
  `CLM-MAT-0001..0004`. Test with the TypeSafe check (plan) or a deterministic content-word overlap.
- [ ] **A3. `assess-source` skill and author records.** Needed for credibility tiers and for
  independence (D3). Every claim is `credibility: unknown` today.
- [ ] **A4. `verify-citation` skill** (audit: does a source say what we claim?). Not built.
- [ ] **A5. Only grade B so far.** Every claim comes from an arXiv preprint. No peer-reviewed venue has
  been read, which is D6.
- [ ] **A6. Coverage is 5 of 10 layers** (ARCH, DEV, MAT, PHOT, PROC). None for LITHO, PKG, MEM, EDA,
  ECON. The synthesis page must keep saying it describes our corpus, not the field.

## 6. Hygiene and watch-list

- [ ] **H1. 2027-01-01: the extraction model's price doubles** (`reference/reader_budget.yaml`). Re-check
  the budget then; the pacing will throttle rather than overspend.
- [ ] **H2. Price table freshness.** `budget.py` warns after 180 days. Re-verify against Google's page.
- [ ] **H3. Google's docs are not proof a model can be called** (`gemini-2.5-flash`, "stable", was refused
  to this project). Any new model gets a small live run first.
- [ ] **H4. Node 20 deprecation warnings** on Actions (`checkout@v4`, `setup-python@v5`, and others).
  Check what current versions exist before changing any.
- [ ] **H5. Harvest sweep names candidate ids with the local date**, the digests use UTC.
- [ ] **H6. Keep `AGENTS.md` "Current state" true** whenever a stage lands. It has gone stale repeatedly
  as the counts moved.
- [ ] **H7. Registry:** four venues block automated access (TechRxiv, ChemRxiv, Intel, Applied
  Materials) and two never answered. Not evaded. Need a legitimate route.

## 7. Done recently (2026-09-21)

Detail is in git history and `AGENTS.md`. Commits are on `main`.

- [x] Corrected published ARCH claims; bound qualifier; corrections trail; digest immutability (`21a914b`).
- [x] `AGENTS.md` is the single source of doctrine; `CLAUDE.md` imports it (`525c300`); skills mirror
  with a CI guard (`70c2f26`).
- [x] Monthly reader budget: checked before every call, paced, fails closed (`6322285`).
- [x] Reader on Gemini; live call proved (`8089fea`). Google refused `gemini-2.5-flash`; moved to
  `gemini-3.5-flash-lite` (`c9ada74`).
- [x] A paper with no accepted claim is kept, not retired; four empty records withdrawn (`3a3d663`).
- [x] Screening on Flash-Lite, extraction on `gemini-3.6-flash` (`3a96164`): 10 claims from 3 papers
  where Flash-Lite gave none.
- [x] Four false conflicts scoped and closed; conditions stated twice must agree (`dabaab4`).
- [x] Reader `reader-v3`: a number needs a verified condition (`29a08cd`).
- [x] The scheduled daily sweep and reading now run on their own (first scheduled reading: 13:21 UTC).
- [x] `docs/typesafe-plan.md` and this file.
