---
name: reconcile
description: Classify detected contradictions using the Type D/C1/C2/B/A protocol and drive each to a recorded resolution or a named data gap. Use after extract-claims has added claims and pipeline/reconcile.py --detect has opened conflicts in live:unexamined. Blocks publication until no conflict remains unexamined.
---

# reconcile

Stage 4. Input: `CFL` records in `live:unexamined`. Output: every one of them moved to
`resolved` or `live:data-absent`, and the register regenerated.

Doctrine — the four types, the three states, what "resolved" means, when to escalate — is in
`AGENTS.md`. Read it. This file holds only the mechanics.

## The split

```bash
python pipeline/reconcile.py --detect     # mechanical: finds disagreeing comparable claims
python pipeline/reconcile.py --register   # mechanical: regenerates the reader-facing register
python pipeline/reconcile.py --check      # mechanical: validates every record's state
```

Detection is arithmetic: same quantity and unit, non-conflicting conditions, **shared subject context**
(`reference/comparability.yaml`), and `si_base` values differing by more than 5%. Pairs that disagree but
share no subject are listed in `ledger/not-compared.md`, not opened: read that file too, since a real
disagreement behind mismatched condition keys would be there. Classification is not arithmetic — it
needs both sources read. The detector therefore opens
every conflict in `live:unexamined`, **the error state**, and stops. Your job is to empty that
state before the next digest.

A detector that classified would be guessing, and guessing is what this project exists to prevent.

## Procedure per conflict

### 1. Re-read both sources

Open the `SRC` records behind both claims — `reported`, `method_summary`, `limitations`. Not the
claims alone. The claim is our compression of the source; a misreading at extraction looks exactly
like a real disagreement from the ledger's point of view.

### 2. Classify, in this order

**Type D first — definitional or unit mismatch.** Do the two numbers mean the same thing? Check
`as_published` on both: a 10⁴ gap in mobility is cm²/(V·s) against m²/(V·s), not a disagreement.
Check `reference/definitions.yaml` `contested_terms` — EOT vs CET, dense vs sparse TOPS, per-stack
vs per-system bandwidth, D0 under different yield models.
→ Resolve by normalizing. Record the normalization in `definitions.yaml` so it is never redone.
Set `resolution: normalized`.

**Type C1 — scopable.** Do the sources differ in a way that determines when each holds — process
maturity, sample quality, measurement technique, temperature regime?
→ These were never one claim. Split each into a claim explicitly conditioned on what makes it
true. The contradiction disappears because it was an artefact of over-broad statements.
Set `resolution: scoped`.

**Type B — supersession.** Is one claim simply newer and better evidenced?
→ **One source can never supersede.** Check `independent_sources` in the conflict record. If
false, the two sources share a corresponding author or lead institution and count as one.
- Two or more independent sources → old claim `superseded`, new `supersedes` it.
  Set `resolution: superseded`.
- One source only → old claim becomes `challenged`, both cross-linked, and the conflict stays
  `live:data-absent` with `missing_data: awaiting-confirmation`.

**Type A — our error.** Did one claim misread its source?
→ Fix immediately, before anything else. Correct or retract the claim. If it was published, record
`correction_published_in`. Set `resolution: our-error`, then ask why extraction let it through.

**Type C2 — unadjudicable.** Only after establishing that scoping genuinely fails. Both credible,
no available evidence decides.
→ Mark both claims `contested`, cross-link, and keep the conflict `live:data-absent` with a
named gap.

### 3. Name the gap, if it stays live

`live:data-absent` requires all three, and `--check` enforces them:

- `missing_data`: `not-yet-measured` · `undisclosed-method` · `awaiting-confirmation` ·
  `access-blocked`
- `gap`: the absent evidence in plain language. **"The sources disagree" is not a gap.** "No one
  has measured this on a production-maturity process" is.
- `resolution_trigger`: what would close it

If you cannot name what is missing, the data is not absent — the work is unfinished, and the
conflict stays `live:unexamined`, which blocks the digest. That is the correct outcome, not a
problem to route around.

### 4. Write the record

Update the `CFL` front matter (`state`, `resolution` or the gap fields) and fill the
**Classification** and **Resolution** sections with the reasoning and what you read to reach it.
The reasoning is the artifact — a state change with no argument behind it is unauditable.

### 5. Regenerate and check

```bash
python pipeline/reconcile.py --register
python pipeline/reconcile.py --check
python pipeline/publication_gate.py
```

## Escalate instead of deciding when

- The type is genuinely ambiguous, especially C2 vs A: is the field disagreeing, or did we err?
- Resolution needs one comparably credible source ranked above another
- A published claim would need retraction
- The inconsistency is in our own method, definitions or taxonomy
- Resolution needs domain judgment not grounded in a source

Present both claims, their sources, grades and credibility tiers, the candidate classifications,
and what each resolution would cost. Then wait.

## Failure modes

**Reaching for C2 too early.** Most apparent deadlocks dissolve into two well-scoped claims.
C2 is a strong statement: that no available evidence decides. Earn it.

**Naming a gap to close a record.** A `missing_data` entry written to make `--check` pass is the
most damaging thing this project can do to itself, because it is indistinguishable from an honest
one and it silently converts unfinished work into a fact about the field.

**Classifying from the claims alone.** The claim is our summary. Go to the source record.

**Treating a 5% detector threshold as meaningful.** It is a trigger for a human look, not a
finding. Two measurements 6% apart may agree perfectly well within their stated error; two 4%
apart may be a real conflict the detector missed. Judge the numbers, not the threshold.
