"""The reader: prove the model cannot put anything into the ledger that the paper does not say.

No network and no credentials. The paper is synthetic; the models are simulated. What is under test
is the deterministic half, the half a model cannot influence, plus the plumbing around the one
place a real model is called.

Usage:  python pipeline/test_reader.py
"""

import sys
import tempfile
import unittest
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

import anthropic  # noqa: E402
import httpx2  # noqa: E402

from candidates import unread_candidates  # noqa: E402
from claims import validate_ledger  # noqa: E402
from fetch_text import FetchResult, fetch_arxiv, normalize  # noqa: E402
from read_paper import (DEFAULT_MODEL, AnthropicModel, Outcome, ReaderError, Repo, StubModel,  # noqa: E402
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
            self.assertEqual((out.decision, out.claims), ("read", []), bad)
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


class ModelClient(unittest.TestCase):
    """The single place a real model is called. Tested with a fake SDK client, real SDK exceptions."""

    class FakeMessages:
        def __init__(self, reply):
            self.reply, self.calls = reply, []
        def create(self, **kw):
            self.calls.append(kw)
            if isinstance(self.reply, Exception):
                raise self.reply
            return self.reply

    class FakeClient:
        def __init__(self, reply):
            self.messages = ModelClient.FakeMessages(reply)

    @staticmethod
    def reply(block_input=None, stop="tool_use", tool="classify_paper"):
        blocks = []
        if block_input is not None:
            blocks.append(type("B", (), {"type": "tool_use", "name": tool, "input": block_input})())
        return type("R", (), {"content": blocks, "stop_reason": stop, "model": "claude-haiku-4-5-20251001",
                              "usage": type("U", (), {"input_tokens": 1200, "output_tokens": 90})()})()

    def test_the_request_is_the_cheapest_model_with_a_forced_tool_and_no_randomness(self):
        client = self.FakeClient(self.reply({"in_scope": True, "layer": "ARCH", "reason": "x"}))
        got, usage = AnthropicModel(client=client).classify("Title", "abstract text")
        call = client.messages.calls[0]
        self.assertEqual(call["model"], DEFAULT_MODEL)
        self.assertEqual(DEFAULT_MODEL, "claude-haiku-4-5-20251001")
        self.assertEqual(call["tool_choice"], {"type": "tool", "name": "classify_paper"})
        self.assertEqual(call["temperature"], 0)
        self.assertIn("<paper_text>", call["messages"][0]["content"])         # the paper is delimited DATA
        self.assertIn("DATA", call["system"])
        self.assertLessEqual(call["max_tokens"], 400)
        self.assertEqual(got["layer"], "ARCH")
        self.assertEqual(usage, {"input": 1200, "output": 90, "model": "claude-haiku-4-5-20251001"})

    def test_the_extraction_tool_offers_only_quantities_defined_in_definitions(self):
        client = self.FakeClient(self.reply(reading([]), tool="record_reading"))
        AnthropicModel(client=client).extract("T", "text", ["mobility", "energy"])
        tool = client.messages.calls[0]["tools"][0]
        enum = tool["input_schema"]["properties"]["claims"]["items"]["properties"]["quantity"]["properties"]["name"]["enum"]
        self.assertEqual(enum, ["mobility", "energy"])
        self.assertEqual(client.messages.calls[0]["tool_choice"]["name"], "record_reading")

    def test_a_truncated_or_toolless_answer_is_an_error_not_a_guess(self):
        for r, kind in ((self.reply({"a": 1}, stop="max_tokens"), "truncated"), (self.reply(None), "no_tool_output")):
            with self.assertRaises(ReaderError) as ctx_:
                AnthropicModel(client=self.FakeClient(r)).classify("T", "x")
            self.assertEqual(ctx_.exception.kind, kind)

    def test_real_sdk_exceptions_map_to_retryable_or_fatal(self):
        req = httpx2.Request("POST", "https://api.anthropic.com/v1/messages")
        def status(cls, code):
            return cls("boom", response=httpx2.Response(code, request=req), body=None)
        cases = [(status(anthropic.RateLimitError, 429), "rate_limited", False),
                 (status(anthropic.AuthenticationError, 401), "api_401", True),
                 (status(anthropic.PermissionDeniedError, 403), "api_403", True),
                 (status(anthropic.InternalServerError, 500), "api_500", False),
                 (anthropic.APIConnectionError(request=req), "network", False),
                 (anthropic.APITimeoutError(request=req), "network", False)]
        for exc, kind, fatal in cases:
            with self.assertRaises(ReaderError) as ctx_:
                AnthropicModel(client=self.FakeClient(exc)).classify("T", "x")
            self.assertEqual((ctx_.exception.kind, ctx_.exception.fatal), (kind, fatal), kind)


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
