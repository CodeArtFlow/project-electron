"""SI conversion engine. Enforces the calculate-in-SI rule from AGENTS.md.

Every quantity that enters a claim passes through here, producing the three representations:

    as_published  -> what the source wrote, transcribed verbatim
    si_base       -> coherent SI, AUTHORITATIVE, the only thing compared
    display       -> field convention, rendered last

Built on `pint` rather than a hand-rolled factor table. Hand-rolled factors are exactly where
silent order-of-magnitude errors enter, and pint additionally gives dimensional analysis for
free: converting a length to a time raises instead of returning a plausible number. It also
distinguishes degC (offset) from delta_degC (no offset), which a factor table cannot express.

`reference/definitions.yaml` remains the authority for WHICH unit is canonical for each quantity.
pint is the mechanism, not the policy.

Self-test:  python pipeline/units.py
"""

import re
import unicodedata
from pathlib import Path

import pint
import yaml

ROOT = Path(__file__).resolve().parent.parent
DEFINITIONS = ROOT / "reference" / "definitions.yaml"

# Domain units the SI system has no opinion about. All are dimensionless counts: a transistor,
# an operation, a wafer and a defect are things you count, so MTr/mm^2 really is 1/m^2 and
# TOPS/W really is 1/J. Declaring them explicitly lets pint check the dimensions we claim in
# definitions.yaml instead of taking our word for them.
CUSTOM_UNITS = [
    "transistor = [] = Tr",
    "operation = [] = op",
    "wafer = []",
    "defect = []",
    "decade = [] = dec",
    "square = [] = sq",
]

# definitions.yaml is written the way the field writes units; pint has its own spellings.
# Longest-first so 'mTorr' is rewritten before 'Torr' would match inside it.
SPELLINGS = [
    ("mTorr", "mtorr"),
    ("Torr", "torr"),
    ("defects", "defect"),
    ("MTr", "megatransistor"),
    ("Tr", "transistor"),
    ("TOPS", "teraoperation/second"),
    ("GOPS", "gigaoperation/second"),
    ("POPS", "petaoperation/second"),
    ("wph", "wafer/hour"),
]


# How authors and PDF extraction write a unit that pint parses once it is rewritten. Kept ASCII with
# escapes so the file stays ASCII. These are SPELLINGS, never guesses about meaning, and the rewrite
# is used for conversion only: as_published keeps the unit exactly as the paper wrote it.
#   RING_A         U+02DA + "A", the paper's angstrom. NFKC would split it into a space and a combining ring.
#   ATTACHED_EXP   an exponent written straight after a unit symbol, its superscript lost: mm2, cm-2,
#                  "ohm sq-1", "mV dec-1". Rewritten only when the letters before it are a unit on their own.
RING_A = "\u02daA"
ANGSTROM = "\u00c5"
ATTACHED_EXP = re.compile(r"(?<![\w*^.])([^\W\d_]+)(-?\d)(?![\d.])")


# Dimensionless quantities still have UNITS. A ratio can be written as a fraction, a percentage or
# a multiplier ("3.8x"), and 2 percent is 0.02, not 2. An earlier version returned the number
# unchanged whatever unit it was given, so record(2, "percent", ...) stored 2.0 and
# record(5, "joule", ...) was accepted as a dimensionless 5. Unknown units now raise.
DIMENSIONLESS_UNITS = {"dimensionless": 1.0, "fraction": 1.0, "x": 1.0, "percent": 0.01, "%": 0.01}

# How a published number relates to the quantity it reports. "up to 5.3x" is an upper bound, not a
# measurement of 5.3x; storing it as exact made two upper bounds look like a contradiction.
BOUNDS = ("exact", "upper_bound", "lower_bound")


class UnitError(ValueError):
    """Raised when a conversion cannot be performed correctly. Never returns a guess."""


