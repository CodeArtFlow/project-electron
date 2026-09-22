"""The reader's run log and report: append-only, bucketed by why the verifier refused, and honest.

No network, no credentials, no git (the git reader is exercised through a fake runner).

Usage:  python pipeline/test_read_report.py
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent))

from read_report import (KIND_NOTES, KINDS, append_run, backfill_from_git, load_runs, log_path,  # noqa: E402
                         reason_kind, render, run_record, summarise)

# Every distinct reason the verifier has actually given on a live run (2026-09-21), and the bucket it
# must land in. A reason that lands in `other` is a bucket we forgot, which the report must not hide.
REAL_REASONS = [
    ("the statement contains the number 6.5, which none of its quotes contain", "number_not_in_quotes"),
    ("unit conversion refused: length_device: could not parse 3 '˚A': '˚A' is not defined in the unit registry",
     "unit_unparsed"),
    ("unit conversion refused: sheet_resistance: could not parse 20 'Ω sq-1': unsupported operand type(s)",
     "unit_unparsed"),
    ("unit conversion refused: power: cannot convert 3 dB to W - Cannot convert from 'decibel' (dimensionless)",
     "unit_incompatible"),
    ("unit conversion refused: energy_advantage_ratio is dimensionless; unit 'me' is not one of ['%']",
     "unit_incompatible"),
    ("a claim with a number needs at least one verified condition saying what it is a value of (component, "
     "variant, configuration, material, mechanism, calculation, benchmark); none was given, or none had its "
     "own quote containing its value", "no_condition"),
    ("anchor quote not found verbatim in the paper (or shorter than 20 characters): 'Total 24'",
     "quote_not_found"),
    ("the value 1e+29 does not appear in any of the claim's quotes", "value_not_in_quotes"),
    ("duplicate of a claim already accepted from this paper", "duplicate"),
    ("the quote says 'up to'/'within'/'at most' before the number but bound is not upper_bound",
     "qualifier_dropped"),
    ("statement is not between 30 and 400 characters", "statement_length"),
    ("no anchor quote", "no_anchor_quote"),
    ("unknown quantity 'foo'; add it to reference/definitions.yaml", "unknown_quantity"),
    ("[compound_statement] the statement joins two assertions", "schema_rule"),
]


class Buckets(unittest.TestCase):
    def test_every_reason_seen_live_has_a_bucket_and_none_falls_into_other(self):
        for reason, kind in REAL_REASONS:
            self.assertEqual(reason_kind(reason), kind, reason)

    def test_an_unrecognised_reason_is_reported_as_other_and_not_hidden(self):
        self.assertEqual(reason_kind("something new the verifier says"), "other")
        self.assertEqual(reason_kind(None), "other")
        self.assertEqual(reason_kind(""), "other")

    def test_every_bucket_has_a_plain_description(self):
        for kind, _ in KINDS:
            self.assertIn(kind, KIND_NOTES)
        self.assertIn("other", KIND_NOTES)

    def test_the_specific_unit_bucket_wins_over_the_general_one(self):
        self.assertEqual(reason_kind("unit conversion refused: x: could not parse 3 'z'"), "unit_unparsed")
        self.assertEqual(reason_kind("unit conversion refused: x: cannot convert 3 T to V"), "unit_incompatible")


def summary(**over):
    s = {"date": "2026-09-21", "model": "screen-a", "extract_model": "extract-b", "prompt_version": "reader-v3",
         "stop_reason": "queue_exhausted", "seconds": 12.5, "cost_usd": 0.05,
         "tokens": {"input": 1000, "output": 200}, "counts": {"read": 1, "out_of_scope": 1, "no_claims": 1},
         "claims_accepted": 2, "claims_rejected": 2,
         "papers": [
             {"candidate": "CAND-1", "decision": "read", "reason": "", "chars": 5000,
              "claims": ["CLM-ARCH-0001", "CLM-ARCH-0002"],
              "rejected": [{"statement": "S1", "reason": "the statement contains the number 7, which none of its "
                                                        "quotes contain", "quotes": ["a quote"]}]},
             {"candidate": "CAND-2", "decision": "out_of_scope", "reason": "wireless", "chars": 900,
              "claims": [], "rejected": []},
             {"candidate": "CAND-3", "decision": "no_claims", "reason": "all rejected", "chars": 7000,
              "claims": [], "rejected": [{"statement": "S2", "reason": "unit conversion refused: q: could not "
                                                                       "parse 3 '˚A': not defined"}]}]}
    s.update(over)
    return s


class TheLog(unittest.TestCase):
    def test_a_run_is_compacted_and_each_rejection_keeps_only_its_bucket_and_reason(self):
        rec = run_record(summary())
        self.assertEqual((rec["model"], rec["extract_model"], rec["prompt_version"]),
                         ("screen-a", "extract-b", "reader-v3"))
        p1, p2, p3 = rec["papers"]
        self.assertEqual(p1["accepted"], 2)
        self.assertEqual(p1["rejected"][0]["kind"], "number_not_in_quotes")
        self.assertNotIn("statement", p1["rejected"][0])                     # statements live elsewhere
        self.assertEqual((p2["accepted"], p2["rejected"]), (0, []))
        self.assertEqual(p3["rejected"][0]["kind"], "unit_unparsed")

    def test_the_log_is_append_only_and_earlier_lines_are_never_rewritten(self):
        with tempfile.TemporaryDirectory() as folder:
            append_run(folder, summary(date="2026-09-21"))
            first = log_path(folder).read_text(encoding="utf-8")
            append_run(folder, summary(date="2026-09-22"))
            both = log_path(folder).read_text(encoding="utf-8")
            self.assertTrue(both.startswith(first))
            self.assertEqual([r["date"] for r in load_runs(folder)], ["2026-09-21", "2026-09-22"])

    def test_a_run_that_was_skipped_for_want_of_a_key_is_not_a_run(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertIsNone(append_run(folder, {"skipped_reason": "GEMINI_API_KEY is not set", "papers": []}))
            self.assertEqual(load_runs(folder), [])

    def test_a_missing_log_reads_as_no_runs(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(load_runs(folder), [])
            self.assertIn("No reader runs", render([]))


class Backfill(unittest.TestCase):
    """The git history is read through a fake runner: no repository is touched."""

    def runner(self, versions):
        def run(cmd, **kw):
            if cmd[:2] == ["git", "log"]:
                return SimpleNamespace(stdout="\n".join(versions))
            sha = cmd[2].split(":")[0]
            return SimpleNamespace(stdout=json.dumps(versions[sha]))
        return run

    def test_history_is_added_once_oldest_first_and_repeating_it_adds_nothing(self):
        versions = {"aaa1111": summary(date="2026-09-20"), "bbb2222": summary(date="2026-09-21"),
                    "ccc3333": {"skipped_reason": "no key", "papers": []}}
        with tempfile.TemporaryDirectory() as folder:
            added = backfill_from_git(folder, runner=self.runner(versions))
            self.assertEqual(len(added), 2)                                  # the skipped one is not a run
            self.assertEqual([r["source"] for r in load_runs(folder)], ["git:aaa1111", "git:bbb2222"])
            again = backfill_from_git(folder, runner=self.runner(versions))
            self.assertEqual(again, [])
            self.assertEqual(len(load_runs(folder)), 2)


class TheReport(unittest.TestCase):
    def runs(self):
        return [run_record(summary(prompt_version="reader-v2", date="2026-09-20")),
                run_record(summary(prompt_version="reader-v3", date="2026-09-21", cost_usd=0.10))]

    def test_a_change_of_prompt_model_or_extractor_is_a_separate_group(self):
        runs = self.runs() + [run_record(summary(extract_model="extract-c"))]
        self.assertEqual(len(summarise(runs)), 3)

    def test_the_numbers_add_up(self):
        g = summarise(self.runs())[("screen-a", "extract-b", "reader-v3")]
        self.assertEqual((g["runs"], g["papers"], g["accepted"], g["rejected"]), (1, 3, 2, 2))
        self.assertEqual((g["extracted"], g["with_claims"]), (2, 1))          # read + no_claims; one gave claims
        self.assertEqual(g["decisions"], {"read": 1, "out_of_scope": 1, "no_claims": 1})
        self.assertEqual(g["kinds"], {"number_not_in_quotes": 1, "unit_unparsed": 1})
        self.assertAlmostEqual(g["cost"], 0.10)

    def test_the_report_says_what_it_does_not_measure_and_names_the_buckets(self):
        text = render(self.runs())
        self.assertIn("Not measured here: whether the ACCEPTED claims are true", text)
        self.assertIn("number_not_in_quotes", text)
        self.assertIn("reader-v2", text)
        self.assertIn("reader-v3", text)
        self.assertIn("acceptance 50%", text)                                 # 2 accepted of 4 proposed
        self.assertIn("$0.0500 per paper read in full", text)                # $0.10 over 2 papers read in full

    def test_a_group_with_nothing_accepted_does_not_divide_by_zero(self):
        s = summary(papers=[{"candidate": "C", "decision": "no_claims", "chars": 1, "claims": [],
                             "rejected": [{"statement": "s", "reason": "no anchor quote"}]}],
                    claims_accepted=0, claims_rejected=1)
        text = render([run_record(s)])
        self.assertIn("n/a per accepted claim", text)
        self.assertIn("acceptance 0%", text)


if __name__ == "__main__":
    unittest.main(verbosity=1)
