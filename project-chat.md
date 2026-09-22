# Project chat — the human decision trail

**What this is.** A chronological record of what the user actually asked for and decided, session by
session, and which commit each decision produced. It exists so a future agent (or the user) can see
*why* the codebase looks the way it does without re-reading the whole transcript.

**What this is not.** Not doctrine (`AGENTS.md`), not a task list (`TODO.md`), not a state summary
(`AGENTS.md`, "Current state"). Those three stay the authority on rules, open work and facts; this file
does not restate their content, only points at it. Prompts below are paraphrased, shortest first.
`corpus/candidates/_reader_spend.json` and `_read_runs.jsonl` are decided, not narrated, here.

**Coverage gap, stated plainly.** The transcript for everything up to and including commit `d9fc82c`
(2026-09-20) was not preserved anywhere this agent can read. That phase is reconstructed from commit
messages and from what `AGENTS.md` records as history — real, but not the user's own words. Everything
from "Switch the reader to Gemini" onward is paraphrased from the actual conversation.

**Keeping this current.** Append a new dated section per session, in the same shape: prompt, decision,
commit(s). Do not edit old sections except to fix an error, and say so if you do (this project's own
rule about corrections applies to its own chat log).

---

## Quick reference: decisions already made — do not re-ask

| Question | Decision | Commit |
|---|---|---|
| Which single doctrine file? | `AGENTS.md`; `CLAUDE.md` only imports it | `525c300` |
| Skills in two places (Claude vs. Codex)? | Canonical + generated mirror, CI guard | `70c2f26` |
| Which LLM provider/model for the reader? | Gemini, not Claude; `gemini-2.5-flash` refused live (404) by Google despite docs | `8089fea`, `43539c8`, `c9ada74` |
| Reader model, final | Screening `gemini-3.5-flash-lite`, extraction `gemini-3.6-flash` | `3a96164` |
| Reader monthly budget | $10/month cap, second line of defence after Google's own spend cap (user action U1, not yet done) | `6322285` |
| A paper the reader accepts 0 claims from | Kept as a candidate (`no_claims`), never retired | `3a3d663` |
| Cross-paper false conflicts (`CFL-0006..0011`) | Deterministic comparability guard first (not TypeSafe pair triage) | `3c551e5` |
| TypeSafe integration order | Claims-against-the-paper (phase 1–2) built before anything else in the plan | `968421d` |
| TypeSafe's role | Advisory only (`reference/semantic_policy.yaml`); never changes a claim, grade, credibility or conflict state | `d9fc82c` |
| Daily reading schedule | Paused twice for false-conflict fixes, resumed each time once the fix deployed; currently **running** | `3c551e5` |
| Fabrication-recipe claims (`CLM-DEV-0002..0004`) | Retracted, not relabelled: they're conditions with no claim to attach to (D7, 2026-09-22) | this session |
| CI regenerating SOTA/digest after reading | Yes, fully automatic — `read.yml` runs it right after reconciling (D4, 2026-09-22) | this session |
| Independence for arXiv-only sources | Wait for author records (A3), no fallback rule for now (D3, 2026-09-22) | this session |
| `reader-v4` (N3/N10/N12 prompt fixes) | Build + pre-register now; then, asked whether to push, chose to push and let the live run happen on the next daily schedule rather than pause it (2026-09-22) | this session |

---

## Origins, 2026-09-20 (no transcript retained: reconstructed from git log and `AGENTS.md`)

Built in one long first push, `0755213` → `d9fc82c`:

- Doctrine, the verified open-access source registry, and the registry verification tooling (`0755213`).
- `extract-claims`: the SI conversion engine (`pipeline/units.py`), claim schemas, extraction refusals (`4a73b59`).
- Topic filtering rebuilt on OpenAlex topic IDs after a keyword allowlist measured at **zero of 49**
  already-harvested candidates passing (`0593627`) — recorded in `AGENTS.md` as the reason topics.yaml
  exists at all.
