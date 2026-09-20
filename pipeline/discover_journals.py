"""Resolve candidate journal titles against Crossref + DOAJ before they enter the registry.

Same gate as verify_registry.py, applied to additions. A candidate that cannot be resolved to a
real ISSN is not added, however plausible its name sounds. This exists because the first draft of
the registry contained a venue that does not exist.

Usage:  python pipeline/discover_journals.py
"""

import json
import sys
import time
import urllib.parse
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verify_registry import (  # noqa: E402
    crossref_journal, crossref_activity, doaj_by_issn, PAUSE,
)

CANDIDATES = [
    # Fully OA, high relevance
    "Science Advances", "Physical Review X", "PRX Quantum", "InfoMat", "Small Science",
    "eLight", "PhotoniX", "Opto-Electronic Advances", "Nanophotonics",
    "Journal of Semiconductors", "npj Flexible Electronics", "Microsystems & Nanoengineering",
    "Light: Science & Applications", "Materials Research Letters", "Carbon Energy",
    "IEEE Open Journal of the Solid-State Circuits Society",
    "IEEE Open Journal of Nanotechnology",
    "IEEE Open Journal of Circuits and Systems",
    "ECS Journal of Solid State Science and Technology",
    "APL Machine Learning", "APL Electronic Devices", "Applied Physics Reviews",
    "Nature Reviews Electrical Engineering",
    # Core hybrid venues - per-article OA check, but too central to omit
    "Nature Electronics", "Nature Materials", "Nature Nanotechnology", "Nature Photonics",
    "IEEE Electron Device Letters",
    "IEEE Transactions on Semiconductor Manufacturing",
    "IEEE Transactions on Components, Packaging and Manufacturing Technology",
    "IEEE Transactions on Very Large Scale Integration (VLSI) Systems",
    "IEEE Journal of Solid-State Circuits",
    "IEEE Solid-State Circuits Letters",
    "IEEE Micro",
    "ACS Applied Electronic Materials", "ACS Nano", "Nano Letters",
    "Advanced Electronic Materials", "Advanced Materials", "Advanced Functional Materials",
    "Applied Physics Letters", "Journal of Applied Physics",
    "Japanese Journal of Applied Physics", "Nanotechnology",
    "Solid-State Electronics", "Microelectronic Engineering", "Microelectronics Journal",
    "Journal of Micromechanics and Microengineering",
    "Journal of Vacuum Science & Technology B",
    "Physical Review Applied", "Physical Review B", "Materials Today",
    "Chip",
]


def main():
    out = []
    for title in CANDIDATES:
        cr = crossref_journal(title)
        time.sleep(PAUSE)
        if not cr.get("ok"):
            print(f"NOT_FOUND   {title}   candidates={cr.get('candidates')}", flush=True)
            out.append({"title": title, "found": False, "candidates": cr.get("candidates")})
            continue
        act = crossref_activity(cr["issn"])
        time.sleep(PAUSE)
        doaj = doaj_by_issn(cr["issn"])
        oa = "FULL_OA" if doaj.get("in_doaj") else "hybrid/unknown"
        print(f"{oa:16} {cr['title']:58} {','.join(cr['issn'][:2]):22} "
              f"recent={act.get('recent_works')}", flush=True)
        out.append({"title": title, "found": True, "crossref_title": cr["title"],
                    "issn": cr["issn"], "publisher": cr.get("publisher"),
                    "in_doaj": doaj.get("in_doaj"), "license": doaj.get("license"),
                    "recent_works": act.get("recent_works")})

    Path(__file__).with_name("discovery_report.json").write_text(
        json.dumps(out, indent=2), encoding="utf-8")
    found = sum(1 for o in out if o["found"])
    full_oa = sum(1 for o in out if o.get("in_doaj"))
    print(f"\nresolved {found}/{len(CANDIDATES)}; DOAJ-confirmed full OA: {full_oa}")


if __name__ == "__main__":
    main()
