"""TypeSafe question packets: what a paper's claims rest on, and the typed questions to ask about it.

WHY. The existing TypeSafe audit (semantic_checks.py) judges each claim against our source RECORD, a
summary of the paper. It cannot catch a record that repeats a wrong abstract, and it cannot see words
the extraction added that the paper never wrote ("in BLG"; "acoustic phonon" for the paper's "AP"). A
packet lets TypeSafe judge a claim against EXCERPTS OF THE PAPER ITSELF (excerpts.py). TypeSafe has no
storage (its documented API is one POST that answers only about what it is sent), so what we want kept
is kept here, in git: the packet is the INPUT (corpus/questions/SRC-nnnnn.json), and the answers file
beside it stores the exact questions that were asked and what came back.

WHAT A PACKET HOLDS. Per accepted claim: the verified quotes it rests on (from the reader's own
verifier) and the distinctive terms in its statement that those quotes do not contain. Plus the source's
method and limitation quotes, and the hash of the exact text the reader was given. No paper text.

WHO WRITES THE QUESTIONS. Code, from a fixed, versioned rubric, so the same question is asked of every
claim in every paper (which is what makes answers comparable across papers and fields) and a model
cannot write a leading one. The reading model's contribution is what it already makes: the structured
claims, conditions and verified quotes that the questions are built from.

WHAT IS DELIBERATELY NOT ASKED. Whether a number matches its quote, whether its qualifier ("up to") was
kept, or what a unit converts to. TypeSafe's own documentation says it is weak at numeric precision and
counting, and code already does all of that. (Which unit the excerpts show a value is in IS asked: that
is reading a table header, not arithmetic.) Every question here is yes/no, choice or rating about MEANING. Paper-level
questions (layer, whether the paper reports uncertainty, ...) need the whole paper, not excerpts, and
belong to a later phase of docs/typesafe-plan.md.

TypeSafe's answers are advisory, uncalibrated review signals. Nothing here changes a claim, a grade,
a credibility tier or a conflict.
"""

import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from excerpts import quotes_of  # noqa: E402
from fetch_text import normalize  # noqa: E402
from semantic_checks import RELATION, choice, noul  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PACKET_VERSION = "paper-packet-v2"
RUBRIC_VERSION = "paper-rubric-v2"
MAX_TERMS = 6
MAX_TERM_CHARS = 40
SRC_ID_RE = re.compile(r"^SRC-\d{5}$")
CLAIM_ID_RE = re.compile(r"^CLM-[A-Z]+-\d{4}$")
EVIDENCE_TYPES = ("measured", "simulated", "projected", "announced", "rumored", "mixed", "unknown")
# Said in the state and in the questions: these are parts of the paper, and TypeSafe reads literally.
COVERAGE_NOTE = ("`paper_excerpts` are selected parts of the paper, not all of it, each with its position. "
                 "If they do not establish something, it is not established here; do not assume the paper "
                 "says or does not say it elsewhere.")


def text_sha256(text):
    return hashlib.sha256((text or "").encode("utf-8")).hexdigest()


def packet_path(source_id, root=ROOT):
    return Path(root) / "corpus" / "questions" / f"{source_id}.json"


def answers_path(source_id, root=ROOT):
    return Path(root) / "corpus" / "questions" / f"{source_id}.answers.json"


# ------------------------------------------------------------------------- terms (deterministic)
_TOKEN = re.compile(r"[A-Za-zΑ-Ωα-ωµ][A-Za-z0-9Α-Ωα-ωµ_+/\-]*")
_GREEK = re.compile(r"[Α-Ωα-ωµ]")


def _distinctive(token):
    """Looks like a name, acronym, symbol or identifier, not an ordinary word: a digit, a capital after
    the first letter, or a Greek letter. "consumes" is not; "BLG", "SiO2", "MiX-INT4g16", "Ω1" are."""
    return len(token) >= 2 and bool(re.search(r"\d", token) or re.search(r"[A-ZΑ-Ω]", token[1:]) or _GREEK.search(token))


