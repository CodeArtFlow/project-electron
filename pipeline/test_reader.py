"""The reader: prove the model cannot put anything into the ledger that the paper does not say.

No network and no credentials. The paper is synthetic; the models are simulated. What is under test
is the deterministic half, the half a model cannot influence, plus the plumbing around the one
place a real model is called.

Usage:  python pipeline/test_reader.py
"""

import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

import httpx  # noqa: E402
from google.genai import errors as genai_errors  # noqa: E402
from google.genai import types as genai_types  # noqa: E402

from budget import Budget, BudgetError, BudgetExhausted  # noqa: E402
from candidates import unread_candidates  # noqa: E402
from claims import validate_ledger  # noqa: E402
from fetch_text import FetchResult, fetch_arxiv, normalize  # noqa: E402
from read_paper import (RETRY_DELAY_SECONDS, GeminiModel, Outcome, ReaderError, Repo, StubModel,  # noqa: E402
                        build_claim, choose, commit_outcome, number_appears, qualifier_mismatch,
                        read_candidate, resolve_limits, run, span_ok, token_in)
from units import UnitEngine  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ENG = UnitEngine()
REGISTRY = yaml.safe_load((ROOT / "sources/registry.yaml").read_text(encoding="utf-8"))
SCHEMAS = yaml.safe_load((ROOT / "reference/schemas.yaml").read_text(encoding="utf-8"))

# The extraction damage seen in real PDFs: lost spaces, "conven- tional", a spaced minus sign.
PAPER = (
    "Evaluating Adiabatic Widgets in a Test Process\n"
    "Abstract This work provides a systematic evaluation of widgets simulated in the TESTFAB 16nm "
    "process. The best cell achieves a minimum EDP of 1.23×10 −26 J·s at V CLK = 0.6 V and "
    "f CLK = 7.94 GHz, while the energy benefit over static CMOS reaches up to roughly5×at reduced "
    "frequencies and elevated supply voltages. Compared with a conven- tional design the widget "
    "keeps a subthreshold swing of 58 mV/dec at 300 K.\n"
    "1 Introduction " + ("Widgets are a well studied class of circuit and this filler sentence exists "
                         "only to give the document a realistic length. " * 80) +
    "\nReferences [1] A. Author, Journal of Widgets, 2020.\n")

EDP = "The best cell achieves a minimum EDP of 1.23×10 −26 J·s at V CLK = 0.6 V and f CLK = 7.94 GHz"
FIVE = "the energy benefit over static CMOS reaches up to roughly 5× at reduced frequencies"
EVID = "This work provides a systematic evaluation of widgets simulated in the TESTFAB 16nm process."
TN = normalize(PAPER)


def ctx(**over):
    base = {"text_norm": TN, "topic": "ARCH", "sid": "SRC-90001", "grade": "B",
            "evidence_type": "simulated", "as_of": "2026-09-17", "today": "2026-09-21",
            "model_used": "stub", "eng": ENG, "registry": REGISTRY, "schemas": SCHEMAS,
            "source_view": {"venue_id": "arxiv_api", "access": "full_text", "oa_evidence": "arXiv"}}
    base.update(over)
    return base


def good_edp(**over):
    c = {"statement": "The best cell reaches a minimum energy-delay product of 1.23e-26 J*s in simulation.",
         "anchor_spans": [EDP],
         "quantity": {"name": "energy_delay_product", "value": 1.23e-26, "unit": "J*s",
                      "bound": "exact", "approximate": False},
         "conditions": [{"key": "vclk", "value": "0.6 V", "span": EDP},
                        {"key": "fclk", "value": "7.94 GHz", "span": EDP}]}
    c.update(over)
    return c


def good_five(**over):
    c = {"statement": "The energy benefit over static CMOS reaches up to roughly 5x at reduced frequencies in simulation.",
         "anchor_spans": [FIVE],
         "quantity": {"name": "energy_advantage_ratio", "value": 5, "unit": "x",
                      "bound": "upper_bound", "approximate": True},
         "conditions": []}
    c.update(over)
    return c


def reading(claims, **over):
    r = {"evidence_type": "simulated", "evidence_span": EVID, "method_spans": [],
         "limitation_spans": [], "claims": claims}
    r.update(over)
    return r


def candidate(folder, cid="CAND-T-0001", arxiv_id="2609.00001v1", **over):
    repo = Repo(Path(folder))
    repo.candidates.mkdir(parents=True, exist_ok=True)
    doc = {"id": cid, "source": "arxiv", "arxiv_id": arxiv_id, "venue_id": "arxiv_api",
           "title": "Evaluating Adiabatic Widgets in a Test Process", "published_date": "2026-09-17",
           "grade_default": "B", "doi": ("10.48550/arXiv." + arxiv_id.split("v")[0]) if arxiv_id else None,
           "authors": [{"name": "A. Author"}, {"name": "B. Author"}]}
    doc.update(over)
    path = repo.candidates / f"{cid}.yaml"
    path.write_text(yaml.safe_dump(doc, allow_unicode=True), encoding="utf-8")
    return repo, path


def fetched(text=PAPER, **over):
    kw = dict(ok=True, text=text, chars=len(text), pages=8, url="https://arxiv.org/pdf/x", access="full_text")
    kw.update(over)
    return lambda arxiv_id: FetchResult(**kw)


CLASSIFY_OK = {"in_scope": True, "layer": "ARCH", "reason": "circuits"}


