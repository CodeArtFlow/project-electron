# AGENTS.md — Project Electron

> **The single source of truth for every agent working in this repository** (Claude Code, Codex,
> or any other). `CLAUDE.md` holds only an import of this file, so there is exactly one copy of
> the doctrine. Change a rule **here**. Never restate one in `CLAUDE.md`, a skill, or a comment:
> duplicated rules drift apart, and that is a contradiction in our own instructions.
> `pipeline/test_agent_files.py` fails CI if `CLAUDE.md` grows rules of its own.

A daily semiconductor research agent. It harvests new open-access literature, extracts atomic
claims, reconciles them against everything we have previously asserted, and publishes a daily
digest plus a living state-of-the-art review for every layer of the stack.

Pipeline: **harvest → triage → extract → reconcile → digest → publish**

Scope is the full stack: materials, device physics, lithography, process integration, advanced
packaging, memory, compute architecture, photonics, EDA, and fab economics.

---

## Prime directive: the corpus must never contradict itself

This is a research project. Its only asset is trustworthiness. A single confidently-stated
falsehood destroys more value than a month of digests creates. Coverage is negotiable; internal
consistency is not.

Six rules follow, and they outrank every other instruction in this file:

1. **Every factual claim we publish traces to a source we actually read.** Never to model memory.
2. **A new claim that conflicts with an existing claim halts the work in progress.** We reconcile
   before we continue. We do not publish around it, defer it, or quietly drop the older claim.
3. **A contradiction may persist if and only if the data to resolve it is absent.** There is no
   other permissible reason. Not time, not difficulty, not "the field is unsettled" on its own.
4. **Absence of data must be named.** State the specific evidence that would settle it. If you
   cannot name what is missing, data is not absent — the work simply has not been done, and the
   contradiction is an error with the standing of a failing test.
5. **Every live contradiction is visible to the reader.** Flagged in the digest, on the site, and
   in the SOTA. Never buried, never silently dropped, never smoothed into false consensus.
6. **When a contradiction cannot be confidently classified or resolved, stop and ask the user.**
   Guessing is the failure mode this project exists to prevent. Asking is cheap and always correct.

### What "resolved" means, and when a contradiction may live

Resolution is **understanding the reason and acting on it** — not deciding who is right, and not
merely writing the reason down. Understanding is necessary but never sufficient: if the reason
tells us how to eliminate the contradiction, we eliminate it. Recording an explanation and leaving
the contradiction standing is not a resolution. It is a contradiction with a note attached.

A contradiction is therefore permitted to live in exactly one circumstance: **we understand the
disagreement, and the evidence that would settle it does not exist or cannot be reached.** That
gap gets named, categorised, watched, and shown to the reader.

The named-gap test is what keeps this honest. "The sources disagree" is not a gap. "No one has
measured this on a production-maturity process" is a gap. The first is an admission we stopped
early; the second is a fact about the field, and it is often the most valuable thing in a digest —
it points at the experiment nobody has run.

Forcing a winner where the evidence doesn't support one is fabrication. Leaving a resolvable
conflict open is negligence. Naming the missing data is the path between them.

### Model memory is not a source

Assistant training data is stale relative to the research frontier and has no provenance. In this
project it is a *hypothesis generator only* — useful for knowing where to look, never for what to
assert. If a statement is not backed by a corpus record, it does not go in the ledger, the digest,
the SOTA, or a reply to the user stated as fact. "I recall that..." is not evidence.

---

## Core data model

Ten artifact types. Each has exactly one job. Never blur them.

| Artifact | Path | Job | Mutability |
|---|---|---|---|
| **Source registry** | `sources/registry.yaml` | Every relevant open-access venue we harvest | Curated, append-mostly |
| **Definitions** | `reference/definitions.yaml` | SI canonicalization, contested terms, and constants sourced from a fetched authority (`reference/authorities/`) | Curated |
| **Source record** | `corpus/papers/` | What a specific paper says, in its own terms | Immutable once written |
| **Author record** | `corpus/authors/` | Public track record behind a source's credibility | Updated as record grows |
| **Claim** | `ledger/claims/<TOPIC>.yaml` | An atomic assertion *we* stand behind, with provenance | Amended only via supersession |
| **Conflict** | `ledger/conflicts/CFL-nnnn.md` | A contradiction, its state, and its named data gap | Live until resolved |
| **Open register** | `ledger/open-contradictions.md` | Reader-facing view of every live contradiction | Derived — regenerated each cycle |
| **Discovery brief** | `discoveries/DSC-nnnn.md` | Condensation of READ material against one gap | Derived — not a claim, never citable |
| **Digest / SOTA** | `digests/`, `sota/` | Reader-facing prose | Derived — never a source of truth |
| **Gold set** | `reference/gold/` | Labelled cases for calibrating the semantic audit and testing the reader | Curated; **independent review pending** |

**The derivation rule:** digests and SOTA documents may only restate claims that exist in the
ledger. If you find yourself writing a sentence in a digest that isn't in the ledger, stop —
either it belongs in the ledger first, or it doesn't belong in the digest.

### Claim anatomy

Claims are atomic and falsifiable. "GAA transistors are promising" is not a claim. A claim carries:

- `id` — `CLM-<TOPIC>-<nnnn>`, stable forever, never reused
- `statement` — one assertion, with measurement conditions
- `quantity` — `as_published` / `si_base` / `display` per `reference/definitions.yaml`, where the
  claim turns on a number, plus `bound` (`exact` / `upper_bound` / `lower_bound`) and `approximate`.
  **A bound is not a measurement:** "up to 5.3x" is an upper bound, and storing it as 5.3x once made
  two upper bounds look like a contradiction. `reconcile` compares by interval overlap, so two
  upper bounds can never conflict, and extraction refuses to record a qualified number as exact.
  A claim states its `conditions` twice, on the claim and inside its `quantity`; validation refuses a
  claim whose two disagree
- `extraction` — on claims written by the automated reader: model, prompt version, and how many
  quotes were verified verbatim against the paper (see *Reading*)