def distinctive_terms(statement, evidence_texts, skip=()):
    """Distinctive terms in the statement that none of its evidence contains (case-insensitively, after
    the verifier's own normalization). Each is a word the model may have supplied, so each becomes a
    literal question: does the paper establish this term for this subject?

    `skip` is for words asked about some other way: the claim's own unit, which has a question of its own
    (a unit is often in a table header and not in the quoted row, which is a different thing to check).
    """
    have = normalize(" ".join(evidence_texts)).lower()
    skipped = {str(s).strip().lower() for s in skip if s}
    out = []
    for m in _TOKEN.finditer(statement or ""):
        tok = m.group(0).rstrip("-_+/")
        if tok and len(tok) <= MAX_TERM_CHARS and _distinctive(tok) and normalize(tok).lower() not in have \
                and tok.lower() not in skipped and tok not in out:
            out.append(tok)
    return out[:MAX_TERMS]


# ------------------------------------------------------------------------- the rubric (code-owned)
def claim_questions(cid, claim, terms=()):
    """The fixed rubric for one claim, against `paper_excerpts`. Keys are `<cid>.<name>`.

    Built from the CURRENT claim, so a later correction to its conditions cannot leave a stale question.
    """
    ref = f"claims.{cid}"
    q = {
        f"{cid}.support": choice(
            f"How do `paper_excerpts` relate to `{ref}.statement`? Judge only from `paper_excerpts`; do not "
            "fill gaps from the statement. Every scope word in the statement counts: a material, device, "
            "configuration or method it names must be stated for this value. " + COVERAGE_NOTE, RELATION),
        f"{cid}.is_result": noul(
            f"Do `paper_excerpts` show that the value in `{ref}.quantity.as_published` (or, if it has no "
            f"quantity, the assertion in `{ref}.statement`) is a result reported by the authors, as opposed "
            "to an input parameter, an assumed or default value, a baseline, or a value quoted from prior "
            "work? If the excerpts do not show which, answer no. " + COVERAGE_NOTE),
        f"{cid}.evidence_type": choice(
            f"Which evidence type do `paper_excerpts` establish for `{ref}.statement`? Use `unknown` if "
            "they do not say. " + COVERAGE_NOTE, {v: v for v in EVIDENCE_TYPES}),
        f"{cid}.atomic": noul(f"Does `{ref}.statement` contain exactly one independently falsifiable assertion?"),
    }
    if claim.get("quantity"):
        q[f"{cid}.unit"] = noul(
            f"Do `paper_excerpts` show that the unit written in `{ref}.quantity.as_published` is the unit this "
            "value is reported in? A unit that appears only in a table header or caption counts if the "
            "excerpts include that header or caption. " + COVERAGE_NOTE)
    for key in sorted((claim.get("conditions") or {})):
        q[f"{cid}.cond.{key}"] = noul(
            f"Do `paper_excerpts` state that the condition `{ref}.conditions.{key}` (its value) applies to "
            f"the value in `{ref}.statement`? Similar conditions elsewhere in the excerpts do not count. "
            + COVERAGE_NOTE)
    for i, term in enumerate(terms, 1):
        q[f"{cid}.term.{i}"] = noul(
            f'Do `paper_excerpts` establish that the term "{term}" correctly describes the subject of '
            f"`{ref}.statement`? A term that appears in the statement but not in the excerpts is not "
            "established. " + COVERAGE_NOTE)
    return q


def claim_view(claim):
    """What TypeSafe is told about a claim: only these fields. Never ids, sources, grades or notes."""
    q = claim.get("quantity") or {}
    view = {"statement": claim.get("statement"), "evidence_type": claim.get("evidence_type"),
            "conditions": claim.get("conditions") or {}}
    if q:
        ap = q.get("as_published") or {}
        view["quantity"] = {"name": q.get("quantity"), "as_published": f"{ap.get('value')} {ap.get('unit')}",
                            "bound": q.get("bound", "exact"), "approximate": bool(q.get("approximate"))}
    return view


