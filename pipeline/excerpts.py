"""Filtered evidence for TypeSafe: the parts of a paper a claim actually rests on, with their context.

WHY. TypeSafe's own documentation says to filter first: it loses accuracy when the state is large and
mostly irrelevant, and a whole paper is nearly all irrelevant to any one claim. Two of the three papers
the reader had read were also longer than its 32k-token window. So a claim is judged against
EXCERPTS: the verified quotes it rests on, each with a window of surrounding text, plus the paper's
opening (title and abstract) and the quotes the reader recorded for its method and limitations.

HOW A QUOTE IS FOUND. The verifier proves a quote is in the paper by comparing fetch_text.normalize()
of both, which deletes all whitespace, so a position in the normalized text is not a position in the
raw text. `locate` maps one to the other by binary search on the length of normalize(raw[:k]). That
uses the verifier's own normalization as a black box, so it can only ever find what the verifier
found. Near a line-break hyphenation the map can be off by a character, which the window absorbs.

WHAT IS NEVER DONE. An excerpt is never trimmed to fit: the windows shrink, in whole steps, and if the
claim's own quotes still do not fit, the result is `too_long` and nothing is sent. What the packet
says TypeSafe saw is exactly what it saw, and every excerpt says where in the paper it came from.
Because these are excerpts, "the paper does not say X" can never be concluded from them. The
questions say so, and the answers file records `coverage: excerpts`.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from fetch_text import normalize  # noqa: E402

OPENING_CHARS = 3000                      # the title and abstract, on the first page
CONTEXT_STEPS = (1500, 800, 300, 0)       # characters of context either side of a quote, widest first
EXCERPT_CHAR_BUDGET = 24_000              # about 8k tokens at 3 characters a token: well inside the 32k window
MIN_QUOTE_CHARS = 12                      # a shorter "quote" is too easy to find by accident


def locate(raw, norm_all, quote):
    """(start, end) in the RAW text of the first place the quote occurs, or None.

    `norm_all` is normalize(raw), passed in so it is computed once per paper. The quote has already
    been verified (it is in norm_all); None means it is not, or it is too short to trust.
    """
    q = normalize(quote)
    if len(q) < MIN_QUOTE_CHARS:
        return None
    p = norm_all.find(q)
    if p < 0:
        return None

    def raw_index(target):
        """Smallest k with len(normalize(raw[:k])) >= target."""
        lo, hi = 0, len(raw)
        while lo < hi:
            mid = (lo + hi) // 2
            if len(normalize(raw[:mid])) >= target:
                hi = mid
            else:
                lo = mid + 1
        return lo

    start = raw_index(p + 1) - 1 if p else 0
    return max(0, start), min(len(raw), raw_index(p + len(q)))


def _widen(raw, start, end, context):
    """Grow a span by `context` characters each side, then out to whitespace so no word is cut."""
    s, e = max(0, start - context), min(len(raw), end + context)
    while s > 0 and not raw[s - 1].isspace():
        s -= 1
    while e < len(raw) and not raw[e].isspace():
        e += 1
    return s, e


def _merge(spans):
    out = []
    for s, e in sorted(spans):
        if out and s <= out[-1][1]:
            out[-1] = (out[-1][0], max(out[-1][1], e))
        else:
            out.append((s, e))
    return out


def quotes_of(field):
    """The quotes in a source record's reported / method_summary / limitations field ("...")."""
    return [q.strip() for q in re.findall(r"“(.+?)”", field or "", flags=re.S) if q.strip()]


def build_excerpts(raw, claim_quotes, extra_quotes=(), budget=EXCERPT_CHAR_BUDGET):
    """Excerpts of `raw` for these claims. Returns (excerpts, info); excerpts is None if it cannot fit.

    claim_quotes  {claim id: [verified quotes]}: what each claim rests on
    extra_quotes  the record's method and limitation quotes: context for every claim, dropped first
                  if space is short

    Each excerpt is {"id", "from", "to", "text"}: its position in the paper's text, in document order.
    info records what happened: which quotes were not found, how many of each claim's quotes were
    located (`located`), the context used, and whether the method and limitation quotes were dropped.
    """
    norm_all = normalize(raw)
    info = {"not_found": [], "located": {}, "context": None, "dropped_extra": False, "chars": 0}

    def spans_for(quotes):
        found = []
        for q in quotes:
            loc = locate(raw, norm_all, q)
            if loc is None:
                info["not_found"].append(q[:80])
            else:
                found.append(loc)
        return found

    core = []
    for cid, quotes in claim_quotes.items():
        found = spans_for(quotes)
        info["located"][cid] = len(found)          # a claim whose quotes were not found has no evidence here
        core += found
    extra = spans_for(extra_quotes) if extra_quotes else []
    opening = [_widen(raw, 0, min(len(raw), OPENING_CHARS), 0)]        # to a word boundary, like every other span

    # A claim's own evidence matters most, so its context is what stays widest. Order of giving way:
    # first the method and limitation quotes, then the context around the claim's own quotes.
    for context in CONTEXT_STEPS:
        for keep_extra in (True, False):
            wide = [_widen(raw, s, e, context) for s, e in core + (extra if keep_extra else [])]
            merged = _merge(opening + wide)
            size = sum(e - s for s, e in merged)
            if size <= budget:
                info.update(context=context, dropped_extra=bool(extra) and not keep_extra, chars=size)
                return [{"id": f"excerpt {i}", "from": s, "to": e, "text": raw[s:e].strip()}
                        for i, (s, e) in enumerate(merged, 1)], info
    info["chars"] = sum(e - s for s, e in _merge(opening + [_widen(raw, s, e, 0) for s, e in core]))
    return None, info
