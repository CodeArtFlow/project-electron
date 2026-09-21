"""The paper-grounded TypeSafe check (phase 1): prove what is sent, what is NOT sent, and that nothing changes.

No network and no credentials: the paper is synthetic and TypeSafe is simulated, but the simulation runs
the REAL response validator, so a request that breaks TypeSafe's documented contract fails here.

Usage:  python pipeline/test_paper_check.py
"""

import copy
import hashlib
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

import paper_check  # noqa: E402
import question_packets as qp  # noqa: E402
from assess_quality import MODEL, PREFIX, validate_response  # noqa: E402
from fetch_text import FetchResult, normalize  # noqa: E402
from read_paper import PROMPT_VERSION, commit_outcome, read_candidate  # noqa: E402
from test_reader import (CLASSIFY_OK, ENG, PAPER, REGISTRY, SCHEMAS, StubModel, candidate, fetched,  # noqa: E402
                         good_edp, reading)

FILLER = "Filler sentence about nothing in particular that only gives the paper some length. "
QUOTE = "Table VI reports that the 512-MAC array of MiX-INT4g16 consumes 31.8 mW in 28nm at 500 MHz."
QUOTE2 = "The array uses a 4-bit integer datapath with group size 16 in every configuration reported."
TEXT = ("MiX power results\nAbstract We evaluate accelerators in 28nm. " + FILLER * 120 + "\nResults. " + QUOTE
        + " " + FILLER * 150 + "\nMethods. " + QUOTE2 + " " + FILLER * 100 + "\nReferences [1] A. Author, 2020.\n")
CID, CID2 = "CLM-ARCH-0001", "CLM-ARCH-0002"
CLAIM = {"id": CID, "topic": "ARCH", "statement": "The 512-MAC array of MiX-INT4g16 consumes 31.8 mW in 28nm at 500 MHz in BLG.",
         "sources": ["SRC-90001"], "grade": "B", "credibility": "unknown", "evidence_type": "simulated",
         "status": "active", "as_of": "2026-09-17", "created": "2026-09-21",
         "conditions": {"architecture": "MiX-INT4g16", "array_size": "512-MAC"},
         "quantity": {"quantity": "power", "as_published": {"value": 31.8, "unit": "mW"},
                      "si_base": {"value": 0.0318, "unit": "W"}, "display": {"value": 31.8, "unit": "mW"},
                      "bound": "exact", "approximate": False,
                      "conditions": {"architecture": "MiX-INT4g16", "array_size": "512-MAC"}}}
CLAIM2 = {**CLAIM, "id": CID2, "statement": "The datapath is a 4-bit integer datapath with group size 16.",
          "conditions": {"architecture": "MiX-INT4g16"}, "quantity": None}
SOURCE = {"id": "SRC-90001", "arxiv_id": "2609.00001v1", "title": "MiX", "reported": f"“{QUOTE}”",
          "method_summary": f"“{QUOTE2}”", "limitations": ""}


def make_repo(folder, text=TEXT, claims=(CLAIM,), spans=None):
    root = Path(folder)
    (root / "corpus" / "papers").mkdir(parents=True)
    (root / "ledger" / "claims").mkdir(parents=True)
    (root / "corpus" / "papers" / "SRC-90001.yaml").write_text(yaml.safe_dump(SOURCE), encoding="utf-8")
    (root / "ledger" / "claims" / "ARCH.yaml").write_text(yaml.safe_dump({"claims": [c for c in claims]}), encoding="utf-8")
    spans = spans or {CID: [QUOTE], CID2: [QUOTE2]}
    packet = qp.build_packet(SOURCE, list(claims), text, spans,
                             {"model": "gemini-3.6-flash", "prompt_version": "reader-v3"}, "2026-09-21")
    qp.save_packet(packet, root)
    return root, packet


def fetch_of(text):
    return lambda arxiv_id: FetchResult(ok=True, text=text, chars=len(text), pages=5, url="u", access="full_text")


