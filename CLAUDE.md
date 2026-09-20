# CLAUDE.md — Project Electron

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

Eight artifact types. Each has exactly one job. Never blur them.

| Artifact | Path | Job | Mutability |
|---|---|---|---|
| **Source registry** | `sources/registry.yaml` | Every relevant open-access venue we harvest | Curated, append-mostly |
| **Definitions** | `reference/definitions.yaml` | SI canonicalization and contested terms — the normalization authority | Curated |
| **Source record** | `corpus/papers/` | What a specific paper says, in its own terms | Immutable once written |
| **Author record** | `corpus/authors/` | Public track record behind a source's credibility | Updated as record grows |
| **Claim** | `ledger/claims/<TOPIC>.yaml` | An atomic assertion *we* stand behind, with provenance | Amended only via supersession |
| **Conflict** | `ledger/conflicts/CFL-nnnn.md` | A contradiction, its state, and its named data gap | Live until resolved |
| **Open register** | `ledger/open-contradictions.md` | Reader-facing view of every live contradiction | Derived — regenerated each cycle |
| **Digest / SOTA** | `digests/`, `sota/` | Reader-facing prose | Derived — never a source of truth |

**The derivation rule:** digests and SOTA documents may only restate claims that exist in the
ledger. If you find yourself writing a sentence in a digest that isn't in the ledger, stop —
either it belongs in the ledger first, or it doesn't belong in the digest.

### Claim anatomy

Claims are atomic and falsifiable. "GAA transistors are promising" is not a claim. A claim carries:

- `id` — `CLM-<TOPIC>-<nnnn>`, stable forever, never reused
- `statement` — one assertion, with measurement conditions
- `quantity` — `as_published` / `si_base` / `display` per `reference/definitions.yaml`, where the
  claim turns on a number
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

> **Planned:** integrate *Jev* and *System One Model* (TypeSafe) for credibility and confidence
> scoring if access is obtained. We have no verified information about these tools' inputs,
> outputs, or methodology yet, so nothing downstream depends on them. Until they are documented
> here from a real source, the tiers above are the authority. Do not implement against assumed
> behavior.

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
that the prose faithfully represents the claim, which stays the `digest` skill's judgement. The
gate names those limits rather than implying coverage it does not have.

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
8. Any correction to a prior digest is stated plainly in the new one — never a silent edit

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

**Report faithfully.** If a harvest was thin, the digest says so. If a claim is weakly supported,
it says that. Never pad a digest to make a day look productive — an honest short digest is worth
more than a padded one, and padding is how low-grade material enters the ledger.

---

## Skills

Project skills live in `.claude/skills/`. Each is one pipeline stage with one responsibility.
Planned roster, to be built incrementally:

| Skill | Stage | Responsibility |
|---|---|---|
| `harvest` | 1 | Sweep registry sources, write corpus records |
| `triage` | 2 | Relevance filter, dedupe against existing corpus |
| `extract-claims` | 3 | Source record → atomic claims, normalized to SI base units — **built** |
| `assess-source` | 3 | Build/update author records, assign credibility tier |
| `reconcile` | 4 | Run the contradiction protocol; regenerate the open contradictions register |
| `digest` | 5 | Compose the daily digest from ledger claims only |
| `publish` | 6 | Build and deploy the site, run the publication gate — **built** |
| `sota` | — | Maintain living state-of-the-art reviews per topic |
| `verify-citation` | — | Audit: does this source actually say what we claim? |

**When writing or editing a skill:** it must not restate a rule from this file in different words.
Duplicated rules drift apart and become a Type A contradiction in our own instructions. Skills
reference `CLAUDE.md` for doctrine and hold only their own mechanics.

---

## Stack and layout

Python for the pipeline (scholarly APIs, dedupe, unit conversion, ledger validation), Markdown and
YAML for all research artifacts, static site for publication. Git history is load-bearing — it is
how we diff what we claimed yesterday against today.