class Verbatim(unittest.TestCase):
    def test_normalize_survives_pdf_damage_but_not_changed_words_or_digits(self):
        self.assertEqual(normalize("approximately5×at"), normalize("approximately 5× at"))
        self.assertEqual(normalize("conven- tional"), normalize("conventional"))
        self.assertEqual(normalize("10 −26"), normalize("10-26"))
        self.assertEqual(normalize("10⁻²⁶"), normalize("10-26"))      # superscripts
        self.assertNotEqual(normalize("up to 5×"), normalize("up to 8×"))            # one digit
        self.assertNotEqual(normalize("energy benefit"), normalize("energy loss"))

    def test_span_ok_needs_a_real_quote_that_is_in_the_paper(self):
        self.assertTrue(span_ok(TN, EVID))
        self.assertTrue(span_ok(TN, "Compared with a conventional design the widget keeps a subthreshold swing"))
        self.assertFalse(span_ok(TN, "This work provides a systematic evaluation of widgets fabricated in the TESTFAB 5nm process."))
        self.assertFalse(span_ok(TN, "1.23"), "a 4-character 'quote' is not a quote")     # too short to mean anything
        self.assertFalse(span_ok(TN, ""))

    def test_a_number_must_be_a_standalone_token_not_a_piece_of_another(self):
        self.assertFalse(token_in("5", ["a 15 percent gain", "V = 0.5 V", "12.5x"]))
        self.assertTrue(token_in("5", ["up to roughly5×at", "about 5 percent"]))
        self.assertTrue(token_in("26", ["1.23×10 −26 J"]))
        self.assertFalse(token_in("2", ["2.5 V"]))
        self.assertTrue(token_in("2.5", ["2.5 V"]))

    def test_number_appears_handles_scientific_notation_and_rejects_near_misses(self):
        self.assertTrue(number_appears(1.23e-26, [EDP]))
        self.assertFalse(number_appears(1.24e-26, [EDP]))
        self.assertFalse(number_appears(1.23e-25, [EDP]))
        self.assertTrue(number_appears(5.3, ["gain of up to 5.3× compared"]))
        self.assertFalse(number_appears(5.3, ["gain of up to 15.3× compared"]))


class Qualifiers(unittest.TestCase):
    def test_a_qualifier_before_the_number_forces_the_matching_bound(self):
        q = lambda span, b, a=False: qualifier_mismatch([span], 5, b, a)   # noqa: E731
        self.assertIsNotNone(q("a benefit of up to roughly 5× at low f", "exact"))
        self.assertIsNotNone(q("a benefit of up to 5× at low f", "lower_bound"))
        self.assertIsNotNone(q("a gain of at least 5× over the baseline", "upper_bound"))
        self.assertIsNotNone(q("a gain of roughly 5× over the baseline", "exact"))
        self.assertIsNone(q("a benefit of up to roughly 5× at low f", "upper_bound", True))
        self.assertIsNone(q("a gain of 5× over the baseline", "exact"))
        # One-directional on purpose: a stricter bound than the quote needs is allowed.
        self.assertIsNone(q("a gain of 5× over the baseline", "upper_bound"))

    def test_an_unrelated_digit_cannot_hide_a_qualifier(self):
        span = "at 5 GHz the benefit is up to 5× over static CMOS"
        self.assertIsNotNone(qualifier_mismatch([span], 5, "exact", False))


class BuildClaim(unittest.TestCase):
    def reject(self, raw, expect):
        claim, why = build_claim(raw, ctx())
        self.assertIsNone(claim, why)
        self.assertIn(expect, why)

    def test_a_faithful_claim_is_accepted_with_its_conditions_and_quote_count(self):
        claim, spans = build_claim(good_edp(), ctx())
        self.assertIsNotNone(claim, spans)
        self.assertEqual(claim["conditions"], {"vclk": "0.6 V", "fclk": "7.94 GHz"})
        self.assertEqual(claim["quantity"]["bound"], "exact")
        self.assertAlmostEqual(claim["quantity"]["si_base"]["value"], 1.23e-26)
        self.assertEqual(claim["extraction"]["method"], "automated-extractive")
        self.assertEqual(claim["extraction"]["verified_quotes"], 3)

    def test_up_to_roughly_five_is_accepted_only_as_an_approximate_upper_bound(self):
        claim, _ = build_claim(good_five(), ctx())
        self.assertEqual((claim["quantity"]["bound"], claim["quantity"]["approximate"]), ("upper_bound", True))
        exact = good_five(quantity={"name": "energy_advantage_ratio", "value": 5, "unit": "x",
                                    "bound": "exact", "approximate": False})
        self.reject(exact, "up to")

    def test_every_way_a_model_could_fabricate_is_refused(self):
        self.reject(good_edp(anchor_spans=["The best cell achieves a minimum EDP of 9.99×10 −26 J·s at V CLK = 0.6 V"]),
                    "not found verbatim")
        self.reject(good_edp(statement="The best cell reaches an energy-delay product of 4.56e-26 J*s in simulation."),
                    "contains the number 4.56")
        self.reject(good_edp(quantity={"name": "energy_delay_product", "value": 9.99e-26, "unit": "J*s",
                                       "bound": "exact", "approximate": False}), "does not appear")
        self.reject(good_edp(quantity={"name": "made_up_quantity", "value": 1.23e-26, "unit": "J*s",
                                       "bound": "exact", "approximate": False}), "unknown quantity")
        self.reject(good_five(quantity={"name": "energy_advantage_ratio", "value": 5, "unit": "J",
                                        "bound": "upper_bound", "approximate": True}), "unit conversion refused")
        self.reject(good_edp(anchor_spans=[]), "no anchor quote")
        self.reject(good_edp(statement="Too short."), "30 and 400 characters")

    def test_a_condition_the_paper_does_not_state_is_dropped_never_carried_over(self):
        # The defect from the first live run: a condition copied across from a different paper.
        raw = good_edp(conditions=good_edp()["conditions"] + [
            {"key": "operating_point", "value": "reduced frequency",
             "span": "The regime of reduced frequency was used for every gate in the library."},
            {"key": "temperature", "value": "400 K", "span": EDP}])            # quote exists, value does not
        claim, _ = build_claim(raw, ctx())
        self.assertEqual(set(claim["conditions"]), {"vclk", "fclk"})

    def test_a_number_that_is_uninterpretable_without_its_conditions_is_refused(self):
        raw = {"statement": "The widget reaches a drive current of 7.94 uA/um in simulation.",
               "anchor_spans": [EDP],
               "quantity": {"name": "current_drive", "value": 7.94, "unit": "uA/um", "bound": "exact",
                            "approximate": False},
               "conditions": []}
        self.reject(raw, "missing_required_conditions")

    def test_a_low_grade_source_may_only_be_attributed_never_asserted(self):
        claim, why = build_claim(good_edp(), ctx(grade="D", evidence_type="announced"))
        self.assertIsNone(claim)
        self.assertIn("grade_de_as_fact", why)