def good_answers(request, **override):
    """Answers that satisfy TypeSafe's documented contract, with `override` {question key: change}."""
    out = {}
    for key, q in request["questions"].items():
        if q["type"] == "noul":
            out[key] = {"type": "noul", "noul": 0.95}
        elif q["type"] == "choice":
            chosen = {"support": "supports", "evidence_type": "simulated"}.get(key.rsplit(".", 1)[-1], next(iter(q["criteria"])))
            out[key] = {"type": "choice", "choice": chosen, "confidence": 1.0,
                        "probabilities": {o: 1.0 if o == chosen else 0.0 for o in q["criteria"]}}
        else:
            n = len(q["criteria"])
            out[key] = {"type": "score", "score": 2.0, "confidence": 1.0,
                        "legend": {str(i): level for i, level in enumerate(q["criteria"])},
                        "probabilities": {str(i): 1.0 if i == 2 else 0.0 for i in range(n)}}
    for key, change in override.items():
        out[key] = {**out[key], **change}
    return out


class FakeTypeSafe:
    def __init__(self, **override):
        self.calls, self.override = [], override

    def __call__(self, request, key):
        self.calls.append(request)
        response = {"model": MODEL, "answers": good_answers(request, **self.override),
                    "usage": {"input_tokens": 5_000, "output_tokens": 0}}
        validate_response(response, request)          # the real contract check
        return response


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run_check(root, **kw):
    kw.setdefault("fetch", fetch_of(TEXT))
    kw.setdefault("call", FakeTypeSafe())
    live = kw.pop("live", True)
    return paper_check.run(root, "test-key-not-real", live, 10, 600, sleep=lambda s: None, today="2026-09-21", **kw)


def answers_doc(root):
    return json.loads(qp.answers_path("SRC-90001", root).read_text(encoding="utf-8"))


class Terms(unittest.TestCase):
    def test_a_distinctive_word_the_evidence_lacks_becomes_a_term_and_ordinary_words_do_not(self):
        terms = qp.distinctive_terms(CLAIM["statement"], [QUOTE, "MiX-INT4g16", "512-MAC"])
        self.assertEqual(terms, ["BLG"])                      # "in BLG" is not in the quote: the model supplied it
        self.assertNotIn("consumes", terms)
        self.assertNotIn("The", terms)

    def test_identifiers_acronyms_symbols_and_formulae_count_as_distinctive(self):
        got = qp.distinctive_terms("The SiO2 substrate, the Ω1 spacing and the FTJ device use MiX-INT4g16 cells.", [])
        self.assertEqual(sorted(got), sorted(["SiO2", "Ω1", "FTJ", "MiX-INT4g16"]))

    def test_a_term_the_evidence_contains_is_not_asked_about_and_case_and_spacing_do_not_matter(self):
        self.assertEqual(qp.distinctive_terms("Uses the FTJ device", ["an  ftj\ndevice was built"]), [])

    def test_the_claims_own_unit_is_asked_about_as_a_unit_and_not_as_a_term(self):
        # "mW" was in the statement but not in the quoted table row: the unit lives in the header.
        self.assertEqual(qp.distinctive_terms("The array consumes 31.8 mW in BLG.", ["31.8"], skip=["mW"]), ["BLG"])
        self.assertEqual(qp.distinctive_terms("The array consumes 31.8 mW in BLG.", ["31.8"]), ["mW", "BLG"])
        self.assertIn(f"{CID}.unit", qp.claim_questions(CID, CLAIM, []))
        self.assertNotIn(f"{CID2}.unit", qp.claim_questions(CID2, CLAIM2, []))          # no quantity, no unit

    def test_terms_are_capped_and_de_duplicated(self):
        many = " ".join(f"AB{i}" for i in range(20)) + " AB1 AB1"
        got = qp.distinctive_terms(many, [])
        self.assertEqual(len(got), qp.MAX_TERMS)
        self.assertEqual(len(set(got)), len(got))


