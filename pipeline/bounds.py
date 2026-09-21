"""Authority-sourced physical bounds: flag extraordinary claims for scrutiny, never refuse them.

Two jobs.

  1. VERIFY that every constant in reference/definitions.yaml `sourced_constants` still matches the
     NIST CODATA file kept in the repo. The file is the authority; the YAML is a convenience copy;
     a test fails if they ever disagree. This is AGENTS.md rule 1 applied to our own numbers: the
     first version of the definitions file carried "59.6 mV/dec at 300 K" typed from memory, and
     the exact constants give 59.53.

  2. FLAG claims that sit outside a derived bound. Today that is one bound, the thermionic limit
     on subthreshold swing. It is a SCRUTINY flag, not a refusal, for two reasons: tunnelling and
     negative-capacitance devices legitimately go below it, and an extraordinary result is exactly
     what a research digest exists to report. The flag tells the reader to look harder; it does not
     say the claim is wrong.

Bounds are derived from the constants at run time, never stored as typed numbers.

Usage:
    python pipeline/bounds.py --verify         # constants vs the NIST file
    python pipeline/bounds.py --check-ledger   # scrutiny flags across the ledger (informational)
    python pipeline/bounds.py --self-test
"""

import argparse
import math
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DEFINITIONS = ROOT / "reference" / "definitions.yaml"

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass


def load_definitions(path=DEFINITIONS):
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


_CACHE = {}


def default_definitions():
    """The repo's definitions, read once per process (scrutiny() runs once per rendered claim)."""
    if "defs" not in _CACHE:
        _CACHE["defs"] = load_definitions()
    return _CACHE["defs"]


# ---------------------------------------------------------------------------- the authority
ROW_RE = re.compile(r"^(?P<name>\S.*?)\s{2,}(?P<value>[-+0-9. eE]+?)(?:\.\.\.)?\s{2,}"
                    r"(?P<unc>\(exact\)|[0-9. eE()+-]+?)\s{2,}(?P<unit>.+?)\s*$")


def parse_codata(path):
    """NIST allascii.txt -> {name: {"value": float, "exact": bool, "unit": str}}.

    The listing writes numbers in digit groups ("1.380 649 e-23") and truncates irrational values
    with "...". Both are handled; a row that does not parse is skipped, not guessed.
    """
    out = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        try:
            # Digit groups ("1.380 649 e-23") lose their spaces. A truncated irrational carries its
            # ellipsis anywhere - "3.14...", or mid-number as in "8.617 333 262... e-5" - and the
            # first version only looked for it at the end, so those rows were dropped silently.
            value = float(re.sub(r"\s+|\.\.\.", "", m.group("value")))
        except ValueError:
            continue
        out[m.group("name").strip()] = {"value": value, "exact": m.group("unc").strip() == "(exact)",
                                        "unit": m.group("unit").strip()}
    return out


def verify_sourced_constants(defs=None, root=ROOT):
    """Compare every `sourced_constants` entry with the authority file. Returns problems."""
    defs = defs or load_definitions()
    block = defs.get("sourced_constants") or {}
    authority = parse_codata(Path(root) / block.get("source_file", ""))
    problems = []
    if not authority:
        return [f"could not parse any constants from {block.get('source_file')!r}"]
    for key, entry in (block.get("values") or {}).items():
        row = authority.get(entry["nist_name"])
        if row is None:
            problems.append(f"{key}: {entry['nist_name']!r} is not in the authority file")
            continue
        if isinstance(entry["value"], bool) or not isinstance(entry["value"], (int, float)):
            # PyYAML reads 6.02e23 (no sign on the exponent) as a STRING. Report it, don't crash.
            problems.append(f"{key}: value {entry['value']!r} is not a number "
                            f"(YAML needs a signed exponent, e.g. 6.02e+23)")
            continue
        if not math.isclose(row["value"], entry["value"], rel_tol=1e-12):
            problems.append(f"{key}: definitions say {entry['value']!r}, NIST says {row['value']!r}")
        if bool(entry.get("exact")) != row["exact"]:
            problems.append(f"{key}: exact flag is {entry.get('exact')} but NIST says {row['exact']}")
    return problems


def constant(name, defs=None):
    defs = defs or load_definitions()
    return float(defs["sourced_constants"]["values"][name]["value"])


# ---------------------------------------------------------------------------- derived bounds
def thermal_voltage(temperature_k, defs=None):
    """k_B * T / q, in volts."""
    return constant("boltzmann_constant", defs) * temperature_k / constant("elementary_charge", defs)


