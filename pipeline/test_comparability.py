"""When two claims may be compared: prove the guard stops false conflicts and never hides a real one.

The first scheduled reading run opened six conflicts that blocked publication. Five were between claims
of unrelated papers that share only a generic quantity name. These tests rebuild those six pairs from the
real claims, and pin the opposite too: a real disagreement about one subject is still detected.

Usage:  python pipeline/test_comparability.py
"""

import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from reconcile import (COMPARABILITY, comparable, detect, load_operating_keys, not_compared,  # noqa: E402
                       shared_subject, write_not_compared)
from units import UnitEngine  # noqa: E402

ENG = UnitEngine()
OPERATING = load_operating_keys()


def claim(cid, value, unit, quantity, conds=None, status="active", **kw):
    return {"id": cid, "status": status, "sources": ["SRC-90001"], "conditions": conds or {},
            "quantity": ENG.record(value, unit, quantity, conditions=conds or None, **kw)}


# The six pairs the scheduled run opened (CFL-0006..0011), from the real claims' conditions and values.
FTJ_NAIVE = claim("CLM-ARCH-0012", 153.53, "ns", "time", {"device_type": "FTJ", "architecture": "Naive"})
FTJ_MERGED = claim("CLM-ARCH-0013", 161.99, "ns", "time", {"device_type": "FTJ", "architecture": "Merged"})
MOS2 = claim("CLM-MAT-0005", 6.1, "ps", "time", {"material": "monolayer MoS2", "temperature": "300 K",
                                                   "excitation_energy": "1.7 eV"})
BLG_AP = claim("CLM-MAT-0003", 150, "K", "temperature", {"calculation": "acoustic phonon scattering"})
BLG_OP = claim("CLM-MAT-0004", 200, "K", "temperature", {"calculation": "optical phonon and surface polar phonon scattering"})
FOIL = claim("CLM-PROC-0001", 300, "K", "temperature", {"thermal_model": "Debye model"})
OMEGA1 = claim("CLM-PHOT-0002", 3.57, "GHz", "frequency", {"component": "photonic molecule"})
OMEGA2 = claim("CLM-PHOT-0003", 15.41, "GHz", "frequency", {"component": "photonic molecule"})


class TheGuard(unittest.TestCase):
    def test_claims_of_unrelated_papers_that_share_only_a_quantity_name_are_not_compared(self):
        for a, b in ((FTJ_NAIVE, MOS2), (FTJ_MERGED, MOS2), (BLG_AP, FOIL), (BLG_OP, FOIL)):
            self.assertFalse(comparable(a, b, OPERATING), (a["id"], b["id"]))
        self.assertEqual(detect({c["id"]: c for c in (FTJ_NAIVE, FTJ_MERGED, MOS2, BLG_AP, BLG_OP, FOIL)}, []), [])

    def test_a_real_disagreement_about_one_subject_is_still_detected(self):
        same = {"cell": "PFAL buffer", "process": "TSMC 16nm"}
        a = claim("A", 5.0, "x", "energy_advantage_ratio", same)
        b = claim("B", 3.83, "x", "energy_advantage_ratio", same)
        self.assertTrue(comparable(a, b, OPERATING))
        self.assertEqual(len(detect({"A": a, "B": b}, [])), 1)

    def test_one_shared_subject_key_is_enough_and_a_differing_one_still_separates_them(self):
        a = claim("A", 5.0, "x", "energy_advantage_ratio", {"cell": "PFAL", "process": "16nm"})
        b = claim("B", 3.0, "x", "energy_advantage_ratio", {"cell": "PFAL", "vclk": "0.6 V"})
        self.assertTrue(comparable(a, b, OPERATING))                              # shares cell
        c = claim("C", 3.0, "x", "energy_advantage_ratio", {"cell": "PFAL", "process": "5nm"})
        self.assertFalse(comparable(a, c, OPERATING))                             # shared key, different value

    def test_sharing_only_an_operating_point_is_not_sharing_a_subject(self):
        a = claim("A", 5.0, "x", "energy_advantage_ratio", {"temperature": "300 K", "vdd": "0.7 V"})
        b = claim("B", 3.0, "x", "energy_advantage_ratio", {"temperature": "300 K", "vdd": "0.7 V"})
        self.assertEqual(shared_subject(a, b, OPERATING), {})
        self.assertFalse(comparable(a, b, OPERATING))
        # ...but a different operating point still separates claims that DO share a subject (rule 2).
        c = claim("C", 3.0, "x", "energy_advantage_ratio", {"cell": "PFAL", "temperature": "77 K"})
        d = claim("D", 5.0, "x", "energy_advantage_ratio", {"cell": "PFAL", "temperature": "300 K"})
        self.assertFalse(comparable(c, d, OPERATING))

    def test_claims_with_no_conditions_at_all_cannot_be_compared(self):
        a = claim("A", 5.0, "x", "energy_advantage_ratio")
        b = claim("B", 3.0, "x", "energy_advantage_ratio")
        self.assertFalse(comparable(a, b, OPERATING))

    def test_values_and_keys_are_compared_case_insensitively(self):
        a = claim("A", 5.0, "x", "energy_advantage_ratio", {"Cell": " PFAL Buffer "})
        b = claim("B", 3.0, "x", "energy_advantage_ratio", {"cell": "pfal buffer"})
        self.assertTrue(comparable(a, b, OPERATING))

    def test_a_different_quantity_or_unit_is_never_comparable_whatever_they_share(self):
        a = claim("A", 5.0, "GHz", "frequency", {"component": "ring"})
        b = claim("B", 3.0, "ns", "time", {"component": "ring"})
        self.assertFalse(comparable(a, b, OPERATING))

    def test_the_two_mode_spacings_of_one_device_still_look_comparable(self):
        # KNOWN LIMIT, not a pass: identical structured conditions cannot tell OMEGA1 from OMEGA2 (CFL-0011).
        # The guard does not fix this case; scoping the claims does, and the reader is asked to record
        # the symbol as a condition (TODO N3).
        self.assertTrue(comparable(OMEGA1, OMEGA2, OPERATING))
        scoped1 = {**OMEGA1, "conditions": {"component": "photonic molecule", "mode_spacing": "Ω1"}}
        scoped2 = {**OMEGA2, "conditions": {"component": "photonic molecule", "mode_spacing": "Ω2"}}
        self.assertFalse(comparable(scoped1, scoped2, OPERATING))