```
.github/workflows/        CI: self-tests -> publication gate -> build -> deploy
sources/registry.yaml     relevant open-access venues, with verification status
reference/definitions.yaml SI canonicalization and contested terms
corpus/papers/            immutable source records
corpus/authors/           author track record and credibility
ledger/claims/            CLM claims, one YAML file per topic code
ledger/conflicts/         CFL conflict records
ledger/open-contradictions.md  derived register, published to the site
digests/                  daily published digests
sota/                     living state-of-the-art reviews, one per topic
pipeline/                 Python: verification tooling, then the harvest pipeline
_site/                    generated site output (gitignored; built in CI)
.claude/skills/           project skills
```

---

## Current state — 2026-09-20

Doctrine, a verified source registry, verification tooling, the `extract-claims` stage, and a
deployable site with the publication gate wired into CI. No harvest yet, so no source records and
no ledger entries exist — the machinery is built and tested but has nothing to consume until
`harvest` lands. The site renders that empty state honestly rather than showing placeholders.

**Registry: verified 2026-09-20.** 131 entries — 71 `true`, 47 `review`, 7 `false`. Grew from ~70
during verification. Evidence in `pipeline/*_report.json`; reproduce with the commands below.

```bash
python pipeline/validate_registry.py              # registry internal consistency (gates harvest)
python pipeline/verify_registry.py --section all  # external re-verification
python pipeline/discover_journals.py              # vet candidate additions
python pipeline/probe_urls.py                     # reachability for non-journal venues
python pipeline/units.py                          # SI engine + validates definitions.yaml
python pipeline/claims.py --self-test             # extraction refusals + claim validation
python pipeline/claims.py --validate              # validate the whole ledger
python pipeline/test_extract_e2e.py               # full extract path on synthetic fixtures
python pipeline/publication_gate.py               # the 8 checks; blocks publication
python pipeline/test_publication_gate.py          # proves every gate check actually fires
python pipeline/build_site.py                     # build _site/ (runs the gate first)
```

`pipeline/units.py` is built on `pint`. Never convert by hand and never write a `quantity` block
manually — `UnitEngine.record()` emits `as_published`/`si_base`/`display` together so they cannot
drift apart. `reference/schemas.yaml` defines the source-record and claim shapes, the quantities
that require stated conditions, and the seven extraction refusals.

Environment: Python 3.14.3, pip 25.3. Dependencies in `pipeline/requirements.txt`.

Verification findings worth carrying forward:
- One first-draft entry, *IEEE Open Journal of the Electron Devices Society*, **does not exist**.
  Recorded in the registry's `removed:` section. The IEEE Open Journal series is real (OJ-SSCS,
  OJ-Nano, OJ-CAS are all verified); that specific title is not.
- Four venues block automated access outright (TechRxiv, ChemRxiv, Intel, Applied Materials —
  all HTTP 403). Their content is open; our access is not. **Not evaded** — they need a
  legitimate route before harvest.
- Two did not respond at all (EE Times, WikiChip). Unresolved, so `false`.
- Crossref journal records can carry stale ISSNs: Physical Review B's record lists only legacy
  ISSNs returning zero works. Verify by current ISSN, never by the record's ISSN list.

Known temporary violation: `ledger/open-contradictions.md` is declared a derived artifact but is
currently hand-written, because `reconcile` does not exist yet. Recorded rather than left
implicit; closes when `reconcile` lands.

Settled: units. Coherent SI for all calculation and comparison, field convention for display
(user, 2026-09-20). `reference/definitions.yaml` is at schema_version 2; the v1 per-quantity
non-SI exceptions are removed.

Open decisions:
- **Semantic Scholar** rate-limits unauthenticated requests to unusability (HTTP 429). A free key
  is available on request. OpenAlex covers the same ground, so this is an enhancement, not a blocker.
- Jev / System One Model (TypeSafe) undocumented; credibility tiers are the authority until then.
  Nothing downstream depends on them, so this does not block the build.

**Keep this section honest.** It is the one part of this file guaranteed to go stale, and a stale
CLAUDE.md is an inconsistency in the project's own foundation. Update it whenever a stage lands.