def thermionic_ss_limit(temperature_k, defs=None):
    """The subthreshold-swing floor of a thermionic-injection FET, in V/decade."""
    return math.log(10) * thermal_voltage(temperature_k, defs)


# ---------------------------------------------------------------------------- claim checks
TEMP_RE = re.compile(r"^\s*(?P<v>[-+]?\d+(?:\.\d+)?)\s*(?P<u>K|kelvin|degC|°C|C|degF|°F|F)\s*$", re.I)


def temperature_k(value):
    """A stated temperature -> kelvin, or None if it cannot be read WITH a unit.

    A bare number is refused, not assumed: 300 could be kelvin, and 27 could be degrees Celsius,
    and guessing which is how a 4 K result becomes a 277 K one.
    """
    if isinstance(value, (int, float)) or value is None:
        return None
    m = TEMP_RE.match(str(value))
    if not m:
        return None
    v, unit = float(m.group("v")), m.group("u").lower().replace("°", "")
    if unit in ("k", "kelvin"):
        return v
    if unit in ("degc", "c"):
        return v + 273.15
    return (v - 32.0) * 5.0 / 9.0 + 273.15


def scrutiny(claim, defs=None):
    """Scrutiny flags for one claim. Empty means no bound was crossed or none applies."""
    q = claim.get("quantity") or {}
    if q.get("quantity") != "subthreshold_swing":
        return []
    defs = defs or default_definitions()
    rule = next(r for r in defs["sanity_bounds"]["subthreshold_swing"]
                if r["id"] == "below-thermionic-limit")
    raw = (claim.get("conditions") or q.get("conditions") or {}).get("temperature")
    temp = temperature_k(raw)
    if temp is None:
        return [{"id": "temperature-unit-unstated",
                 "message": (f"the thermionic limit cannot be checked: temperature {raw!r} has no "
                             f"readable unit (write '300 K' or '27 degC', not a bare number)")}]
    limit = thermionic_ss_limit(temp, defs)
    value = (q.get("si_base") or {}).get("value")
    if value is None or q.get("bound", "exact") == "lower_bound":
        return []   # "at least X" cannot be below a floor
    if value < limit * (1 - float(rule["tolerance"])):
        return [{"id": rule["id"],
                 "message": (f"{value * 1e3:.2f} mV/dec at {temp:g} K is below the thermionic limit "
                             f"of {limit * 1e3:.2f} mV/dec (ln10*k_B*T/q). Extraordinary unless the "
                             f"device is not thermionic (tunnelling, negative capacitance). "
                             f"Flagged for scrutiny, not judged wrong.")}]
    return []


def ledger_scrutiny(claims_dir=None, defs=None):
    claims_dir = Path(claims_dir or ROOT / "ledger" / "claims")
    defs = defs or load_definitions()
    found = []
    for p in sorted(claims_dir.glob("*.yaml")):
        for c in (yaml.safe_load(p.read_text(encoding="utf-8")) or {}).get("claims", []) or []:
            for flag in scrutiny(c, defs):
                found.append((c["id"], flag))
    return found


# ---------------------------------------------------------------------------- CLI
def self_test():
    defs = load_definitions()
    failures = verify_sourced_constants(defs)
    # The derived 300 K figure must equal the number recorded in definitions.yaml.
    derived = thermionic_ss_limit(300.0, defs)
    recorded = defs["constants"]["boltzmann_limit_ss_300K_V_dec"]
    if not math.isclose(derived, recorded, rel_tol=1e-6):
        failures.append(f"boltzmann_limit_ss_300K_V_dec is {recorded} but the constants give {derived:.8f}")
    print(f"authority constants checked: {len(defs['sourced_constants']['values'])}; "
          f"thermionic limit at 300 K = {derived * 1e3:.4f} mV/dec")
    if failures:
        print(f"FAILED - {len(failures)}:")
        for f in failures:
            print("  " + f)
        return 1
    print("OK - definitions agree with the NIST authority file")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--check-ledger", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.verify or a.self_test:
        return self_test()
    if a.check_ledger:
        found = ledger_scrutiny()
        for cid, flag in found:
            print(f"  scrutiny {cid} [{flag['id']}]: {flag['message']}")
        print(f"bounds: {len(found)} claim(s) flagged for scrutiny (informational; nothing refused)")
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
