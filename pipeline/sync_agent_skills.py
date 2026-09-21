"""Keep .agents/skills/ an exact mirror of .claude/skills/.

Skills must sit in a tool-specific folder (Claude Code reads .claude/skills/, Codex reads
.agents/skills/), so one shared file is not possible. Two hand-edited copies drift apart, and
that had already happened: the Codex copy of the harvest skill kept saying reading could not be
scripted after the automated reader existed. So there is ONE canonical copy, .claude/skills/, and
this script writes the other. pipeline/test_agent_files.py fails CI when they differ.

Usage:  python pipeline/sync_agent_skills.py           # rewrite the mirror from the canonical copy
        python pipeline/sync_agent_skills.py --check   # report differences, change nothing
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANONICAL = ROOT / ".claude" / "skills"
MIRROR = ROOT / ".agents" / "skills"


def _files(base):
    if not base.is_dir():
        return {}
    return {p.relative_to(base).as_posix(): p for p in sorted(base.rglob("*"))
            if p.is_file() and p.name != ".gitkeep"}


def _content(path):
    return path.read_bytes().replace(b"\r\n", b"\n")      # line endings are git's business


def differences(canonical=CANONICAL, mirror=MIRROR):
    """Human-readable differences between the canonical skills and their mirror; [] when identical."""
    src, dst = _files(canonical), _files(mirror)
    found = []
    for name in sorted(src.keys() - dst.keys()):
        found.append(f"missing from the mirror: {name}")
    for name in sorted(dst.keys() - src.keys()):
        found.append(f"in the mirror but not canonical: {name}")
    for name in sorted(src.keys() & dst.keys()):
        if _content(src[name]) != _content(dst[name]):
            found.append(f"content differs: {name}")
    return found


def sync(canonical=CANONICAL, mirror=MIRROR):
    """Make the mirror identical to the canonical copy. Returns the number of files written."""
    src, dst = _files(canonical), _files(mirror)
    written = 0
    for name, path in src.items():
        target = mirror / name
        data = _content(path)
        if name not in dst or _content(dst[name]) != data:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            written += 1
    for name in dst.keys() - src.keys():
        dst[name].unlink()
        written += 1
    return written


def main(argv):
    if "--check" in argv:
        found = differences()
        for line in found:
            print("  " + line)
        print("OK - .agents/skills matches .claude/skills" if not found else
              "DIFFERENT - run: python pipeline/sync_agent_skills.py")
        return 1 if found else 0
    n = sync()
    print(f"mirror updated: {n} file(s) written")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
