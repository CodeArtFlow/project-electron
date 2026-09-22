# Reader v5: expectations, written BEFORE any live run

Addresses TODO `N15`, `N14`, `N13`. Written and committed 2026-09-22, the same day `reader-v4`'s
first live call (a targeted single-candidate run on `CAND-20260921-0042`, not the daily schedule)
produced the two defects this version fixes. Same practice as `docs/reader-v4-preregistration.md`
and `docs/typesafe-preregistration.md`: written first, corrected in place afterward if wrong.

## How these defects were found

Not from reading rejection statistics in bulk. A source and 6 claims were extracted **by hand**
from `CAND-20260921-0042` (an arXiv perovskite-photonics paper), independently, reading the full
fetched text before reader-v4's live result was known. The two sets were then compared. Reader-v4
had proposed exactly 1 claim for the whole paper and the verifier rejected it — net 0 claims,
against 6 hand-drafted and quote-verified. Reading why exposed two separate defects, not one.

## What changed, and the defect each change targets

| Change | TODO | Defect it targets | What it does |
|---|---|---|---|
| `STATEMENT_NUMBER_RE` replaces a bare `\d+(?:\.\d+)?` in `build_claim`'s statement-number check | N13 | The live rejection was "the statement contains the number 3, which none of its quotes contain" — the "3" in `CsPbBr3`, a chemical-formula subscript, not a measurement. Confirmed by direct test: `re.findall(r"\d+(?:\.\d+)?", "...CsPbBr3 nanocrystal is 4.9% to 5.2%...")` → `['3', '4.9', '5.2']`. Same failure class as N4's largest rejection bucket (its own examples, MoS2 and SrVO3, have this exact shape) | Skips a digit run immediately preceded by a letter with no space. A real value glued to its unit the other way round (`9.9x`, `20.8nm`) is unaffected — the digit there comes first |
| `evidence_type`/`evidence_span` moved from once-per-paper to once-per-claim in `extract_schema`, `SYSTEM` rule 6, and `build_claim` | N14 | The candidate mixes measured (CPL/HRTEM) and simulated (DFT/COMSOL) results — exactly what rule 6 already told the model to distinguish — but the paper-level field could only hold one answer. `extract_schema` already allowed `"mixed"` there, but `EVIDENCE_TYPES` (what the code actually checked) did not, so a `"mixed"` answer silently produced **zero** claims regardless of how many the model proposed. The model's only remaining option was picking one type for the whole paper, which the live run's single accepted-shape proposal (a measured claim, no simulated ones) is consistent with | Each claim now carries and verifies its own evidence_type/evidence_span independently. A paper's overall field may legitimately be `"mixed"`; a claim's own field may never be. An invalid per-claim evidence_type rejects only that claim, not the paper. The source record (whose schema has no `"mixed"` value) records the majority type among its accepted claims, with an `evidence_type_note` when they are not all one type |
| none (re-analysis only) | N15 | Measured ranges ("4.9-5.2%") looked like a schema gap requiring new range support | Re-reading `build_claim` shows a claim with no `quantity` block already skips the "no_condition" refusal and any per-number unit/bound check, verified purely by literal number-token presence in its quotes — a range already passes as an unstructured statement. The live rejection was entirely explained by N13 (the *statement's* digit, not the range's two numbers), not by any range-specific limitation. `test_a_measured_range_is_accepted_without_a_structured_quantity` locks this in as a regression test rather than a design change |

## Baseline: reader-v4's only live data point (2026-09-22, targeted single-candidate run)

`CAND-20260921-0042`, screen `gemini-3.5-flash-lite`, extract `gemini-3.6-flash`, prompt
`reader-v4`: 1 claim proposed, 1 rejected (the CsPbBr3 digit), 0 accepted. `n=1` paper — far too
small to be a rate, but it is the only live v4 data that exists, and it is the paper these fixes
were built against.

For a larger (but `reader-v3`) baseline, `docs/reader-v4-preregistration.md` recorded 42%
acceptance over 31 proposed claims across 11 papers.

## Expectations for the first live run

1. **The known CsPbBr3 rejection does not recur.** `CAND-20260921-0042` already carries a
   `read_decision` (`no_claims`), which means the daily sweep will not re-offer it automatically —
   the natural first test is a targeted `--candidate CAND-20260921-0042` run, not the next
   scheduled 06:45 UTC sweep. If the model proposes the same spacing-mismatch claim again, it
   should now be accepted (or rejected for some other, new reason worth reading — not this one).
2. **A mixed-evidence paper yields claims of more than one type.** On the same candidate, or the
   next one shaped like it (design/simulation validated by physical fabrication — an ordinary
   paper shape, not a rarity), accepted claims should include both `measured` and `simulated`
   entries when the paper's own content supports both, and the source record's
   `evidence_type_note` should be present when they do.
3. **Acceptance does not regress against the reader-v3 baseline (42%).** No existing rule was
   loosened, only two rejection paths corrected, so a comparable paper mix should not accept
   fewer claims than before. A drop is a reason to read the new rejections before trusting the
   number, per `read_report.py`'s discipline.
4. **No claim is accepted whose own evidence_type is unverified.** Spot-check any run for a claim
   whose `extraction.verified_quotes` implies an evidence_span was never checked — should not
   happen given `build_claim`'s new gate, but is cheap to confirm on the first live data.

## How the run is scored

Same as `reader-v4`'s: compare `_read_runs.jsonl` via `read_report.py`, read every rejection
rather than only counting it, and treat a surprising result as a reason to read the excerpt before
changing the prompt again.

## What would change the plan

- If the CsPbBr3 claim is still rejected for the same reason (expectation 1 fails), the regex
  exemption is wrong or insufficient — read the actual rejection reason before adjusting it again.
- If a mixed paper still yields only one evidence type (expectation 2 fails), either the model is
  not using the new per-claim freedom (a prompting problem) or a claim's own evidence_span is
  failing verification silently (a code problem) — `out.rejected` on that run distinguishes them.
- If acceptance drops (expectation 3 fails), read the new rejections in full before touching the
  prompt again, exactly as `reader-v4`'s own "what would change the plan" says.

## Suggested first live call

`python pipeline/read_paper.py --candidate CAND-20260921-0042 --require-key` — the exact candidate
these fixes were built against, so the comparison is direct rather than hoping a similarly-shaped
paper appears in the next sweep. Not run as part of this commit; local test coverage
(`test_reader.py`, 5 new tests: N13's formula-digit exemption and the number-glued-to-unit
counter-case, N14's mixed-paper acceptance and per-claim isolation, N15's range regression) is what
stands behind this change until it runs live.

## Results

Not yet run. This section is filled in after the first live `reader-v5` call, following the same
rule `docs/reader-v4-preregistration.md` and `docs/typesafe-preregistration.md` use: append, do
not rewrite the expectations above.