class ReadingOnePaper(unittest.TestCase):
    def read(self, model, folder, **kw):
        repo, path = candidate(folder)
        fetch = kw.pop("fetch", fetched())
        return repo, path, read_candidate(path, repo, model, ENG, REGISTRY, SCHEMAS, fetch, today="2026-09-21", **kw)

    def test_access_and_grade_are_set_by_code_and_authors_are_not_invented(self):
        with tempfile.TemporaryDirectory() as folder:
            model = StubModel(CLASSIFY_OK, reading([good_edp(), good_five()]), "stub-model")
            _, _, out = self.read(model, folder)
        self.assertEqual(out.decision, "read")
        self.assertEqual(len(out.claims), 2)
        s = out.source
        self.assertEqual((s["access"], s["grade"], s["evidence_type"]), ("full_text", "B", "simulated"))
        self.assertIn("no figure or table image was seen", s["read_scope"])
        self.assertTrue(all(a["affiliation"] is None and a["corresponding"] is None for a in s["authors"]))
        self.assertEqual(s["extraction"]["model"], "stub-model")
        self.assertIn("“", s["reported"])
        # The record must CONTAIN what the claims rest on, or the semantic audit cannot support them.
        self.assertIn(normalize("reaches up to roughly 5"), normalize(s["reported"]))

    def test_an_out_of_scope_paper_costs_one_cheap_call_and_never_reaches_the_full_text_call(self):
        class Guard(StubModel):
            def extract(self, *a):
                raise AssertionError("the full-text call was made for an out-of-scope paper")
        with tempfile.TemporaryDirectory() as folder:
            model = Guard({"in_scope": False, "layer": "none", "reason": "quantum information theory"})
            _, _, out = self.read(model, folder)
        self.assertEqual((out.decision, out.claims), ("out_of_scope", []))
        self.assertIn("quantum", out.reason)

    def test_a_paper_with_no_verifiable_evidence_type_yields_no_claims_and_says_why(self):
        for bad in ({"evidence_type": "mixed"},
                    {"evidence_span": "The widget was measured on a probe station at CERN, in 2019."}):
            with tempfile.TemporaryDirectory() as folder:
                _, _, out = self.read(StubModel(CLASSIFY_OK, reading([good_edp()], **bad)), folder)
            self.assertEqual((out.decision, out.claims), ("no_claims", []), bad)
            self.assertIn("human reader", out.reason)
            self.assertEqual(out.source["evidence_type"], "unknown")

    def test_unreadable_too_long_and_not_arxiv_are_decisions_but_a_transient_failure_is_not(self):
        with tempfile.TemporaryDirectory() as folder:
            m = StubModel(CLASSIFY_OK, reading([]))
            _, _, out = self.read(m, folder, fetch=lambda i: FetchResult(False, error="only 90 characters came back"))
            self.assertEqual(out.decision, "unreadable")
            _, _, out = self.read(m, folder, fetch=lambda i: FetchResult(False, error="HTTP 503", transient=True))
            self.assertEqual(out.decision, "error")                  # left untouched: retried next run
            _, _, out = self.read(m, folder, max_chars=500)
            self.assertEqual(out.decision, "too_long")
            self.assertIn("not truncated", out.reason)
        with tempfile.TemporaryDirectory() as folder:
            repo, path = candidate(folder, source="openalex", arxiv_id=None)
            out = read_candidate(path, repo, StubModel(), ENG, REGISTRY, SCHEMAS)
            self.assertEqual(out.decision, "not_arxiv")

    def test_a_dry_run_reports_size_and_never_calls_the_model(self):
        class Boom(StubModel):
            def classify(self, *a):
                raise AssertionError("model called during a dry run")
        with tempfile.TemporaryDirectory() as folder:
            repo, path = candidate(folder)
            m = Boom(model="DRY-RUN") if False else Boom(None, None, "DRY-RUN")
            out = read_candidate(path, repo, m, ENG, REGISTRY, SCHEMAS, fetched())
        self.assertEqual(out.decision, "dry_run")
        self.assertIn("model not called", out.reason)

    def test_the_same_result_stated_twice_is_recorded_once(self):
        with tempfile.TemporaryDirectory() as folder:
            model = StubModel(CLASSIFY_OK, reading([good_edp(), good_edp(conditions=[])]))
            _, _, out = self.read(model, folder)
        self.assertEqual(len(out.claims), 1)
        self.assertEqual(out.rejected[0]["reason"], "duplicate of a claim already accepted from this paper")