- `corrections` — dated audit trail of changes made after the claim was written. `public: true`
  means readers had already seen it, so the change must appear under `## Corrections` in a digest
- `sources` — corpus record IDs (at least one)
- `grade` — evidence grade (below)
- `credibility` — source credibility tier (below)
- `status` — `active` | `challenged` | `contested` | `superseded` | `retracted`
- `as_of` — the date the underlying measurement was made, **not** the date we read it
- `supersedes` / `superseded_by` / `challenged_by` — claim IDs, when applicable

Topic codes: `MAT` `DEV` `LITHO` `PROC` `PKG` `MEM` `ARCH` `PHOT` `EDA` `ECON`

Claim statuses:

- `active` — stands, no live dispute
- `challenged` — one credible source disputes it; **not enough to supersede** (see below)
- `contested` — the field genuinely disagrees; reason recorded; competing claims cross-linked
- `superseded` — retired by confirmed newer evidence; retained for history
- `retracted` — we were wrong; correction published

---

## Sources

**Open access only, for now.** If a source is paywalled, we do not infer its content from the
abstract or from secondary coverage — we record the access limitation and move on. Check for a
legitimate open version before giving up: OpenAlex's `best_oa_location` is the authority here,
plus author preprints and institutional repositories.

`sources/registry.yaml` is the comprehensive list of relevant open-access venues, maintained as a
first-class artifact. A registry compiled from assumption is exactly the failure mode rule 1
forbids, so every entry carries a verification state backed by recorded evidence:

- **`true`** — exists, active, and OA status confirmed by an authority (DOAJ for journals, a
  successful endpoint probe for APIs). Harvestable.
- **`review`** — exists and is active, but OA status is *not* confirmed. Harvestable **only**
  with a per-article OA check. Every `hybrid` venue is permanently `review`, because there OA
  is a property of the article, not the venue.
- **`false`** — existence or reachability could not be established. **Do not harvest.** Requires
  a recorded `blocker` saying why.

Two states would not survive contact with reality: "exists and is active, but I cannot confirm
open access" is a common outcome, and forcing it to `true` asserts OA we never established while
forcing it to `false` discards reachable venues. Both are falsehoods, just in opposite directions.

Verification is reproducible, not a one-time judgement:

- `pipeline/verify_registry.py` — checks entries against Crossref, DOAJ and live probes
- `pipeline/validate_registry.py` — checks the registry against its own stated rules
- `pipeline/discover_journals.py` — puts candidate additions through the same gate before entry

Journals are identified by **ISSN, not title.** Crossref's journal search is punctuation-sensitive,
returns nothing for `&`, and does not surface generic titles like "Nature" at all. Title matching
must be exact; never resolve a near-miss to the closest-looking candidate. An early version of the
verifier accepted substring matches and silently identified *NatureJobs* as *Nature*.

Keep the registry comprehensive and current: when harvest encounters a relevant venue not in the
registry, putting it through the gate and adding it is part of the task, not a follow-up.
Removals stay recorded in the `removed:` section, with the reason, so a deletion is auditable.

### Topic filtering: strict about domain, not about sub-field

Broad multidisciplinary venues are gated by `sources/topics.yaml`, which uses OpenAlex topic IDs
rather than keywords. Keywords cannot do this job: OpenAlex's own topic search returns *Memory
and Neural Mechanisms* for "memory" and *Meat and Animal Product Quality* for "packaging".

Three tiers:

- **core** — unambiguously our stack. Harvested normally.
- **adjacent** — a neighbouring sub-field of the same domain: devices, fabrication or materials
  that end up on a wafer. Harvested and stamped `relevance: adjacent` on the candidate, so the
  reading stage applies a higher bar and the digest can distinguish them.
- **exclude** — a different domain entirely. Food science, neuroscience, psychology, medicine.

Adjacency is **recorded on the candidate, not silently decided by the filter.** A reader can see
what came in as a near-miss instead of trusting that the filter judged correctly.

Venues marked `scope: specialist` skip this filter entirely, which is what makes strictness safe:
photonics coverage comes from the photonics journals regardless of what the allowlist contains.

A first version of this allowlist was strict in the wrong direction — it rejected wafer-scale
metasurfaces and lithium-niobate modulators alongside food packaging. Measuring it against 49
already-harvested candidates caught it: zero passed. Strict must mean "only relevant", not "only
the topics I thought of first".

### Reading: the model proposes, code decides

Reading a paper into a source record and claims is done by `pipeline/read_paper.py` for arXiv
(daily, `.github/workflows/read.yml`) and by the `harvest` skill, in an agent session, for everything else.
The automated reader uses two Google models, both named in `reference/reader_budget.yaml`:
`gemini-3.5-flash-lite` for the screening call (title and abstract only; most arXiv is not
semiconductor research, so this is where the volume is) and `gemini-3.6-flash` for extraction (the
whole paper, where quality matters). The user chose the split after the first live run, in which the
cheap model extracted nothing usable. `gemini-3.8-flash` stays priced as an alternative. A model is a
**transcriber, not an author.** It may propose quotes and structure. It cannot influence any of the
following, all of which are deterministic code:

- **`access`** is set from what `pipeline/fetch_text.py` actually retrieved. A model never claims it read.
- **`grade`** is set from the venue's default. A model never grades its own source.
- **Every quote** must appear verbatim in the fetched paper (after normalising PDF extraction damage
  such as lost spaces, line-break hyphenation and minus signs). A quote that is not there is
  discarded along with any claim resting on it. The match is deliberately not fuzzy.
- **Every number** must appear as a standalone token in the quote it is anchored to, and a statement
  may not introduce a number its own quotes lack.
- **Every qualifier** ("up to", "at least", "roughly") before a number must be recorded as a bound
  or approximation, or the claim is rejected.
- **Every condition** needs its own quote containing its value. A condition can never be copied
  across papers, which was a real defect in hand extraction.
