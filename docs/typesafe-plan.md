# TypeSafe integration: the plan

**Status: APPROVED by the user, 2026-09-21. Phases 1 and 2 are DONE: the paper-grounded check is built
(section 7) and ran once, live, on 9 papers, scored against expectations committed beforehand (12 of 15 on
its main question; results and what they do and do not show are in `docs/typesafe-preregistration.md`).
Phases 3 onward are not started.** Rules stay in
`AGENTS.md`; how the current advisory audit works stays in `docs/typesafe.md`. This file says what we
intend to build next and why, and it changes as decisions are made.

## 1. What TypeSafe is, from its own documentation

Read from docs.typesafe.ai on 2026-09-21 (paraphrased; the pages are the authority):

- One endpoint. A request carries a **state** (text, or JSON of text) and named **questions** of three
  kinds: **noul** (probability that a yes/no statement is true), **choice** (pick one of the options you
  define, with a probability for each) and **score** (a position along levels you define).
- Every question in a request is evaluated against the same state, **independently and in parallel**.
  Asking many questions in one request costs little extra, and TypeSafe recommends asking every
  question you might need and letting code decide which answers to use.
- Every answer carries a **confidence**. The docs recommend using it as a second axis: route on the
  answer, then on the confidence, with thresholds chosen per decision by what a wrong answer costs.
- **No storage is documented.** Each request stands alone. Anything we want kept, we keep.
- `jev-1.13.0`: **$0.042 per million input tokens, output free.** Context 64k tokens, of which the state
  plus the longest single question may use 32k. Text only. 1,200 requests a minute (subject to change).
- Its own **known weaknesses** (the jaggedness page, last reviewed 2026-09-17): it reads questions
  literally; it is not a calculator and does not count reliably or handle numeric precision; it compares
  dates poorly; it loses accuracy when the state is large and mostly irrelevant; it does poorly with
  extra indirection; and it does not generate text. Its advice for each is the same shape: write the
  exact condition, filter the state first, and **keep arithmetic, counting and comparison in code**.

The user's summary of where it excels is right and matches this: **yes/no, true/false, classification
and choice, ratings.**

## 2. The division of labour

The rule that makes the rest safe: each job goes to the tool that is actually good at it.

| Job | Who | Why |
|---|---|---|
| Fetch text, verify quotes are verbatim, check numbers appear, convert units, compare in SI, interval overlap, counting, dates, thresholds, storing, fingerprinting | **Code** | Deterministic, testable, and TypeSafe is documented as weak at exactly these |
| Turn a paper into structured claims, conditions and quotes (transcription) | **Gemini reader** | Needs long-context reading and structured output. Already verified by code |
| Typed semantic judgments over a small piece of evidence: is this a result or an input parameter, does the paper state this scope word, which evidence type, which layer, how well are the methods disclosed | **TypeSafe** | Yes/no, choice and rating are what it is built for, and it is cheap enough to ask many at once |
| Deciding what a judgment means for the ledger | **A human, or the `reconcile` skill** | Doctrine: TypeSafe changes no claim, grade, tier or conflict |

TypeSafe is a **judge, not a store, a calculator or an author.**

## 3. What we store, and where

TypeSafe keeps nothing, so the repository does. All of it is data in git, so the history is the audit
trail.

| Artifact | Path | Written by | Notes |
|---|---|---|---|
| Question packet | `corpus/questions/SRC-nnnnn.json` | the reader, at read time | The typed questions for one paper's claims, the evidence references, the hash of the text |
| Answers | `corpus/questions/SRC-nnnnn.answers.json` | the check | Raw answers, confidence, model version, request fingerprint, date, cost |
| Paper facts | derived table | code, from answers | The same paper-level questions for every paper, so papers and fields compare |
| Gold labels | `reference/gold/` | a human, then reviewed | What thresholds are measured against. **Nothing is calibrated without it** |

## 4. The question families

Every question is **typed, code-owned and versioned.** The same question is asked of every claim and
every paper, which is what makes cross-paper comparison mean anything, and a model cannot write a
leading one. Questions are literal and specific, per TypeSafe's own guidance.

**A. Screening.** For a candidate's title and abstract: noul *in scope*, choice *stack layer*, score
*priority*. About 1,000 tokens, so about $0.00004. It runs beside Gemini's cheap screening call. Where
the two disagree, that is a review signal, and the agreement rate is a measurement of both.