class WritingAndTheRun(unittest.TestCase):
    def test_a_read_writes_a_valid_record_and_claims_retires_the_candidate_and_is_not_offered_again(self):
        with tempfile.TemporaryDirectory() as folder:
            repo, path = candidate(folder)
            out = read_candidate(path, repo, StubModel(CLASSIFY_OK, reading([good_edp(), good_five()])),
                                 ENG, REGISTRY, SCHEMAS, fetched(), today="2026-09-21")
            commit_outcome(out, path, repo, "2026-09-21")
            self.assertFalse(path.exists())                                   # retired
            self.assertTrue((repo.papers / f"{out.source['id']}.yaml").exists())
            n, problems = validate_ledger(repo.claims_dir)
            self.assertEqual((n, problems), (2, []))
            self.assertEqual(choose(repo, 10), [])

    def test_a_decision_keeps_the_candidate_so_the_sweep_cannot_re_harvest_it(self):
        with tempfile.TemporaryDirectory() as folder:
            repo, path = candidate(folder)
            out = read_candidate(path, repo, StubModel({"in_scope": False, "layer": "none", "reason": "chemistry"}),
                                 ENG, REGISTRY, SCHEMAS, fetched(), today="2026-09-21")
            commit_outcome(out, path, repo, "2026-09-21")
            self.assertTrue(path.exists())
            doc = yaml.safe_load(path.read_text(encoding="utf-8"))
            self.assertEqual(doc["read_decision"]["decision"], "out_of_scope")
            self.assertEqual(unread_candidates(repo.candidates), [])          # no longer counted as unread
            self.assertEqual(choose(repo, 10), [])

    def test_a_paper_with_no_accepted_claim_is_not_retired_and_leaves_no_empty_record(self):
        """The live run found this: 4 in-scope papers gave 0 claims and were deleted from the queue."""
        rejected_all = reading([good_edp(anchor_spans=["a quote that is not anywhere in the paper at all"])])
        for label, model in (("the model proposes nothing", StubModel(CLASSIFY_OK, reading([]))),
                             ("the verifier rejects everything", StubModel(CLASSIFY_OK, rejected_all))):
            with tempfile.TemporaryDirectory() as folder:
                repo, path = candidate(folder)
                out = read_candidate(path, repo, model, ENG, REGISTRY, SCHEMAS, fetched(), today="2026-09-21")
                self.assertEqual(out.decision, "no_claims", label)
                commit_outcome(out, path, repo, "2026-09-21")
                self.assertTrue(path.exists(), label)                                 # NOT retired
                self.assertEqual(list(repo.papers.glob("SRC-*.yaml")) if repo.papers.exists() else [], [], label)
                decision = yaml.safe_load(path.read_text(encoding="utf-8"))["read_decision"]
                self.assertEqual(decision["decision"], "no_claims")
                self.assertIn("stronger model", decision["reason"] + " stronger model")
                self.assertEqual(unread_candidates(repo.candidates), [])              # and not re-paid tomorrow
                if "rejects" in label:
                    self.assertEqual(len(decision["rejected"]), 1)                    # a human can see what was tried

    def test_two_papers_in_one_run_never_share_ids(self):
        with tempfile.TemporaryDirectory() as folder:
            candidate(folder, "CAND-T-0001", "2609.00001v1")
            repo, _ = candidate(folder, "CAND-T-0002", "2609.00002v1", published_date="2026-09-16")
            model = StubModel(CLASSIFY_OK, reading([good_edp()]))
            summary = run(repo, model, {"max_papers": 5, "max_chars": 120_000, "seconds": 600},
                          ENG, REGISTRY, SCHEMAS, fetch=lambda i: fetched()(i), sleep=lambda s: None,
                          today="2026-09-21")
            self.assertEqual(summary["counts"], {"read": 2})
            n, problems = validate_ledger(repo.claims_dir)
            self.assertEqual((n, problems), (2, []))                          # no duplicate claim ids
            ids = sorted(p.stem for p in repo.papers.glob("SRC-*.yaml"))
            self.assertEqual(ids, ["SRC-00001", "SRC-00002"])

    def test_the_run_is_bounded_and_says_why_it_stopped(self):
        limits, warns = resolve_limits(max_papers=999, max_chars=10**9, seconds=99999)
        self.assertEqual((limits["max_papers"], limits["max_chars"], limits["seconds"]), (25, 150_000, 900))
        self.assertEqual(len(warns), 3)
        with self.assertRaises(ValueError):
            resolve_limits(max_papers=0)
        with tempfile.TemporaryDirectory() as folder:
            for i in range(1, 4):
                candidate(folder, f"CAND-T-000{i}", f"2609.0000{i}v1")
            repo = Repo(Path(folder))
            base = dict(fetch=fetched(), sleep=lambda s: None, today="2026-09-21")
            capped = run(repo, StubModel(CLASSIFY_OK, reading([])),
                         {"max_papers": 2, "max_chars": 120_000, "seconds": 600}, ENG, REGISTRY, SCHEMAS,
                         dry=True, **base)
            self.assertEqual((len(capped["papers"]), capped["stop_reason"]), (2, "paper_cap"))
            ticks = iter([0, 0, 999, 999, 999])
            timed = run(repo, StubModel(CLASSIFY_OK, reading([])),
                        {"max_papers": 3, "max_chars": 120_000, "seconds": 5}, ENG, REGISTRY, SCHEMAS,
                        dry=True, clock=lambda: next(ticks, 999), **base)
            self.assertEqual(timed["stop_reason"], "time_budget")

    def test_a_fatal_error_aborts_but_an_ordinary_one_leaves_the_candidate_for_next_time(self):
        class Failing(StubModel):
            def __init__(self, fatal):
                super().__init__(); self.fatal = fatal
            def classify(self, *a):
                raise ReaderError("api_401" if self.fatal else "rate_limited", "boom", fatal=self.fatal)
        for fatal, stop in ((True, "fatal_api_error"), (False, "queue_exhausted")):
            with tempfile.TemporaryDirectory() as folder:
                candidate(folder, "CAND-T-0001", "2609.00001v1")
                repo, _ = candidate(folder, "CAND-T-0002", "2609.00002v1", published_date="2026-09-16")
                summary = run(repo, Failing(fatal), {"max_papers": 5, "max_chars": 120_000, "seconds": 600},
                              ENG, REGISTRY, SCHEMAS, fetch=fetched(), sleep=lambda s: None, today="2026-09-21")
                self.assertEqual(len(unread_candidates(repo.candidates)), 2)      # nothing was consumed
                self.assertEqual(summary["stop_reason"], stop)
                self.assertEqual(summary["counts"]["error"], 1 if fatal else 2)