- The full pipeline wired end to end — harvest, reconcile, sota, digest, publish — and its first real
  run (`d4b75ac`); made deployable on GitHub Pages with the publication gate in CI (`ec221ac`); the site
  went live (`265757c`).
- TypeSafe (Jev/System One) integrated as a semantic-audit adapter (`5c2fee6`, `96f40a7`), then made
  **advisory by committed policy** after its first live audit flagged 15 of 15 cases with no
  discrimination (`d9fc82c`, which also seeded the gold set).
- The reader first built to call **Claude**, not Gemini (`787ec7a`) — later switched, see below.
- ARCH claim corrections, a bound-qualifier fix, the corrections trail and digest immutability
  (`21a914b`) — the incident (a hand-typed bound stored as an exact value) is recorded in `AGENTS.md`'s
  claim-anatomy section, not repeated here.

Other findings from this phase live only in `AGENTS.md`, "Verification findings worth carrying
forward": the fake *IEEE Open Journal of the Electron Devices Society* venue, stale Crossref ISSNs,
PyYAML silently reading `6.02e23` as a string, and a dimensionless quantity once accepting `2 percent`
as `2.0`.

## AGENTS.md becomes the single source of doctrine

**Prompt (paraphrased):** why not one file, like `AGENTS.md`, as the single source of truth, and point
every agent at it instead of restating rules elsewhere.

**Decided:** commit and push; mirror the skills into `.agents/skills/` from one canonical copy with a
CI guard, rather than hand-keeping two copies in sync.

**Result:** `525c300`, `70c2f26`. `pipeline/test_agent_files.py` now fails CI if `CLAUDE.md` grows its
own rules or the two skill trees diverge.

## Switch the reader from Claude to Gemini, and cap spend

**Prompt (paraphrased):** stop using `ANTHROPIC_API_KEY`; use `GEMINI_API_KEY` and a Gemini Flash
model; keep spend to about $10/month.

**Decided (AskUserQuestion):** commit and push.

**Result:** `6322285` (`pipeline/budget.py`, checked before every call, paced, fails closed — see
`AGENTS.md`, "Reader budget"), `8089fea` (reader switched to Gemini 3.8 Flash, spending through the
budget).

## Choosing which Gemini model, in three tries

**Prompt (paraphrased):** for the first live run, use `gemini-2.5-flash` — volumes are high and this
should be a live call, not a dry run.

**What happened:** `43539c8` set it up; the live API then refused `gemini-2.5-flash` outright (HTTP
404, "no longer available to new users") despite Google's own docs listing it as stable with no
shutdown date (`78790e0`). Recorded in `AGENTS.md`, "Reader budget": *a docs page is not proof a model
can be called.*

**Decided (AskUserQuestion):** `gemini-3.5-flash-lite` (recommended, and chosen).

**Prompt, mid-turn:** pick the cheapest valid flash model, not the newest one.

**Prompt, mid-turn, correcting a re-litigation:** "Stop. We have already chosen 3.5 flash lite."
→ saved as a standing preference: once the user has answered, act on it, do not reopen it.

**Result:** `c9ada74`.

## First live run: zero claims accepted, and what to do about it

**What happened:** with `gemini-3.5-flash-lite` alone, 12 papers cost $0.041 and the verifier accepted
**zero** claims — every rejection was correct, but nothing useful came through either (`63a8a41`,
`938c2d7`).

**Decided (AskUserQuestion):**
- A paper the reader gets nothing usable from stays a candidate (`no_claims`), never silently retired
  — retiring had already deleted four real candidates by mistake.
- Split the two calls: `gemini-3.5-flash-lite` screens (title/abstract, cheap, high volume),
  `gemini-3.6-flash` extracts (whole paper, where quality matters).

**Result:** `3a3d663`, `3a96164`. With the split, the same 12 papers gave **10 accepted claims** from 3
papers.

## The TypeSafe idea is proposed

**Prompt (paraphrased):** now that a stronger model reads the papers, have it translate the whole paper
into TypeSafe-specific questions; use TypeSafe to store and validate information across papers and
fields.