**B. Claim against the paper (the family the prototype started).** For each accepted claim, against
filtered excerpts of the paper: choice *does the paper support the statement* (every scope word counts);
noul *is this value a result, and not an input parameter, a baseline, or a value from prior work*;
choice *evidence type*; noul *one assertion*; and one literal noul per **condition** and per **scope
word**. This is the check meant to catch "in BLG" and the phonon-energy parameters (untested: see
section 6.4). It targets the standing blind spot: the older audit judges a summary of the paper, never
the paper.

**C. Paper facts.** A fixed set, identical for every paper: layer, evidence overall, reports
uncertainty, compares against a baseline with numbers, states limitations, method disclosure (score).
This is the cross-paper, cross-field table: it lets us ask "which papers on this layer report
uncertainty" and lets us check the reader's topic against an independent judge.

**D. Across papers.** Claims grouped by quantity or topic, each with its excerpt: choice *same quantity,
comparable conditions, different definition, or unrelated*; noul *do these two appear to contradict*;
choice *which discrepancy class this most resembles*. Output is a **proposal to `reconcile`**, never a
classification. Arithmetic (do the numbers differ, by how much, in SI) stays in `reconcile.py`.
The first scheduled reading run made this urgent: five of the six conflicts it opened were between
claims of unrelated papers that share only a generic quantity name (a computing time and an orbital
lifetime; two unrelated temperatures). A judge that answers "are these about the same thing?" is the
missing piece, and it is a yes/no question, which is what TypeSafe is for. But whether an uncalibrated
judge may *decline to open* a conflict is a doctrine question and the user's to decide (section 10).

**E. Terms and definitions.** Does a paper use "EOT", "node", "TOPS/W" in the sense
`reference/definitions.yaml` records? Choice answers, checked by a person before any definition moves.

**F. Our own documents.** The existing publication audit of digests and SOTA. Unchanged.

**Deliberately not asked of TypeSafe:** whether a number matches its quote or its qualifier ("up to",
"at least"), whether a unit converts, counts, dates, or any comparison. Code already does those, and the
prototype's `numbers` question asked TypeSafe to do the one thing its documentation says it is weakest
at. It is removed in the revision.

## 5. Evidence: filter first

The prototype sends the **whole paper** as state. TypeSafe says to filter first, and a whole paper is
mostly irrelevant to any one claim. Also, two of the three papers the reader has read (96,404 and
90,908 characters) are at or over the 90,000 characters (about 29k tokens, at an assumed 3.1
characters a token) that the prototype allows, so "whole paper" would exclude them.

The revision sends, per claim: the **verified anchor quotes with a window of surrounding text** (the
reader already proves the quotes are verbatim), the paper's abstract, and its method and limitation
quotes, in document order, labelled. Typically 3 to 8k tokens. That needs a map from the
whitespace-stripped text the verifier matches to positions in the raw text, which does not exist yet
and is the main piece of engineering in this plan. The packet records that a check used **excerpts**, so
"the paper is silent on X" is never claimed from an excerpt.

## 6. From answers to action: confidence-routed, and calibrated against gold

TypeSafe's provisional thresholds (0.9 and 0.1) flagged nearly everything in the first live audit (7 of
7 claims, 12 of 12 documents, 9 of 10 conflict pairs), so they say nothing. The plan replaces one global cut with what its own docs recommend:

1. **Route on answer and confidence.** Below a per-question confidence floor, a judgment goes to a
   human queue. Above it, the answer is used.
2. **Set each threshold from labelled data**, per question, from the gold set. Not before.
3. **Prefer disagreement between independent judges as the flag.** When Gemini and TypeSafe disagree
   about a claim, that is worth a look even with uncalibrated thresholds, and it needs no threshold at
   all. Agreement is weaker evidence than it looks (both are models), so it lowers priority, never clears.
4. **Pre-register expected outcomes on cases we already understand**, before any live run, so we test
   TypeSafe and not our reading of it. We already know: the MAT claims are input parameters, so
   `is_result` should be low for them and high for the MiX Table VI power results; the "in BLG" and
   "acoustic phonon for AP" statements should not be fully supported; `CLM-ARCH-0004`'s old
   "EDP-optimal" condition should be flagged against its paper.
