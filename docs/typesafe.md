# TypeSafe research engine

The System One API is connected through the repository Actions secret
TYPESAFE_API_KEY. The authenticated synthetic check passed on 2026-09-21
([run](https://github.com/CodeArtFlow/project-electron/actions/runs/35556452679)).
The model is pinned to jev-1.13.0. Semiconductor calibration is still pending.

## Integrated decisions

| Stage | Primitive | Evidence and output |
|---|---|---|
| Triage | Choice + Score | Eight candidate metadata records per daily run: relevance, stack layer, reading priority. Does not read or promote a paper. |
| Extraction audit | Choice + Noul | Every current claim against its cited local source summaries: support, conditions, evidence type, atomicity, numerical qualifiers. |
| Source assessment | Noul + Score + Choice | Method availability gates disclosure score; limitations and internal access assertions are checked. |
| Group assessment | Noul + Score + Choice | Identity, outcome history, lineage documentation, documented integrity concerns. Absent professional evidence stays unknown. |
| Reconciliation | Choice + Noul | Same-topic claim pairs: comparability, potential contradiction, shared-group evidence and proposed discrepancy class. Also checks recorded conflict explanations. |
| Discovery | Choice + Noul | Existing discovery briefs against supplied read records and claims; no network discovery or new scientific assertions. |
| Publication | Choice + Noul | Digest and SOTA fidelity, overstatement, visibility of uncertainty. Existing deterministic gate remains authoritative. |

These are typed review signals, not original-paper verification or automatic scientific
adjudication. Checking a local source summary cannot establish that its author transcribed
the original paper correctly. The discovery audit is separate from the offline discovery
loop; only explicitly live audit runs send snapshots to TypeSafe.

## Run and limits

    python pipeline/semantic_checks.py --scope all
    python pipeline/semantic_checks.py --scope all --live
    python pipeline/semantic_checks.py --scope publication --live
    python pipeline/semantic_checks.py --scope triage --live --candidate-limit 8 --max-calls 8 --seconds 60
    python pipeline/run_pipeline.py --no-sweep --typesafe live

Preview makes no API calls. A preview publication audit cannot pass the gate.
Live runs use TYPESAFE_API_KEY from the environment. Do not put the key in files or chat.

Defaults: 64 API evaluations, 180 seconds for evaluation, one pass. Hard allowed limits:
100 evaluations, 300 seconds. Each evaluation runs in a subprocess killed at the smaller
of 30 seconds and the remaining budget. Up to three HTTP attempts per evaluation, with
backoff for 429/529. Maximum default HTTP attempts: 192. Each request is capped at 40 KB;
oversized jobs remain pending rather than silently truncating evidence. Planning and
report serialization are outside the evaluation deadline. Local exact-request cache
avoids repeat calls for unchanged evidence/model/rubric. Hosted jobs start with fresh caches.

Unfinished jobs and API failures are explicit. Publication requires complete selected
coverage; triage deliberately samples only eight most-recent candidate filenames and
reports total/selected counts. It is not an exhaustive queue ranking.

## Workflows and reports

- typesafe-research.yml: manual full audit, 180s, including eight candidate records.
- harvest.yml: daily metadata triage after the existing sweep, 60s, eight requests.
- deploy.yml: live publication audit on trusted main, mandatory before deployment.
  Pull requests run offline tests without credentials. Missing credentials on main fail.
- typesafe-check.yml: manual synthetic credential/contract check.

Reports under run/typesafe-*.json and .md are derived and ignored by git. Actions artifacts
retain the requests, evidence snapshots, raw answers, model/rubric versions, fingerprints,
token usage and per-call timing. The Actions summary surfaces flags even if deployment
is blocked. The Research checks site page displays the passing publication audit.
A blocked deployment leaves the prior live site unchanged; consult its failed run artifact.

The gate regenerates the current plan, checks exact coverage and evidence fingerprints,
validates raw answers and recomputes flags. Stale, preview, missing, incomplete or invalid
production audits fail. Required claim, document, pair and conflict-review flags also fail.
Source/group quality signals remain proposals and do not automatically alter evidence grades
or credibility tiers. There is no override switch or model-triggered resolution.

Provisional review thresholds are 0.9 for affirmative evidence/Choice confidence and
0.1 for adverse Noul signals. They are deliberately not presented as calibrated scientific
confidence. Score is an ordinal expected index, not probability of truth. A premise below
0.9 suppresses its dependent score; missing evidence is not a zero score. Build a labelled
semiconductor evaluation set before interpreting these thresholds quantitatively.

## Professional provenance

There are currently no author records. Therefore the engine cannot yet produce grounded
group track-record or lineage assessments. Record public professional evidence first.

Automated group checks consume corpus/authors/*.yaml with id and an evidence list.
Each item requires excerpt, source_url, locator and read_at. Excerpts must have actually
been read and be attributable to the named person/group. Structural completeness is checked;
a reviewer verifies identity, original-source fidelity and professional provenance.

For stricter excerpt-to-record checking, the existing curated packet adapter remains:

    python pipeline/assess_quality.py --packet reference/typesafe-packet.example.json
    python pipeline/assess_quality.py --packet PATH.json --live

Packet evidence requires id, dimension, record_path, field, excerpt, source_url and locator.
The excerpt must occur in the named field of a local corpus/papers or corpus/authors record.
Results go to assessments/typesafe for review. The available dimensions are
method_transparency, claim_support, independent_replication, group_track_record,
academic_lineage and integrity_record. No evidence means no question.

Independent confirmation remains a deterministic requirement. Missing author/affiliation
metadata cannot establish independence; a model's shared-group signal cannot establish it
either. Neither reputation nor confidence replaces the project's evidence rules.

## Provider references

- [Primitives](https://docs.typesafe.ai/primitives)
- [API contract](https://docs.typesafe.ai/api)
- [Models](https://docs.typesafe.ai/models)
- [Confidence](https://docs.typesafe.ai/confidence)
- [Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring)
- [Official skill](https://github.com/typesafe-ai/skills/tree/main/skills/typesafe-ai)
