"""Excerpts: prove a claim's verified quotes are found in the raw text, and that nothing is trimmed to fit.

No network. The text carries the extraction damage seen in real PDFs: lost spaces, line-break
hyphenation, a spaced minus sign and superscripts.

Usage:  python pipeline/test_excerpts.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from excerpts import (CONTEXT_STEPS, EXCERPT_CHAR_BUDGET, OPENING_CHARS, build_excerpts, locate,  # noqa: E402
                      quotes_of)
from fetch_text import normalize  # noqa: E402

OPENING = ("Evaluating Adiabatic Widgets in a Test Process\nAbstract This work provides a systematic evaluation "
           "of widgets simulated in the TESTFAB 16nm process. " * 3)
FILLER = "Widgets are a well studied class of circuit and this filler sentence exists only to give length. "
EDP = "The best cell achieves a minimum EDP of 1.23×10 −26 J·s at V CLK = 0.6 V and f CLK = 7.94 GHz"
FIVE = "the energy benefit over static CMOS reaches up to roughly 5× at reduced frequencies"
HYPH = "Compared with a conventional design the widget keeps a subthreshold swing of 58 mV/dec"
LATE = "The measured leakage of the widget array was 4.2 nA per cell at the operating point."

# The paper as a PDF extractor would hand it over: damage in the middle of the quotes we will look for.
RAW = (OPENING + "\n" + FILLER * 40 + "\nResults. " + EDP + ", while " + FIVE.replace("× at", "×at")
       + ". " + "Compared with a conven- tional design the widget keeps a subthreshold swing of 58 mV/dec at 300 K.\n"
       + FILLER * 60 + "\nDiscussion. " + LATE + "\n" + FILLER * 30 + "\nReferences [1] A. Author, 2020.\n")


class Locate(unittest.TestCase):
    def test_a_quote_is_found_in_the_raw_text_despite_lost_spaces_hyphenation_and_minus_signs(self):
        norm = normalize(RAW)
        for quote in (EDP, FIVE, HYPH, LATE):
            loc = locate(RAW, norm, quote)
            self.assertIsNotNone(loc, quote)
            s, e = loc
            found = normalize(RAW[max(0, s - 3):e + 3])
            self.assertIn(normalize(quote), found, quote)             # the slice really contains the quote
            self.assertLess(len(RAW[s:e]), len(quote) + 60, quote)     # and is tight, not a whole page

    def test_a_late_quote_is_located_late_and_not_at_the_start(self):
        s, _ = locate(RAW, normalize(RAW), LATE)
        self.assertAlmostEqual(s, RAW.index("The measured leakage"), delta=5)

    def test_a_quote_that_is_not_there_or_is_too_short_is_not_located(self):
        norm = normalize(RAW)
        self.assertIsNone(locate(RAW, norm, "The widget array leaked 9.9 nA per cell at the operating point."))
        self.assertIsNone(locate(RAW, norm, "1.23"))
        self.assertIsNone(locate(RAW, norm, ""))


class Build(unittest.TestCase):
    def test_every_claims_quotes_are_inside_some_excerpt_in_document_order_with_the_opening_first(self):
        ex, info = build_excerpts(RAW, {"CLM-A-0001": [EDP, FIVE], "CLM-A-0002": [LATE]})
        self.assertIsNotNone(ex)
        self.assertEqual(ex[0]["from"], 0)                                             # the opening is always there
        self.assertEqual([e["id"] for e in ex], [f"excerpt {i}" for i in range(1, len(ex) + 1)])
        self.assertEqual([e["from"] for e in ex], sorted(e["from"] for e in ex))
        for a, b in zip(ex, ex[1:]):
            self.assertLess(a["to"], b["from"])                                        # merged: never overlapping
        for quote in (EDP, FIVE, LATE):
            self.assertTrue(any(normalize(quote) in normalize(e["text"]) for e in ex), quote)
        self.assertEqual(info["located"], {"CLM-A-0001": 2, "CLM-A-0002": 1})
        self.assertEqual(info["not_found"], [])

    def test_an_excerpt_is_exactly_the_papers_own_text_never_a_summary_or_a_cut_word(self):
        ex, _ = build_excerpts(RAW, {"CLM-A-0001": [LATE]})
        for e in ex:
            self.assertEqual(e["text"], RAW[e["from"]:e["to"]].strip())
            self.assertTrue(RAW[e["from"]:e["to"]].strip() == e["text"])
            self.assertTrue(e["from"] == 0 or RAW[e["from"] - 1].isspace())            # begins on a word boundary
            self.assertTrue(e["to"] == len(RAW) or RAW[e["to"]].isspace())            # and ends on one

    def test_a_quote_that_cannot_be_located_is_reported_and_its_claim_counts_as_unlocated(self):
        ex, info = build_excerpts(RAW, {"CLM-A-0001": ["A sentence that is nowhere in this paper at all."], "CLM-A-0002": [EDP]})
        self.assertEqual(info["located"], {"CLM-A-0001": 0, "CLM-A-0002": 1})
        self.assertEqual(len(info["not_found"]), 1)

    def test_the_context_shrinks_in_whole_steps_before_anything_is_dropped_or_cut(self):
        # Eight facts, each a few thousand characters from the next: wide windows cannot all fit in 12k.
        spread = "\n".join(FILLER * 40 + f"Fact {i}: the measured value {i}.{i} of parameter number {i} was recorded here." for i in range(1, 9))
        quotes = {"CLM-A-0001": [f"Fact {i}: the measured value {i}.{i} of parameter number {i} was recorded here." for i in range(1, 9)]}
        wide, wide_info = build_excerpts(spread, quotes, budget=10**9)
        tight, tight_info = build_excerpts(spread, quotes, budget=12_000)
        self.assertEqual(wide_info["context"], CONTEXT_STEPS[0])
        self.assertIsNotNone(tight)
        self.assertLess(tight_info["context"], CONTEXT_STEPS[0])
        self.assertIn(tight_info["context"], CONTEXT_STEPS)
        self.assertLessEqual(tight_info["chars"], 12_000)
        for quote in quotes["CLM-A-0001"]:                                              # nothing the claim rests on was lost
            self.assertTrue(any(normalize(quote) in normalize(e["text"]) for e in tight), quote)

    def test_a_claims_own_evidence_keeps_its_context_longer_than_the_method_and_limitation_quotes_are_kept(self):
        ex, info = build_excerpts(RAW, {"CLM-A-0001": [LATE]}, extra_quotes=[EDP, FIVE], budget=OPENING_CHARS + 150)
        self.assertIsNotNone(ex)
        self.assertTrue(info["dropped_extra"])
        self.assertTrue(any(normalize(LATE) in normalize(e["text"]) for e in ex))
        self.assertFalse(any(normalize(EDP) in normalize(e["text"]) for e in ex))

    def test_if_the_claims_own_evidence_does_not_fit_nothing_is_returned_not_a_truncation(self):
        ex, info = build_excerpts(RAW, {"CLM-A-0001": [EDP, LATE]}, budget=100)
        self.assertIsNone(ex)
        self.assertGreater(info["chars"], 100)

    def test_the_default_budget_leaves_room_in_typesafes_window(self):
        # 32k tokens of state and question; the budget is about 8k tokens at 3 characters a token.
        self.assertLessEqual(EXCERPT_CHAR_BUDGET / 3, 8_500)

    def test_quotes_are_parsed_from_a_source_record_field(self):
        field = "“First quote about power.”\n“Second quote\nspans lines.”\nno quote here"
        self.assertEqual(quotes_of(field), ["First quote about power.", "Second quote\nspans lines."])
        self.assertEqual(quotes_of(None), [])


if __name__ == "__main__":
    unittest.main(verbosity=1)