class TheRubric(unittest.TestCase):
    def test_a_claim_gets_the_fixed_rubric_plus_one_literal_question_per_condition_and_per_term(self):
        q = qp.claim_questions(CID, CLAIM, ["BLG"])
        self.assertEqual(sorted(q), sorted([f"{CID}.support", f"{CID}.is_result", f"{CID}.evidence_type", f"{CID}.atomic",
                                            f"{CID}.unit", f"{CID}.cond.architecture", f"{CID}.cond.array_size",
                                            f"{CID}.term.1"]))
        self.assertIn('"BLG"', q[f"{CID}.term.1"]["instructions"])

    def test_no_question_asks_typesafe_to_do_arithmetic_check_a_qualifier_or_count(self):
        # TypeSafe's own documentation: weak at numeric precision, counting and comparison. Code does those.
        self.assertFalse(any(k.endswith(".numbers") for k in qp.claim_questions(CID, CLAIM, [])))
        # The shared safety PREFIX every question carries is not the rubric: scan the rubric's own words.
        text = " ".join(x["instructions"].replace(PREFIX, "") for x in qp.claim_questions(CID, CLAIM, ["BLG"]).values()).lower()
        # Phrases that ASK for arithmetic, counting, comparison or unit work ("counts" as a verb is fine).
        for banned in ("convert", "how many", "count the", "number of", "sum of", "difference between",
                       "percent", "larger than", "greater than", "less than", "round"):
            self.assertNotIn(banned, text, banned)

    def test_every_question_is_about_the_excerpts_says_they_are_partial_and_references_the_claim_in_backticks(self):
        for key, x in qp.claim_questions(CID, CLAIM, ["BLG"]).items():
            if key.endswith(".atomic"):
                self.assertIn(f"`claims.{CID}.statement`", x["instructions"])
                continue
            self.assertIn("`paper_excerpts`", x["instructions"], key)
            self.assertIn("not all of it", x["instructions"], key)
            self.assertIn(f"`claims.{CID}.", x["instructions"], key)

    def test_the_rubric_follows_the_current_claim_so_a_correction_cannot_leave_a_stale_question(self):
        after = {**CLAIM, "conditions": {"architecture": "MiX-INT4g16", "mode": "x"}}
        keys = set(qp.claim_questions(CID, after, []))
        self.assertIn(f"{CID}.cond.mode", keys)
        self.assertNotIn(f"{CID}.cond.array_size", keys)

    def test_a_claim_with_no_conditions_or_quantity_still_gets_its_core_questions(self):
        bare = {"id": CID, "statement": "The widget was evaluated by simulation in the test process.", "conditions": {}}
        self.assertEqual(sorted(qp.claim_questions(CID, bare, [])),
                         sorted([f"{CID}.support", f"{CID}.is_result", f"{CID}.evidence_type", f"{CID}.atomic"]))


class ThePacket(unittest.TestCase):
    def test_a_packet_holds_the_evidence_and_terms_not_the_paper_and_hashes_the_exact_text(self):
        with tempfile.TemporaryDirectory() as f:
            _, packet = make_repo(f)
        self.assertEqual(qp.validate_packet(packet), [])
        self.assertEqual(packet["text_sha256"], hashlib.sha256(TEXT.encode("utf-8")).hexdigest())
        self.assertNotIn("Filler sentence", json.dumps(packet))               # the paper itself is never stored
        self.assertEqual(packet["claims"][CID]["evidence_spans"], [QUOTE])
        self.assertEqual(packet["claims"][CID]["terms"], ["BLG"])
        self.assertEqual(packet["extra_quotes"], [QUOTE2])                    # the method quote, as context

    def test_a_broken_packet_is_reported_not_trusted(self):
        with tempfile.TemporaryDirectory() as f:
            _, good = make_repo(f)
        breakers = {
            "wrong version": lambda p: p.update(packet_version="x"),
            "bad hash": lambda p: p.update(text_sha256="abc"),
            "no source id": lambda p: p.update(source="paper-1"),
            "no claims": lambda p: p.update(claims={}),
            "claim with no evidence": lambda p: p["claims"][CID].update(evidence_spans=[]),
            "blank evidence": lambda p: p["claims"][CID].update(evidence_spans=["  "]),
            "too many terms": lambda p: p["claims"][CID].update(terms=[f"AB{i}" for i in range(9)]),
            "a term that is not a plain token": lambda p: p["claims"][CID].update(terms=["`inject` this"]),
            "bad extra quotes": lambda p: p.update(extra_quotes=[3]),
        }
        for name, breaker in breakers.items():
            p = copy.deepcopy(good)
            breaker(p)
            self.assertTrue(qp.validate_packet(p), name)


