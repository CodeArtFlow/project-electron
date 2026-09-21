"""Which candidates still need reading.

A candidate is UNREAD until something has read it and either turned it into a source record (the
candidate file is then deleted) or recorded a decision on it (`read_decision`). A candidate the
reader judged out of scope, unreadable or too long stays on disk, because deleting it would let the
next sweep re-harvest it, but it is no longer "unread" and must not inflate the queue count or be
offered for reading again.
"""

from pathlib import Path

import yaml


def load(path):
    try:
        return yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError):
        return {}


def is_unread(doc):
    return not doc.get("read_decision")


def unread_candidates(directory):
    """Paths of candidates with no read_decision, in filename order."""
    return [p for p in sorted(Path(directory).glob("CAND-*.yaml")) if is_unread(load(p))]


def decided_candidates(directory):
    return [p for p in sorted(Path(directory).glob("CAND-*.yaml")) if not is_unread(load(p))]