class UnitEngine:
    def __init__(self, definitions_path=DEFINITIONS):
        self.defs = yaml.safe_load(Path(definitions_path).read_text(encoding="utf-8"))
        self.ureg = pint.UnitRegistry()
        for d in CUSTOM_UNITS:
            self.ureg.define(d)
        self.Q = self.ureg.Quantity
        self.units = self.defs["units"]

    # ------------------------------------------------------------------ helpers
    @staticmethod
    def _pint_str(u):
        """Translate a definitions.yaml unit spelling into something pint parses."""
        if u in (None, "dimensionless"):
            return "dimensionless"
        s = u.replace("^", "**")
        for src, dst in SPELLINGS:
            s = s.replace(src, dst)
        return s

    def published_unit(self, unit):
        """A unit as a paper wrote it -> a spelling pint can parse. Conversion only; never stored.

        Refuses nothing itself: whatever it cannot rewrite it returns unchanged, and to_si then fails
        exactly as before. It never chooses a unit for the caller, so "TFLOPGEMM/s" and "dB" stay refused.
        """
        s = unicodedata.normalize("NFKC", str(unit).replace(RING_A, ANGSTROM))

        def attach(m):
            symbol, exponent = m.group(1), m.group(2)
            try:
                self.ureg.parse_units(self._pint_str(symbol))
            except Exception:  # noqa: BLE001 - not a unit on its own: leave the text alone
                return m.group(0)
            return f"{symbol}**{exponent}"

        return ATTACHED_EXP.sub(attach, s)

    def quantity_spec(self, quantity):
        if quantity not in self.units:
            raise UnitError(
                f"unknown quantity {quantity!r}. Add it to reference/definitions.yaml rather "
                f"than converting ad hoc - the definitions file is the authority."
            )
        return self.units[quantity]

    # ------------------------------------------------------------------ conversion
    def to_si(self, value, unit, quantity):
        """as_published -> si_base. Raises on dimensional mismatch; never guesses."""
        spec = self.quantity_spec(quantity)
        si_unit = spec["si_base"]
        if si_unit == "dimensionless":
            if unit not in DIMENSIONLESS_UNITS:
                raise UnitError(
                    f"{quantity} is dimensionless; unit {unit!r} is not one of "
                    f"{sorted(DIMENSIONLESS_UNITS)}. Recording it as a bare number would hide "
                    f"a unit error.")
            return float(value) * DIMENSIONLESS_UNITS[unit], "dimensionless"
        try:
            q = self.Q(float(value), self._pint_str(self.published_unit(unit)))
            return float(q.to(self._pint_str(si_unit)).magnitude), si_unit
        except pint.DimensionalityError as e:
            raise UnitError(
                f"{quantity}: cannot convert {value} {unit} to {si_unit} - {e}. "
                f"A dimensional mismatch means the value was recorded against the wrong "
                f"quantity, not that the conversion needs forcing."
            ) from e
        except Exception as e:  # noqa: BLE001
            raise UnitError(f"{quantity}: could not parse {value} {unit!r}: {e}") from e

    def to_display(self, si_value, quantity):
        """si_base -> display. Rendering only; never feed the result back into a comparison."""
        spec = self.quantity_spec(quantity)
        disp = spec.get("display", spec["si_base"])
        if spec["si_base"] == "dimensionless":
            return (float(si_value) * float(spec.get("display_factor", 1.0)),
                    spec.get("display", "dimensionless"))
        offset = spec.get("display_offset")
        if offset is not None:
            # Temperature: pint owns the offset so we never hand-apply -273.15.
            q = self.Q(float(si_value), self._pint_str(spec["si_base"]))
            return float(q.to(self._pint_str(disp)).magnitude), disp
        q = self.Q(float(si_value), self._pint_str(spec["si_base"]))
        return float(q.to(self._pint_str(disp)).magnitude), disp

    def record(self, value, unit, quantity, conditions=None, bound="exact", approximate=False):
        """Produce the full three-representation block for a claim.

        `bound` and `approximate` describe the PUBLISHED statement ("up to roughly 5x" is an
        approximate upper bound) and carry through unchanged: they qualify as_published and
        si_base alike. reconcile compares bounds by inequality, never as if they were points.
        """
        if bound not in BOUNDS:
            raise UnitError(f"bound must be one of {BOUNDS}, got {bound!r}")
        si_value, si_unit = self.to_si(value, unit, quantity)
        disp_value, disp_unit = self.to_display(si_value, quantity)
        out = {
            "quantity": quantity,
            "bound": bound,
            "approximate": bool(approximate),
            "as_published": {"value": value, "unit": unit},
            "si_base": {"value": si_value, "unit": si_unit},
            "display": {"value": disp_value, "unit": disp_unit},
        }
        if conditions:
            out["conditions"] = conditions
        return out

    def compare(self, a, b):
        """Compare two records. Refuses anything but si_base, by construction."""
        if a["si_base"]["unit"] != b["si_base"]["unit"]:
            raise UnitError(
                f"refusing to compare {a['si_base']['unit']} with {b['si_base']['unit']} - "
                f"different dimensions are not comparable quantities"
            )
        return a["si_base"]["value"] - b["si_base"]["value"]