class TheRequest(unittest.TestCase):
    def test_typesafe_is_sent_excerpts_with_positions_and_only_allowlisted_claim_fields_never_the_whole_paper(self):
        with tempfile.TemporaryDirectory() as f:
            root, _ = make_repo(f)
            tsafe = FakeTypeSafe()
            run_check(root, call=tsafe)
        request = tsafe.calls[0]
        state = request["state"]
        self.assertEqual(request["model"], MODEL)
        self.assertEqual(state["paper_excerpts"][0]["id"], "excerpt 1")
        self.assertTrue(all(e["position_in_paper"].startswith("characters ") for e in state["paper_excerpts"]))
        joined = " ".join(e["text"] for e in state["paper_excerpts"])
        self.assertIn(normalize(QUOTE), normalize(joined))                    # the evidence is in there
        self.assertLess(len(joined), len(TEXT) / 2)                           # and most of the paper is not
        self.assertNotIn(TEXT, json.dumps(request))
        self.assertIn("not all of it", state["about_this_state"])
        view = state["claims"][CID]
        self.assertEqual(sorted(view), ["conditions", "evidence_type", "quantity", "statement"])
        self.assertEqual(view["quantity"], {"name": "power", "as_published": "31.8 mW", "bound": "exact", "approximate": False})
        blob = json.dumps(request)
        for secret in ("SRC-90001", "sources", "credibility", "grade", "created", "test-key-not-real"):
            self.assertNotIn(secret, blob, secret)

    def test_only_claims_whose_quotes_were_found_are_sent_and_the_rest_are_recorded(self):
        with tempfile.TemporaryDirectory() as f:
            root, _ = make_repo(f, claims=(CLAIM, CLAIM2), spans={CID: [QUOTE], CID2: ["A quote about nothing that is anywhere in this paper."]})
            tsafe = FakeTypeSafe()
            run_check(root, call=tsafe)
            doc = answers_doc(root)
        self.assertTrue(all(k.startswith(CID) for k in tsafe.calls[0]["questions"]))
        self.assertEqual(sorted(tsafe.calls[0]["state"]["claims"]), [CID])
        self.assertEqual(doc["unlocated_claims"], [CID2])
        self.assertEqual(len(doc["quotes_not_found"]), 1)