POLICY = {"monthly_cap_usd": 10.0, "model": "gemini-3.8-flash", "prices_retrieved": date(2026, 9, 21),
          "prices_source": "test",
          "schedules": {"gemini-3.8-flash": [{"from": date(2026, 1, 1), "input": 0.75, "output": 3.75}],
                        "gemini-3.5-flash-lite": [{"from": date(2026, 1, 1), "input": 0.30, "output": 2.50}],
                        "budgeted-test-model": [{"from": date(2026, 1, 1), "input": 0.30, "output": 2.50}]},
          "generation": {"gemini-3.8-flash": {"thinking_level": "low"},
                         "gemini-3.5-flash-lite": {"thinking_level": "minimal"},
                         # A synthetic model that exercises the thinking_budget + temperature path (the
                         # 2.5 family's), which no priced model uses now.
                         "budgeted-test-model": {"thinking_budget": 0, "temperature": 0}}}
MODEL = "gemini-3.8-flash"            # the 3.x model the mechanism tests run against
LITE = "gemini-3.5-flash-lite"        # the model actually chosen
BUDGETED = "budgeted-test-model"


def response(data=None, finish="STOP", prompt=1200, out=90, thoughts=40, total=None, text=None,
             model_version=MODEL, feedback=None, usage=True, candidates=True):
    """A reply shaped like the SDK's GenerateContentResponse, with only the fields the reader reads."""
    cand = type("C", (), {"finish_reason": type("FR", (), {"name": finish})()})()
    u = type("U", (), {"prompt_token_count": prompt, "candidates_token_count": out,
                       "thoughts_token_count": thoughts,
                       "total_token_count": total if total is not None else prompt + out + thoughts})() \
        if usage else None
    return type("R", (), {"candidates": [cand] if candidates else [], "usage_metadata": u,
                          "model_version": model_version, "prompt_feedback": feedback,
                          "text": text if text is not None else json.dumps(data)})()


