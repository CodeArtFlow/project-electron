"""Claim ledger: ID allocation, schema validation, and the extraction refusals.

Enforces reference/schemas.yaml mechanically so the rules are not left to judgement at 2am.
Doctrine lives in AGENTS.md; this file is the enforcement surface for it.

The refusals matter more than the validation. A malformed claim is annoying; a well-formed claim
that should never have been extracted is a falsehood with provenance attached, which is worse
than no claim at all.

Usage:
    python pipeline/claims.py --validate          # validate the whole ledger
    python pipeline/claims.py --next-id DEV       # allocate the next claim id
    python pipeline/claims.py --self-test
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

import yaml

from units import BOUNDS   # one vocabulary for bounds, defined where quantities are built

ROOT = Path(__file__).resolve().parent.parent
SCHEMAS = ROOT / "reference" / "schemas.yaml"
REGISTRY = ROOT / "sources" / "registry.yaml"
CLAIMS_DIR = ROOT / "ledger" / "claims"
CORPUS_DIR = ROOT / "corpus" / "papers"

TOPICS = ("MAT", "DEV", "LITHO", "PROC", "PKG", "MEM", "ARCH", "PHOT", "EDA", "ECON")
CLAIM_ID_RE = re.compile(r"^CLM-(" + "|".join(TOPICS) + r")-(\d{4})$")
SRC_ID_RE = re.compile(r"^SRC-(\d{5})$")

# Statements that assert rather than attribute. Grade D/E material may only attribute.
ASSERTIVE_HEDGE_RE = re.compile(
    r"\b(states?|claims?|announced|reported(?: by)?|according to|says?)\b", re.I)

# Crude compound-statement detector. Deliberately noisy: it raises a question for a human rather
# than deciding. Under-splitting a claim is a real defect, so a false positive is cheap.
COMPOUND_RE = re.compile(r"\b(\d[\d.]*\s*\w+.*\band\b.*\d[\d.]*\s*\w+)", re.I)

# Words that make a published number a BOUND or an APPROXIMATION rather than a measurement.
# "up to 5.3x" is not 5.3x. These are unambiguous multi-word forms on purpose: bare "over",
# "above" and "below" also appear in ordinary comparisons ("advantage over static CMOS") and would
# refuse correct claims. A false positive here costs an extractor one explicit `bound` argument;
# a false negative stores a bound as a measurement, which is how two upper bounds once looked like
# a contradiction.
UPPER_RE = re.compile(r"\b(up to|at most|no more than|not exceeding|less than|within)\b", re.I)
LOWER_RE = re.compile(r"\b(at least|no less than|more than|greater than)\b", re.I)
APPROX_RE = re.compile(r"(\b(roughly|approximately|approx\.?|about|around|nearly)\b|[~\u2248])", re.I)

NODE_NAME_RE = re.compile(r"\b(\d+\s?nm|\d+A)\b.*\b(node|process|technology)\b", re.I)


class Refusal(Exception):
    """An extraction that must not happen. Carries the schema rule id."""

    def __init__(self, rule_id, message):
        super().__init__(f"[{rule_id}] {message}")
        self.rule_id = rule_id


def load(path):
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


# --------------------------------------------------------------------------- ids
def next_claim_id(topic, claims_dir=CLAIMS_DIR, reserved=()):
    """Allocate the next id for a topic. Never reuses, even after a retraction.

    `reserved` holds ids already handed out in this session but not yet written to disk.
    Without it, extracting several claims in one batch allocated the SAME id to all of them,
    because the allocator only saw the ledger on disk. Callers extracting more than one claim
    must pass the ids they are holding.
    """
    if topic not in TOPICS:
        raise ValueError(f"unknown topic {topic!r}; valid: {', '.join(TOPICS)}")
    path = Path(claims_dir) / f"{topic}.yaml"
    highest = 0
    known = []
    if path.exists():
        doc = load(path) or {}
        known = [c.get("id", "") for c in doc.get("claims", []) or []]
    for cid in list(known) + list(reserved):
        m = CLAIM_ID_RE.match(cid or "")
        if m and m.group(1) == topic:
            highest = max(highest, int(m.group(2)))
    return f"CLM-{topic}-{highest + 1:04d}"


def next_source_id(corpus_dir=CORPUS_DIR):
    highest = 0
    for p in Path(corpus_dir).glob("SRC-*.yaml"):
        m = SRC_ID_RE.match(p.stem)
        if m:
            highest = max(highest, int(m.group(1)))
    return f"SRC-{highest + 1:05d}"


# --------------------------------------------------------------------------- refusals
def check_refusals(claim, source, registry=None, schemas=None):
    """Apply reference/schemas.yaml refuse_extraction_when. Raises Refusal on the first hit.

    Called BEFORE a claim is written, never after.
    """
    schemas = schemas or load(SCHEMAS)
    registry = registry if registry is not None else load(REGISTRY)
    stmt = claim.get("statement", "") or ""
    quantitative = bool(claim.get("quantity"))

    # --- venue must be harvestable ---
    venue_id = source.get("venue_id")
    entry = None
    for section, rows in registry.items():
        if not isinstance(rows, list):
            continue
        for e in rows:
            if isinstance(e, dict) and e.get("id") == venue_id:
                entry = e
                break
    if entry is None:
        raise Refusal("unverified_venue", f"venue_id {venue_id!r} is not in sources/registry.yaml")
    if entry.get("verified") is False:
        raise Refusal("unverified_venue",
                      f"venue {venue_id!r} is verified:false - {entry.get('blocker', 'no blocker recorded')}")
    if entry.get("verified") == "review" and not source.get("oa_evidence"):
        raise Refusal("unverified_venue",
                      f"venue {venue_id!r} is `review`; a per-article OA check must be recorded "
                      f"in oa_evidence before its content may be cited")

    # --- access bounds what may be claimed ---
    if quantitative and source.get("access") in ("abstract_only", "metadata_only"):
        raise Refusal("abstract_only_quantitative",
                      f"access is {source.get('access')}; a number without its method is not a result")

    # --- node names are not dimensions ---
    if NODE_NAME_RE.search(stmt) and claim.get("quantity", {}).get("quantity") == "length_device":
        raise Refusal("node_name_as_dimension",
                      "a process node label is being treated as a physical length")
    if re.search(r"\b(TSMC|Samsung|Intel|GlobalFoundries|SMIC)\b", stmt, re.I) and \
            re.search(r"\b\d+\s?nm\b", stmt) and re.search(r"\b(vs\.?|versus|compared)\b", stmt, re.I):
        raise Refusal("cross_foundry_node",
                      "cross-foundry node-name comparison is invalid by construction")

    # --- low-grade material is attributed, never asserted ---
    if claim.get("grade") in ("D", "E") and not ASSERTIVE_HEDGE_RE.search(stmt):
        raise Refusal("grade_de_as_fact",
                      f"grade {claim.get('grade')} claim asserts rather than attributes; "
                      f"rewrite as '<source> states that ...'")

    # --- conditions that make a number interpretable ---
    q = claim.get("quantity") or {}
    qname = q.get("quantity")
    required = (schemas.get("conditions_required") or {}).get(qname)
    if required:
        have = set((claim.get("conditions") or q.get("conditions") or {}).keys())
        missing = [c for c in required if c not in have]
        if missing:
            raise Refusal("missing_required_conditions",
                          f"{qname} requires {', '.join(required)}; missing {', '.join(missing)}")

    # --- a bound must not become an equality ---
    if q:
        bound = q.get("bound", "exact")
        approx = bool(q.get("approximate"))
        says_upper, says_lower = bool(UPPER_RE.search(stmt)), bool(LOWER_RE.search(stmt))
        problem = None
        if bound == "exact" and (says_upper or says_lower):
            problem = "the statement is a bound but quantity.bound is 'exact'"
        elif bound == "upper_bound" and says_lower and not says_upper:
            problem = "the statement says a lower bound but quantity.bound is 'upper_bound'"
        elif bound == "lower_bound" and says_upper and not says_lower:
            problem = "the statement says an upper bound but quantity.bound is 'lower_bound'"
        elif not approx and APPROX_RE.search(stmt):
            problem = "the statement says the value is approximate but quantity.approximate is false"
        if problem:
            raise Refusal("qualifier_dropped", problem + ". Record the qualifier the source used "
                          "- UnitEngine.record(..., bound=..., approximate=...).")

    # --- atomicity ---
    if COMPOUND_RE.search(stmt):
        raise Refusal("compound_statement",
                      "statement appears to join two falsifiable assertions - split it")

    return True


# --------------------------------------------------------------------------- validation
def validate_claim(claim, schemas=None):
    schemas = schemas or load(SCHEMAS)
    spec = schemas["claim"]
    problems = []

    cid = claim.get("id", "")
    if not CLAIM_ID_RE.match(cid):
        problems.append(f"id {cid!r} does not match CLM-<TOPIC>-nnnn")
    elif claim.get("topic") and CLAIM_ID_RE.match(cid).group(1) != claim["topic"]:
        problems.append(f"id topic {CLAIM_ID_RE.match(cid).group(1)} != topic {claim['topic']}")

    for field, fspec in spec.items():
        if field == "id":
            continue
        if fspec.get("required") and claim.get(field) in (None, "", [], {}):
            problems.append(f"missing required field {field!r}")
        enum = fspec.get("enum")
        if enum and claim.get(field) is not None and claim[field] not in enum:
            problems.append(f"{field}={claim[field]!r} not in {enum}")

    for s in claim.get("sources", []) or []:
        if not SRC_ID_RE.match(s):
            problems.append(f"source {s!r} does not match SRC-nnnnn")

    q = claim.get("quantity")
    if q:
        for part in ("as_published", "si_base", "display"):
            if part not in q:
                problems.append(f"quantity missing {part!r} - build it with pipeline/units.py")
        if q.get("bound", "exact") not in BOUNDS:
            problems.append(f"quantity.bound {q.get('bound')!r} not in {BOUNDS}")
        if "approximate" in q and not isinstance(q["approximate"], bool):
            problems.append("quantity.approximate must be true or false")
        # Conditions live in two places on a claim. If both are stated they must be the same dict:
        # a claim that says two different things is an internal contradiction of our own making.
        if q.get("conditions") and claim.get("conditions") and q["conditions"] != claim["conditions"]:
            problems.append("quantity.conditions and conditions differ; a claim must state its conditions "
                            "once, consistently")

    # A correction to a claim is an audit-trail entry, not an edit to be hidden.
    for i, corr in enumerate(claim.get("corrections", []) or []):
        if not isinstance(corr, dict) or not corr.get("date") or not corr.get("reason") \
                or not isinstance(corr.get("public"), bool):
            problems.append(f"corrections[{i}] needs date, reason and public: true|false")

    # Supersession requires two independent sources (AGENTS.md Type B).
    if claim.get("supersedes") and len(claim.get("sources", []) or []) < 2:
        problems.append("supersedes set with fewer than 2 sources - one source can only challenge")

    return problems


def validate_ledger(claims_dir=CLAIMS_DIR):
    schemas = load(SCHEMAS)
    all_problems, seen, n = [], {}, 0
    for path in sorted(Path(claims_dir).glob("*.yaml")):
        doc = load(path) or {}
        for claim in doc.get("claims", []) or []:
            n += 1
            for p in validate_claim(claim, schemas):
                all_problems.append(f"{path.name}:{claim.get('id', '?')}: {p}")
            cid = claim.get("id")
            if cid in seen:
                all_problems.append(f"duplicate claim id {cid} in {path.name} and {seen[cid]}")
            seen[cid] = path.name
    return n, all_problems


# --------------------------------------------------------------------------- self-test
def self_test():
    schemas = load(SCHEMAS)
    registry = load(REGISTRY)
    failures = []

    good_source = {"venue_id": "nat_comms", "access": "full_text_figures",
                   "oa_evidence": "registry oa_status: full, DOAJ-confirmed"}

    def expect_refusal(rule_id, claim, source=None):
        try:
            check_refusals(claim, source or good_source, registry, schemas)
            failures.append(f"expected refusal {rule_id} but none raised")
        except Refusal as r:
            if r.rule_id != rule_id:
                failures.append(f"expected {rule_id}, got {r.rule_id}")

    # quantitative claim from an abstract
    expect_refusal("abstract_only_quantitative",
                   {"statement": "Drive current reaches 800 uA/um.", "grade": "A",
                    "quantity": {"quantity": "current_drive"},
                    "conditions": {"vdd": 0.7, "ioff": "100 nA/um", "temperature": 300}},
                   {**good_source, "access": "abstract_only"})

    # grade E asserted as fact
    expect_refusal("grade_de_as_fact",
                   {"statement": "The process achieves 30% higher density.", "grade": "E"})

    # missing conditions
    expect_refusal("missing_required_conditions",
                   {"statement": "Drive current is high.", "grade": "A",
                    "quantity": {"quantity": "current_drive"}, "conditions": {"vdd": 0.7}})

    # unverified venue
    expect_refusal("unverified_venue",
                   {"statement": "X states that Y happened.", "grade": "D"},
                   {**good_source, "venue_id": "techrxiv"})

    # a bound recorded as an equality is refused (the CLM-ARCH-0002/0004/0005/0006 defect)
    exact_q = {"quantity": "energy_advantage_ratio", "bound": "exact", "approximate": False}
    for stmt in ("PFAL reaches up to 5.3x energy gain over static CMOS in simulation.",
                 "Energy stays within 2 percent of the ideal case in simulation.",
                 "Gain of at least 3x over the baseline in simulation."):
        expect_refusal("qualifier_dropped", {"statement": stmt, "grade": "B", "quantity": exact_q})
    expect_refusal("qualifier_dropped",
                   {"statement": "Gain is roughly 5x over static CMOS in simulation.", "grade": "B",
                    "quantity": exact_q})
    expect_refusal("qualifier_dropped",
                   {"statement": "Gain of at least 3x over the baseline in simulation.", "grade": "B",
                    "quantity": {"quantity": "energy_advantage_ratio", "bound": "upper_bound",
                                 "approximate": False}})
    try:      # correctly bounded, and an ordinary "over" comparison, both pass
        check_refusals({"statement": "PFAL reaches up to roughly 5x energy gain over static CMOS in "
                                     "simulation.", "grade": "B",
                        "quantity": {"quantity": "energy_advantage_ratio", "bound": "upper_bound",
                                     "approximate": True}}, good_source, registry, schemas)
        check_refusals({"statement": "PFAL shows a 3.8x energy advantage over static CMOS in "
                                     "simulation.", "grade": "B", "quantity": exact_q},
                       good_source, registry, schemas)
    except Refusal as r:
        failures.append(f"correctly qualified claim wrongly refused: {r}")

    # a well-formed claim must pass
    try:
        check_refusals(
            {"statement": "Reported electron mobility of 1000 cm2/Vs at 300 K.", "grade": "A",
             "quantity": {"quantity": "mobility"},
             "conditions": {"temperature": 300, "carrier_type": "electron"}},
            good_source, registry, schemas)
    except Refusal as r:
        failures.append(f"well-formed claim wrongly refused: {r}")

    # id allocation, against a temp ledger so the test does not depend on the real one.
    # An earlier version asserted CLM-DEV-0001 against the live ledger and started failing the
    # moment a real DEV claim existed - a test that only passed on an empty corpus.
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        if next_claim_id("DEV", claims_dir=tmp) != "CLM-DEV-0001":
            failures.append("empty ledger should allocate CLM-DEV-0001")
        # ids reserved in-session must not be handed out twice
        got = [next_claim_id("DEV", claims_dir=tmp, reserved=r)
               for r in ([], ["CLM-DEV-0001"], ["CLM-DEV-0001", "CLM-DEV-0002"])]
        if got != ["CLM-DEV-0001", "CLM-DEV-0002", "CLM-DEV-0003"]:
            failures.append(f"batch allocation collided: {got}")

    # validation catches a bad claim
    bad = validate_claim({"id": "CLM-XXX-1", "statement": "x"}, schemas)
    if not bad:
        failures.append("validate_claim accepted a malformed claim")

    print(f"refusal rules in schema: {len(schemas['refuse_extraction_when'])}")
    if failures:
        print(f"\nFAILED - {len(failures)}:")
        for f in failures:
            print("  " + f)
        return 1
    print("OK - refusals fire, well-formed claims pass, ids allocate, validation catches errors")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--validate", action="store_true")
    ap.add_argument("--next-id", metavar="TOPIC")
    ap.add_argument("--next-source-id", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()

    if a.self_test:
        return self_test()
    if a.next_id:
        print(next_claim_id(a.next_id))
        return 0
    if a.next_source_id:
        print(next_source_id())
        return 0
    if a.validate:
        n, problems = validate_ledger()
        print(f"claims validated: {n}")
        if problems:
            print(f"FAILED - {len(problems)}:")
            for p in problems:
                print("  " + p)
            return 1
        print("OK - ledger valid")
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