# ---------------------------------------------------------------------- self-test
def self_test():
    """Validate definitions.yaml against pint, then check the known traps.

    This tests the DEFINITIONS, not just the code: if a quantity's declared si_base does not
    match the dimensionality of its declared display unit, that is an error in
    reference/definitions.yaml and it surfaces here.
    """
    eng = UnitEngine()
    failures = []

    for name, spec in eng.units.items():
        si, disp = spec.get("si_base"), spec.get("display")
        if si == "dimensionless" or disp is None:
            continue
        try:
            d_si = eng.ureg.Quantity(1, eng._pint_str(si)).dimensionality
            d_dp = eng.ureg.Quantity(1, eng._pint_str(disp)).dimensionality
            if d_si != d_dp and spec.get("display_offset") is None:
                failures.append(f"{name}: si_base {si} ({d_si}) != display {disp} ({d_dp})")
        except Exception as e:  # noqa: BLE001
            failures.append(f"{name}: unparseable ({si} / {disp}): {e}")

    # The traps documented in definitions.yaml, asserted rather than trusted.
    checks = [
        # (value, unit, quantity, expected si, tolerance)
        (1000, "cm**2/(V*s)", "mobility", 0.1, 1e-12),
        (20, "mtorr", "pressure", 2.6664473684, 1e-6),
        (400, "degC", "temperature", 673.15, 1e-9),
        (800, "uA/um", "current_drive", 800.0, 1e-9),
        (5, "nm", "length_device", 5e-9, 1e-20),
        (60, "mV/dec", "subthreshold_swing", 0.06, 1e-12),
        (300, "mm", "wafer_diameter", 0.3, 1e-12),
    ]
    for value, unit, quantity, expected, tol in checks:
        try:
            got, _ = eng.to_si(value, unit, quantity)
            if abs(got - expected) > tol:
                failures.append(f"{quantity}: {value} {unit} -> {got}, expected {expected}")
        except UnitError as e:
            failures.append(f"{quantity}: {e}")

    # Dimensional guard must fire.
    try:
        eng.to_si(5, "nm", "time")
        failures.append("dimensional guard did NOT fire for nm -> time")
    except UnitError:
        pass

    # Spellings a PDF or an author produces (TODO N2). All of these were refused on live papers.
    spellings = [
        (4, "\u02daA", "length_device", 4e-10),                  # ring-above + A: the angstrom
        (1.5, "mm2", "area_die", 1.5e-6),
        (25, "\u00b5m2", "area_die", 25e-12),                    # micro sign
        (25, "\u03bcm2", "area_die", 25e-12),                    # Greek mu
        (3, "cm\u00b2", "area_die", 3e-4),                       # a real superscript
        (20, "\u03a9 sq-1", "sheet_resistance", 20.0),           # ohm per square
        (20, "\u03a9/sq", "sheet_resistance", 20.0),             # already fine: must stay fine
        (60, "mV dec-1", "subthreshold_swing", 0.06),
        (1000, "cm2/(V*s)", "mobility", 0.1),
    ]
    for value, unit, quantity, expected in spellings:
        try:
            got, _ = eng.to_si(value, unit, quantity)
            if abs(got - expected) > abs(expected) * 1e-9:
                failures.append(f"{quantity}: {value} {unit!r} -> {got}, expected {expected}")
        except UnitError as e:
            failures.append(f"{quantity}: {unit!r} was refused: {e}")
    if eng.record(20, "\u03a9 sq-1", "sheet_resistance")["as_published"]["unit"] != "\u03a9 sq-1":
        failures.append("as_published must keep the unit exactly as the paper wrote it")

    # Rewriting a spelling must never launder a wrong unit: each of these was, or could be, an error.
    still_refused = [
        (3.6, "TFLOPGEMM/s", "efficiency_compute"),   # a unit the model invented
        (3, "dB", "power"),                            # dB is not a power without a reference
        (3, "T", "voltage"),                           # tesla is not volt
        (20, "%", "area_die"),                         # a percentage is not an area
        (1.5, "mm2", "length_device"),                 # an area recorded against a length
        (5, "INT8", "length_device"),                  # not a unit at all
        (5, "m2", "time"),
    ]
    for value, unit, quantity in still_refused:
        try:
            eng.to_si(value, unit, quantity)
            failures.append(f"{quantity}: {unit!r} was ACCEPTED and must be refused")
        except UnitError:
            pass
    if eng.published_unit("INT8") != "INT8" or eng.published_unit("x86-64") != "x86-64":
        failures.append("published_unit rewrote something that is not a unit")

    # Round trip through display must return the original si value.
    for quantity in ("mobility", "pressure", "temperature", "length_device", "energy",
                     "relative_deviation"):
        si_in = 1.234
        d, _ = eng.to_display(si_in, quantity)
        spec = eng.units[quantity]
        back, _ = eng.to_si(d, spec["display"], quantity)
        if abs(back - si_in) > abs(si_in) * 1e-9:
            failures.append(f"{quantity}: round trip {si_in} -> {d} -> {back}")

    # Dimensionless units: percent converts, and a unit that is not a unit of a ratio is refused.
    try:
        got, _ = eng.to_si(2, "percent", "relative_deviation")
        if abs(got - 0.02) > 1e-12:
            failures.append(f"2 percent -> {got}, expected 0.02")
    except UnitError as e:
        failures.append(f"relative_deviation percent: {e}")
    for bad_unit in ("joule", "nonsense", "nm"):
        try:
            eng.to_si(5, bad_unit, "energy_advantage_ratio")
            failures.append(f"dimensionless quantity silently accepted unit {bad_unit!r}")
        except UnitError:
            pass
    rec = eng.record(5.3, "x", "energy_advantage_ratio", bound="upper_bound", approximate=True)
    if (rec["bound"], rec["approximate"], rec["si_base"]["value"]) != ("upper_bound", True, 5.3):
        failures.append(f"bound/approximate not carried through record(): {rec}")
    try:
        eng.record(1, "x", "energy_advantage_ratio", bound="roughly")
        failures.append("an invalid bound was accepted")
    except UnitError:
        pass

    print(f"quantities checked: {len(eng.units)}")
    if failures:
        print(f"\nFAILED - {len(failures)}:")
        for f in failures:
            print("  " + f)
        return 1
    print("OK - definitions.yaml is dimensionally consistent and traps behave")
    return 0


if __name__ == "__main__":
    raise SystemExit(self_test())