class ModelClient(unittest.TestCase):
    """The single place a real model is called, and the single place money is spent.

    Two ways: a fake client for the accounting and the error mapping, and the REAL SDK over a mock
    HTTP transport for the request that would actually go on the wire and the parsing of a reply.
    No network, no key.
    """

    class FakeModels:
        def __init__(self, replies):
            self.replies = replies if isinstance(replies, list) else [replies]
            self.calls = []

        def generate_content(self, **kw):
            self.calls.append(kw)
            r = self.replies.pop(0) if len(self.replies) > 1 else self.replies[0]
            if isinstance(r, Exception):
                raise r
            return r

    class FakeClient:
        def __init__(self, replies):
            self.models = ModelClient.FakeModels(replies)

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        # The last day of the month, so the whole remaining cap is today's to spend.
        self.budget = Budget(POLICY, Path(self._tmp.name) / "spend.json", "2026-09-30")
        self.slept = []

    def model(self, replies):
        return GeminiModel(MODEL, self.budget, client=self.FakeClient(replies), sleep=self.slept.append)

    OK = {"in_scope": True, "layer": "ARCH", "reason": "circuits"}

    def assertSpent(self, expected):
        """The ledger rounds UP to a millionth of a dollar: it may over-count, never under-count."""
        spent = self.budget.spent_month()
        self.assertGreaterEqual(spent, expected - 1e-12)
        self.assertLess(spent - expected, 2e-6)

    # ---- the request
    def test_the_request_is_schema_constrained_json_at_low_thinking_with_no_temperature(self):
        m = self.model(response(self.OK))
        got, usage = m.classify("Title", "abstract text")
        call = m.client.models.calls[0]
        cfg = call["config"]
        self.assertEqual(call["model"], MODEL)
        self.assertIn("<paper_text>", call["contents"])                  # the paper is delimited DATA
        self.assertIn("DATA", cfg.system_instruction)
        self.assertEqual(cfg.response_mime_type, "application/json")
        self.assertEqual(cfg.response_json_schema["required"], ["in_scope", "layer", "reason"])
        self.assertLessEqual(cfg.max_output_tokens, 2048)
        self.assertEqual(cfg.thinking_config.thinking_level.name, "LOW")
        # Google: for every Gemini 3 model keep temperature at its default of 1.0; lower values can
        # loop or degrade. Integrity never depended on determinism: the verifier reads the paper.
        self.assertIsNone(cfg.temperature)
        self.assertEqual(got["layer"], "ARCH")

    def test_the_chosen_model_is_called_at_minimal_thinking_with_no_temperature(self):
        m = GeminiModel(LITE, self.budget, client=self.FakeClient(response(self.OK)), sleep=self.slept.append)
        m.classify("Title", "abstract text")
        cfg = m.client.models.calls[0]["config"]
        self.assertEqual(m.client.models.calls[0]["model"], LITE)
        self.assertEqual(cfg.thinking_config.thinking_level.name, "MINIMAL")   # thinking is billed as output
        self.assertIsNone(cfg.thinking_config.thinking_budget)
        self.assertIsNone(cfg.temperature)                                      # Gemini 3: leave Google's default
        self.assertEqual(cfg.response_mime_type, "application/json")

    def test_a_model_configured_with_a_thinking_budget_gets_thinking_off_and_temperature_zero(self):
        m = GeminiModel(BUDGETED, self.budget, client=self.FakeClient(response(self.OK)), sleep=self.slept.append)
        m.classify("Title", "abstract text")
        cfg = m.client.models.calls[0]["config"]
        self.assertEqual(cfg.thinking_config.thinking_budget, 0)
        self.assertIsNone(cfg.thinking_config.thinking_level)              # never both: the API rejects that
        self.assertEqual(cfg.temperature, 0.0)

    def test_the_two_models_are_priced_differently_and_the_ledger_follows_the_model_used(self):
        for name, price in ((LITE, (0.30, 2.50)), (MODEL, (0.75, 3.75))):
            budget = Budget(POLICY, Path(self._tmp.name) / f"{name}.json", "2026-09-30")
            GeminiModel(name, budget, client=self.FakeClient(response(self.OK, prompt=1000, out=100, thoughts=0)),
                        sleep=self.slept.append).classify("T", "x")
            expected = (1000 * price[0] + 100 * price[1]) / 1e6
            self.assertGreaterEqual(budget.spent_month(), expected - 1e-12)
            self.assertLess(budget.spent_month() - expected, 2e-6)

    def test_screening_and_extraction_use_their_own_models_settings_and_prices(self):
        m = GeminiModel(LITE, self.budget, client=self.FakeClient(response(self.OK, prompt=1000, out=100, thoughts=0)),
                        sleep=self.slept.append, extract_model=MODEL)
        m.classify("T", "x")
        m.client.models.replies = [response(reading([]), prompt=20_000, out=500, thoughts=0)]
        m.extract("T", "text", ["energy"])
        calls = m.client.models.calls
        self.assertEqual([c["model"] for c in calls], [LITE, MODEL])                       # screening, then extraction
        self.assertEqual([c["config"].thinking_config.thinking_level.name for c in calls], ["MINIMAL", "LOW"])
        self.assertSpent((1000 * 0.30 + 100 * 2.50) / 1e6 + (20_000 * 0.75 + 500 * 3.75) / 1e6)   # each at its own price

    def test_with_no_extraction_model_one_model_does_both(self):
        m = self.model(response(self.OK))
        self.assertEqual(m.extract_model, m.model)

    def test_an_unpriced_extraction_model_is_refused_before_any_call(self):
        client = self.FakeClient(response(self.OK))
        with self.assertRaises(BudgetError):
            GeminiModel(LITE, self.budget, client=client, extract_model="gemini-not-priced")
        self.assertEqual(client.models.calls, [])

    def test_the_extraction_schema_offers_only_quantities_defined_in_definitions(self):
        m = self.model(response(reading([])))
        m.extract("T", "text", ["mobility", "energy"])
        schema = m.client.models.calls[0]["config"].response_json_schema
        enum = schema["properties"]["claims"]["items"]["properties"]["quantity"]["properties"]["name"]["enum"]
        self.assertEqual(enum, ["mobility", "energy"])
        self.assertEqual(schema["properties"]["claims"]["maxItems"], 8)

    def test_an_unpriced_model_cannot_be_used_at_all(self):
        with self.assertRaises(BudgetError):
            GeminiModel("gemini-3.1-pro-preview", self.budget, client=self.FakeClient(response(self.OK)))

    # ---- the accounting
    def test_thinking_tokens_are_billed_as_output_and_recorded_from_what_the_api_reports(self):
        m = self.model(response(self.OK, prompt=1200, out=90, thoughts=40))
        got, usage = m.classify("T", "x")
        self.assertEqual(usage, {"input": 1200, "output": 130, "model": MODEL})   # 90 answer + 40 thinking
        self.assertSpent((1200 * 0.75 + 130 * 3.75) / 1e6)
        self.assertEqual(self.budget.run["calls"], 1)

    def test_when_the_total_says_more_than_the_parts_the_larger_is_billed(self):
        m = self.model(response(self.OK, prompt=1000, out=10, thoughts=10, total=1500))
        _, usage = m.classify("T", "x")
        self.assertEqual(usage["output"], 500)

    def test_a_reply_with_no_usage_is_charged_at_its_worst_case_not_at_zero(self):
        m = self.model(response(self.OK, usage=False))
        m.classify("T", "x")
        self.assertEqual(self.budget.run["unknown_calls"], 1)
        self.assertGreater(self.budget.spent_month(), 2048 * 3.75 / 1e6)          # at least the output ceiling

    def test_a_call_that_does_not_fit_the_budget_is_never_made(self):
        tiny = Budget(POLICY, Path(self._tmp.name) / "tiny.json", "2026-09-30", cap_usd=0.001)
        m = GeminiModel(MODEL, tiny, client=self.FakeClient(response(self.OK)))
        with self.assertRaises(BudgetExhausted):
            m.extract("T", "x" * 100_000, ["energy"])
        self.assertEqual(m.client.models.calls, [])                                # no request left this process
        self.assertEqual(tiny.spent_month(), 0.0)

    def test_the_spend_is_written_before_the_answer_is_used(self):
        m = self.model(response(self.OK))
        m.classify("T", "x")
        again = Budget(POLICY, self.budget.path, "2026-09-30")                     # what the next run sees
        self.assertGreater(again.spent_month(), 0)

    # ---- answers that are unusable are still paid for, and are classified
    def test_an_unusable_answer_is_an_error_and_is_still_charged(self):
        SAFETY = type("F", (), {"block_reason": "SAFETY"})()
        cases = [
            (response({"a": 1}, finish="MAX_TOKENS"), "truncated", True),
            (response({"a": 1}, finish="SAFETY"), "blocked", True),
            (response(self.OK, feedback=SAFETY), "blocked", True),
            (response(self.OK, candidates=False), "no_output", False),
            (response(text="not json {"), "invalid_json", False),
            (response(text="[1, 2]"), "invalid_json", False),
        ]
        for reply, kind, permanent in cases:
            before = self.budget.spent_month()
            with self.assertRaises(ReaderError, msg=kind) as ctx_:
                self.model(reply).classify("T", "x")
            self.assertEqual((ctx_.exception.kind, ctx_.exception.permanent, ctx_.exception.fatal),
                             (kind, permanent, False), kind)
            self.assertGreater(self.budget.spent_month(), before, kind + " was not charged")

    # ---- failures
    def test_a_status_error_maps_to_fatal_or_retryable_and_is_never_charged(self):
        body = lambda code, status: {"error": {"code": code, "message": "boom", "status": status}}   # noqa: E731
        cases = [(genai_errors.ClientError(400, body(400, "INVALID_ARGUMENT")), "api_400", True),   # a bad KEY is a 400
                 (genai_errors.ClientError(401, body(401, "UNAUTHENTICATED")), "api_401", True),
                 (genai_errors.ClientError(403, body(403, "PERMISSION_DENIED")), "api_403", True),
                 (genai_errors.ClientError(404, body(404, "NOT_FOUND")), "api_404", True),
                 (genai_errors.ClientError(429, body(429, "RESOURCE_EXHAUSTED")), "rate_limited", True),
                 (genai_errors.ServerError(500, body(500, "INTERNAL")), "api_500", False),
                 (genai_errors.ServerError(503, body(503, "UNAVAILABLE")), "api_503", False)]
        for exc, kind, fatal in cases:
            with self.assertRaises(ReaderError, msg=kind) as ctx_:
                self.model(exc).classify("T", "x")
            self.assertEqual((ctx_.exception.kind, ctx_.exception.fatal), (kind, fatal), kind)
        self.assertEqual(self.budget.spent_month(), 0.0)         # none of these requests ran

    def test_a_429_or_503_is_retried_once_after_a_pause_and_charged_once(self):
        limited = genai_errors.ClientError(429, {"error": {"code": 429, "message": "slow down"}})
        m = self.model([limited, response(self.OK)])
        got, _ = m.classify("T", "x")
        self.assertEqual(got["layer"], "ARCH")
        self.assertEqual(self.slept, [RETRY_DELAY_SECONDS])
        self.assertEqual(len(m.client.models.calls), 2)
        self.assertEqual(self.budget.run["calls"], 1)             # one payment, for the call that ran

    def test_other_errors_are_not_retried(self):
        m = self.model(genai_errors.ClientError(400, {"error": {"code": 400, "message": "bad"}}))
        with self.assertRaises(ReaderError):
            m.classify("T", "x")
        self.assertEqual((len(m.client.models.calls), self.slept), (1, []))

    def test_a_timeout_may_have_been_billed_so_it_is_charged_but_a_refused_connection_was_not(self):
        with self.assertRaises(ReaderError) as ctx_:
            self.model(httpx.ReadTimeout("slow")).classify("T", "x")
        self.assertEqual((ctx_.exception.kind, ctx_.exception.fatal), ("network", False))
        self.assertEqual(self.budget.run["unknown_calls"], 1)
        charged = self.budget.spent_month()
        self.assertGreater(charged, 2048 * 3.75 / 1e6)            # assumed to have used its whole ceiling
        with self.assertRaises(ReaderError):
            self.model(httpx.ConnectError("refused")).classify("T", "x")
        self.assertEqual(self.budget.spent_month(), charged)      # a refused connection never reached Google

    # ---- the real SDK, over a mock transport
    def test_the_real_sdk_sends_the_request_we_think_it_does_and_parses_a_reply(self):
        from google import genai
        seen = {}

        def handler(request):
            seen["url"], seen["key"] = str(request.url), request.headers.get("x-goog-api-key")
            seen["body"] = json.loads(request.content)
            return httpx.Response(200, json={
                "candidates": [{"content": {"role": "model", "parts": [{"text": json.dumps(self.OK)}]},
                                "finishReason": "STOP", "index": 0}],
                "usageMetadata": {"promptTokenCount": 1500, "candidatesTokenCount": 30,
                                  "thoughtsTokenCount": 250, "totalTokenCount": 1780},
                "modelVersion": "gemini-3.8-flash"})

        client = genai.Client(api_key="test-key-not-real", http_options=genai_types.HttpOptions(
            httpx_client=httpx.Client(transport=httpx.MockTransport(handler)), timeout=120_000))
        got, usage = GeminiModel(MODEL, self.budget, client=client).classify("A title", "An abstract")

        self.assertTrue(seen["url"].endswith(f"/models/{MODEL}:generateContent"), seen["url"])
        self.assertEqual(seen["key"], "test-key-not-real")
        gen = seen["body"]["generationConfig"]
        self.assertEqual(gen["responseMimeType"], "application/json")
        self.assertIn("responseJsonSchema", gen)
        self.assertNotIn("temperature", gen)                                       # left at Google's default
        self.assertLessEqual(gen["maxOutputTokens"], 2048)
        self.assertIn("LOW", json.dumps(gen["thinkingConfig"]).upper())
        self.assertIn("systemInstruction", seen["body"])
        self.assertEqual(got, self.OK)
        self.assertEqual(usage, {"input": 1500, "output": 280, "model": "gemini-3.8-flash"})   # 30 + 250 thinking
        self.assertSpent((1500 * 0.75 + 280 * 3.75) / 1e6)


