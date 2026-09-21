"""AGENTS.md is the one copy of the doctrine; CLAUDE.md must stay a thin import of it.

Two copies of the rules drift apart, and drift between our own instructions is a contradiction in
the project's foundation. This was real: a Codex-flavoured copy of the whole doctrine sat beside
CLAUDE.md and went stale the moment CLAUDE.md was corrected.

Usage:  python pipeline/test_agent_files.py
"""

import sys
import unittest
from pathlib import Path

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


if __name__ == "__main__":
    unittest.main(verbosity=1)
