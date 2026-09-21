"""Authority-sourced bounds: the definitions must match the fetched NIST file, and the scrutiny
flag must fire on an extraordinary subthreshold swing and stay quiet otherwise.

Usage:  python pipeline/test_authority_bounds.py
"""

import copy
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from bounds import (load_definitions, parse_codata, scrutiny, temperature_k,  # noqa: E402
                    thermionic_ss_limit, verify_sourced_constants)
from units import UnitEngine  # noqa: E402

DEFS = load_definitions()
ENG = UnitEngine()


def swing(mv_per_dec, temperature="300 K", bound="exact"):
    return {"id": "CLM-DEV-0001", "conditions": {"temperature": temperature, "carrier_type": "n"},
            "quantity": ENG.record(mv_per_dec, "mV/dec", "subthreshold_swing", bound=bound)}


class Authority(unittest.TestCase):
    def test_definitions_agree_with_the_nist_file(self):
        self.assertEqual(verify_sourced_constants(DEFS), [])

    def test_the_check_actually_bites(self):
        bad = copy.deepcopy(DEFS)
        bad["sourced_constants"]["values"]["boltzmann_constant"]["value"] = 1.38e-23   # a "rounded" k_B
        problems = verify_sourced_constants(bad)
        self.assertTrue(any("boltzmann_constant" in p for p in problems), problems)
        wrong_flag = copy.deepcopy(DEFS)
        wrong_flag["sourced_constants"]["values"]["elementary_charge"]["exact"] = False
        self.assertTrue(verify_sourced_constants(wrong_flag))
        missing = copy.deepcopy(DEFS)
        missing["sourced_constants"]["values"]["boltzmann_constant"]["nist_name"] = "Boltzmann"
        self.assertTrue(any("not in the authority file" in p for p in verify_sourced_constants(missing)))

    def test_a_yaml_string_exponent_is_reported_not_crashed_on(self):
        # PyYAML reads 6.02e23 (unsigned exponent) as a string. This crashed the first version.
        bad = copy.deepcopy(DEFS)
        bad["sourced_constants"]["values"]["avogadro_constant"]["value"] = "6.02214076e23"
        self.assertTrue(any("not a number" in p for p in verify_sourced_constants(bad)))

    def test_the_authority_file_parses_the_awkward_rows(self):
        rows = parse_codata(Path(__file__).resolve().parent.parent / DEFS["sourced_constants"]["source_file"])
        self.assertTrue(rows["Boltzmann constant"]["exact"])
        self.assertAlmostEqual(rows["Boltzmann constant in eV/K"]["value"], 8.617333262e-5, places=13)  # "..."
        self.assertEqual(rows["speed of light in vacuum"]["value"], 299792458.0)                          # groups
        self.assertFalse(rows["Newtonian constant of gravitation"]["exact"])

    def test_the_recorded_limit_is_the_derived_one_not_the_typed_one(self):
        derived = thermionic_ss_limit(300.0, DEFS)
        self.assertAlmostEqual(derived * 1e3, 59.5264, places=3)
        self.assertTrue(math.isclose(DEFS["constants"]["boltzmann_limit_ss_300K_V_dec"], derived,
                                     rel_tol=1e-6))
        # The value this replaced, 59.6, is the limit at about 300.4 K, not at 300 K.
        self.assertAlmostEqual(thermionic_ss_limit(300.4, DEFS) * 1e3, 59.6, places=1)
        self.assertGreater(abs(0.0596 - derived) / derived, 5e-4)
        self.assertAlmostEqual(thermionic_ss_limit(77.0, DEFS) * 1e3, 15.28, places=2)


class Scrutiny(unittest.TestCase):
    def ids(self, claim):
        return [f["id"] for f in scrutiny(claim, DEFS)]

    def test_below_the_limit_is_flagged_and_says_it_is_not_a_verdict(self):
        flags = scrutiny(swing(40.0), DEFS)
        self.assertEqual([f["id"] for f in flags], ["below-thermionic-limit"])
        self.assertIn("not judged wrong", flags[0]["message"])
        self.assertIn("tunnelling", flags[0]["message"])

    def test_ordinary_and_borderline_values_are_not_flagged(self):
        for mv in (65.0, 60.0, 59.53, 59.0):        # 59.0 is inside the 1 percent tolerance
            self.assertEqual(self.ids(swing(mv)), [], mv)

    def test_a_lower_bound_cannot_be_below_a_floor(self):
        self.assertEqual(self.ids(swing(40.0, bound="lower_bound")), [])
        self.assertEqual(self.ids(swing(40.0, bound="upper_bound")), ["below-thermionic-limit"])

    def test_the_limit_moves_with_temperature(self):
        self.assertEqual(self.ids(swing(10.0, "4 K")), [])                          # limit ~0.8 mV/dec
        self.assertEqual(self.ids(swing(30.0, "77 K")), [])                         # limit ~15.3
        self.assertEqual(self.ids(swing(55.0, "350 K")), ["below-thermionic-limit"])  # limit ~69.4
        self.assertEqual(self.ids(swing(60.0, "27 degC")), [])                       # 300.15 K

    def test_a_bare_temperature_is_not_guessed(self):
        self.assertEqual(self.ids(swing(40.0, 300)), ["temperature-unit-unstated"])
        self.assertEqual(self.ids(swing(40.0, "warm")), ["temperature-unit-unstated"])
        self.assertIsNone(temperature_k(300))
        self.assertAlmostEqual(temperature_k("27 degC"), 300.15)
        self.assertAlmostEqual(temperature_k("80 degF"), 299.8166, places=3)

    def test_other_quantities_are_left_alone(self):
        c = {"id": "X", "quantity": ENG.record(5.0, "x", "energy_advantage_ratio")}
        self.assertEqual(scrutiny(c, DEFS), [])
        self.assertEqual(scrutiny({"id": "Y"}, DEFS), [])


if __name__ == "__main__":
    unittest.main(verbosity=1)