class TheCheck(unittest.TestCase):
    def test_a_live_check_stores_the_questions_and_answers_but_no_paper_text_and_changes_nothing_else(self):
        with tempfile.TemporaryDirectory() as f:
            root, packet = make_repo(f)
            before = {p: digest(p) for p in (root / "ledger" / "claims" / "ARCH.yaml",
                                             root / "corpus" / "papers" / "SRC-90001.yaml",
                                             qp.packet_path("SRC-90001", root))}
            summary = run_check(root)
            doc = answers_doc(root)
            raw = qp.answers_path("SRC-90001", root).read_text(encoding="utf-8")
            after = {p: digest(p) for p in before}
        self.assertEqual(before, after)                                          # ledger, source and packet untouched
        self.assertEqual((doc["status"], doc["coverage"], doc["model"]), ("checked", "excerpts", MODEL))
        self.assertEqual(doc["text_sha256"], packet["text_sha256"])
        self.assertIn(f"{CID}.term.1", doc["questions"])                         # the exact questions asked are kept
        self.assertEqual(set(doc["questions"]), set(doc["answers"]))
        self.assertTrue(all({"id", "from", "to", "chars"} == set(e) for e in doc["excerpts"]))   # positions only
        self.assertNotIn("Filler sentence", raw)                                 # no paper text
        self.assertIn("uncalibrated", doc["note"].lower())
        self.assertEqual(summary["counts"], {"checked": 1})
        self.assertAlmostEqual(summary["estimated_cost_usd"], 5_000 * 0.042 / 1e6)

    def test_answers_that_lean_against_a_claim_are_flagged_and_worded_about_the_excerpts_not_the_paper(self):
        with tempfile.TemporaryDirectory() as f:
            root, _ = make_repo(f)
            run_check(root, call=FakeTypeSafe(**{
                f"{CID}.is_result": {"noul": 0.2},
                f"{CID}.support": {"choice": "unsupported", "probabilities": {"supports": 0.0, "contradicts": 0.0, "unsupported": 1.0, "unknown": 0.0}},
                f"{CID}.evidence_type": {"choice": "measured", "probabilities": {v: 1.0 if v == "measured" else 0.0 for v in qp.EVIDENCE_TYPES}},
                f"{CID}.cond.array_size": {"noul": 0.1},
                f"{CID}.term.1": {"noul": 0.05},
                f"{CID}.unit": {"noul": 0.2},
                f"{CID}.atomic": {"noul": 0.3}}))
            flags = answers_doc(root)["flags"][CID]
        text = " | ".join(flags)
        for needle in ("do not clearly support", "input, assumed or baseline", "suggest measured", "array_size",
                       'the term "BLG"', "more than one thing", "the unit is the unit"):
            self.assertIn(needle, text)
        self.assertTrue(all("excerpts" in f or "statement" in f for f in flags), flags)
        self.assertFalse(any("the paper does not" in f.lower() or "paper lacks" in f.lower() for f in flags))

    def test_a_clean_check_flags_nothing(self):
        with tempfile.TemporaryDirectory() as f:
            root, _ = make_repo(f)
            run_check(root)
            self.assertEqual(answers_doc(root)["flags"], {CID: []})

    def test_a_paper_that_has_changed_is_recorded_stale_and_never_sent(self):
        with tempfile.TemporaryDirectory() as f:
            root, _ = make_repo(f)
            tsafe = FakeTypeSafe()
            summary = run_check(root, fetch=fetch_of(TEXT + " A revised version."), call=tsafe)
            doc = answers_doc(root)
        self.assertEqual(tsafe.calls, [])
        self.assertEqual((doc["status"], summary["counts"]), ("stale", {"stale": 1}))

    def test_a_paper_whose_evidence_does_not_fit_is_recorded_too_long_and_never_cut(self):
        with tempfile.TemporaryDirectory() as f:
            root, _ = make_repo(f)
            tsafe = FakeTypeSafe()
            with mock.patch.object(paper_check, "build_excerpts", return_value=(None, {"chars": 99_999, "located": {CID: 1}})):
                summary = run_check(root, call=tsafe)
            doc = answers_doc(root)
        self.assertEqual(tsafe.calls, [])
        self.assertEqual((doc["status"], summary["counts"]), ("too_long", {"too_long": 1}))
        self.assertIn("not cut", doc["detail"])

    def test_a_paper_in_which_no_quote_can_be_found_is_recorded_unlocated_and_never_sent(self):
        with tempfile.TemporaryDirectory() as f:
            root, _ = make_repo(f, spans={CID: ["A quote about nothing that is anywhere in this paper."]})
            tsafe = FakeTypeSafe()
            run_check(root, call=tsafe)
            self.assertEqual(answers_doc(root)["status"], "unlocated")
        self.assertEqual(tsafe.calls, [])

    def test_a_failed_fetch_or_transport_error_records_nothing_so_it_is_retried(self):
        with tempfile.TemporaryDirectory() as f:
            root, _ = make_repo(f)
            run_check(root, fetch=lambda i: FetchResult(ok=False, error="HTTP 503", transient=True))
            self.assertFalse(qp.answers_path("SRC-90001", root).exists())

            def boom(request, key):
                raise RuntimeError("TypeSafe transport failure; no assessment recorded")
            summary = run_check(root, call=boom)
            self.assertFalse(qp.answers_path("SRC-90001", root).exists())
            self.assertEqual(summary["errors"], 1)
            self.assertEqual(run_check(root)["counts"], {"checked": 1})          # and the next run succeeds

    def test_a_bad_key_stops_the_run_instead_of_trying_every_paper(self):
        with tempfile.TemporaryDirectory() as f:
            root, _ = make_repo(f)
            def denied(request, key):
                raise RuntimeError("TypeSafe HTTP 401; no assessment recorded")
            self.assertEqual(run_check(root, call=denied)["stop_reason"], "api_error")

    def test_checked_papers_are_not_paid_for_again_unless_asked(self):
        with tempfile.TemporaryDirectory() as f:
            root, _ = make_repo(f)
            tsafe = FakeTypeSafe()
            run_check(root, call=tsafe)
            run_check(root, call=tsafe)
            self.assertEqual(len(tsafe.calls), 1)
            run_check(root, call=tsafe, recheck=True)
            self.assertEqual(len(tsafe.calls), 2)

    def test_a_preview_sends_nothing_and_writes_nothing(self):
        with tempfile.TemporaryDirectory() as f:
            root, _ = make_repo(f)
            tsafe = FakeTypeSafe()
            summary = run_check(root, call=tsafe, live=False)
            self.assertEqual(tsafe.calls, [])
            self.assertFalse(qp.answers_path("SRC-90001", root).exists())
            self.assertEqual(summary["counts"], {"preview": 1})

    def test_a_claim_no_longer_in_the_ledger_is_not_sent(self):
        with tempfile.TemporaryDirectory() as f:
            root, _ = make_repo(f)
            (root / "ledger" / "claims" / "ARCH.yaml").write_text(
                yaml.safe_dump({"claims": [{**CLAIM, "status": "retracted"}]}), encoding="utf-8")
            tsafe = FakeTypeSafe()
            run_check(root, call=tsafe)
        self.assertEqual(tsafe.calls, [])

    def test_a_malformed_packet_is_reported_loudly(self):
        with tempfile.TemporaryDirectory() as f:
            root, packet = make_repo(f)
            packet["claims"][CID]["evidence_spans"] = []
            qp.save_packet(packet, root)
            summary = run_check(root)
        self.assertEqual(summary["invalid"][0]["source"], "SRC-90001")
        self.assertEqual(summary["papers"], [])

    def test_a_missing_key_is_a_visible_skip_not_a_failure(self):
        env = {k: v for k, v in os.environ.items() if k != "TYPESAFE_API_KEY"}
        with mock.patch.dict(os.environ, env, clear=True), mock.patch.object(sys, "argv", ["paper_check.py", "--live"]):
            self.assertEqual(paper_check.main(), 0)
            with mock.patch.object(sys, "argv", ["paper_check.py", "--live", "--require-key"]):
                with self.assertRaises(SystemExit):
                    paper_check.main()

    def test_stored_answers_that_disagree_with_their_packet_are_reported(self):
        with tempfile.TemporaryDirectory() as f:
            root, _ = make_repo(f)
            run_check(root)
            self.assertEqual(paper_check.validate_answers(root), [])
            path = qp.answers_path("SRC-90001", root)
            doc = json.loads(path.read_text(encoding="utf-8"))
            doc["text_sha256"] = "0" * 64
            path.write_text(json.dumps(doc), encoding="utf-8")
            self.assertTrue(any("different text" in p for p in paper_check.validate_answers(root)))


