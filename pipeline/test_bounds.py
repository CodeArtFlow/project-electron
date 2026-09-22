"""Bounds, corrections and the digest: regression tests for defects found in the first live run.

Each test names the defect it guards. All fixtures are temporary trees; nothing here touches the
real ledger.

  1. "up to X" stored as a measurement made two upper bounds look like a contradiction (CFL-0001).
  2. A dimensionless quantity silently ignored its unit ("2 percent" stored as 2.0).
  3. A same-day digest rebuild counted its own earlier digest as history and reported "Nothing new"
     while the ledger held seven claims.
  4. A correction to an already-published claim had nowhere to be reported.

Usage:  python pipeline/test_bounds.py
"""

import sys
import tempfile
import unittest
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from claims import Refusal, check_refusals, validate_claim  # noqa: E402
from publication_gate import run_gate  # noqa: E402
from reconcile import bound_of, comparable, detect, disagree  # noqa: E402
from sota import build_digest, collect_corrections, qty  # noqa: E402
from test_publication_gate import tree, write_claim, write_source  # noqa: E402
from units import UnitEngine, UnitError  # noqa: E402

ENG = UnitEngine()


def claim(cid, value, bound="exact", approx=False, conds=None, quantity="energy_advantage_ratio"):
    return {"id": cid, "status": "active", "sources": ["SRC-00001"], "conditions": conds or {},
            "quantity": ENG.record(value, "x", quantity, bound=bound, approximate=approx)}


class Defect1_BoundsAreNotPoints(unittest.TestCase):
    def test_the_cfl_0001_pair_no_longer_conflicts(self):
        # "up to roughly 5x" and "up to 3.83x": two upper bounds cannot contradict each other.
        a = claim("A", 5.0, "upper_bound", approx=True)
        b = claim("B", 3.83, "upper_bound")
        self.assertEqual(disagree(a, b), (False, None))
        # The same two numbers as exact values DO differ by 23.4% - the false alarm we had.
        ea, eb = claim("A", 5.0), claim("B", 3.83)
        differs, rel = disagree(ea, eb)
        self.assertTrue(differs)
        self.assertAlmostEqual(rel, 0.234, places=3)

    def test_interval_semantics(self):
        cases = [  # (a, b, expected conflict?, why)
            (("exact", 5), ("exact", 5), False, "identical points"),
            (("exact", 5), ("exact", 3), True, "distinct points"),
            (("upper_bound", 3), ("exact", 5), True, "a measured 5 breaks 'up to 3'"),
            (("upper_bound", 5), ("exact", 3), False, "3 satisfies 'up to 5'"),
            (("lower_bound", 5), ("exact", 3), True, "a measured 3 breaks 'at least 5'"),
            (("lower_bound", 3), ("exact", 5), False, "5 satisfies 'at least 3'"),
            (("upper_bound", 3), ("lower_bound", 5), True, "no value is both <=3 and >=5"),
            (("upper_bound", 5), ("lower_bound", 3), False, "the interval [3,5] is non-empty"),
            (("upper_bound", 3), ("upper_bound", 5), False, "two upper bounds"),
            (("lower_bound", 3), ("lower_bound", 5), False, "two lower bounds"),
        ]
        for (ba, va), (bb, vb), expected, why in cases:
            got, _ = disagree(claim("A", va, ba), claim("B", vb, bb))
            self.assertEqual(got, expected, why)

    def test_approximate_widens_the_trigger(self):
        a, b = claim("A", 5.0), claim("B", 5.5)                       # 9% apart
        self.assertTrue(disagree(a, b)[0])
        self.assertFalse(disagree(claim("A", 5.0, approx=True), b)[0])

    def test_detection_end_to_end(self):
        # The same cell in the same process: a shared SUBJECT, which the comparability rule now requires
        # (reference/comparability.yaml). What this test is about is the bounds, not the subject.
        same = {"cell": "PFAL buffer", "process": "TSMC 16nm"}
        bounded = {"A": claim("A", 5.0, "upper_bound", True, conds=same),
                   "B": claim("B", 3.83, "upper_bound", conds=same)}
        self.assertEqual(detect(bounded, []), [])
        exact = {"A": claim("A", 5.0, conds=same), "B": claim("B", 3.83, conds=same)}
        found = detect(exact, [])
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]["bounds"]["A"], ("exact", False))
        # Different stated conditions are different results, bounded or not.
        far = {"A": claim("A", 5.0, conds={"vclk": "1 V"}), "B": claim("B", 3.0, conds={"vclk": "0.6 V"})}
        self.assertFalse(comparable(far["A"], far["B"]))
        self.assertEqual(bound_of({}), ("exact", False))               # legacy claims stay exact

    def test_extraction_refuses_a_bound_recorded_as_exact(self):
        src = {"venue_id": "arxiv_api", "access": "full_text"}
        exact = {"quantity": "energy_advantage_ratio", "bound": "exact", "approximate": False}
        with self.assertRaises(Refusal) as ctx:
            check_refusals({"statement": "PFAL reaches up to 5.3x energy gain over static CMOS "
                                         "in simulation.", "grade": "B", "quantity": exact}, src)
        self.assertEqual(ctx.exception.rule_id, "qualifier_dropped")
        # Recorded correctly, the same statement goes through.
        good = {"quantity": "energy_advantage_ratio", "bound": "upper_bound", "approximate": False}
        check_refusals({"statement": "PFAL reaches up to 5.3x energy gain over static CMOS in "
                                     "simulation.", "grade": "B", "quantity": good}, src)

    def test_validation_rejects_a_bad_bound(self):
        c = {"id": "CLM-ARCH-0001", "topic": "ARCH", "statement": "x", "sources": ["SRC-00001"],
             "grade": "B", "credibility": "unknown", "evidence_type": "simulated",
             "status": "active", "as_of": "2026-09-17", "created": "2026-09-21",
             "quantity": dict(claim("A", 1.0)["quantity"], bound="roughly")}
        self.assertTrue(any("bound" in p for p in validate_claim(c)))

    def test_a_bound_is_rendered_as_one(self):
        self.assertEqual(qty(claim("A", 5.3, "upper_bound")), "≤ 5.3 ×")
        self.assertEqual(qty(claim("A", 5.0, "upper_bound", True)), "≤ ≈5 ×")
        self.assertEqual(qty(claim("A", 3.0, "lower_bound")), "≥ 3 ×")
        self.assertEqual(qty(claim("A", 1.23)), "1.23 ×")