class TheLog(unittest.TestCase):
    def test_pairs_that_disagree_but_share_no_subject_are_listed_not_dropped(self):
        claims = {c["id"]: c for c in (FTJ_NAIVE, MOS2, BLG_AP, FOIL)}
        skipped = not_compared(claims, [], OPERATING)
        self.assertEqual({tuple(s["claims"]) for s in skipped},
                         {("CLM-ARCH-0012", "CLM-MAT-0005"), ("CLM-MAT-0003", "CLM-PROC-0001")})

    def test_a_pair_with_a_conflict_record_is_not_listed_twice(self):
        claims = {c["id"]: c for c in (BLG_AP, FOIL)}
        self.assertEqual(not_compared(claims, [{"claims": ["CLM-MAT-0003", "CLM-PROC-0001"]}], OPERATING), [])

    def test_a_pair_that_agrees_or_has_conflicting_conditions_is_not_listed(self):
        same = claim("S", 300, "K", "temperature", {"calculation": "x"})
        also = claim("T", 300, "K", "temperature", {"thermal_model": "y"})              # agrees numerically
        self.assertEqual(not_compared({"S": same, "T": also}, [], OPERATING), [])
        far1 = claim("U", 1, "K", "temperature", {"material": "a"})
        far2 = claim("V", 2, "K", "temperature", {"material": "b"})                     # conditions conflict: not comparable, old rule
        self.assertEqual(not_compared({"U": far1, "V": far2}, [], OPERATING), [])

    def test_only_live_claims_are_considered(self):
        retired = claim("R", 150, "K", "temperature", {"calculation": "x"}, status="retracted")
        other = claim("O", 300, "K", "temperature", {"thermal_model": "y"})
        self.assertEqual(not_compared({"R": retired, "O": other}, [], OPERATING), [])

    def test_the_log_file_says_what_it_is_and_shows_both_claims_and_their_conditions(self):
        skipped = not_compared({c["id"]: c for c in (BLG_AP, FOIL)}, [], OPERATING)
        with tempfile.TemporaryDirectory() as f:
            path = Path(f) / "not-compared.md"
            self.assertEqual(write_not_compared(skipped, path), 1)
            text = path.read_text(encoding="utf-8")
            self.assertIn("Generated artifact", text)
            self.assertIn("not a finding", text)
            self.assertIn("`CLM-MAT-0003`", text)
            self.assertIn("thermal_model=Debye model", text)
            self.assertEqual(write_not_compared([], path), 0)
            self.assertIn("No pair was skipped", path.read_text(encoding="utf-8"))


class TheCommittedFile(unittest.TestCase):
    def test_the_real_file_loads_and_treats_the_operating_point_as_not_a_subject(self):
        keys = load_operating_keys()
        for k in ("temperature", "frequency", "voltage", "pressure", "time"):
            self.assertIn(k, keys)
        for subject in ("device_type", "material", "component", "architecture", "process", "mechanism"):
            self.assertNotIn(subject, keys, subject + " says WHAT was measured and must count as subject")

    def test_a_missing_or_malformed_file_stops_detection_instead_of_loosening_it(self):
        with tempfile.TemporaryDirectory() as f:
            for name, content in (("missing.yaml", None), ("empty.yaml", ""), ("bad.yaml", "operating_keys: temperature"),
                                  ("blank.yaml", "operating_keys: ['', 'x']"), ("junk.yaml", "a: [")):
                path = Path(f) / name
                if content is not None:
                    path.write_text(content, encoding="utf-8")
                with self.assertRaises(SystemExit, msg=name):
                    load_operating_keys(path)


if __name__ == "__main__":
    unittest.main(verbosity=1)