**What happened:** this is the seed of the paper-grounded check built later (see "TypeSafe planned
properly" below). It was not built immediately — the next scheduled run surfaced a more urgent problem
first (false conflicts), and the user later stopped a half-built prototype to plan TypeSafe properly.

## Same-paper false conflicts, and reader-v3

**What happened:** the first scheduled daily run read 3–6 papers and opened 4–6 conflicts
(`091fcd5`, `3456f1d`). The first batch were all within **one paper**: numbers of the same kind (power
of different arrays, temperature of different calculations) carried nothing to tell them apart, so the
detector saw unrelated numbers as contradicting each other.

**Decided (AskUserQuestion):**
- Scope the false conflicts by hand and fix the reader's method (rather than just closing the tickets).
- Let the daily schedule keep running.
- TypeSafe's first job: claim packets, checked against the paper (not pair-triage of conflicts, not
  document review first).

**Result:** `dabaab4` (scoped `CFL-0002..0005`; claims must state their conditions identically in two
places, or validation refuses them), `29a08cd` (reader-v3: a claim's number must have a verified
condition saying what it is a value of, or it is rejected).

## "Continue, and build a TODO.md"

**Prompt (paraphrased):** continue the remaining work; also create a `TODO.md` to track everything.

**Result:** `2e2632c` — `TODO.md` created (work only; rules and state facts stay in `AGENTS.md`), and a
first cut of `docs/typesafe-plan.md`.

## Cross-paper false conflicts halt the half-built TypeSafe prototype

**What happened:** the first fully scheduled run (06:45 UTC path) read 25 candidates and opened 6
conflicts (`3456f1d`). Five were between claims of **different, unrelated papers** sharing only a
generic quantity name (a computing time against an orbital lifetime, two unrelated temperatures) with
no shared condition; one was two mode spacings of one device with identical conditions.

**Prompt (paraphrased):** stop — let's first plan the TypeSafe integration properly. TypeSafe is good
at yes/no, true/false, classification and ratings (implying: use it for that, not for things it is not
suited to, and plan before building further).

**Decided (AskUserQuestion, four questions):**
1. Comparability: a deterministic guard first (not TypeSafe pair triage — that can refine it later).
2. The TypeSafe plan: approved as written; claims-against-the-paper (phase 1) built before anything
   else in it.
3. Daily reading schedule: paused until the guard lands.
4. Docs: commit and push the planning docs only (no code yet).

**Result:** `3c551e5` (`reference/comparability.yaml`; a pair is compared only if it shares subject
context; non-comparable disagreements logged to `ledger/not-compared.md` instead of dropped; closed
`CFL-0006..0011`); `968421d` (`docs/typesafe-plan.md` approved in full, `docs/typesafe-preregistration.md`
committed **before** any TypeSafe answer existed). Reading Google's own TypeSafe docs during this
planning pass changed the design in two ways a half-built prototype had wrong: send filtered excerpts,
not the whole paper, and keep every numeric check in code, not in TypeSafe's judgment. Saved as a
standing preference: plan large integrations in `docs/`, get approval, pre-register expectations before
the first live run.

## TypeSafe phases 1–2 run live, scored against pre-registered expectations

**What happened (autonomous — the plan was already approved, no new prompt needed):** built
`pipeline/excerpts.py`, `pipeline/question_packets.py`, `pipeline/paper_check.py` (`968421d`, `e89b20b`),
then ran the check live on 9 papers for about $0.003 (`00602fc`). Scored against
`docs/typesafe-preregistration.md`, written before any answer existed:

- 12 of 15 right on "is this a reported result" — meets the pre-registered bar by the letter, falls
  slightly short of it as a proportion (the file's own count of "14" was a miscount of its own 15-row
  tables; left visible as a correction rather than fixed silently).
- Found one real defect TypeSafe caught and a person confirmed: the reading model had added "CMOS" to a
  statement; the excerpts sent to TypeSafe contain no such word.