class TheBackfill(unittest.TestCase):
    def source_with_claim(self, folder, automated=True):
        root = Path(folder)
        (root / "corpus" / "papers").mkdir(parents=True)
        (root / "ledger" / "claims").mkdir(parents=True)
        src = {**SOURCE, "extraction": {"method": "automated-extractive", "model": "gemini-3.6-flash", "prompt_version": "reader-v3"}}
        claim = {**CLAIM, "extraction": {"method": "automated-extractive"}} if automated else dict(CLAIM)
        (root / "corpus" / "papers" / "SRC-90001.yaml").write_text(yaml.safe_dump(src), encoding="utf-8")
        (root / "ledger" / "claims" / "ARCH.yaml").write_text(yaml.safe_dump({"claims": [claim]}), encoding="utf-8")
        return root

    def test_a_paper_read_before_packets_existed_gets_one_that_says_when_its_text_was_hashed(self):
        with tempfile.TemporaryDirectory() as f:
            root = self.source_with_claim(f)
            done = qp.backfill(root, fetch=fetch_of(TEXT), today="2026-09-22")
            packet = json.loads(qp.packet_path("SRC-90001", root).read_text(encoding="utf-8"))
        self.assertEqual(len(done), 1)
        self.assertEqual(qp.validate_packet(packet), [])
        self.assertEqual(packet["reader"]["backfilled"], "2026-09-22")           # the honest limit, on the record
        self.assertEqual(packet["claims"][CID]["evidence_spans"], [QUOTE])       # all of the record's quotes: the reader kept no per-claim evidence

    def test_it_never_overwrites_a_packet_nor_touches_hand_extracted_papers_nor_a_failed_fetch(self):
        with tempfile.TemporaryDirectory() as f:
            root = self.source_with_claim(f)
            self.assertIn("not backfilled", qp.backfill(root, fetch=lambda i: FetchResult(ok=False, error="HTTP 503"))[0][1])
            self.assertFalse(qp.packet_path("SRC-90001", root).exists())
            qp.backfill(root, fetch=fetch_of(TEXT))
            before = digest(qp.packet_path("SRC-90001", root))
            self.assertEqual(qp.backfill(root, fetch=fetch_of(TEXT + " changed")), [])
            self.assertEqual(digest(qp.packet_path("SRC-90001", root)), before)
        with tempfile.TemporaryDirectory() as f:
            root = self.source_with_claim(f, automated=False)
            self.assertEqual(qp.backfill(root, fetch=fetch_of(TEXT)), [])


