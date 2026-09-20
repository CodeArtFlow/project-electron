"""Live HTTP probe for registry entries that no scholarly API can verify.

Preprint servers, conference sites, vendor technical pages, standards bodies and trade press
have no ISSN and no DOAJ record, so existence and reachability are established by probing.
A probe proves reachability only - it says nothing about OA status or content quality, both of
which remain the harvest step's job.

Candidate URLs here were written from recall; the probe is exactly what converts them from
assumption into evidence. A URL that 404s or redirects somewhere unrelated is not quietly
corrected - it is reported.

Usage:  python pipeline/probe_urls.py
"""

import json
import time
from pathlib import Path

import requests

UA = {"User-Agent": "ProjectElectron/0.1 (semiconductor research agent; verification)"}
TIMEOUT = 30

TARGETS = {
    # preprints
    "techrxiv": "https://www.techrxiv.org/",
    "chemrxiv": "https://chemrxiv.org/",
    "zenodo": "https://zenodo.org/",
    "research_square": "https://www.researchsquare.com/",
    # conferences
    "iedm": "https://www.ieee-iedm.org/",
    "vlsi": "https://www.vlsisymposium.org/",
    "isscc": "https://www.isscc.org/",
    "hotchips": "https://hotchips.org/",
    "isca": "https://iscaconf.org/",
    "micro": "https://microarch.org/",
    "asplos": "https://www.asplos-conference.org/",
    "date": "https://www.date-conference.com/",
    "dac": "https://www.dac.com/",
    "ecs_meet": "https://www.electrochem.org/meetings",
    # institutional
    "imec": "https://www.imec-int.com/en/publications",
    "cea_leti": "https://www.leti-cea.com/cea-tech/leti/english",
    "fraunhofer": "https://www.iisb.fraunhofer.de/en.html",
    "nist": "https://www.nist.gov/publications",
    "hal": "https://hal.science/",
    "cordis": "https://cordis.europa.eu/",
    # standards
    "irds": "https://irds.ieee.org/",
    "jedec": "https://www.jedec.org/standards-documents",
    "ucie": "https://www.uciexpress.org/",
    "cxl": "https://computeexpresslink.org/",
    "ocp": "https://www.opencompute.org/",
    "riscv": "https://riscv.org/technical/specifications/",
    # vendor
    "tsmc": "https://www.tsmc.com/english/dedicatedFoundry/technology",
    "intel": "https://www.intel.com/content/www/us/en/research/publications.html",
    "samsung": "https://semiconductor.samsung.com/foundry/",
    "asml": "https://www.asml.com/en/technology",
    "amat": "https://www.appliedmaterials.com/us/en/blog.html",
    "lam": "https://www.lamresearch.com/",
    "kla": "https://www.kla.com/",
    "micron": "https://www.micron.com/about/blog",
    "sk_hynix": "https://news.skhynix.com/",
    "nvidia": "https://resources.nvidia.com/l/en-us-whitepapers",
    "amd": "https://www.amd.com/en/developer/resources.html",
    # trade press
    "semiengineering": "https://semiengineering.com/",
    "ieee_spectrum": "https://spectrum.ieee.org/",
    "chipsandcheese": "https://chipsandcheese.com/",
    "eetimes": "https://www.eetimes.com/",
    "wikichip": "https://en.wikichip.org/wiki/WikiChip",
    "chipletter": "https://thechipletter.substack.com/",
}


def probe(url):
    try:
        r = requests.get(url, headers=UA, timeout=TIMEOUT, allow_redirects=True)
        return {"status": r.status_code, "final_url": r.url, "bytes": len(r.content)}
    except Exception as e:  # noqa: BLE001
        return {"status": None, "error": f"{type(e).__name__}: {e}"}


def main():
    out = {}
    for key, url in TARGETS.items():
        res = probe(url)
        res["url"] = url
        st = res.get("status")
        ok = st is not None and st < 400
        # A redirect landing on a different host is worth a human look, not a silent pass.
        moved = ""
        if ok and res.get("final_url"):
            from urllib.parse import urlparse
            if urlparse(res["final_url"]).netloc != urlparse(url).netloc:
                moved = f"  -> REDIRECT {urlparse(res['final_url']).netloc}"
        res["verdict"] = "PASS" if ok else "FAIL"
        out[key] = res
        print(f"{res['verdict']:5} {st!s:5} {key:16} {url}{moved}", flush=True)
        time.sleep(0.2)

    Path(__file__).with_name("url_probe_report.json").write_text(
        json.dumps(out, indent=2), encoding="utf-8")
    p = sum(1 for v in out.values() if v["verdict"] == "PASS")
    print(f"\nPASS {p}/{len(out)}")


if __name__ == "__main__":
    main()
