# TypeSafe quality engine

Status: adapter implemented; authenticated service validation and semiconductor-domain calibration pending.
The official typesafe-ai skill is installed in the operator's Codex skills directory.

## Access required

Create a **TypeSafe System One API key** at https://console.typesafe.ai/keys.
Endpoint: POST https://api.typesafe.ai/v1/systemone
Authorization: Bearer <key>
Pinned model: jev-1.13.0 (verified in official docs on 2026-09-20).
No OpenAI, Anthropic, or Firecrawl key is required by this adapter.

For GitHub Actions, create repository secret TYPESAFE_API_KEY at:
https://github.com/CodeArtFlow/project-electron/settings/secrets/actions
Choose New repository secret. Paste the key there, not in chat, a source file, or a packet.
The adapter reads TYPESAFE_API_KEY from the process environment locally.
Installing the skill does not supply service credentials.

## Run

Install existing dependencies: python -m pip install -r pipeline/requirements.txt

Preview (no API call):
python pipeline/assess_quality.py --packet reference/typesafe-packet.example.json

Evaluate a curated packet once the key is available:
python pipeline/assess_quality.py --packet PATH_TO_PACKET.json --live

There is no recurring paid workflow yet. --live explicitly sends the packet's excerpts to
TypeSafe. Requests are capped at 40 KB locally, use 5s connect / 20s read timeouts,
and allow at most three attempts with backoff for HTTP 429/529. Socket timeouts are not
a hard whole-process deadline.

## Evidence packets

Each target is a disambiguated source or research group, not an institution-wide reputation.
Use the example JSON; populate evidence with objects containing:
id, dimension, record_path, field, excerpt, source_url, locator.
record_path must point to corpus/papers or corpus/authors.
excerpt must be verbatim within the named field, and the locator must identify the
underlying page/section or public professional record. The adapter checks local provenance;
a reviewer must verify the underlying source and whether it belongs to the target.
Do not invent academic lineage or affiliations. A missing author record stays unknown.

Dimensions: method_transparency, claim_support, independent_replication,
group_track_record, academic_lineage, integrity_record.
Each is evaluated separately with an explicit unknown answer. No evidence means no
question for that dimension, rather than a zero quality score. Lineage measures documentation,
not prestige. Integrity concerns require source verification and review before any adverse label.

## Audit and policy

Results go to assessments/typesafe as review proposals. They retain the full request,
exact evidence, rubric version, resolved model, probabilities, confidence, usage, latency
and request hash. Assessment files are not rendered to the public site automatically.
Review them before committing: they contain the excerpts sent to the service.

The adapter never alters claims, evidence grades, source records, published material,
or group credibility tiers. It cannot resolve a contradiction or satisfy independent
confirmation just by returning high confidence. Missing evidence and model disagreement
must be reviewed under AGENTS.md. Every live result initially needs review because there
is no labelled semiconductor calibration set yet.

The existing corpus has no author records at setup time. Build documented author/group
records before requesting track-record assessment. Neither a model's prior knowledge nor
an institution's prestige is evidence.

## Verified provider references

- API: https://docs.typesafe.ai/api
- Model/version: https://docs.typesafe.ai/models
- Credentials: https://docs.typesafe.ai/introduction/quickstart
- Confidence meaning: https://docs.typesafe.ai/confidence
- Separate dimensions: https://docs.typesafe.ai/patterns/composite-scoring
- Official skill: https://github.com/typesafe-ai/skills/tree/main/skills/typesafe-ai
