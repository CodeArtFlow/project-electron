"""Deterministic text retrieval for the reader. No model, no judgement, no guessing.

Everything the reader records about WHAT WAS READ comes from here, not from a model. A source
record's `access` field says what was actually read, and the only honest way to set it is from
what was actually retrieved: this module fetches the paper, counts what came back, and decides
`full_text` or `unreadable` by rule. A model never gets to claim it read something.

Two properties matter.

  1. Only arXiv, and only by ID. The URL is built from a validated arXiv identifier, never taken
     from a candidate's stored `url`, so a candidate file cannot steer this at an arbitrary host.
     (Publisher pages were measured at 25% fetchable and mostly bot-walled; that lane needs a
     legitimate route first, see AGENTS.md.)

  2. `normalize()` defines what "verbatim" means. PDF text extraction mangles spacing
     ("approximately5x at"), hyphenates across lines ("conven- tional"), and swaps minus signs and
     superscripts. A quote is accepted if it matches the paper AFTER both sides are normalised the
     same way, so the check survives extraction damage but still catches any changed word or
     digit. It is deliberately not fuzzy: no edit distance, no "close enough".
"""

import io
import logging
import re
import time
import unicodedata
import warnings
from dataclasses import dataclass, field

import requests

UA = {"User-Agent": "ProjectElectron/0.1 (semiconductor research agent; reader; open-access only)"}
MIN_FULL_TEXT_CHARS = 8000
MIN_FULL_TEXT_PAGES = 3
ARXIV_DELAY_SECONDS = 3.0        # arXiv's API guidance asks for no more than one request per 3 s
TIMEOUT = 60

# pypdf logs a warning per unparsed font; the numbers that matter are checked by the verifier,
# not by reading that log.
logging.getLogger("pypdf").setLevel(logging.ERROR)
warnings.filterwarnings("ignore", module="pypdf")

ARXIV_ID_RE = re.compile(r"^(?:\d{4}\.\d{4,5}|[a-z\-]+(?:\.[A-Z]{2})?/\d{7})(?:v\d+)?$")

_DASHES = dict.fromkeys(map(ord, "‐‑‒–—―−"), "-")


def normalize(text):
    """The canonical form used to decide whether a quote appears in a paper.

    NFKC folds superscripts, ligatures and width variants ("10⁻²⁶" -> "10-26"); every
    dash-like character becomes "-"; soft hyphens go; a hyphen followed by whitespace between
    letters is line-break hyphenation and is removed; then ALL whitespace is dropped, because PDF
    extraction adds and loses spaces arbitrarily. Both the paper and the quote pass through this
    same function, so it can only ever make two strings equal if they carry the same characters.
    """
    s = unicodedata.normalize("NFKC", text or "")
    s = s.translate(_DASHES).replace("­", "")
    s = re.sub(r"(?<=\w)-\s+(?=\w)", "", s)
    return re.sub(r"\s+", "", s)


@dataclass
class FetchResult:
    ok: bool
    text: str = ""
    chars: int = 0
    pages: int = 0
    url: str = ""
    access: str = "unreadable"            # full_text | unreadable - set here, never by a model
    error: str = ""
    transient: bool = False               # True: worth retrying later (network, 429, 5xx)
    notes: list = field(default_factory=list)


def extract_pdf_text(content):
    from pypdf import PdfReader
    reader = PdfReader(io.BytesIO(content))
    pages = [(p.extract_text() or "") for p in reader.pages]
    return "\n".join(pages), len(pages)


def classify_access(chars, pages):
    """`full_text` only when a real paper came back. Anything thinner is not 'read'."""
    return "full_text" if chars >= MIN_FULL_TEXT_CHARS and pages >= MIN_FULL_TEXT_PAGES else "unreadable"


def fetch_arxiv(arxiv_id, get=requests.get, sleep=time.sleep, attempts=3):
    """Fetch an arXiv paper's PDF and return its text. Never raises: failure is a FetchResult."""
    if not isinstance(arxiv_id, str) or not ARXIV_ID_RE.match(arxiv_id):
        return FetchResult(False, error=f"not a valid arXiv id: {arxiv_id!r}")
    url = f"https://arxiv.org/pdf/{arxiv_id}"
    delay, last, transient = 2.0, "", False
    for attempt in range(attempts):
        try:
            r = get(url, headers=UA, timeout=TIMEOUT, allow_redirects=True)
        except requests.RequestException as e:
            last, transient = type(e).__name__, True
            sleep(delay)
            delay *= 2
            continue
        if r.status_code == 200:
            head = r.content[:5]
            if head != b"%PDF-":
                return FetchResult(False, url=url, error="response was not a PDF")
            try:
                text, pages = extract_pdf_text(r.content)
            except Exception as e:  # noqa: BLE001 - a corrupt PDF is a result, not a crash
                return FetchResult(False, url=url, error=f"PDF could not be parsed: {type(e).__name__}")
            access = classify_access(len(text), pages)
            return FetchResult(access == "full_text", text=text, chars=len(text), pages=pages,
                               url=url, access=access,
                               error="" if access == "full_text" else
                               f"only {len(text)} characters over {pages} page(s) came back")
        last = f"HTTP {r.status_code}"
        if r.status_code in (429, 500, 502, 503, 504):
            transient = True
            sleep(delay)
            delay *= 2
            continue
        transient = False              # a 404 will not get better by asking again
        break
    return FetchResult(False, url=url, error=f"{last} after {attempts} attempt(s)", transient=transient)