- Found one real defect **TypeSafe missed**: three MiX claims and their source record were labelled
  `measured` when the paper's own caption says the figures are RTL synthesis estimates. The reader and
  TypeSafe **agreed** and were both wrong — only a person reading the excerpt caught it. Recorded as a
  concrete instance of the plan's principle that two models agreeing is weak evidence, never proof.
- Corrections applied to `CLM-ARCH-0007/0008/0009` and `SRC-00005` (evidence_type → `simulated`;
  "CMOS" removed), all non-public (nothing published cited them). `CLM-DEV-0002..0004` were **not**
  corrected — no evidence-type label fits fabrication-recipe details, which is TODO D7.

## This session (2026-09-22): measuring and fixing the reader, no new user steering

**Prompt:** continue the remaining items in `TODO.md` (no further direction given).

- **N4 — measure the reader.** Added `pipeline/read_report.py`: every run now appends a compact record
  to `corpus/candidates/_read_runs.jsonl` (the five earlier runs were backfilled from git history so
  nothing already spent is lost from the record). Rejections are bucketed by *why* the verifier refused
  them and now keep the quotes the model offered, so a rejection can be audited later rather than taken
  on faith. Finding: of 35 rejections logged so far, 16 (46%) are a statement naming something (a
  material, a model name, a thickness) that none of its quotes contain — the check working as intended
  — and 11 are units. Commit `ba70527`.
- **N2 — recoverable unit spellings.** Of those 11 unit rejections, 6 were spellings `UnitEngine` could
  have parsed: a PDF-mangled ring-above angstrom (`˚A`), and a lost superscript (`mm2`, `cm-2`,
  `Ω sq-1`, `mV dec-1`). Added `UnitEngine.published_unit()` (`pipeline/units.py`) to rewrite these for
  conversion only — `as_published` still keeps the paper's own spelling — and only when the letters
  before the exponent are a unit on their own, so it cannot launder a wrong unit. Tests assert both
  directions: the recoverable spellings now convert, and everything that was rightly refused (an
  invented `TFLOPGEMM/s`, `dB` for a power, `T` for a voltage, `%` for an area) still is. Commit
  `17e563d`.
- **N12 opened, not yet built.** The largest rejection class (N4) is a statement using a word or number
  none of its quotes contain. The prompt (`reader-v3`) never actually tells the model that the statement
  itself, not just its conditions, is checked. Proposed for a future `reader-v4` together with N3
  (a distinguishing condition is required but not verified to actually distinguish) and the synthesis
  half of N10 (make "RTL/EDA synthesis results are `simulated`" explicit in the prompt). Not started:
  per the standing preference, a prompt change needs its own expectations written first.
- **This file.** The user asked for this conversation's decision trail to be written to the repo as
  `project-chat.md`, covering the project from its start, so a future agent can pick up context without
  re-reading the whole transcript.

---

## This session (2026-09-22, continued): TODO cleanup and four decisions

**Prompt (paraphrased):** use `project-chat.md` as context, knock off as many `TODO.md` items as
possible, and ask for any input or key decision through the Q&A interface rather than guessing.

**Done without a decision (facts, not judgment calls):**
- **N6** — the Research checks page rendered the audit as raw Markdown inside a `<pre>` tag instead
  of through the site's own `md()` renderer. One-line fix.
- **H4** — checked live (`gh api repos/actions/<name>/releases/latest`) rather than assuming: GitHub
  removes Node 20 from Actions runners on 2026-09-23, one day out, so this had become urgent, not
  just hygiene. Bumped every workflow to the current Node 24 majors.
- **H5** — `harvest.py` named candidate ids and `harvested_date` from the machine's local date while
  digests are dated in UTC, exactly the divergence `AGENTS.md` already warns about for digests. Fixed,
  and the same audit found the identical bug already present in `sota.py` (the `Last reviewed` /
  `Generated` stamps) and `build_site.py` (the footer stamp) — three more places nobody had checked.