5. **Advisory until measured.** Whether any check may ever block publication is decided per question,
   after calibration, by the user, in `reference/semantic_policy.yaml`.

## 7. What exists today

Phase 1 is built and tested offline (11 tests for excerpts, 34 for packets and the check), and ran live once
on 2026-09-21 (phase 2):

- `pipeline/excerpts.py`: finds each verified quote in the raw text (through the verifier's own
  normalization), widens it with context, merges, orders and labels the excerpts, and never trims. Proven
  on the three real papers first read: every recorded quote was located, and the excerpts were 10 to 23%
  of the paper (about 3.4k to 4k tokens), so the two papers that exceeded a whole-paper window fit easily.
- `pipeline/question_packets.py`: the packet (each claim's verified quotes and the unverified words in
  its statement), the code-owned rubric, and a backfill for papers read before packets existed.
- `pipeline/paper_check.py`: fetch, hash, cut, send one request per paper, store the questions and
  answers, flag. Never sends a stale, too-long or unlocated paper; a missing key is a visible skip.
- The reader writes a packet whenever it reads a paper (13 lines; **no prompt change**, so the daily
  extraction is unaffected). Nine packets were backfilled for the papers already read.
- A manual workflow, `paper-check.yml`, and CI tests. It is deliberately **not** a step of the daily
  reading workflow yet: it runs by hand until phase 2 says what it is worth.

Two things from the original prototype were dropped: the model-proposed extra questions (low value, and
they needed a prompt change to a live daily job) and the paper-level questions (they need the whole
paper; phase 4). The existing advisory audit (`semantic_checks.py`) is untouched.

## 8. Phases

| Phase | What | Done when |
|---|---|---|
| **1** | Filtered excerpts with a position map; drop `numbers`; literal per-condition and per-scope-word questions; keep the packet and answers storage | Offline tests prove excerpts contain every verified anchor and are labelled as excerpts; a request never exceeds the window |
| **2** | Pre-register expectations (section 6.4), then one live run on the 3 automated papers | The recorded outcomes are compared with the expectations in a committed note, whichever way they fall |
| **3** | Gold cases for family B (at least 30, at least 3 layers, defects included) and independent review; per-question thresholds; Gemini-vs-TypeSafe agreement | A committed evaluation shows precision and recall per question, with the caveats `gold_eval.py` already prints |
| **4** | Paper facts (C) and screening comparison (A) | A derived table of paper facts; a measured screening agreement rate |
| **5** | Cross-paper proposals (D) into a review queue | `reconcile` receives proposals with their evidence; none is auto-applied |
| **6** | Decide, per question, whether anything may gate | A user decision recorded in the policy file |

Costs should stay negligible throughout: at the documented $0.042 per million input tokens, a request
of a few thousand tokens is well under a tenth of a cent. That is a documented rate applied to an
estimated size, not a measurement.

## 9. Risks and what is not yet known

- **Numbers.** TypeSafe is documented as weak on them. The plan keeps every numeric check in code.
- **Adversarial text.** Paper text is untrusted input to a model. Questions state that the text is data,
  and Phase 2 includes edge-case tests, as the docs advise.
- **A whole-paper request already exceeds the window** for two of the three papers read so far, which is
  why phase 1 is first.
- **Unknown:** how accurate TypeSafe is on semiconductor papers. Phases 2 and 3 exist to find out, and
  until then everything it says is a prompt for a human look.
- **Unknown:** whether the position map can be made exact across PDF extraction damage. If not, excerpts
  fall back to windows found by the verifier's own matching, with the limit stated on each packet.

## 10. Decisions for the user

Asked on 2026-09-21. Answers:

1. **Comparability (`TODO.md` D1): a deterministic guard first.** Require shared subject context, log
   what was not compared visibly. TypeSafe pair triage (family D) is deferred, not rejected.
2. **The plan is approved, and claims against the paper (family B, phase 1) come first.** Family D
   waits for the guard to prove insufficient.
3. **The evidence rule stands** as written in section 5: filtered excerpts, numeric checks in code.
   (Approved by approving the plan; not asked separately.)
4. **What TypeSafe may decide: advisory only** until calibrated against gold, the standing policy.
   Whether any check ever gates is a later decision, per question.