class Defect2_DimensionlessUnits(unittest.TestCase):
    def test_percent_converts_and_junk_is_refused(self):
        self.assertAlmostEqual(ENG.record(2, "percent", "relative_deviation")["si_base"]["value"], 0.02)
        self.assertAlmostEqual(ENG.record(2, "%", "relative_deviation")["display"]["value"], 2.0)
        for unit in ("joule", "nonsense", "nm"):
            with self.assertRaises(UnitError):
                ENG.record(5, unit, "energy_advantage_ratio")


class Defect3And4_DigestAndCorrections(unittest.TestCase):
    def ledger(self):
        return [{"id": "CLM-ARCH-0001", "topic": "ARCH", "statement": "First claim.",
                 "grade": "B", "credibility": "unknown", "evidence_type": "simulated",
                 "status": "active", "as_of": "2026-09-17", "sources": ["SRC-00001"]},
                {"id": "CLM-ARCH-0002", "topic": "ARCH", "statement": "Second claim.",
                 "grade": "B", "credibility": "unknown", "evidence_type": "simulated",
                 "status": "active", "as_of": "2026-09-17", "sources": ["SRC-00001"]}]

    def test_same_day_rebuild_is_idempotent_and_never_reports_nothing_new(self):
        with tempfile.TemporaryDirectory() as folder:
            d = Path(folder) / "digests"
            d.mkdir()
            kw = dict(digests_dir=d, candidates_dir=Path(folder), today="2026-09-20")
            first_path, n1 = build_digest(self.ledger(), [], {}, **kw)
            first = first_path.read_text(encoding="utf-8")
            # The defect: this second run saw its own output as history and said "Nothing new".
            second_path, n2 = build_digest(self.ledger(), [], {}, **kw)
            self.assertEqual((n1, n2), (2, 2))
            self.assertEqual(first, second_path.read_text(encoding="utf-8"))
            self.assertNotIn("## Nothing new", first)
            self.assertIn("CLM-ARCH-0001", first)

    def test_a_later_digest_reports_only_what_is_new(self):
        with tempfile.TemporaryDirectory() as folder:
            d = Path(folder) / "digests"
            d.mkdir()
            kw = dict(digests_dir=d, candidates_dir=Path(folder))
            build_digest(self.ledger()[:1], [], {}, today="2026-09-20", **kw)
            _, n = build_digest(self.ledger(), [], {}, today="2026-09-21", **kw)
            self.assertEqual(n, 1)
            text = (d / "2026-09-21.md").read_text(encoding="utf-8")
            self.assertIn("CLM-ARCH-0002", text)

    def test_a_claim_retracted_before_ever_being_cited_is_never_introduced_as_new(self):
        # Found 2026-09-22: CLM-DEV-0002..0004 were extracted and retracted the same day, before
        # any digest had cited them, then still appeared as "new claims" the next time a digest
        # was built, because "not previously seen" was the only filter - status wasn't checked.
        # publication_gate.py check 3 (a digest may only cite active/challenged/contested claims)
        # caught it live. A never-published claim that is already retracted by the time a digest
        # runs should not appear at all - it was never a live finding a reader should see.
        led = self.ledger()
        led[1]["status"] = "retracted"
        with tempfile.TemporaryDirectory() as folder:
            d = Path(folder) / "digests"
            d.mkdir()
            _, n = build_digest(led, [], {}, digests_dir=d, candidates_dir=Path(folder),
                                today="2026-09-20")
            self.assertEqual(n, 1)
            text = (d / "2026-09-20.md").read_text(encoding="utf-8")
            self.assertIn("CLM-ARCH-0001", text)
            self.assertNotIn("CLM-ARCH-0002", text)

    def test_corrections_appear_once_after_the_previous_digest(self):
        led = self.ledger()
        led[0]["corrections"] = [
            {"date": "2026-09-19", "public": False, "reason": "before first publication"},
            {"date": "2026-09-21", "public": True, "fields": ["quantity.bound"],
             "reason": "stored an upper bound as exact"}]
        got = collect_corrections(led, since="2026-09-20", digest_corrections_file=Path("nope"))
        self.assertEqual(len(got), 1)                                  # only the public, recent one
        self.assertIn("upper bound", got[0])
        self.assertEqual(collect_corrections(led, since="2026-09-21",
                                             digest_corrections_file=Path("nope")), [])
        with tempfile.TemporaryDirectory() as folder:
            f = Path(folder) / "dc.yaml"
            f.write_text(yaml.safe_dump({"corrections": [
                {"date": "2026-09-21", "digest": "2026-09-20", "text": "said nothing was new."}]}))
            self.assertIn("said nothing was new",
                          collect_corrections([], since="2026-09-20", digest_corrections_file=f)[0])

    def test_a_malformed_corrections_file_fails_loudly_not_silently(self):
        # Found 2026-09-22: an unquoted colon inside a plain YAML scalar broke
        # ledger/digest-corrections.yaml, and collect_corrections caught the parse error and
        # returned no corrections - a correction that silently failed to parse is a correction
        # nobody sees. A MISSING file is still a legitimate "none recorded yet" state.
        with tempfile.TemporaryDirectory() as folder:
            f = Path(folder) / "dc.yaml"
            f.write_text("corrections:\n- text: \"status: retracted\" (unquoted colon breaks this)\n")
            with self.assertRaises(SystemExit):
                collect_corrections([], since="2026-09-20", digest_corrections_file=f)
        self.assertEqual(collect_corrections([], since="2026-09-20",
                                             digest_corrections_file=Path("nope")), [])

    def test_gate_blocks_an_unreported_public_correction_then_passes_when_reported(self):
        correction = [{"date": "2026-09-21", "public": True, "fields": ["quantity.bound"],
                       "reason": "stored an upper bound as exact"}]
        with tempfile.TemporaryDirectory() as folder:
            root = tree(Path(folder))
            write_source(root)
            write_claim(root, corrections=correction)
            (root / "digests/2026-09-20.md").write_text("Cites CLM-DEV-0001.\n", encoding="utf-8")
            results, _ = run_gate(root)
            self.assertIn(8, {r["check"] for r in results if not r["passed"]})
            # Reported under '## Corrections' in a digest dated on or after the correction: passes.
            (root / "digests/2026-09-21.md").write_text(
                "# Digest\n\n## Corrections\n\n- `CLM-DEV-0001` corrected: stored an upper bound "
                "as exact.\n\n## Open contradictions\n\n_None._\n", encoding="utf-8")
            results, _ = run_gate(root)
            self.assertNotIn(8, {r["check"] for r in results if not r["passed"]})
            # Mentioning the claim elsewhere in that digest is NOT enough.
            (root / "digests/2026-09-21.md").write_text(
                "# Digest\n\n## Corrections\n\n_None._\n\n## New\n\n- `CLM-DEV-0001` again.\n",
                encoding="utf-8")
            results, _ = run_gate(root)
            self.assertIn(8, {r["check"] for r in results if not r["passed"]})