class TheReaderWritesPackets(unittest.TestCase):
    """The reader keeps what each claim rests on, at the moment it is read. No prompt change."""

    def test_the_reader_prompt_is_unchanged_by_this_feature(self):
        self.assertEqual(PROMPT_VERSION, "reader-v3")

    def test_a_read_paper_yields_a_valid_packet_with_each_claims_own_verified_quotes_written_beside_the_claims(self):
        with tempfile.TemporaryDirectory() as folder:
            repo, path = candidate(folder)
            out = read_candidate(path, repo, StubModel(CLASSIFY_OK, reading([good_edp()]), "stub"), ENG, REGISTRY,
                                 SCHEMAS, fetched(), today="2026-09-21")
            self.assertEqual(out.decision, "read")
            self.assertEqual(qp.validate_packet(out.packet), [])
            self.assertEqual(out.packet["text_sha256"], qp.text_sha256(PAPER))
            spans = out.packet["claims"][out.claims[0]["id"]]["evidence_spans"]
            self.assertTrue(spans and all(normalize(s) in normalize(PAPER) for s in spans))     # verified quotes, in the paper
            commit_outcome(out, path, repo, "2026-09-21")
            stored = qp.packet_path(out.source["id"], Path(folder))
            self.assertEqual(json.loads(stored.read_text(encoding="utf-8"))["source"], out.source["id"])

    def test_a_paper_with_no_accepted_claim_gets_no_packet(self):
        with tempfile.TemporaryDirectory() as folder:
            repo, path = candidate(folder)
            out = read_candidate(path, repo, StubModel(CLASSIFY_OK, reading([])), ENG, REGISTRY, SCHEMAS,
                                 fetched(), today="2026-09-21")
            commit_outcome(out, path, repo, "2026-09-21")
            self.assertEqual(out.packet, {})
            self.assertFalse((Path(folder) / "corpus" / "questions").exists())


if __name__ == "__main__":
    unittest.main(verbosity=1)
