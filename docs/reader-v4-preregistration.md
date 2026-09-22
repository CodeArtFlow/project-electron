# Reader v4: expectations, written BEFORE any live run

Addresses TODO `N3`, `N10`, `N12` and the reader-guidance half of `D7`. Written and committed
2026-09-22, before `reader-v4` has read a single paper live, so a future run tests the prompt
change (and our reading of it) rather than confirming whatever we already believe. Same practice
as `docs/typesafe-preregistration.md`: written first, corrected in place afterward if wrong.

**Update, 2026-09-22, same day:** the user initially asked to hold the live spend for a separate
go-ahead, then, asked directly whether to push this to `main` given the code and the daily
schedule are in the same file (`read.yml`), chose to push and let `reader-v4` run on the next
scheduled 06:45 UTC read rather than pause the schedule first. So the "suggested first live call"
below was **not** run by hand as a small cautious test before the scheduled run reads live with
it — the first live data on `reader-v4` will be that scheduled run. Score it against the baseline
and expectations below exactly as planned; nothing about the expectations or scoring changes,
only that the first data point comes from the daily schedule instead of a hand-run small batch.

## What changed, and the defect each change targets

All four are additions to `SYSTEM` in `pipeline/read_paper.py` (rules 4, 6, 11, 12). None removes
or loosens a `reader-v3` rule, so nothing that was rejected before should now be accepted, only
the reverse or no change.

| Rule | TODO | Defect it targets | What it asks for |
|---|---|---|---|
| 4 (extended) | N3 | `CLM-PHOT-0002/0003`: two mode spacings (Ω1, Ω2) got the *same* condition category ("mode spacing"), which satisfied v3's "a condition that distinguishes" without distinguishing anything | The paper's own symbol or label, not just a category name |
| 6 (extended) | N10 | `CLM-ARCH-0007..0009`: an RTL-synthesis table was labelled `measured`, caught only by a human reading the excerpt after TypeSafe missed it too | Synthesis/EDA-tool output is named `simulated` explicitly |
| 11 (new) | D7 | `CLM-DEV-0002..0004`: fabrication-recipe values (deposition pressure, sheet resistance) extracted as freestanding claims with no result to attach to; retracted 2026-09-22 | A fabrication/setup value is a `conditions` entry on a result claim, never a claim of its own |
| 12 (new) | N12 | 8 of 18 rejections in the `reader-v3` baseline below are a statement naming a number, material or model that no quote contains; the prompt never said the statement itself is checked | States plainly that the statement is checked the same way conditions are |

## Baseline, measured before this change (`pipeline/read_report.py`, run 2026-09-22)

The only `reader-v3` group with enough volume to compare against: screen
`gemini-3.5-flash-lite`, extract `gemini-3.6-flash`, prompt `reader-v3`. 25 papers, 11 read in
full, 6 gave at least one claim.

- **Acceptance: 13 of 31 proposed claims (42%).**
- Rejections (18 total): `number_not_in_quotes` 8, `no_condition` 3, `unit_unparsed` 3,
  `value_not_in_quotes` 2, `quote_not_found` 1, `unit_incompatible` 1.
- `number_not_in_quotes` and `value_not_in_quotes` together (10 of 18, 56%) are the rule-12
  target: a statement or its recorded value naming something no quote backs.
- `no_condition` (3 of 18, 17%) is adjacent to rule 4/11: a number offered with nothing that
  tells it apart from the paper's other numbers, or with nothing but a bare setup value.

These are small counts from one run of one paper mix — `docs/typesafe-preregistration.md`'s own
caution applies here too: this is a smoke test, not a calibration, and a couple of items moves
any percentage by several points.

## Expectations for the first live run

Written as falsifiable, in the same spirit as the TypeSafe file: each is something a look at the
run's `_read_runs.jsonl` entry and rejection log can confirm or refute, not a vague hope.

1. **Acceptance does not regress.** No `reader-v3` rule was removed, only extended, so acceptance
   on a comparable paper mix should be **at or above 42%**, not below it. A drop would mean a new
   rule is refusing things it should not, and is a reason to read the rejections before trusting
   the number.
2. **The `number_not_in_quotes` / `value_not_in_quotes` share of rejections falls.** Baseline is
   56% (10 of 18). If rule 12 is doing anything, this share should be visibly lower on the next
   run — not a specific target number (the baseline is too small to justify one), but a real
   downward move, not noise in the other direction.
3. **No freestanding fabrication/setup claim is proposed.** Grep the run's proposed and accepted
   claims for a statement whose entire content is a setup value (pressure, resistance, area, an
   instrument setting) with no accompanying result. Zero is the bar; even one is worth reading in
   full, since it means rule 11 did not land.
4. **No synthesis/EDA-tool output is labelled `measured`.** If any accepted claim's evidence type
   is `measured` and its conditions or quotes mention synthesis, RTL, SPICE, TCAD or a named EDA
   tool, read the excerpt before trusting the label — this is exactly the `CLM-ARCH-0007..0009`
   pattern rule 6 targets.
5. **Rule 4 (symbol/label conditions) is likely untestable on one small run.** It only fires when
   a paper reports several same-kind numbers distinguished by a symbol, which `CLM-PHOT-0002/0003`
   happened to hit and most papers will not. No expectation is pre-registered for it beyond "not
   worse"; it is verified properly only when a paper with that shape is read again.

## How the run is scored

- Compare the new run's `_read_runs.jsonl` entry (via `read_report.py`) against the baseline
  table above, on the same screen/extract model pair.
- Every rejection in the new run is read, not just counted, the same discipline `read_report.py`
  already applies (quotes are kept with rejections precisely so this is possible).
- If a rejection looks like an over-correction, particular attention goes to whether rule 12's
  wording ("must not name a material, model, mechanism ... that none of your quotes contain") is
  refusing a claim that is actually fine — the prompt only asks the model to police itself; it does
  not add a new deterministic check, so any regression is a prompting effect, not a code defect.

## What would change the plan

- If acceptance drops meaningfully (expectation 1 fails), read the new rejections before touching
  the prompt again — a false regression here would mean rule 11 or 12 is too aggressive and needs
  softer wording, not that the underlying defects are unreal.
- If the `number_not_in_quotes`/`value_not_in_quotes` share does not move (expectation 2 fails),
  the next step floated in `TODO.md` A2 — a deterministic content-word overlap check, run
  alongside the number check that already exists — moves from "future work" to "worth building
  now," since telling the model is not enough on its own.
- If a freestanding fabrication claim is proposed again (expectation 3 fails), rule 11's wording
  needs to be sharper about what counts as "a result to attach it to."

## Suggested first live call

`python pipeline/read_paper.py --max-papers 2 --budget-usd 0.25` (or similar): the smallest live
call that can be read in full and compared against the baseline group above, at roughly the same
few cents earlier `reader-v3` live tests cost. Not run as part of this commit — see the note at
the top of this file.

## Results

Not yet run. This section is filled in after the first live `reader-v4` call, following the same
rule `docs/typesafe-preregistration.md` uses: append, do not rewrite the expectations above.