- **Every number needs a condition that says what it is a value of** (component, variant,
  configuration, material, mechanism, calculation, benchmark). A paper reports many numbers of one
  kind, and numbers with nothing to tell them apart look like contradictions of each other, which is
  what happened on the first extraction run. A number with no verified condition is rejected.
- **Units** go through `UnitEngine`, then the same extraction refusals as manual extraction.

The model is asked for JSON that matches a schema. That fixes the *shape* of its answer and nothing
else; whether the answer is *true of the paper* is still decided only by the checks above.

A paper from which the verifier accepts **no claim is not retired.** Retiring it would delete the
candidate and write an empty source record for what may only be a weak model's failure, which is what
the first live run did to four papers. It stays a candidate with a `no_claims` decision, recording
what was rejected, so it is not re-paid for every day and a stronger model or a human can take it.

Precision over recall: extracting nothing is a correct answer. Rejected candidate claims (the first ten
per paper) are recorded on the source record with their reasons, because "this venue states numbers without their
conditions" is evidence about the field. A paper is never silently truncated: over the character
budget it is skipped with a recorded reason. Affiliations and the corresponding author are **not**
recorded by the reader (arXiv does not state them); they are left `null` for `assess-source`, since
`authors` is a `never_inferred` field.

Only arXiv is read automatically (14 of 14 probed were fetchable). Of 36 publisher candidates
probed, 9 could be fetched as full text; 20 returned HTTP 403 and 7 were gated or stub landing
pages, so OpenAlex's `is_oa: true` overstates what an automated client can read. That lane needs a legitimate full-text route or a human reader.

### Reader budget: a cap that refuses to spend

The automated reader may spend **at most $10 a month** (user, 2026-09-21). The limit is the committed
file `reference/reader_budget.yaml`, enforced by `pipeline/budget.py`. Like the semantic-audit policy
it is a file and not a switch: no workflow input or environment variable raises it, and the CLI can
only lower it. Changing it is a visible commit.

- **Checked before every call.** The worst case (all the input plus the whole `max_output_tokens`,
  which for Gemini covers thinking and answer together) must fit in what is left today, or the call
  is never made and the run stops with `stop_reason: budget`. Nothing is read on credit.
- **Paced.** A day may spend an even share of what is left of the month, so a backfill or a bug
  cannot burn the month on its first day.
- **Recorded after every call**, from the tokens the API reports (thinking is billed as output), in
  `corpus/candidates/_reader_spend.json`, and committed even when a run fails, because the money was
  spent either way. A timeout is charged at its worst case, since the server may have finished and
  billed us without our seeing it. The ledger rounds up, so it can only over-count.
- **Priced or refused.** A model with no dated price in the file cannot be used. Prices are Google's
  Standard paid-tier list prices. The free tier costs nothing but its content may be used to improve
  Google's products, and we cannot see which tier a key is on, so everything is budgeted at the paid
  price. `gemini-3.5-flash-lite` is $0.30 in / $2.50 out per million tokens with no announced change.
  **`gemini-3.6-flash` and `gemini-3.8-flash` double on 2027-01-01** ($0.75/$3.75 to $1.50/$7.50); the
  file records the step, so the ledger cannot under-count in the new year. The extraction model is
  one of them, so extraction gets twice as expensive then and the cap throttles it sooner.
- **As little thinking as each model offers.** Thinking is billed as output and reading is
  transcription, so the policy asks for `minimal` on 3.5 Flash-Lite and 3.6 Flash and `low` on 3.8
  (which cannot go lower). If extraction stays poor, raising the 3.6 level is the first thing to try. Temperature is left at Google's default, because Google says to keep 1.0 for every Gemini 3
  model. Nothing depends on either: the verifier checks every quote.