# ------------------------------------------------------------------------- building and checking
def current_terms(entry, claim):
    """The unverified words in the claim's CURRENT statement. Derived at check time from the current claim
    and the packet's verified quotes, so correcting a statement (or its conditions) cannot leave a stale
    term question. The terms stored in the packet are the record of what was true when it was built."""
    unit = ((claim.get("quantity") or {}).get("as_published") or {}).get("unit")
    return distinctive_terms(claim.get("statement") or entry.get("statement"),
                             list(entry["evidence_spans"]) + [str(v) for v in (claim.get("conditions") or {}).values()],
                             skip=[unit])


def build_packet(source, claims, text, spans_by_claim, reader, today):
    """A packet for one source record.

    source          the source record dict (needs id, arxiv_id; method_summary and limitations are read)
    claims          the accepted claim dicts (with ids)
    text            the exact paper text the reader was given (hashed, never stored)
    spans_by_claim  {claim id: [the verified quotes that claim rests on]}
    reader          {"model": ..., "prompt_version": ..., optionally "backfilled": date}
    """
    entries = {}
    for c in claims:
        spans = [s for s in (spans_by_claim or {}).get(c["id"], []) if isinstance(s, str) and s.strip()]
        unit = ((c.get("quantity") or {}).get("as_published") or {}).get("unit")
        entries[c["id"]] = {"statement": c["statement"], "evidence_spans": spans,
                            "terms": distinctive_terms(c["statement"], spans + [str(v) for v in (c.get("conditions") or {}).values()],
                                                       skip=[unit])}
    extra = quotes_of(source.get("method_summary")) + quotes_of(source.get("limitations"))
    return {"packet_version": PACKET_VERSION, "rubric_version": RUBRIC_VERSION, "source": source["id"],
            "arxiv_id": source.get("arxiv_id"), "generated": today, "reader": reader,
            "text_sha256": text_sha256(text), "text_chars": len(text or ""),
            "claims": entries, "extra_quotes": extra}


def validate_packet(p):
    """Problems with a stored packet; [] when it is well formed. Shape only."""
    if not isinstance(p, dict) or p.get("packet_version") != PACKET_VERSION:
        return [f"not a {PACKET_VERSION} packet"]
    problems = []
    if not SRC_ID_RE.match(str(p.get("source", ""))):
        problems.append("source is not SRC-nnnnn")
    if not re.fullmatch(r"[0-9a-f]{64}", str(p.get("text_sha256", ""))):
        problems.append("text_sha256 is not a sha256 hex digest")
    if not isinstance(p.get("text_chars"), int) or p["text_chars"] <= 0:
        problems.append("text_chars must be a positive integer")
    if not all(isinstance(q, str) and q.strip() for q in p.get("extra_quotes") or []):
        problems.append("extra_quotes must be a list of non-empty strings")
    claims = p.get("claims")
    if not isinstance(claims, dict) or not claims:
        return problems + ["claims must be a non-empty mapping"]
    for cid, e in claims.items():
        if not CLAIM_ID_RE.match(cid):
            problems.append(f"bad claim id {cid!r}")
        if not isinstance(e, dict) or not e.get("statement"):
            problems.append(f"{cid}: needs a statement")
            continue
        spans = e.get("evidence_spans")
        if not isinstance(spans, list) or not spans or not all(isinstance(s, str) and s.strip() for s in spans):
            problems.append(f"{cid}: evidence_spans must be a non-empty list of quotes")
        terms = e.get("terms")
        if not isinstance(terms, list) or len(terms) > MAX_TERMS or not all(
                isinstance(t, str) and 0 < len(t) <= MAX_TERM_CHARS and _TOKEN.fullmatch(t) for t in terms):
            problems.append(f"{cid}: terms must be at most {MAX_TERMS} plain tokens")
    return problems


