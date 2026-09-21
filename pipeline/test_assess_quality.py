"""Offline contract tests; never spend API credits."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock
import yaml
from assess_quality import load_packet, make_request, validate_response, evaluate

def make_request_for_choice(classes):
    return {"model": "jev-test", "questions": {"cls": {"type": "choice", "instructions": "x",
            "criteria": {c: c for c in classes}}}}


class QualityTests(unittest.TestCase):
    def setUp(self):
        self.state = {"target_type":"source", "target_id":"SRC-test", "evidence":[
            {"id":"E1","dimension":"claim_support","excerpt":"observed result"}]}
        self.request = make_request(self.state)
        self.response = {"model":self.request["model"],"usage":{"input_tokens":10,"output_tokens":5},
            "answers":{"claim_support":{"type":"choice","choice":"unknown","confidence":1,
            "probabilities":{"unknown":1,"limited":0,"supported":0,"strong":0}}}}

    def test_empty_evidence_no_questions(self):
        self.assertEqual(make_request(dict(self.state,evidence=[]))["questions"], {})

    def test_response_contract(self):
        validate_response(self.response,self.request)
        for change in ("missing","nan","model","winner"):
            bad=copy.deepcopy(self.response)
            if change=="missing": bad["answers"]={}
            if change=="nan": bad["answers"]["claim_support"]["confidence"]=float("nan")
            if change=="model": bad["model"]="unexpected"
            if change=="winner": bad["answers"]["claim_support"]["choice"]="strong"
            with self.assertRaises(ValueError): validate_response(bad,self.request)

    def test_rounded_distribution_is_accepted_but_a_bad_sum_is_not(self):
        # Regression: the live API rounds each probability to 2 dp. A valid 6-class classification
        # summed to 0.99 and was rejected at the old fixed 0.001 tolerance, failing a whole run.
        classes = ["A", "C1", "C2", "D", "none", "unknown"]
        request = make_request_for_choice(classes)
        def response(probs, chosen):
            return {"model": request["model"], "usage": {"input_tokens": 1, "output_tokens": 1},
                    "answers": {"cls": {"type": "choice", "choice": chosen, "confidence": probs[chosen],
                                        "probabilities": probs}}}
        rounded = {"A": 0.10, "C1": 0.60, "C2": 0.10, "D": 0.05, "none": 0.03, "unknown": 0.01}
        self.assertAlmostEqual(sum(rounded.values()), 0.89, places=6)      # sanity: far too low
        with self.assertRaises(ValueError): validate_response(response(rounded, "C1"), request)
        ok = {"A": 0.10, "C1": 0.60, "C2": 0.11, "D": 0.09, "none": 0.03, "unknown": 0.06}
        self.assertAlmostEqual(sum(ok.values()), 0.99, places=6)           # the observed failure
        validate_response(response(ok, "C1"), request)
        # Two classes have almost no rounding slack, so a 0.98 sum must still be rejected.
        req2 = make_request_for_choice(["x", "y"])
        bad2 = {"model": req2["model"], "usage": {"input_tokens": 1, "output_tokens": 1},
                "answers": {"cls": {"type": "choice", "choice": "x", "confidence": 0.7,
                                    "probabilities": {"x": 0.7, "y": 0.28}}}}
        with self.assertRaises(ValueError): validate_response(bad2, req2)

    def test_retry_and_no_redirect(self):
        post=Mock(side_effect=[Mock(status_code=429),Mock(status_code=200,json=lambda:self.response)])
        sleeper=Mock()
        self.assertEqual(evaluate(self.request,"test",post,sleeper),self.response)
        self.assertEqual(post.call_count,2)
        self.assertFalse(post.call_args.kwargs["allow_redirects"])

    def test_auth_fail_not_retried_or_echoed(self):
        post=Mock(return_value=Mock(status_code=401))
        with self.assertRaisesRegex(RuntimeError,"HTTP 401"):
            evaluate(self.request,"secret-not-in-error",post,Mock())
        self.assertEqual(post.call_count,1)

    def test_retry_bounded(self):
        post=Mock(return_value=Mock(status_code=529))
        with self.assertRaises(RuntimeError): evaluate(self.request,"test",post,Mock())
        self.assertEqual(post.call_count,3)

    def test_size_cap(self):
        bad=copy.deepcopy(self.state)
        bad["evidence"][0]["excerpt"]="x"*41000
        with self.assertRaises(ValueError): make_request(bad)

    def test_local_provenance_and_path_guard(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            paper=root/"corpus/papers/SRC-test.yaml"
            paper.parent.mkdir(parents=True)
            paper.write_text(yaml.safe_dump({"access":"full_text","reported":"observed result"}))
            item={"id":"E1","dimension":"claim_support","record_path":"corpus/papers/SRC-test.yaml",
                  "field":"reported","excerpt":"observed result","source_url":"https://example.org/paper",
                  "locator":"Results, paragraph 1"}
            packet=dict(self.state,evidence=[item])
            path=root/"packet.json"
            path.write_text(json.dumps(packet))
            self.assertEqual(load_packet(path,root)["target_id"],"SRC-test")
            item["excerpt"]="invented result"
            path.write_text(json.dumps(packet))
            with self.assertRaises(ValueError): load_packet(path,root)
            item["record_path"]="../secret.yaml"
            path.write_text(json.dumps(packet))
            with self.assertRaises(ValueError): load_packet(path,root)

if __name__=="__main__":
    unittest.main()
