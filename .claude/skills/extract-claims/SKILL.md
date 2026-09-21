---
name: extract-claims
description: Turn a corpus source record into atomic, graded, SI-normalized claims in the ledger. Use after a source record exists in corpus/papers/ and before reconcile. Handles claim decomposition, unit conversion, grade and credibility assignment, and the extraction refusals.
---

# extract-claims

Stage 3 of the pipeline. Input: one source record in `corpus/papers/SRC-nnnnn.yaml`.
Output: zero or more claims appended to `ledger/claims/<TOPIC>.yaml`.

**Zero is a legitimate output.** Most sources yield fewer claims than they appear to, and a paper
that produces none because its numbers lack conditions is correctly handled, not failed.

Doctrine — why these rules exist, what a claim is for, how contradictions are treated — is in
`AGENTS.md`. Read it first. This file holds only the mechanics of the extraction step and
deliberately does not restate the reasoning.

## Before starting

```bash
python pipeline/units.py              # conversion engine self-test
python pipeline/claims.py --self-test # refusals and validation
```

Both must pass. They validate `reference/definitions.yaml` and `reference/schemas.yaml`, so a
failure here means the authorities are wrong and no extraction should proceed.

## Procedure

### 1. Read the source record and check what it permits

Load `corpus/papers/SRC-nnnnn.yaml`. Three fields bound everything that follows:

- `access` — `abstract_only` or `metadata_only` forbids **any** quantitative claim
- `venue_id` — must resolve in `sources/registry.yaml`, and `verified` must not be `false`;
  a `review` venue requires `oa_evidence` recording the per-article check
- `evidence_type` — `measured` / `simulated` / `projected` / `announced` / `rumored` carries
  through to every claim. Never upgrade it. A simulation does not become a measurement because
  the paper sounds confident.

### 2. Find the candidate assertions

Work from `reported` (the source's own words) and `method_summary`, not from the abstract or
your memory of the field. For each candidate ask: **what would falsify this?** If nothing would,
it is not a claim — it is framing, and it does not enter the ledger.

Discard: motivation, related-work summaries, future work, "promising"/"significant"/
"state-of-the-art" without a number, and anything the source attributes to someone else
(that belongs to the original source, which needs its own record).

### 3. Split until atomic

A claim is atomic when it has exactly one truth condition.

| Source sentence | Claims |
|---|---|
| "Ion of 1.2 mA/µm at Ioff = 100 nA/µm and Vdd = 0.75 V" | 1 |
| "Mobility improved 40% while SS fell to 65 mV/dec" | 2 |
| "The device shows record mobility and excellent stability" | 1 (mobility); "stability" has no truth condition |
| "Both NMOS and PMOS exceeded 1 mA/µm" | 2 — different devices, independently falsifiable |

The test: could one half be superseded while the other stands? Then they are two claims.
Compound claims cannot be contested or superseded cleanly, which is why `claims.py` refuses them.

### 4. Convert every number

Never convert by hand, and never write a `quantity` block manually:

```python
from pipeline.units import UnitEngine
eng = UnitEngine()
q = eng.record(1000, "cm**2/(V*s)", "mobility",
               conditions={"temperature": 300, "carrier_type": "electron"})
```

This produces `as_published` / `si_base` / `display` together, so they cannot drift apart.
`as_published` must match the paper exactly — it is what `verify-citation` checks against.

If the quantity is not in `reference/definitions.yaml`, **add it there first**. Converting ad hoc
puts a number in the ledger that no authority defines.

`conditions_required` in `reference/schemas.yaml` lists quantities that are meaningless without
stated conditions. If the source does not give them, the claim is not extracted — and that
absence is worth noting, because it is what an `undisclosed-method` gap later cites.

### 5. Assign grade and credibility — two independent axes

**Grade** starts at the venue's `grade_default` and moves **down only**, based on what this item
actually contains. A vendor page with no data is D even though the venue defaults to C. A
peer-reviewed paper reporting only simulation is still A for what it is — a simulation result —
with `evidence_type: simulated` carrying that weight.

**Credibility** comes from `corpus/authors/`. If no author record exists, either build one
(`assess-source`) or use `unknown` — never guess a tier. `unknown` is an honest, usable value.

### 6. Run the refusals before writing

```python
from pipeline.claims import check_refusals, Refusal
try:
    check_refusals(claim, source)
except Refusal as r:
    ...  # do not write; record why
```

A refusal is a result, not an obstacle. Record refused candidates in the extraction notes — a
paper whose headline number was refused for missing conditions is exactly the kind of thing the
digest should mention, and it is evidence about the field's disclosure practices.

### 7. Allocate ids and write

```bash
python pipeline/claims.py --next-id DEV
```

Ids are never reused, including after retraction. Append to `ledger/claims/<TOPIC>.yaml` under
`claims:`, set `created` and `as_of` (`as_of` is the **measurement** date from the source's
`published_date`, not today), then:

```bash
python pipeline/claims.py --validate
```

### 8. Hand off

Do not reconcile here. `extract-claims` does not compare new claims against existing ones — that
is `reconcile`'s job, and doing it here would split the contradiction protocol across two skills.
Report which claims were created so `reconcile` can pick them up.

## Choosing the topic code

One code per claim, the primary one. A claim about HBM bandwidth in an accelerator is `MEM` if
it is about the memory, `ARCH` if about the system. When genuinely torn, pick the layer whose
state-of-the-art document a reader would check for it.

## Failure modes specific to this step

**Extracting the abstract's number instead of the figure's.** Abstracts round, omit conditions,
and quote best-case values. Take numbers from tables and figures.

**Inheriting the paper's framing.** A paper arguing its result is a breakthrough will phrase the
comparison favourably. Extract what was measured, not what it was compared against, unless the
comparison itself was measured in the same work.

**Turning an improvement into an absolute.** "40% better mobility" is a claim about a ratio and
needs the baseline. If the baseline is not stated, the ratio is not extractable.

**Letting `as_of` drift to today.** The date belongs to the measurement. A 2019 result read this
morning is 2019 evidence, and reconcile's supersession logic depends on that being right.

**Best-case as typical.** Papers report champion devices. If a number is the best of N, the claim
says so — "best of 12 devices" is part of the statement, not a footnote.