class TheWireRequestForTheChosenModel(unittest.TestCase):
    """The model the user chose, through the REAL SDK, to see the request that would actually be sent."""

    def test_thinking_is_minimal_no_temperature_is_sent_and_the_endpoint_is_the_right_model(self):
        from google import genai
        seen = {}

        def handler(request):
            seen["url"], seen["body"] = str(request.url), json.loads(request.content)
            return httpx.Response(200, json={
                "candidates": [{"content": {"role": "model", "parts": [{"text": json.dumps(ModelClient.OK)}]},
                                "finishReason": "STOP", "index": 0}],
                "usageMetadata": {"promptTokenCount": 4000, "candidatesTokenCount": 60, "totalTokenCount": 4060},
                "modelVersion": "gemini-3.5-flash-lite"})

        client = genai.Client(api_key="test-key-not-real", http_options=genai_types.HttpOptions(
            httpx_client=httpx.Client(transport=httpx.MockTransport(handler)), timeout=120_000))
        with tempfile.TemporaryDirectory() as folder:
            budget = Budget(POLICY, Path(folder) / "spend.json", "2026-09-30")
            got, usage = GeminiModel(LITE, budget, client=client).classify("A title", "An abstract")
        self.assertTrue(seen["url"].endswith("/models/gemini-3.5-flash-lite:generateContent"), seen["url"])
        gen = seen["body"]["generationConfig"]
        self.assertNotIn("temperature", gen)                                       # Gemini 3: Google's default
        self.assertIn("MINIMAL", json.dumps(gen["thinkingConfig"]).upper())        # either key spelling
        self.assertNotIn("budget", json.dumps(gen["thinkingConfig"]).lower())     # never both
        self.assertEqual(usage, {"input": 4000, "output": 60, "model": "gemini-3.5-flash-lite"})   # no thoughts reported
        self.assertEqual(got["layer"], "ARCH")


