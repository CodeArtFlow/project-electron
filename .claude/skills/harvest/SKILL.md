---
name: harvest
description: Turn unread candidates from corpus/candidates/ into source records in corpus/papers/ by actually reading them. Use after the daily sweep (pipeline/harvest.py, run by CI) has queued candidates, and before extract-claims. Covers the publisher candidates the automated arXiv reader cannot take, reviewing that reader's output, and recording what a source says in its own terms.
---

# harvest

Stage 1 of the pipeline, second half. The sweep is already done: `pipeline/harvest.py` runs daily
in CI and queues candidates in `corpus/candidates/`. Reading them has two lanes:

- **arXiv: automated.** `pipeline/read_paper.py` (`.github/workflows/read.yml`, daily) reads arXiv
  candidates with a cheap model. The model only proposes quotes and structure; code verifies every
  quote against the fetched text and sets `access` and `grade` itself (`AGENTS.md`, *Reading*).
  It writes the same records this skill does, so nothing downstream can tell the lanes apart except
  the `extraction` block. Never hand-read an arXiv candidate the reader has not yet had.
- **Everything else: this skill, in a session.** Publisher pages are mostly bot-walled to a script,
  so they stay a human-and-Claude job until a legitimate full-text route exists.

The automated lane's output is also this skill's job to **review** (see the last section): a model
that cannot fabricate a quote can still pick the wrong sentence.

Input: `corpus/candidates/CAND-YYYYMMDD-nnnn.yaml`
Output: `corpus/papers/SRC-nnnnn.yaml`

Doctrine is in `AGENTS.md`; the record shape is in `reference/schemas.yaml`. This file holds only
the mechanics.

## Why the split exists

A candidate carries metadata and a verified OA location. It carries **nothing about content**,
because nothing has read it. A source record carries `reported`, `method_summary` and
`limitations`, and declares in `access` what was actually read.

Writing those fields without reading the paper is fabrication with provenance attached — worse
than no record, because everything downstream trusts it. That is the entire reason the sweep and
the reading are separate programs, and why the sweep writes to `candidates/` and never to
`papers/`.

**Never promote a candidate to a source record without opening the source.**

## Procedure

### 1. Pick up the queue

```bash
python pipeline/read_paper.py --dry-run     # the arXiv lane's queue, sized; no API call, no writes
cat corpus/candidates/_last_sweep.json
```

The manual lane is every unread candidate whose `source` is not arXiv. A candidate is unread until
it has a source record (then it is deleted) or a `read_decision` (then it stays on disk so the next
sweep does not re-harvest it). `pipeline/candidates.py` defines that, so do not re-derive it.

`_last_sweep.json` reports the window, counts, and any venues that failed. **If it records an
incomplete sweep, say so in the digest** — partial coverage that looks like a quiet day is the
failure mode the sweep script exits non-zero to prevent.

### 2. Open the actual source

Use `oa_location.url` from the candidate. That URL was verified open by OpenAlex at sweep time,
but verify it still resolves and actually contains the paper.

If it does not resolve, or the copy is a stub, or the landing page is paywalled despite the
metadata: **do not guess from the abstract.** Record the decision on the candidate and move on —
that outcome is what makes the `access-blocked` count meaningful:

```yaml
read_decision: {decision: unreadable, date: <UTC date>, reason: "HTTP 403 from the publisher", model: null, prompt_version: null}
```

Use the same shape as the reader (`unreadable`, `out_of_scope`, `too_long`). A candidate left with no
decision reappears in the queue every day and inflates the unread count.

Read the abstract *plus* the figures and tables carrying the results. A number in an abstract has
no method behind it.

### 3. Decide `access` honestly

This field bounds everything downstream, so it records what you read, not what was available:

| Value | Means |
|---|---|
| `full_text_figures` | Read the text **and looked at** the figures/tables carrying the numbers |
| `full_text` | Read the text; figures unavailable, unreadable, or not looked at |
| `abstract_only` | Only the abstract — **forbids every quantitative claim** |
| `metadata_only` | Did not read the content at all |

A candidate whose OA copy failed to open is `metadata_only`, not `abstract_only`.