class Defect5_PublishedDigestsAreImmutable(unittest.TestCase):
    """Found when the digest builder overwrote a digest that was already committed and deployed."""

    def git(self, repo, *args):
        import subprocess
        return subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@example.org", *args],
                              cwd=repo, capture_output=True, text=True, check=True)

    def test_a_committed_digest_is_never_rewritten_but_an_uncommitted_one_is(self):
        import sota
        from sota import DigestAlreadyPublished, published_and_different
        with tempfile.TemporaryDirectory() as folder:
            repo = Path(folder)
            self.git(repo, "init", "-q")
            d = repo / "digests"
            d.mkdir()
            out = d / "2026-09-20.md"
            out.write_text("# Digest\n\n## Nothing new\n", encoding="utf-8")
            # Untracked: it has not been published, so it may be rebuilt freely.
            self.assertFalse(published_and_different(out, "anything else", repo))
            self.git(repo, "add", "-A")
            self.git(repo, "commit", "-q", "-m", "publish")
            # Committed and unchanged: rebuilding to identical text is harmless.
            self.assertFalse(published_and_different(out, "# Digest\n\n## Nothing new\n", repo))
            # Committed and different: that would rewrite history.
            self.assertTrue(published_and_different(out, "# Digest\n\n## 7 new claims\n", repo))
            # The builder itself refuses, and leaves the published bytes alone.
            saved = sota.ROOT
            sota.ROOT = repo
            try:
                claims = [{"id": "CLM-ARCH-0001", "topic": "ARCH", "statement": "x", "grade": "B",
                           "credibility": "unknown", "evidence_type": "simulated", "status": "active",
                           "as_of": "2026-09-17", "sources": []}]
                with self.assertRaises(DigestAlreadyPublished):
                    build_digest(claims, [], {}, digests_dir=d, candidates_dir=repo,
                                 today="2026-09-20")
                self.assertEqual(out.read_text(encoding="utf-8"), "# Digest\n\n## Nothing new\n")
                # A NEW date is fine: yesterday's digest is history, today's is a fresh file.
                path, n = build_digest(claims, [], {}, digests_dir=d, candidates_dir=repo,
                                       today="2026-09-21")
                self.assertEqual((path.name, n), ("2026-09-21.md", 1))
            finally:
                sota.ROOT = saved

    def test_digest_dates_are_utc(self):
        from datetime import datetime, timezone
        from sota import today_utc
        self.assertEqual(today_utc(), datetime.now(timezone.utc).date().isoformat())


if __name__ == "__main__":
    unittest.main(verbosity=1)
