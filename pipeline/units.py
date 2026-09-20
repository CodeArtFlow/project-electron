"""SI conversion engine. Enforces the calculate-in-SI rule from CLAUDE.md.

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
            return float(value), "dimensionless"
        try:
            q = self.Q(float(value), self._pint_str(unit))
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
            return float(si_value), "dimensionless"
        offset = spec.get("display_offset")
        if offset is not None:
            # Temperature: pint owns the offset so we never hand-apply -273.15.
            q = self.Q(float(si_value), self._pint_str(spec["si_base"]))
            return float(q.to(self._pint_str(disp)).magnitude), disp
        q = self.Q(float(si_value), self._pint_str(spec["si_base"]))
        return float(q.to(self._pint_str(disp)).magnitude), disp

    def record(self, value, unit, quantity, conditions=None):
        """Produce the full three-representation block for a claim."""
        si_value, si_unit = self.to_si(value, unit, quantity)
        disp_value, disp_unit = self.to_display(si_value, quantity)
        out = {
            "quantity": quantity,
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

    # Round trip through display must return the original si value.
    for quantity in ("mobility", "pressure", "temperature", "length_device", "energy"):
        si_in = 1.234
        d, _ = eng.to_display(si_in, quantity)
        spec = eng.units[quantity]
        back, _ = eng.to_si(d, spec["display"], quantity)
        if abs(back - si_in) > abs(si_in) * 1e-9:
            failures.append(f"{quantity}: round trip {si_in} -> {d} -> {back}")

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
