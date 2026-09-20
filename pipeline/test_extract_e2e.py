"""End-to-end check of the extract-claims path: source record -> conversion -> refusals -> claim.

Fixtures are inline and synthetic. They deliberately do NOT live in corpus/papers/, which holds
records of real sources only - a fabricated record there would be indistinguishable from a real
one to every downstream step, which is the exact failure this project is built to prevent.

Usage:  python pipeline/test_extract_e2e.py
"""

import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from claims import Refusal, check_refusals, next_claim_id, validate_claim  # noqa: E402
from units import UnitEngine  # noqa: E402

# A synthetic source record shaped like corpus/papers/SRC-nnnnn.yaml
SOURCE = {
    "id": "SRC-00000",
    "title": "[FIXTURE] Synthetic device paper",
    "venue_id": "nat_comms",
    "access": "full_text_figures",
    "oa_evidence": "registry oa_status: full, DOAJ-confirmed 2026-09-20",
    "published_date": "2026-03-11",
    "evidence_type": "measured",
    "grade": "A",
}


def build_claim(eng, topic, statement, value, unit, quantity, conditions, grade="A"):
    return {
        "id": next_claim_id(topic),
        "topic": topic,
        "statement": statement,
        "quantity": eng.record(value, unit, quantity, conditions=conditions),
        "conditions": conditions,
        "sources": [SOURCE["id"]],
        "grade": grade,
        "credibility": "unknown",
        "evidence_type": SOURCE["evidence_type"],
        "status": "active",
        "as_of": SOURCE["published_date"],
        "created": date.today().isoformat(),
    }


def main():
    eng = UnitEngine()
    failures = []

    # --- 1. a well-formed quantitative claim survives the whole path ---
    c = build_claim(
        eng, "DEV",
        "Electron mobility of 1000 cm2/(V*s) measured at 300 K in the fabricated channel.",
        1000, "cm**2/(V*s)", "mobility",
        {"temperature": 300, "carrier_type": "electron"})
    try:
        check_refusals(c, SOURCE)
    except Refusal as r:
        failures.append(f"well-formed claim refused: {r}")
    problems = validate_claim(c)
    if problems:
        failures.append(f"well-formed claim failed validation: {problems}")

    si = c["quantity"]["si_base"]
    if abs(si["value"] - 0.1) > 1e-12 or si["unit"] != "m^2/(V*s)":
        failures.append(f"mobility si_base wrong: {si}")
    disp = c["quantity"]["display"]
    if abs(disp["value"] - 1000) > 1e-9:
        failures.append(f"mobility display round trip wrong: {disp}")
    if c["quantity"]["as_published"] != {"value": 1000, "unit": "cm**2/(V*s)"}:
        failures.append("as_published was not preserved verbatim")

    # --- 2. as_of must be the measurement date, not today ---
    if c["as_of"] == date.today().isoformat():
        failures.append("as_of drifted to today instead of the publication date")

    # --- 3. comparison is refused across dimensions ---
    other = build_claim(eng, "DEV", "Gate length of 12 nm.", 12, "nm", "length_device", {})
    try:
        eng.compare(c["quantity"], other["quantity"])
        failures.append("compare() allowed mobility vs length")
    except Exception:
        pass

    # --- 4. same-dimension comparison works, in si_base ---
    a = eng.record(1000, "cm**2/(V*s)", "mobility")
    b = eng.record(0.05, "m**2/(V*s)", "mobility")
    if abs(eng.compare(a, b) - 0.05) > 1e-12:
        failures.append(f"si comparison wrong: {eng.compare(a, b)}")

    # --- 5. a number whose conditions are missing does not become a claim ---
    bad = build_claim(
        eng, "DEV", "Drive current of 1.2 mA/um.", 1.2, "mA/um", "current_drive",
        {"vdd": 0.75})  # ioff and temperature absent
    try:
        check_refusals(bad, SOURCE)
        failures.append("claim with missing required conditions was not refused")
    except Refusal as r:
        if r.rule_id != "missing_required_conditions":
            failures.append(f"wrong refusal for missing conditions: {r.rule_id}")

    # --- 6. supersession needs two independent sources ---
    sup = dict(c, supersedes=["CLM-DEV-9999"])
    if "supersedes set with fewer than 2 sources - one source can only challenge" not in \
            validate_claim(sup):
        failures.append("single-source supersession was not rejected")

    print("end-to-end: source record -> units -> refusals -> validation")
    print(f"  claim id allocated : {c['id']}")
    print(f"  as_published       : {c['quantity']['as_published']['value']} "
          f"{c['quantity']['as_published']['unit']}")
    print(f"  si_base            : {si['value']} {si['unit']}")
    print(f"  display            : {disp['value']} {disp['unit']}")
    print(f"  as_of              : {c['as_of']}  (today is {date.today().isoformat()})")

    if failures:
        print(f"\nFAILED - {len(failures)}:")
        for f in failures:
            print("  " + f)
        return 1
    print("\nOK - all 6 end-to-end checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