**Decided (AskUserQuestion, four questions, then one follow-up to nail down D7's mechanics):**
1. **D7 (fabrication-recipe claims).** The user's framing reset how this was understood: these
   values are *conditions*, not claims — `AGENTS.md`'s own claim anatomy already has a place for
   "what environment was this validated under" (`conditions`, carried on the claim it conditions).
   `CLM-DEV-0002..0004` had no result claim from `SRC-00006` to attach to, so on confirmation they
   were retracted (status only, non-public correction), not relabelled to a new evidence type.
2. **D4 (CI regeneration).** Yes, fully automatic. `read.yml` now runs `sota.py --sota`/`--synthesis`/
   `--digest` right after reconciling, before committing, so a claim the reader adds reaches the site
   the same day rather than waiting on a manual `run_pipeline.py`. The publication gate is unchanged
   and still runs at deploy time regardless of what got committed here.
3. **D3 (arXiv independence).** Wait for author records (A3); no fallback rule adopted. Recorded as
   decided, not left open — a real answer, even though the answer is "not yet."
4. **Reader v4 (N3/N10/N12).** Build the prompt/verifier changes and write the expectations doc now;
   hold the live run for a separate go-ahead, initially. `docs/reader-v4-preregistration.md` was
   written before any `reader-v4` call, following the same discipline as
   `docs/typesafe-preregistration.md`: a falsifiable expectation per fix, scored against a measured
   `reader-v3` baseline (not a remembered one — `read_report.py` was run fresh), with a suggested
   small first live call (`--max-papers 2 --budget-usd 0.25`).

**Follow-up (after the four commits were made, before pushing):**
5. **D5 (reading throughput).** Raise the per-run cap, not a second daily run — every run so far hit
   the 25-paper cap in well under its time budget, so time wasn't the constraint. `read_paper.py`'s
   ceilings raised 25/900s to 40/1440s; `read.yml`'s default and workflow timeout raised to match.
6. **D6 (publisher lane).** Retry Europe PMC and other legitimate full-text APIs before accepting
   human reading as final. Retried live: Europe PMC now answers but has zero coverage of this
   corpus's domain (materials/photonics, not biomedical); a direct landing-page fetch and Crossref's
   link metadata both confirm no full text is reachable without JS rendering. No route found; the
   `harvest` skill stays the primary lane. Recorded as decided (with a negative result), not left
   open.

**The push decision.** With everything committed locally, pushing to `main` meant two things at
once: the urgent Node 24 bump (GitHub removes Node 20 from Actions runners 2026-09-23, one day
out) ships immediately, but so does `reader-v4`'s `PROMPT_VERSION` inside `read.yml`, meaning the
next scheduled 06:45 UTC read would run it live automatically — the exact live run item 4 above
said to hold. Asked directly (push-and-pause-the-schedule vs. push-and-let-it-run vs. don't-push-
yet): the user chose **push now, let reader-v4 run on the next schedule**, treating the push
decision itself as the go-ahead rather than pausing to test it by hand first.

**Result:** four commits on `main` (`5f7f283`, `093ea0f`, `0ee8da7`, `9d7d42b`), pushed. Everything
built this session — the ledger retraction, `AGENTS.md` Current state, `TODO.md`, six workflow
files, `sota.py`, `build_site.py`, `harvest.py`, `read_paper.py`, and this file — is on `main`.

## Where to look for more

- **`AGENTS.md`** — doctrine (permanent rules) and "Current state" (counts, costs, what was learned,
  kept current as of the last stage that landed).
- **`TODO.md`** — every open item (`D#` decisions, `U#` user actions, `N#` next-up engineering, `A#`
  assurance, `H#` hygiene), with IDs that are never reused.
- **`docs/typesafe-plan.md`**, **`docs/typesafe-preregistration.md`**, **`docs/typesafe.md`** — the
  TypeSafe integration: design, phases, and the first live run's scorecard.
- **Claude's persistent memory** (outside this repo, not visible to other tools): standing preferences
  the user has given — ask decisions via a question tool rather than prose, do not re-litigate an
  answered decision, plan and pre-register before building a large integration. Any agent without
  access to that memory should infer the same preferences from this file's pattern.
