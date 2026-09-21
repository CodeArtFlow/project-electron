"""The gold set and its evaluator. No credentials, no network: the model is simulated.

The simulated models are the point. A 'perfect' model must score perfectly, and a 'hedging' model
(right answers, low confidence) must reproduce the failure seen live: the shipped thresholds flag
everything, while a confident-adverse rule separates real defects from clean cases. If the
evaluator could not tell those apart, its numbers would mean nothing.

Usage:  python pipeline/test_gold_eval.py
"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gold_eval import (agreement, build_jobs_from_gold, confident_adverse, confusion,  # noqa: E402
                       current_flags, is_defective, load_gold, match, render, status)
from semantic_checks import MODEL, extraction_questions, publication_questions, run  # noqa: E402

CASES, PROVENANCE = load_gold()
EXTRACTION = [c for c in CASES if c["stage"] == "extraction"]
PUBLICATION = [c for c in CASES if c["stage"] == "publication"]


def answers_for(case, conf):
    """A model that gives every label as its answer, with the given confidence."""
    questions = extraction_questions() if case["stage"] == "extraction" else publication_questions()
    out = {}
    for q, spec in questions.items():
        label = case["labels"][q]
        if spec["type"] == "noul":
            out[q] = {"type": "noul", "noul": conf if label else 1 - conf}
        else:
            keys = list(spec["criteria"])
            rest = (1 - conf) / (len(keys) - 1)
            out[q] = {"type": "choice", "choice": label, "confidence": conf,
                      "probabilities": {k: (conf if k == label else rest) for k in keys}}
    return out


def report_from(cases, conf):
    records = []
    for c in cases:
        request = {"model": MODEL, "state": c.get("state") or {"document": c.get("document", "")},
                   "questions": (extraction_questions() if c["stage"] == "extraction"
                                 else publication_questions())}
        records.append({"id": c["audit_id"], "stage": c["stage"], "required": True,
                        "fingerprint": c.get("fingerprint"), "request": request,
                        "response": {"model": MODEL, "usage": {"input_tokens": 1, "output_tokens": 1},
                                     "answers": answers_for(c, conf)}, "status": "x"})
    return {"records": records, "version": "test", "mode": "live"}


class Gold(unittest.TestCase):
    def test_the_seed_is_what_it_claims_to_be(self):
        self.assertEqual(len(EXTRACTION), 7)
        self.assertEqual(len(PUBLICATION), 8)
        self.assertIn("PENDING", PROVENANCE["independent_review"])
        self.assertIn("SEED", PROVENANCE["warning"])
        for c in CASES:
            self.assertTrue(c["fingerprint"] and c["audit_id"] and c["basis"], c["id"])
        for c in EXTRACTION:
            self.assertTrue(c["state"]["claim"] and c["state"]["sources"], c["id"])
            self.assertEqual(set(c["labels"]), set(extraction_questions()), c["id"])
        for c in PUBLICATION:
            self.assertEqual(set(c["labels"]), set(publication_questions()), c["id"])
            self.assertIn("No claims in the ledger", c["document"], c["id"])

    def test_defect_definition(self):
        defect = {c["id"]: is_defective(c) for c in EXTRACTION}
        self.assertFalse(defect["gold-ex-arch0001"])          # the one clean claim
        self.assertFalse(defect["gold-ex-dev0001"])
        for n in (2, 3, 4, 5, 6):
            self.assertTrue(defect[f"gold-ex-arch000{n}"], n)  # bound lost / quantity mistyped
        self.assertFalse(any(is_defective(c) for c in PUBLICATION))

    def test_the_documented_blind_spot_is_recorded_not_hidden(self):
        blind = [c for c in EXTRACTION if c.get("blind_spot")]
        self.assertEqual([c["id"] for c in blind], ["gold-ex-arch0004"])
        self.assertIn("record", blind[0]["blind_spot"])


class Evaluator(unittest.TestCase):
    def test_a_perfect_model_scores_perfectly_under_the_shipped_thresholds(self):
        pairs, skipped = match(report_from(CASES, 0.99), CASES)
        self.assertEqual((len(pairs), len(skipped)), (15, 0))
        self.assertTrue(all(s["ok"] == s["n"] for s in agreement(pairs).values()))
        tp, fp, fn, tn = confusion(pairs, lambda r: bool(current_flags(r)))
        self.assertEqual((fp, fn), (0, 0))
        self.assertEqual((tp, tn), (5, 10))

    def test_a_hedging_model_reproduces_the_live_failure_and_the_rule_that_fixes_it(self):
        # Right answers, 0.7 confidence: exactly the regime the first live run was in.
        pairs, _ = match(report_from(CASES, 0.70), CASES)
        tp, fp, fn, tn = confusion(pairs, lambda r: bool(current_flags(r)))
        self.assertEqual((tp, fp, fn, tn), (5, 10, 0, 0))      # flags EVERYTHING: no discrimination
        # A rule that only acts on CONFIDENT adverse answers separates them at tau 0.5...
        tp, fp, fn, tn = confusion(pairs, lambda r: confident_adverse(r, 0.5))
        self.assertEqual((tp, fp, fn, tn), (5, 0, 0, 10))
        # ...and going too strict throws away every defect: the trade-off is real and visible.
        tp, fp, fn, tn = confusion(pairs, lambda r: confident_adverse(r, 0.9))
        self.assertEqual((tp, fn), (0, 5))

    def test_labels_stop_applying_when_the_input_changes(self):
        report = report_from(EXTRACTION, 0.99)
        report["records"][0]["fingerprint"] = "0" * 64
        del report["records"][1]
        pairs, skipped = match(report, EXTRACTION)
        reasons = dict(skipped)
        self.assertIn("no longer applies", reasons["gold-ex-arch0001"])
        self.assertEqual(reasons["gold-ex-arch0002"], "not in the report")
        self.assertEqual(len(pairs), 5)
        pairs, _ = match(report, EXTRACTION, check_fingerprint=False)     # frozen-input re-runs
        self.assertEqual(len(pairs), 6)

    def test_a_disagreeing_answer_is_listed_for_review_with_its_confidence(self):
        report = report_from(EXTRACTION, 0.95)
        rec = next(r for r in report["records"] if r["id"] == "claim:CLM-ARCH-0002")
        rec["response"]["answers"]["support"] = {"type": "choice", "choice": "supports",
            "confidence": 0.94, "probabilities": {"supports": 0.94, "contradicts": 0.02,
                                                  "unsupported": 0.03, "unknown": 0.01}}
        pairs, _ = match(report, EXTRACTION)
        text = render(pairs, [], "t")
        self.assertIn("DISAGREE with the label", text)
        self.assertIn("gold-ex-arch0002", text)
        self.assertIn("the LABEL as much as the model", text)

    def test_the_caveats_are_always_printed(self):
        pairs, _ = match(report_from(CASES, 0.99), CASES)
        text = render(pairs, [], "t")
        for must in ("a seed, not a benchmark", "NOT independently reviewed",
                     "'publication' has NO defective examples", "gold-ex-arch0004"):
            self.assertIn(must, text)
        self.assertIn("independent review of the labels", status(CASES, PROVENANCE))

    def test_gold_inputs_can_be_re_run_without_the_repo_state(self):
        jobs = build_jobs_from_gold(CASES)
        self.assertEqual(len(jobs), 7)                                    # extraction only
        self.assertEqual({j["id"] for j in jobs}, {c["audit_id"] for c in EXTRACTION})

        def fake(request, timeout):
            case = next(c for c in EXTRACTION if c["state"]["claim"]["id"] == request["state"]["claim"]["id"])
            return {"model": MODEL, "usage": {"input_tokens": 1, "output_tokens": 1},
                    "answers": answers_for(case, 0.99)}
        with tempfile.TemporaryDirectory() as folder:
            report = run(jobs, {}, Path(folder), True, 30, 60, fake)
        self.assertTrue(report["complete"])
        pairs, _ = match(report, EXTRACTION, check_fingerprint=False)
        self.assertEqual(len(pairs), 7)
        self.assertTrue(all(s["ok"] == s["n"] for s in agreement(pairs).values()))


if __name__ == "__main__":
    unittest.main(verbosity=1)