Extracted PDF text is `full_text`, however complete. `full_text_figures` needs the figure or table
itself to have been viewed, and two early records claimed it when it had not been. Whichever value
you choose, fill `read_scope` with exactly what you looked at and what you did not ("all extracted
text; no figure image was seen"). `access` says how much was available, `read_scope` how much was
actually read.

### 4. Write `reported` in the source's own terms

Transcribe what the paper says, in **its** units, before any normalization. This is the audit
anchor: `verify-citation` compares this against the paper without doing arithmetic, so a
converted number here defeats its purpose.

Capture the measurement conditions alongside each number — Vdd, Ioff, temperature, precision,
sample. If the paper does not state them, record that absence explicitly; it is what an
`undisclosed-method` gap later cites.

### 5. Write `method_summary` and `limitations`

`method_summary`: how the result was obtained, concretely. If the paper does not disclose enough
to compare its number against another group's, **say that in the field**. That sentence is
evidence, and reconcile depends on it.

`limitations`: sample size, process maturity, single-lab result, missing error bars, champion
device, simulation calibrated against limited data, author conflicts of interest. An empty list
is itself a claim — leave it empty only deliberately.

### 6. Set `evidence_type` and `grade`

`evidence_type` is `measured` / `simulated` / `projected` / `announced` / `rumored`. A simulation
paper is `simulated` no matter how confident its language. This is the single most common way
semiconductor reporting goes wrong.

`grade` starts at the candidate's `grade_default` (the venue's) and moves **down only**, based on
what this item actually contains. A paper in a grade-A venue that reports only simulation is
still grade A evidence *of a simulation* — `evidence_type` carries that, not the grade. A vendor
page with no data is D regardless of its venue default.

### 7. Assign the topic code

The candidate carries `topic_hint` from OpenAlex's field classification. It is advisory and
frequently wrong at the margin. Pick the code whose state-of-the-art document a reader would
check for this result.

### 8. Write the record and retire the candidate

```bash
python pipeline/claims.py --next-source-id     # allocate SRC-nnnnn
```

Write `corpus/papers/SRC-nnnnn.yaml` per `reference/schemas.yaml`, carrying over `doi`,
`arxiv_id`, `venue_id`, `authors` and `published_date` from the candidate, and adding
`oa_evidence` describing how open access was established for *this article*.

`authors` is `never_inferred`. Names come from the candidate. Leave `affiliation` and
`corresponding` as `null` unless the paper itself states them, and never fill them from memory or
from author order: both were done once, one flag was wrong, and the fix is in that record's
`corrections` trail. `assess-source` owns them.

Then delete the candidate file. It has served its purpose, and leaving both creates two records
of one paper — the dedupe index reads both directories, so a stale candidate will also suppress
a legitimate re-harvest later.

Source records are **immutable once written**. If a paper is later revised, that is a new record
superseding this one, because claims already cite this one's content.

### 9. Hand off

Do not extract claims here. `extract-claims` is a separate stage with its own refusals. Report
which records were created.

## Failure modes specific to this step

**Trusting `is_oa` over what you can see.** The metadata says a legal copy exists; it can still
be a stub, the wrong version, or an author page with no PDF. Trust the page in front of you.

**Recording the publisher's version claim.** `oa_location.version` distinguishes
`publishedVersion` from `submittedVersion` (a preprint). They can differ in substance after peer
review. Record which one you read.

**Reading a candidate from a `review` venue without the per-article check.** Registry `review`
means the venue is reachable but open access is an article-level property. `oa_evidence` must
describe *this article's* licence or repository copy, not the venue's status.

**Letting the topic hint pick the code.** It comes from a generic field classifier that has never
heard of our topic taxonomy.

**Harvesting the same paper twice via different routes.** A paper often appears both as an arXiv
preprint and as a journal article. These are two sources with different grades (B and A) and
different content — the preprint may predate peer review. Record both if both were read, and
cross-reference them, but never merge them into one record.

## Reviewing the automated lane

Records with an `extraction` block were written by `read_paper.py`. Its verifier guarantees each
quote is in the paper and each number is in its quote; it cannot guarantee that the quote is the
paper's *finding* rather than a baseline, a prior result it cites, or a projection. Spot-check:

```bash
python pipeline/read_paper.py --dry-run           # what the next run would take
cat corpus/candidates/_last_read.json             # decisions, accepted and rejected claims, cost
```

For each new claim, open the paper at the quoted passage and ask three things: is this the paper's
own result, are the stated conditions the ones that produced this number, and is `evidence_type`
right (a simulation is `simulated`). A defect here is a Type A error: correct it with a `corrections`
entry, never a silent edit, and add it to `reference/gold/extraction.yaml` so it counts against the
audit. A run whose rejected-claim count is high and accepted count is zero is a working verifier,
not a broken reader.
