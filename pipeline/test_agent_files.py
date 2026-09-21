"""AGENTS.md is the one copy of the doctrine; CLAUDE.md must stay a thin import of it.

Two copies of the rules drift apart, and drift between our own instructions is a contradiction in
the project's foundation. This was real: a Codex-flavoured copy of the whole doctrine sat beside
CLAUDE.md and went stale the moment CLAUDE.md was corrected.

Usage:  python pipeline/test_agent_files.py
"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import sync_agent_skills  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
MAX_CLAUDE_LINES = 12          # an import plus a pointer. Anything longer is rules leaking in.


class SingleSource(unittest.TestCase):
    def test_agents_md_holds_the_doctrine(self):
        text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("Prime directive", text)
        self.assertIn("The contradiction protocol", text)
        self.assertIn("single source of truth", text)

    def test_claude_md_imports_agents_md(self):
        lines = (ROOT / "CLAUDE.md").read_text(encoding="utf-8").splitlines()
        self.assertIn("@AGENTS.md", [l.strip() for l in lines])

    def test_claude_md_carries_no_rules_of_its_own(self):
        lines = [l for l in (ROOT / "CLAUDE.md").read_text(encoding="utf-8").splitlines() if l.strip()]
        self.assertLessEqual(len(lines), MAX_CLAUDE_LINES,
                             "CLAUDE.md must stay an import. Put rules in AGENTS.md instead.")

    def test_no_other_file_claims_to_be_the_doctrine(self):
        # Doctrine is referenced as AGENTS.md everywhere; a stray CLAUDE.md reference means a
        # comment or skill still points at the wrong file.
        stray = []
        for folder in ("pipeline", "reference", "sources", ".claude/skills"):
            for p in (ROOT / folder).rglob("*"):
                if p.suffix in {".py", ".yaml", ".md"} and p.is_file() and p.name != Path(__file__).name:
                    if "CLAUDE.md" in p.read_text(encoding="utf-8", errors="ignore"):
                        stray.append(str(p.relative_to(ROOT)))
        self.assertEqual(stray, [], "these refer to CLAUDE.md; the doctrine is in AGENTS.md")


class SkillMirror(unittest.TestCase):
    def test_agents_skills_mirror_the_canonical_skills(self):
        self.assertEqual(sync_agent_skills.differences(), [],
                         "run: python pipeline/sync_agent_skills.py")

    def test_the_guard_fires_on_each_kind_of_drift(self):
        # A guard that has never failed is not a guard: build a mirror, then break it three ways.
        with tempfile.TemporaryDirectory() as folder:
            canonical, mirror = Path(folder) / "c", Path(folder) / "m"
            (canonical / "harvest").mkdir(parents=True)
            (canonical / "harvest" / "SKILL.md").write_text("one\n", encoding="utf-8")
            sync_agent_skills.sync(canonical, mirror)
            self.assertEqual(sync_agent_skills.differences(canonical, mirror), [])

            (mirror / "harvest" / "SKILL.md").write_text("edited by hand\n", encoding="utf-8")
            self.assertEqual(len(sync_agent_skills.differences(canonical, mirror)), 1)   # content differs
            sync_agent_skills.sync(canonical, mirror)
            self.assertEqual(sync_agent_skills.differences(canonical, mirror), [])       # and is repaired

            (mirror / "harvest" / "SKILL.md").unlink()
            self.assertIn("missing from the mirror", sync_agent_skills.differences(canonical, mirror)[0])
            sync_agent_skills.sync(canonical, mirror)

            (mirror / "stray").mkdir()
            (mirror / "stray" / "SKILL.md").write_text("x\n", encoding="utf-8")
            self.assertIn("not canonical", sync_agent_skills.differences(canonical, mirror)[0])
            sync_agent_skills.sync(canonical, mirror)
            self.assertEqual(sync_agent_skills.differences(canonical, mirror), [])

    def test_crlf_is_not_drift(self):
        with tempfile.TemporaryDirectory() as folder:
            canonical, mirror = Path(folder) / "c", Path(folder) / "m"
            for base, eol in ((canonical, b"\n"), (mirror, b"\r\n")):
                (base / "s").mkdir(parents=True)
                (base / "s" / "SKILL.md").write_bytes(b"a" + eol + b"b" + eol)
            self.assertEqual(sync_agent_skills.differences(canonical, mirror), [])


if __name__ == "__main__":
    unittest.main(verbosity=1)