- **A docs page is not proof a model can be called.** Google's docs listed `gemini-2.5-flash` as stable
  with no shutdown date, and the live API refused it to this project (404, "no longer available to new
  users"). A model is priced here only if it is one we intend to call, and the first live call is
  small for that reason.
- **Fails closed.** A policy or ledger that cannot be read stops the reader with a failed job. It is
  never treated as a fresh start.

This is a *second* line of defence, only as right as our copy of the prices. The cap that cannot be
wrong is Google's, and only the account owner can set it: AI Studio > Spend > Monthly spend cap
(marked experimental, with about ten minutes of lag), or Prepaid billing with auto-reload off, which
stops service the moment the balance reaches zero.

### Evidence grades — *what kind of evidence is this?*

Semiconductor discourse mixes measured silicon with marketing at identical rhetorical confidence.
Grading is how we refuse to.

- **A** — Peer-reviewed measurement, method disclosed (OA journals, IEDM/VLSI/ISSCC author copies)
- **B** — Preprint or conference abstract with data (arXiv, TechRxiv, extended abstracts)
- **C** — Vendor/foundry technical disclosure containing actual data
- **D** — Press release, keynote, or roadmap slide with no data
- **E** — Analyst note, trade journalism, rumor

**Grade ceiling rule:** a claim's confidence can never exceed its weakest load-bearing source.
Grade D and E material may never be stated as fact. It is reported as attribution — "TSMC states
that…" — and it never contradicts a grade A/B claim; it is simply lower-grade information.

### Source credibility — *how much does this source's track record earn?*

Grade and credibility are **two independent axes**. A preprint from a group with a decade of
replicated results is not the same as a preprint from an unknown group, and neither is the same as
a peer-reviewed paper. Track both.

For every source, build the author record in `corpus/authors/`: publication history, institutional
affiliation, academic lineage (advisor and group, where public), citation and replication record,
and any corrections or retractions. **Public professional record only** — this is scholarly
provenance, not a dossier on a person.

Credibility tiers:

- `established` — sustained record of results that held up; no integrity flags
- `emerging` — real record, too short or too narrow to weight heavily
- `unknown` — insufficient public record; treat the claim on its evidence alone
- `flagged` — retractions, unreplicated headline results, or integrity findings on record

**Credibility can lower confidence but never raise it above the grade ceiling.** An established
group's press release is still grade D. Reputation modulates trust in evidence; it does not
substitute for evidence.

> **TypeSafe (Jev / System One) is integrated as an advisory review layer** — see
> `docs/typesafe.md`. It checks claims against the source records, documents against claims, and
> conflicts against their evidence. Its signals are **uncalibrated review prompts, not verification**.
> That audit sees the record, never the paper, so a record that faithfully repeats a wrong abstract
> cannot be caught; a second, **paper-grounded check** judges claims against excerpts of the paper
> itself (`docs/typesafe-plan.md`). TypeSafe stores nothing, so what we keep of it is kept in git. It
> changes no claim, grade, credibility tier or conflict state. Whether it blocks
> publication is decided by a committed file, `reference/semantic_policy.yaml`, currently
> **`advisory`** (user, 2026-09-21): against the first live run its thresholds flagged 7 of 7 claims,
> 12 of 12 documents and 9 of 10 conflict pairs, which is no discrimination and froze the site.
> Credibility tiers above remain the authority until author records exist.

---

## Units and definitions

**All calculation and comparison happens in coherent SI base units. No exceptions.** Presentation
happens in field convention. These are two layers and they never mix.
`reference/definitions.yaml` is the single authority for both, and for terms whose definitions
vary between sources (EOT, drive current conditions, TOPS/W precision, node labels).

The rule is not "record the units" — it is **convert first, then reason**. Comparing two numbers
in different units is how a false claim gets made with everyone acting in good faith.

Every quantity carries three representations, with a fixed one-way derivation:

`as_published` → *(recorded conversion)* → `si_base` → *(display factor/offset)* → `display`

- **`as_published`** — the source's own number and unit, transcribed verbatim. The audit anchor:
  `verify-citation` must be able to check us against the paper without doing arithmetic.
  Never computed with.
- **`si_base`** — coherent SI. **Authoritative.** Every comparison, aggregation, threshold and
  derivation uses this and nothing else.
- **`display`** — field convention, rendered at the last moment. Never computed with.

This is not three sources of truth: a transcription, an authoritative value, and a rendering.
A comparison performed on `display` values is a defect even when the answer comes out right.

### SI normalization is not semantic comparability

Two numbers in identical SI units can still be incomparable. INT8 TOPS/W and FP16 TFLOPS/W both
reduce to operations per joule and remain different quantities. D0 under Poisson and under Murphy
share a unit and different meanings. EOT and CET are both lengths.

Converting units settles *dimension*. It says nothing about whether the two things were measured
under conditions that permit comparison. The SI rule must never become a reason to skip that
second question — see `contested_terms` in the definitions file, which exists precisely because
unit conversion cannot resolve semantic mismatch.

**Write the number with its conditions.** A value without units, temperature, voltage, geometry,
or test method is not a result — it's a rumor with digits.

**Node names are marketing, not dimensions.** "2nm" is a product name. Never treat process node
labels as physical measurements, never compare them across foundries as if they were, and always
prefer disclosed gate pitch, metal pitch, or transistor density.

**Distinguish always:** measured / simulated / projected / announced / rumored. Collapsing these
is the single most common way semiconductor reporting becomes false.

---

## The contradiction protocol

When a new claim appears to conflict with the ledger, **classify before acting.** Not every
disagreement is the same defect, and the four types get four different responses. Misclassifying
is itself an error.

**What counts as "appears to conflict".** The detector compares two claims only if they measure the
same quantity in the same SI unit, no condition they both name has a different value, **and they share
subject context**: at least one condition, named on both with an equal value, that says *what* was
measured (a device, material, component, architecture, process, mechanism). Operating points such as
temperature or frequency do not count as subject: two unrelated results at 300 K share 300 K and
nothing else. The last rule exists because claims with no condition in common were being treated as
comparable, and a computing time and an orbital lifetime opened a conflict that blocked publication. It
is `reference/comparability.yaml`, a committed file. **Nothing is silently dropped:** a pair that
disagrees numerically but shares no subject is listed in `ledger/not-compared.md` on every detection
run and counted on the open-contradictions register, so a real disagreement hiding behind mismatched
condition keys can be seen. A comparison that cannot be made is a fact about our conditions, not a
finding about the field.

### Type D — Definitional or unit mismatch *(check first; most apparent conflicts are this)*

Sources use different units, definitions, test conditions, or normalizations.
→ **Resolve by converting to SI base units and normalizing definitions.** Record the
normalization in `reference/definitions.yaml` so it is never redone. If normalization is
impossible, the claims are about different things — split them and scope each explicitly.

### Type C — Genuine field disagreement

Two credible sources disagree. Understanding *why* is the whole job, and the answer splits this
type in two. Never stop at "the field disagrees" — that is where the work starts, not ends.

**C1 — Scopable.** We understand why they differ *and* the reason determines when each holds
(different process maturity, sample quality, measurement technique, temperature regime).
→ **Resolve by scoping.** These were never one claim. Split into two claims, each explicitly
conditioned on what makes it true. The contradiction disappears because it was an artefact of
over-broad statements. Record the scoping in the conflict file.

**C2 — Unadjudicable.** We understand the disagreement, but no available evidence determines which
is right.
→ **The contradiction lives.** Mark both `contested`, cross-link them, **name the missing data**,
and surface it. Cite both sides in the digest with the gap stated plainly. Never average them,
never pick the more exciting one, never silently drop one. Flattening real scientific uncertainty
into false confidence is a fabrication.

C1 is the more common case and the easier one to miss — apparent deadlocks usually dissolve into
two well-scoped claims. Reach for C2 only after establishing that scoping genuinely fails.

### Type B — Supersession *(requires independent confirmation)*

Newer evidence legitimately overrides older evidence.
→ **One source can never supersede.** Supersession requires **two independent sources**.
Independent means: no shared corresponding author, no shared lead institution, and preferably a
different measurement method. Two papers from the same group count as one source.

- **Two or more independent sources** → old claim `superseded`, new claim `supersedes` it. Retire,
  never delete. If the superseded claim was published, the correction appears in the next digest.
- **One source only** → old claim becomes `challenged`, new claim recorded at its own grade, both
  cross-linked, and the conflict is held `live:data-absent` with `missing_data:
  awaiting-confirmation`. The old claim still stands, visibly flagged, until confirmation arrives.

### Type A — Internal contradiction

We asserted both X and not-X as fact. This is always our bug.
→ **Fix immediately, before any other work.** Halt the current task. Trace both claims to their
sources. Whichever misread its source is corrected or retracted. Then ask why the error got
through and fix that too.

### Conflict states

Every `CFL` record is in exactly one of three states.

**`resolved`** — the contradiction is gone. Closes with the reason: `normalized` (D) ·
`scoped` (C1) · `superseded` (B, independently confirmed) · `our-error` (A).

**`live:data-absent`** — the contradiction persists, legitimately. Permitted only with a named
`missing_data` entry (below), a `resolution_trigger` describing what would close it, and a place
in the open contradictions register. Both sides stay visible to the reader.

**`live:unexamined`** — we have not finished the work. **This is an error state.** It is the only
conflict state that blocks publication, and no record may sit here across a digest cycle. A record
lands here the moment a contradiction is detected and must leave before the next digest ships.

The distinction between the two `live` states is the entire discipline. `data-absent` is a claim
about the world; `unexamined` is a claim about us. Never let the second wear the costume of the
first — a `missing_data` entry written to make a record look closed is the most damaging thing
this project can do to itself.

### Naming the absence: `missing_data` categories

- `not-yet-measured` — the experiment that would settle it has not been performed
- `undisclosed-method` — sources exist but withhold the conditions needed to compare them
- `awaiting-confirmation` — one credible source stands unreplicated (per Type B)
- `access-blocked` — resolving evidence likely exists but sits behind a paywall

`access-blocked` is a consequence of the open-access-only policy, not a fact about the field.
It is tracked separately so the cost of that policy stays measurable: a rising `access-blocked`
count is evidence for revisiting source access, and it is reported to the user as such rather
than quietly accumulating.

### When to escalate to the user

Stop and ask — do not resolve by judgment — when:

- The type is genuinely ambiguous (especially C vs. A: is the field disagreeing, or did we err?)
- Resolution requires ranking two comparably credible sources against each other
- A **published** digest claim would need retraction or correction
- The inconsistency is in our own method, definitions, or taxonomy rather than in the sources
- Resolving it requires domain judgment we cannot ground in a source

Present: the two claims, their sources, grades and credibility tiers, the candidate
classifications, and what each resolution would cost. Then wait.

---

## The open contradictions register

Live contradictions are **published, not withheld**. A `live:data-absent` claim is never excluded
from the digest to keep things tidy — excluding it would present the corpus as more settled than
it is, which is the same falsehood as asserting a wrong number.

`ledger/open-contradictions.md` is the standing register, derived from `CFL` records. It is not
an appendix. It surfaces in four places, and all four are mandatory:

1. **A permanent top-level page on the site**, linked from the front page — not buried in an archive
2. **A section in every digest**, including when it is empty ("no open contradictions" is a
   finding, and an empty section that is never empty is a visible problem)
3. **Inline in every SOTA document**, at the point where the disputed claim appears — a reader of
   the DEV state-of-the-art must see the live disagreement without navigating elsewhere
4. **In-session to the user** whenever one is opened, aged, or closed

Every entry shows: both claims with sources, grades and credibility tiers, the `missing_data`
category, the named gap in plain language, what would resolve it, and how long it has been open.

**Ageing is tracked and reported.** A contradiction open for a week is normal; one open for six
months with an `awaiting-confirmation` gap is telling us something about the field, and one open
that long with an `undisclosed-method` gap is telling us something about our own investigation.
Re-examine on a schedule rather than letting entries calcify. Age is displayed, never hidden.

### The publication gate

Enforced by `pipeline/publication_gate.py` and run in CI before every deploy. Checks 3 and 8 are
structural only — the gate verifies a claim reference resolves and that a correction exists, not
that the prose faithfully represents the claim. The digest is rendered from ledger fields by
`sota.py`, which keeps it faithful by construction, but nothing in the gate checks that
independently. The gate names those limits rather than implying coverage it does not have.

On an empty corpus every check passes trivially, and the gate says so out loud: a vacuous pass is
not evidence it works. `pipeline/test_publication_gate.py` proves each check fires by running it
against deliberately broken fixtures.

Before any digest is published:

1. **No `CFL` record is in `live:unexamined`.** This is the hard gate — unfinished reconciliation
   blocks the digest outright
2. Every `live:data-absent` record has a named `missing_data` category and a `resolution_trigger`
3. Every digest sentence traces to an `active`, `challenged`, or `contested` ledger claim
4. Every claim under a live contradiction carries its flag wherever it appears
5. Every cited source has a corpus record, and its venue is a `verified` registry entry
6. Every quantity carries `as_published` and `si_base`, and every comparison was performed in `si_base`
7. No grade D/E material is phrased as fact
8. Any correction to a prior digest, and any change to a claim that had already been published, is
   stated plainly under `## Corrections` in a digest dated on or after it — never a silent edit.
   Mentioning the claim elsewhere in that digest does not count
9. The TypeSafe audit, **as its committed policy directs.** Under `advisory` (today) it always
   passes and reports its findings; under `blocking` a missing, stale, preview-only or incomplete
   audit fails, as does any flagged required record. The policy is a file, not a switch: no workflow
   input, environment variable or `continue-on-error` alters it, because a gate CI can route around
   is not a gate. A missing policy file means `blocking`.

**A published digest is never rewritten.** Errors in it are corrected in the *next* digest. The
digest builder refuses to change a digest that git already holds, dates digests in UTC so that CI
and a developer's machine agree, and builds each digest from the digests strictly before it.

---

## State of the art

`sota/` holds one living document per topic code — the standing answer to "where is this layer of
the stack right now." This is the project's primary output; digests are how it gets updated.

Each SOTA document carries: the current best-supported position with its key numbers in display
units (`si_base` recorded), what changed recently and why, every live contradiction shown inline
with both sides and its named data gap, the open questions the field hasn't answered, and a
last-reviewed date.

A SOTA document that reads as settled while the register holds live contradictions for its topic
is wrong, however accurate each individual sentence is. The reader's picture of certainty must
match ours.

SOTA documents are derived. Every statement traces to a ledger claim — no exceptions, no
"connective tissue" assertions that quietly introduce unsourced facts.

---

## Working rules

**Corrections are published, not hidden.** Once a digest is out, errors are fixed by visible
correction with a dated note. Never rewrite history to look right retroactively. The audit trail
is the product.

**Read before citing.** Abstract plus the figures/tables carrying the claim, at minimum. Never
cite from a title, another paper's summary, or a search-result snippet.

**One claim, one source of truth.** If the same fact needs to live in two places, one of them is
derived and must say so.

**Read what you published.** A page that returns 200 is not a page that is right. The live
2026-09-20 digest said "Nothing new" while the ledger held seven claims, and nobody noticed for a
day because only its status code had been checked.

**Say what was actually read.** `access` and `read_scope` describe what was looked at, not what was
available. Two records once claimed `full_text_figures` when no figure had been viewed (one had
only had its abstract read). A `never_inferred` field is not filled from memory or from author
order: corresponding-author flags inferred that way were recorded as fact and one was wrong (the
paper marks a different author), and an affiliation written from recall could not be confirmed and
was removed. All are in the records' `corrections` trails.

**Report faithfully.** If a harvest was thin, the digest says so. If a claim is weakly supported,
it says that. Never pad a digest to make a day look productive — an honest short digest is worth
more than a padded one, and padding is how low-grade material enters the ledger.

---

## Skills

Project skills live in `.claude/skills/`, the **canonical** copy. `.agents/skills/` is a generated mirror
for tools that read that path (Codex): edit only the canonical copy, then run
`python pipeline/sync_agent_skills.py`. `test_agent_files.py` fails CI if the two differ.
Each skill is one pipeline stage with one responsibility.
Planned roster, to be built incrementally:

| Skill | Stage | Responsibility |
|---|---|---|
| `harvest` | 1 | Sweep registry sources (CI, daily), then read candidates into source records. arXiv is read by `read_paper.py`; the skill covers the rest — **built** |
| `triage` | 2 | Relevance filter, dedupe against existing corpus (the TypeSafe triage samples candidates; the reader's abstract-only first call screens arXiv) |
| `extract-claims` | 3 | Source record → atomic claims, normalized to SI base units — **built** |
| `assess-source` | 3 | Build/update author records, assign credibility tier |
| `discover` | — | Condense READ material against a named gap; bounded loop, no network — **built** |
| `reconcile` | 4 | Detect (`reconcile.py`, mechanical) then classify (the skill, needs both sources read) — **built** |
| `digest` | 5 | *Not a skill, deliberately.* Derived by `sota.py` from the ledger; prose is the attack surface for unsourced facts — **built as code** |
| `publish` | 6 | Build and deploy the site, run the publication gate — **built** |
| `sota` | — | *Not a skill, deliberately.* Derived by `sota.py`, one document per layer plus a cross-stack synthesis — **built as code** |
| `verify-citation` | — | Audit: does this source actually say what we claim? |

**When writing or editing a skill:** it must not restate a rule from this file in different words.
Duplicated rules drift apart and become a Type A contradiction in our own instructions. Skills
reference `AGENTS.md` for doctrine and hold only their own mechanics.

---

## Stack and layout

Python for the pipeline (scholarly APIs, dedupe, unit conversion, ledger validation), Markdown and
YAML for all research artifacts, static site for publication. Git history is load-bearing — it is
how we diff what we claimed yesterday against today.

```
AGENTS.md                 the doctrine: single source of truth (CLAUDE.md only imports it)
.github/workflows/        CI: self-tests -> publication gate -> build -> deploy
sources/registry.yaml     relevant open-access venues, with verification status
sources/topics.yaml       topic tiers gating broad venues: core / adjacent / exclude
reference/definitions.yaml SI canonicalization, contested terms, NIST-sourced constants and bounds
reference/authorities/    authority files we fetched and keep, so derived numbers can be audited offline
reference/gold/           labelled cases for the semantic audit and the reader (independent review pending)
reference/semantic_policy.yaml  whether the semantic audit blocks publication: advisory | blocking
reference/reader_budget.yaml    the reader's monthly spending cap, model, and dated prices
reference/comparability.yaml    when two claims may be compared: the operating-point keys that do not count as subject
docs/typesafe.md          how the TypeSafe review layer works and its limits
docs/typesafe-plan.md     the TypeSafe integration plan: what it is for, the phases, the decisions
docs/typesafe-preregistration.md  what we expected from the first paper-grounded run, written before it ran
TODO.md                   open work: blocked, in flight, next; rules and state stay in this file
project-chat.md            the human decision trail: what was asked, decided, and which commit it produced
corpus/candidates/        sweep output; unread ones are queue, decided ones (read_decision) are not
corpus/questions/         TypeSafe packets (inputs, one per read paper) and answers (the exact questions and what came back)
corpus/papers/            immutable source records
corpus/authors/           author track record and credibility
ledger/claims/            CLM claims, one YAML file per topic code
ledger/conflicts/         CFL conflict records
ledger/open-contradictions.md  derived register, published to the site
ledger/not-compared.md    derived: pairs that disagree numerically but share no subject, so were not compared
discoveries/              DSC condensation briefs (derived working documents)
digests/                  daily published digests
sota/                     living state-of-the-art reviews, one per topic
pipeline/                 Python: verification tooling, then the harvest pipeline
_site/                    generated site output (gitignored; built in CI)
.claude/skills/           project skills (canonical)
.agents/skills/           generated mirror of the above; pipeline/sync_agent_skills.py
```

---

## Deployment

Live at **https://codeartflow.github.io/project-electron/** — public repo, GitHub Pages, built
and deployed by `.github/workflows/deploy.yml` on every push to `main`.

The repository is public deliberately. This project's claim is that every statement traces to a
source and a reader can check it; a private audit trail would make that claim unverifiable. The
ledger, the conflict records, the corrections and the git history are the product as much as the
digests are.

GitHub Pages requires either a public repository or a paid plan — a private repo on the free plan
is rejected with "Your current plan does not support GitHub Pages for this repository." If the
repo is ever made private again, deployment must move to Cloudflare Pages, Netlify, or a
separate public site repo.

The workflow is: self-tests → publication gate → build → deploy. Pull requests build and are
gated but never deploy. There is no `continue-on-error` and no manual override input anywhere in
it, because a gate CI can route around is not a gate.

---

## Current state — 2026-09-22

**What exists and runs.** The full pipeline: verified registry, daily sweep (`harvest.yml`, 06:15
UTC), daily arXiv reader (`read.yml`, 06:45 UTC), reconcile, derived SOTA/synthesis/digest, the
nine-check publication gate, and a live site. The whole deterministic pipeline runs in about 12 s.
`read.yml` now regenerates SOTA, synthesis and the digest from the ledger and commits them itself
right after reading (D4, decided 2026-09-22), so the site no longer waits on someone running
`run_pipeline.py` by hand.

**What the corpus holds** (counted from the repository on 2026-09-22). 12 source records (3 read by
hand, 9 by the automated reader) and 27 active claims (14 ARCH, 3 DEV, 5 MAT, 4 PHOT, 1 PROC, all
grade B; 20 automated), which is **5 of 10 layers**. Three further DEV claims
(`CLM-DEV-0002..0004`) were retracted 2026-09-22 (D7): they were fabrication-environment details
(a deposition chamber's base pressure, an ITO substrate's sheet resistance) extracted as
freestanding claims from a paper that yielded no result claim for them to be a `conditions` entry
on, so they had no claim to condition and did not belong in the ledger on their own. 11 conflicts,
all `resolved` (the six opened by the first scheduled reading run, `CFL-0006..0011`, were closed as
`scoped` once the comparability rule in *The contradiction protocol* was fixed). 314 candidates are
unread: 117 arXiv (the automated lane) and 197 publisher (manual; about 25% fetchable as full
text). Of the arXiv ones already handled, 29 were judged out of scope, 8 were read with no claim
accepted (`no_claims`) and 2 were too long.

Open work is tracked in **`TODO.md`**. Keep it and this section consistent: facts about the state live
here, tasks live there.

**The reader has run live, on 2026-09-21, and its first two results taught different things.**
With `gemini-3.5-flash-lite` alone, 12 papers cost $0.041: 8 were out of scope and 4 were read in
full, and the verifier accepted **0 claims** and rejected 6. Every rejection was correct (a magnetic
field labelled as a voltage, a "25%" labelled as an area, statements that added model names their
quotes lack), so recall was zero but nothing false entered. With `gemini-3.6-flash` extracting, 12
papers cost $0.127 and **10 claims were accepted** from 3 papers, and 3 more papers gave none.

The first scheduled reading run (13:21 UTC) then read 25 candidates for $0.18 (12 out of scope, 6
read, 5 `no_claims`, 2 too long), accepted 13 claims and opened 6 conflicts that block the deploy. Five
are between claims of *different, unrelated* papers that share only a generic quantity name (a
computing time against an orbital lifetime, two unrelated temperatures) with no shared condition, and
one is two different mode spacings of one device with identical structured conditions. So the
comparability rule, not only the reader, is at fault: two claims with no shared context are treated as
comparable. The user decided the same day to add a deterministic guard, and it has landed (rule 3 of
*The contradiction protocol*; `reference/comparability.yaml`). Under it the five cross-paper pairs are
no longer compared. The sixth (two different mode spacings of one device, identical conditions) is not
separated by any guard and was scoped by hand, with the spacing symbol added as a condition. The daily
reading run was paused while this was fixed.

Earlier the same day, 10 claims opened four conflicts, and all four were between claims of **one paper** and caused by
our method: numbers of the same kind (the power of different arrays, the temperature of different
calculations) carried nothing to tell them apart, and the detector saw them as comparable. The
publication gate blocked the deploy, as designed. The user decided to scope them (they are
`CFL-0002..0005`, resolved as `scoped`, with non-public correction entries on the claims) and to fix
the reader, whose prompt `reader-v3` now asks for distinguishing conditions and whose verifier
rejects a number that has none. Not fixed, and not checked by the verifier: statements can carry words
that are not in their anchor quotes ("in BLG", "acoustic phonon" for the paper's "AP"). The
paper-grounded TypeSafe check tests exactly that. It was built and run once on 9 papers (2026-09-21,
about $0.003, scored against expectations committed first): it found one model-supplied word ("CMOS"),
missed two errors a person then found by reading (synthesis results labelled `measured`, which the
reader and TypeSafe both got wrong; three fabrication details called results), and is a smoke test, not a
calibration (`docs/typesafe-preregistration.md`).

```bash
python pipeline/run_pipeline.py --no-sweep        # the whole flow, timed (writes run/timings.json)
python pipeline/read_paper.py --dry-run           # fetch and size the arXiv queue; no API, no writes
python pipeline/read_paper.py --max-papers 25     # read (needs GEMINI_API_KEY; spends, capped at $10/month)
python pipeline/budget.py                         # spend so far this month, and what today may spend
python pipeline/gold_eval.py --status             # gold set size, and what is still missing
python pipeline/gold_eval.py --score REPORT.json  # score an audit report against the gold labels
python pipeline/bounds.py --verify                # definitions vs the NIST authority file
python pipeline/harvest.py --dry-run              # preview a sweep
```

Tests (all run in CI before any deploy): `validate_registry.py`, `units.py`, `bounds.py --verify`,
`claims.py --self-test`, `test_extract_e2e.py`, `test_publication_gate.py`, `test_discover.py`,
`test_bounds.py`, `test_authority_bounds.py`, `test_gold_eval.py`, `test_reader.py`,
`test_build_site.py`, `test_budget.py`, `test_comparability.py`, `test_excerpts.py`,
`test_paper_check.py`, `test_assess_quality.py`, `test_semantic_checks.py`, `test_agent_files.py`.

**Registry.** 125 active entries: 70 `true`, 48 `review`, 7 `false` (evidence in `pipeline/*_report.json`).

**Open decisions and known gaps.**
- **`GEMINI_API_KEY` secret** must be added by the user (Settings → Secrets → Actions) before the
  reader runs. Never in a file or in chat. The user should also set Google's own monthly cap (see
  *Reader budget*): ours is the second line of defence.
- **Reading cost is only partly measured.** Measured: 12 papers cost $0.041 on Flash-Lite, of which 4
  were in scope, and a screening call costs about a tenth of a cent. Not measured: the extraction
  call on `gemini-3.6-flash`. The median arXiv paper fetched (measured on 14) is about 59,000
  characters; at an assumed 3 to 4 characters a token that is 15,000 to 20,000 input tokens, plus an
  assumed 3,000 output tokens. At $0.75/$3.75 that is about $0.025 for a full read in 2026 and about
  twice that after 2027-01-01. The reader takes up to 40 candidates a day (raised from 25, D5,
  2026-09-22). If a third are in scope (this batch had 4 of 12) that is about 13 full reads, roughly
  $0.33 a day or $10 a month in 2026 - at the cap - and over it after the price doubles, which is
  when the pacing throttles extraction rather than overspending. `python pipeline/budget.py` shows
  the real spend; trust that over this.
- **CI now regenerates the SOTA and digest pages after reading (D4, 2026-09-22).** `read.yml` runs
  `sota.py --sota`, `--synthesis` and `--digest` right after reconciling, and commits `sota/` and
  `digests/` alongside `corpus/` and `ledger/`. Deploy still decides whether any of it reaches
  readers: the publication gate runs at deploy time regardless of what got committed here, so an
  unexamined conflict still blocks the site on the last good build.
- **Throughput (D5, decided 2026-09-22: raise the cap, not a second daily run).** The first sweep
  queued 98 arXiv candidates over a three-day look-back, about 33 a day, and every run so far has
  hit the paper cap in well under its time budget (25 papers took 78s against a 900s budget on the
  biggest run yet) - the bottleneck was the paper count, not time. Raised proportionally instead of
  adding a second scheduled run: a run is now capped at 40 papers and 1440s (the workflow's timeout
  is 30 minutes), keeping the same one-run-a-day shape while covering the ~33/day inflow with
  headroom. The cost estimate above already reflects this.
- **The semantic audit is advisory and uncalibrated.** The gold set is a seed (15 cases, labelled by
  the same agent that made the extractions, no independent review, no defective *publication*
  examples), so no threshold can yet be validated. `python pipeline/gold_eval.py` shows where it
  stands. Scored against the first live audit (question set semantic-v1): the shipped thresholds
  flagged 15 of 15 cases (all 5 real defects caught, all 10 clean cases falsely flagged); a "flag only
  confident adverse answers" rule at 0.5 caught 4 of 5 defects with 1 false alarm. That is a hint
  about where a threshold might sit, not a validation of one, and it predates the semantic-v2 questions.
- **The audit cannot see the paper.** The wrong "EDP-optimal" condition on `CLM-ARCH-0004` was
  invisible to it because the record repeated the abstract's error. Only reading the paper found it.
- **Independence for arXiv sources (D3, decided 2026-09-22: wait for author records).** arXiv states
  no corresponding author, and `reconcile` correctly treats missing metadata as not-independent, so
  two arXiv papers can currently never be established independent of each other and no arXiv-only
  supersession is possible. The user chose to leave this as-is rather than adopt a fallback rule now:
  arXiv-only supersession stays impossible until `assess-source` (A3) builds real author records.
- **Publisher lane (D6, retried 2026-09-22): still no automated route.** Europe PMC's 503 was not
  the real problem: retried live on three unread Nature Communications DOIs, it now answers (200)
  but reports **zero hits** for all three (`hitCount: 0`) - Europe PMC indexes biomedical/MEDLINE
  literature, not materials science or photonics, so it is the wrong tool for most of this corpus
  regardless of uptime. Also checked whether the landing page itself carries full text: a plain GET
  on the DOI resolver for the same paper returns HTTP 200 (not blocked) but only the page shell -
  navigation, notices, CSS - with the actual article body absent from the initial HTML, and
  Crossref's `link` metadata for the same DOI points at that identical landing-page URL, not a
  separate XML/PDF endpoint. Confirms rather than overturns the existing finding (9 of 36 publisher
  candidates fetchable, most gated or JS-rendered): no legitimate full-text API was found this
  session. `harvest` skill (human reading) stays the primary route; a further candidate (CORE,
  which needs a registered API key) is unexplored.
- **Semantic Scholar** rate-limits unauthenticated requests. A free key is an enhancement, not a blocker.

**Verification findings worth carrying forward.**
- *IEEE Open Journal of the Electron Devices Society* does not exist (registry `removed:`). A first
  draft blended two real IEEE titles; only checking against Crossref caught it.
- Four venues block automated access (TechRxiv, ChemRxiv, Intel, Applied Materials, HTTP 403) and two
  never answered (EE Times, WikiChip). **Not evaded.**
- Crossref journal records can carry stale ISSNs (Physical Review B). Verify by current ISSN.
- The hand-typed "59.6 mV/dec at 300 K" was wrong; the exact constants give 59.53. It is now derived
  from `reference/authorities/nist-codata-2022-allascii.txt` and a test fails if they drift.
- PyYAML reads `6.02e23` (unsigned exponent) as a **string**. Write `6.02e+23`.
- A dimensionless quantity once ignored its unit (`2 percent` stored as 2.0, `5 joule` accepted).

**Keep this section honest.** It is the one part of this file guaranteed to go stale, and a stale
AGENTS.md is an inconsistency in the project's own foundation. Update it whenever a stage lands.