def build_request(packet, claims, excerpts, model, located):
    """The one TypeSafe request for a paper: excerpts and the claims as state, the rubric against them.

    `located` is {claim id: quotes found}: a claim whose quotes were not found in the text has no
    evidence in the excerpts and is not sent.
    """
    sent = {cid: claims[cid] for cid in packet["claims"] if cid in claims and located.get(cid)}
    questions = {}
    for cid, claim in sent.items():
        questions.update(claim_questions(cid, claim, current_terms(packet["claims"][cid], claim)))
    state = {"about_this_state": COVERAGE_NOTE,
             "paper_excerpts": [{"id": e["id"], "position_in_paper": f"characters {e['from']:,} to {e['to']:,}",
                                 "text": e["text"]} for e in excerpts],
             "claims": {cid: claim_view(c) for cid, c in sent.items()}}
    return {"model": model, "state": state, "questions": questions}


def save_packet(packet, root=ROOT):
    path = packet_path(packet["source"], root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(packet, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    return path


def load_packets(root=ROOT):
    folder = Path(root) / "corpus" / "questions"
    out = {}
    for p in sorted(folder.glob("SRC-*.json")) if folder.is_dir() else []:
        if p.name.endswith(".answers.json"):
            continue
        out[p.stem] = json.loads(p.read_text(encoding="utf-8"))
    return out


def backfill(root=ROOT, fetch=None, today=None):
    """Packets for papers the reader read BEFORE packets existed. Returns [(source id, note)].

    The paper is fetched again now, so the packet's text_sha256 is the hash of the text fetched TODAY,
    not of the text the reader was given: recorded on the packet (`reader.backfilled`), and the honest
    limit of a backfill. Nor is the evidence per claim: the reader did not keep it, so every claim of the
    paper is given ALL of the source record's verified quotes. Only automated papers with at least one
    active automated claim get a packet.
    """
    import yaml
    from datetime import datetime, timezone
    if fetch is None:
        from fetch_text import fetch_arxiv as fetch
    today = today or datetime.now(timezone.utc).date().isoformat()
    root = Path(root)
    claims_by_source = {}
    for f in sorted((root / "ledger" / "claims").glob("*.yaml")):
        for c in (yaml.safe_load(f.read_text(encoding="utf-8")) or {}).get("claims", []):
            if c.get("status") in ("active", "challenged", "contested") and (c.get("extraction") or {}).get("method"):
                for sid in c.get("sources", []):
                    claims_by_source.setdefault(sid, []).append(c)
    done = []
    for f in sorted((root / "corpus" / "papers").glob("SRC-*.yaml")):
        src = yaml.safe_load(f.read_text(encoding="utf-8"))
        ext = src.get("extraction") or {}
        if ext.get("method") != "automated-extractive" or packet_path(src["id"], root).exists():
            continue
        claims = claims_by_source.get(src["id"], [])
        quotes = quotes_of(src.get("reported"))
        if not claims or not quotes:
            continue
        got = fetch(src.get("arxiv_id"))
        if not got.ok:
            done.append((src["id"], f"not backfilled: {got.error}"))
            continue
        packet = build_packet(src, claims, got.text, {c["id"]: quotes for c in claims},
                              {"model": ext.get("model"), "prompt_version": ext.get("prompt_version"),
                               "backfilled": today}, today)
        save_packet(packet, root)
        done.append((src["id"], f"backfilled {len(claims)} claim(s); text hashed as fetched {today}"))
    return done


def main(argv):
    if "--backfill" in argv:
        for sid, note in backfill():
            print(f"  {sid}: {note}")
        return 0
    if "--validate" in argv:
        bad = 0
        packets = load_packets()
        for sid, p in packets.items():
            for problem in validate_packet(p):
                bad += 1
                print(f"  {sid}: {problem}")
        print(f"{len(packets)} packet(s), {bad} problem(s)")
        return 1 if bad else 0
    print(__doc__)
    print("  --validate   shape-check every stored packet")
    print("  --backfill   packets for papers read before packets existed (fetches the papers)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
