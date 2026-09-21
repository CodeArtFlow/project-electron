"""The site must BUILD in the situation CI is actually in: with an audit report present.

Found when the full pipeline was first run end to end: build_site.py called json.loads without
importing json, a bug that only fires when run/typesafe-publication.json exists - which it always
does in CI on main, where the deploy job downloads the audit artifact before building. Every
earlier test built the site with no audit on disk, so the crash was invisible until the gate
stopped blocking and the build became reachable.

Usage:  python pipeline/test_build_site.py
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_site  # noqa: E402


def report(policy="advisory", **extra):
    r = {"schema_version": 1, "version": "semantic-v2", "model": "jev-test", "created": "2026-09-21T00:00:00Z",
         "mode": "live", "elapsed_seconds": 1.0, "calls": 1, "complete": True, "policy": policy,
         "scope_coverage": {"candidate_total": 0, "candidate_selected": 0},
         "records": [{"id": "claim:CLM-ARCH-0001", "stage": "extraction", "status": "needs_review",
                      "flags": ["numbers: uncertain"], "required": True,
                      "response": {"answers": {"numbers": {"type": "choice", "choice": "faithful",
                                                           "confidence": 0.57, "probabilities": {}}}}}],
         "status_counts": {"needs_review": 1}, "calibration": "not_calibrated"}
    r.update(extra)
    return r


class Build(unittest.TestCase):
    def build(self, audit):
        saved = build_site.AUDIT_PATH
        with tempfile.TemporaryDirectory() as folder:
            build_site.AUDIT_PATH = Path(folder) / "typesafe-publication.json"
            if audit is not None:
                build_site.AUDIT_PATH.write_text(json.dumps(audit), encoding="utf-8")
            out = Path(folder) / "site"
            try:
                # The gate has its own tests; here the question is whether rendering survives.
                build_site.build(out, skip_gate=True)
                page = (out / "checks.html").read_text(encoding="utf-8")
                index = (out / "index.html").read_text(encoding="utf-8")
            finally:
                build_site.AUDIT_PATH = saved
        return page, index

    def test_the_site_builds_when_an_audit_report_is_present(self):
        page, index = self.build(report())
        self.assertIn("Research checks", page)
        self.assertIn("numbers: uncertain", page)
        self.assertIn("Project Electron", index)

    def test_an_advisory_audit_says_so_on_the_page_that_shows_it(self):
        page, _ = self.build(report("advisory"))
        self.assertIn("Advisory", page)
        self.assertIn("do not block publication", page)

    def test_a_skipped_audit_says_why_it_did_not_run(self):
        page, _ = self.build(report("advisory", mode="preview", complete=False,
                                    skipped_reason="TYPESAFE_API_KEY is not set; the audit did not run"))
        self.assertIn("Not run", page)
        self.assertIn("TYPESAFE_API_KEY", page)

    def test_the_site_builds_with_no_audit_at_all(self):
        page, _ = self.build(None)
        self.assertIn("No current TypeSafe audit", page)


if __name__ == "__main__":
    unittest.main(verbosity=1)