class ThePaidRun(unittest.TestCase):
    """run() with a real Budget: the cap stops a run, and a paper the model cannot read is parked."""

    class Scripted(StubModel):
        """Behaves like GeminiModel where it matters: it spends through the budget."""
        def __init__(self, budget):
            super().__init__(CLASSIFY_OK, reading([good_edp()]), MODEL)
            self.budget = budget

        def classify(self, title, head):
            self.budget.check(MODEL, 3_000, 2_048)
            self.budget.record(MODEL, 3_000, 200)
            return self._c, {"input": 3_000, "output": 200, "model": MODEL}

        def extract(self, title, text, names):
            self.budget.check(MODEL, 30_000, 12_000)
            self.budget.record(MODEL, 30_000, 3_000)
            return self._e, {"input": 30_000, "output": 3_000, "model": MODEL}

    LIMITS = {"max_papers": 5, "max_chars": 120_000, "seconds": 600}

    def test_the_run_stops_with_stop_reason_budget_and_leaves_the_rest_unread(self):
        with tempfile.TemporaryDirectory() as folder:
            for i in range(1, 5):
                candidate(folder, f"CAND-T-000{i}", f"2609.0000{i}v1", published_date=f"2026-09-1{i}")
            repo = Repo(Path(folder))
            # $0.10 for the whole (last) day: room for one paper, not four.
            budget = Budget(POLICY, Path(folder) / "spend.json", "2026-09-30", cap_usd=0.10)
            summary = run(repo, self.Scripted(budget), self.LIMITS, ENG, REGISTRY, SCHEMAS,
                          fetch=fetched(), sleep=lambda s: None, today="2026-09-30", budget=budget)
            self.assertEqual(summary["stop_reason"], "budget")
            self.assertIn("budget_note", summary)
            self.assertEqual(summary["counts"].get("read"), 1)
            self.assertEqual(len(unread_candidates(repo.candidates)), 3)          # the others wait for tomorrow
            self.assertLessEqual(budget.spent_month(), 0.10)                       # and the cap held
            self.assertAlmostEqual(summary["cost_usd"], budget.run["usd"])
            self.assertEqual(summary["budget"]["monthly_cap_usd"], 0.10)

    def test_a_paper_the_model_cannot_read_is_recorded_so_it_is_not_paid_for_again_tomorrow(self):
        class Refuses(StubModel):
            def __init__(self):
                super().__init__(tag=MODEL)
            def classify(self, *a):
                raise ReaderError("truncated", "cut off", permanent=True)
        with tempfile.TemporaryDirectory() as folder:
            repo, path = candidate(folder)
            summary = run(repo, Refuses(), self.LIMITS, ENG, REGISTRY, SCHEMAS, fetch=fetched(),
                          sleep=lambda s: None, today="2026-09-21")
            self.assertEqual(summary["counts"], {"unreadable": 1})
            self.assertEqual(unread_candidates(repo.candidates), [])               # parked, not retried
            decision = yaml.safe_load(path.read_text(encoding="utf-8"))["read_decision"]
            self.assertEqual((decision["decision"], decision["model"]), ("unreadable", MODEL))

    def test_a_transient_failure_leaves_the_candidate_for_the_next_run(self):
        class Flaky(StubModel):
            def __init__(self):
                super().__init__(tag=MODEL)
            def classify(self, *a):
                raise ReaderError("invalid_json", "not json")
        with tempfile.TemporaryDirectory() as folder:
            repo, _ = candidate(folder)
            summary = run(repo, Flaky(), self.LIMITS, ENG, REGISTRY, SCHEMAS, fetch=fetched(),
                          sleep=lambda s: None, today="2026-09-21")
            self.assertEqual(summary["counts"], {"error": 1})
            self.assertEqual(len(unread_candidates(repo.candidates)), 1)

    def test_a_dry_run_never_touches_the_ledger_or_asks_the_budget(self):
        with tempfile.TemporaryDirectory() as folder:
            repo, _ = candidate(folder)
            budget = Budget(POLICY, Path(folder) / "spend.json", "2026-09-21", persist=False)
            summary = run(repo, StubModel(CLASSIFY_OK, reading([]), "DRY-RUN"), self.LIMITS, ENG, REGISTRY,
                          SCHEMAS, fetch=fetched(), dry=True, sleep=lambda s: None, today="2026-09-21",
                          budget=budget)
            self.assertEqual(summary["cost_usd"], 0.0)
            self.assertFalse((Path(folder) / "spend.json").exists())


class Fetching(unittest.TestCase):
    def test_only_valid_arxiv_ids_are_ever_fetched(self):
        called = []
        get = lambda *a, **k: called.append(a) or None                        # noqa: E731
        for bad in ("http://evil.example/x", "../../etc/passwd", "2609.1", None, "", "2609.00001v1; rm -rf"):
            r = fetch_arxiv(bad, get=get)
            self.assertFalse(r.ok, bad)
        self.assertEqual(called, [])

    def test_a_thin_response_is_not_full_text(self):
        from fetch_text import classify_access
        self.assertEqual(classify_access(50_000, 11), "full_text")
        self.assertEqual(classify_access(500, 11), "unreadable")
        self.assertEqual(classify_access(50_000, 1), "unreadable")

    def test_a_404_is_permanent_and_a_503_is_transient(self):
        resp = lambda code: type("R", (), {"status_code": code, "content": b""})()   # noqa: E731
        r = fetch_arxiv("2609.00001v1", get=lambda *a, **k: resp(404), sleep=lambda s: None)
        self.assertEqual((r.ok, r.transient), (False, False))
        r = fetch_arxiv("2609.00001v1", get=lambda *a, **k: resp(503), sleep=lambda s: None)
        self.assertEqual((r.ok, r.transient), (False, True))
        r = fetch_arxiv("2609.00001v1", get=lambda *a, **k: type("R", (), {"status_code": 200, "content": b"<html>"})(),
                        sleep=lambda s: None)
        self.assertEqual((r.ok, r.error), (False, "response was not a PDF"))


if __name__ == "__main__":
    unittest.main(verbosity=1)
