"""Gap-driven discovery: condense what we have already READ against a question or named gap.

This loop looks inward, never outward. It makes no network calls and fetches nothing. Its entire
universe is the material already in the repository, and within that, only material that has
actually been read:

    EVIDENCE  (may be condensed and cited)   corpus/papers/SRC-*.yaml, ledger/claims/*.yaml
    ROUTING   (never evidence)               corpus/candidates/CAND-*.yaml

Candidates are unread - they carry a title and metadata, nothing else - and AGENTS.md forbids
citing from a title. So a candidate can only ever appear in the output as "read this next", in a
section labelled as not-evidence.

WHY EXTRACTIVE. The condensing engine only ever emits sentences that exist verbatim in the
corpus. It cannot introduce outside information because it has no way to produce text that is
not already there. A generative engine would bring its training knowledge with it, and that is
exactly what this loop must not do. Every finding is still run through `verify()` - true by
construction here, but it is the contract any future engine would have to meet.

THE LOOP (bounded, inverted deep-research):
    1. Decompose the question into sub-queries.
    2. Retrieve unseen passages for each (BM25 over the read corpus only).
    3. Extract the sentences that bear on the query.
    4. Expand each productive query with salient terms from its own evidence, so the next
       iteration reaches connected passages that do not share the question's wording.
    5. Stop when an iteration reads nothing new (converged - the local data is exhausted),
       or when a limit is hit. The stop reason is always recorded, because a loop that stopped
       on its time budget has NOT established that the data is exhausted.

CONDENSING:
    Near-duplicate sentences merge into one finding that keeps every citation - five sources
    stating one fact become one statement with five citations. Sentences merge only if their
    wording is near-identical AND their numbers are identical. "1000 cm2/(V*s)" and
    "100 cm2/(V*s)" overlap almost entirely by token; merging them would hide a contradiction
    inside a condensed finding. Same shape with different numbers is kept apart and reported as
    DIVERGENT, for reconcile to classify. The loop flags; it never adjudicates.

OUTPUT: discoveries/DSC-nnnn.md - a derived working document. Not a claim, not citable. A
finding that should enter the ledger goes through extract-claims from its source record.

Usage:
    python pipeline/discover.py --question "..."
    python pipeline/discover.py --gap CFL-0001
    python pipeline/discover.py --question "..." --dry-run
"""

import argparse
import math
import re
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "corpus" / "papers"
CANDIDATES = ROOT / "corpus" / "candidates"
CLAIMS = ROOT / "ledger" / "claims"
CONFLICTS = ROOT / "ledger" / "conflicts"
DISCOVERIES = ROOT / "discoveries"

# ---------------------------------------------------------------------------------- limits
# Defaults are what a run gets. Ceilings are hard: a value above a ceiling is clamped with a
# warning, so the loop cannot be configured into running away.
DEFAULTS = {"max_iterations": 4, "iteration_seconds": 30, "total_seconds": 120, "breadth": 3}
CEILINGS = {"max_iterations": 6, "iteration_seconds": 60, "total_seconds": 300, "breadth": 6}
PASSAGES_PER_QUERY = 8
MAX_GAPS_PER_RUN = 10       # batch mode (--all-gaps) never processes more than this

# condensing thresholds
MERGE_JACCARD = 0.80        # near-identical wording
DIVERGE_JACCARD = 0.55      # same statement shape
MIN_SHARED_TERMS = 2        # a sentence must share this many content terms with its query
EXPANSION_TERMS = 4

STOPWORDS = set("""
a an and are as at be been being by can could did do does for from had has have how in into is it
its of on or our over such than that the their them then there these they this those through to
under was we were what when where which while who why will with within without would you your
using used use based show shows shown also both each more most other some very via per between
""".split())

NUMBER_RE = re.compile(r"(?<![A-Za-z])[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?")
TOKEN_RE = re.compile(r"[a-z0-9]+(?:\.[0-9]+)?")
SENT_SPLIT_RE = re.compile(r"(?<=[.!?;])\s+|\n+")


class LimitError(ValueError):
    pass


def resolve_limits(**overrides):
    """Apply defaults, clamp to ceilings. Returns (limits, warnings)."""
    limits, warnings = dict(DEFAULTS), []
    for key, value in overrides.items():
        if value is None:
            continue
        if value <= 0:
            raise LimitError(f"{key} must be positive, got {value}")
        if value > CEILINGS[key]:
            warnings.append(f"{key}={value} exceeds the ceiling; clamped to {CEILINGS[key]}")
            value = CEILINGS[key]
        limits[key] = value
    return limits, warnings


# ---------------------------------------------------------------------------------- text
def tokenize(text):
    out = []
    for t in TOKEN_RE.findall((text or "").lower()):
        if t in STOPWORDS or len(t) < 2:
            continue
        if len(t) > 4 and t.endswith("s") and not t.endswith("ss"):
            t = t[:-1]                      # light plural folding: transistors -> transistor
        out.append(t)
    return out


def numbers_in(text):
    return Counter(NUMBER_RE.findall(text or ""))


def sentences(text):
    return [s.strip() for s in SENT_SPLIT_RE.split(text or "") if len(s.strip()) > 12]


def norm_ws(text):
    return " ".join((text or "").split())


def flatten(value, prefix=""):
    """Turn a YAML value into plain text lines, deterministically, so verbatim checks are stable."""
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, (int, float, bool)):
        return str(value)
    if isinstance(value, list):
        return "\n".join(flatten(v) for v in value)
    if isinstance(value, dict):
        return "\n".join(f"{k}: {flatten(v)}" if not isinstance(v, (dict, list))
                         else f"{k}:\n{flatten(v)}" for k, v in value.items())
    return str(value)


# ---------------------------------------------------------------------------------- corpus
@dataclass
class Passage:
    pid: str                 # e.g. SRC-00001:reported  or  CLM-DEV-0001:statement
    doc_id: str              # SRC-00001 / CLM-DEV-0001
    field: str
    text: str
    sources: list            # SRC ids this passage ultimately rests on
    tokens: list = field(default_factory=list)


@dataclass
class Corpus:
    passages: list
    source_meta: dict        # SRC id -> {"authors": [...], "affiliations": [...]}
    candidates: list         # unread; routing only


def load_corpus(papers_dir=PAPERS, claims_dir=CLAIMS, candidates_dir=CANDIDATES):
    passages, source_meta = [], {}

    for p in sorted(Path(papers_dir).glob("SRC-*.yaml")):
        rec = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        sid = rec.get("id") or p.stem
        # An unread or metadata-only record has nothing to condense. Its title alone is not
        # evidence, so it contributes no passages.
        if rec.get("access") in ("metadata_only", None):
            continue
        corr = [a for a in rec.get("authors", []) or [] if a.get("corresponding")] or \
               (rec.get("authors") or [])[:1]
        source_meta[sid] = {
            "authors": [str(a.get("name", "")).strip().lower() for a in corr if a.get("name")],
            "affiliations": [str(a.get("affiliation", "")).strip().lower()
                             for a in corr if a.get("affiliation")],
        }
        for fld in ("reported", "method_summary", "limitations"):
            text = flatten(rec.get(fld))
            if text.strip():
                passages.append(Passage(f"{sid}:{fld}", sid, fld, text, [sid]))

    for p in sorted(Path(claims_dir).glob("*.yaml")):
        doc = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        for c in doc.get("claims", []) or []:
            if c.get("status") in ("retracted", "superseded"):
                continue                     # not citable, so not condensable
            if c.get("statement"):
                passages.append(Passage(f"{c['id']}:statement", c["id"], "statement",
                                        c["statement"], list(c.get("sources", []) or [])))

    candidates = []
    for p in sorted(Path(candidates_dir).glob("CAND-*.yaml")):
        c = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        candidates.append({"id": c.get("id", p.stem), "title": c.get("title") or "",
                           "venue_id": c.get("venue_id"), "doi": c.get("doi"),
                           "arxiv_id": c.get("arxiv_id"),
                           "tokens": tokenize(f"{c.get('title', '')} {c.get('primary_topic', '')}")})

    for ps in passages:
        ps.tokens = tokenize(ps.text)
    return Corpus(passages, source_meta, candidates)


# ---------------------------------------------------------------------------------- retrieval
class BM25:
    def __init__(self, token_lists, k1=1.5, b=0.75):
        self.docs = token_lists
        self.N = len(token_lists)
        self.avgdl = (sum(len(d) for d in token_lists) / self.N) if self.N else 0.0
        self.k1, self.b = k1, b
        self.df = Counter()
        for d in token_lists:
            self.df.update(set(d))
        self.tf = [Counter(d) for d in token_lists]

    def idf(self, term):
        n = self.df.get(term, 0)
        return math.log(1 + (self.N - n + 0.5) / (n + 0.5))

    def score(self, query_tokens, i):
        if not self.N:
            return 0.0
        dl = len(self.docs[i]) or 1
        s = 0.0
        for t in set(query_tokens):
            f = self.tf[i].get(t, 0)
            if f:
                s += self.idf(t) * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * dl / self.avgdl))
        return s

    def top(self, query_tokens, k, exclude=()):
        scored = [(self.score(query_tokens, i), i) for i in range(self.N) if i not in exclude]
        scored = [x for x in scored if x[0] > 0]
        scored.sort(reverse=True)
        return scored[:k]


# ---------------------------------------------------------------------------------- engine
def extract_relevant(query_tokens, passage):
    """Verbatim sentences from one passage that bear on the query."""
    q = set(query_tokens)
    out = []
    for s in sentences(passage.text):
        st = tokenize(s)
        shared = q & set(st)
        if len(shared) >= MIN_SHARED_TERMS or (len(q) <= 2 and shared):
            # quantitative sentences carry most research value; nudge them up
            score = len(shared) + (0.5 if NUMBER_RE.search(s) else 0.0)
            out.append((score, s, st))
    return out


def expansion_terms(evidence, used, n=EXPANSION_TERMS):
    """Salient terms from this query's own evidence. Discovery within the corpus: reaching
    passages connected by the evidence rather than by the question's original wording."""
    weights = Counter()
    for score, _, toks in evidence:
        for t in set(toks):
            if t not in used and not t.replace(".", "").isdigit():
                weights[t] += score
    return [t for t, _ in weights.most_common(n)]


def jaccard(a, b):
    a, b = set(a), set(b)
    return len(a & b) / len(a | b) if a | b else 0.0


# ---------------------------------------------------------------------------------- condensing
@dataclass
class Finding:
    text: str
    tokens: list
    numbers: Counter
    citations: list = field(default_factory=list)     # [(pid, verbatim sentence)]
    score: float = 0.0

    @property
    def doc_ids(self):
        return sorted({pid.split(":")[0] for pid, _ in self.citations})


def condense(items):
    """items: [(score, sentence, tokens, passage)] -> (findings, divergent_pairs)."""
    findings, divergent = [], []
    for score, sent, toks, ps in sorted(items, key=lambda x: -x[0]):
        nums = numbers_in(sent)
        placed = False
        for f in findings:
            j = jaccard(toks, f.tokens)
            if j >= MERGE_JACCARD and nums == f.numbers:
                if (ps.pid, sent) not in f.citations:
                    f.citations.append((ps.pid, sent))
                placed = True
                break
            if j >= DIVERGE_JACCARD and nums and f.numbers and nums != f.numbers:
                divergent.append({"a": (f.citations[0][0], f.text), "b": (ps.pid, sent),
                                  "similarity": round(j, 2)})
        if not placed:
            findings.append(Finding(sent, toks, nums, [(ps.pid, sent)], score))
    return findings, divergent


def independent_groups(src_ids, source_meta):
    """AGENTS.md: independent = no shared corresponding author and no shared lead institution.
    Sources sharing either collapse into one group (union-find)."""
    parent = {s: s for s in src_ids}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    ids = list(src_ids)
    for i, a in enumerate(ids):
        for b in ids[i + 1:]:
            ma, mb = source_meta.get(a, {}), source_meta.get(b, {})
            if set(ma.get("authors", [])) & set(mb.get("authors", [])) or \
               set(ma.get("affiliations", [])) & set(mb.get("affiliations", [])):
                parent[find(a)] = find(b)
    return len({find(s) for s in ids})


def verify(findings, corpus):
    """Every citation must be verbatim in the passage it names. Returns (kept, rejected).

    True by construction for the extractive engine. Kept anyway: it is the contract any future
    engine must meet, and a non-zero rejection count from THIS engine would mean a bug.
    """
    by_pid = {p.pid: norm_ws(p.text) for p in corpus.passages}
    kept, rejected = [], []
    for f in findings:
        bad = [pid for pid, s in f.citations
               if pid not in by_pid or norm_ws(s) not in by_pid[pid]]
        (rejected if bad else kept).append(f)
    return kept, rejected


# ---------------------------------------------------------------------------------- the loop
@dataclass
class Result:
    question: str
    limits: dict
    warnings: list
    stop_reason: str = ""
    iterations: int = 0
    elapsed: float = 0.0
    trace: list = field(default_factory=list)
    findings: list = field(default_factory=list)
    divergent: list = field(default_factory=list)
    rejected: int = 0
    residual: list = field(default_factory=list)
    read_next: list = field(default_factory=list)
    passages_read: int = 0
    corpus_passages: int = 0


def decompose(question):
    parts = [p.strip() for p in re.split(r"\?|;|\band\b|,", question) if len(tokenize(p)) >= 2]
    return parts or [question]


def run_loop(question, corpus, clock=time.monotonic, **limit_overrides):
    limits, warnings = resolve_limits(**limit_overrides)
    res = Result(question, limits, warnings, corpus_passages=len(corpus.passages))
    bm25 = BM25([p.tokens for p in corpus.passages])
    seen = set()
    collected = []
    used_terms = set(tokenize(question))
    queries = [{"text": q, "tokens": tokenize(q), "origin": "question"}
               for q in decompose(question)][:limits["breadth"]]
    answered = set()
    start = clock()

    for it in range(1, limits["max_iterations"] + 1):
        if clock() - start >= limits["total_seconds"]:
            res.stop_reason = "time_budget"
            break
        deadline = min(clock() + limits["iteration_seconds"], start + limits["total_seconds"])
        res.iterations = it
        step = {"iteration": it, "queries": [], "new_passages": 0}
        next_queries = []
        timed_out = False

        for q in queries:
            if clock() >= deadline:
                timed_out = True
                break
            hits = bm25.top(q["tokens"], PASSAGES_PER_QUERY, exclude=seen)
            evidence = []
            for _, i in hits:
                seen.add(i)
                step["new_passages"] += 1
                for score, sent, toks in extract_relevant(q["tokens"], corpus.passages[i]):
                    evidence.append((score, sent, toks))
                    collected.append((score, sent, toks, corpus.passages[i]))
            step["queries"].append({"query": q["text"], "passages": len(hits),
                                    "sentences": len(evidence)})
            if evidence:
                answered.add(q["text"])
                extra = expansion_terms(evidence, used_terms)
                if extra:
                    used_terms.update(extra)
                    next_queries.append({"text": f"{q['text']} + [{' '.join(extra)}]",
                                         "tokens": q["tokens"] + extra, "origin": "expansion"})
            elif q["origin"] == "question":
                res.residual.append(q["text"])

        res.trace.append(step)
        if timed_out:
            # The iteration deadline is capped by the total budget, so a timeout here can mean
            # either limit fired. Report the one that actually bit: they imply the same thing
            # about the data (not exhausted) but point at different knobs.
            res.stop_reason = ("time_budget" if clock() - start >= limits["total_seconds"]
                               else "iteration_timeout")
            break
        if step["new_passages"] == 0:
            res.stop_reason = "converged"
            break
        queries = next_queries[:limits["breadth"]]
        if not queries:
            res.stop_reason = "converged"
            break
    else:
        res.stop_reason = "iteration_cap"

    res.elapsed = round(clock() - start, 3)
    res.passages_read = len(seen)
    findings, res.divergent = condense(collected)
    res.findings, rejected = verify(findings, corpus)
    res.rejected = len(rejected)
    res.residual = sorted(set(res.residual))

    # Routing only: unread candidates whose titles touch the question or its residual gap.
    route_terms = tokenize(question) + [t for r in res.residual for t in tokenize(r)]
    if corpus.candidates and route_terms:
        cb = BM25([c["tokens"] for c in corpus.candidates])
        res.read_next = [corpus.candidates[i] for _, i in cb.top(route_terms, 10)]
    return res


# ---------------------------------------------------------------------------------- output
def next_discovery_id(directory=DISCOVERIES):
    highest = 0
    for p in Path(directory).glob("DSC-*.md"):
        try:
            highest = max(highest, int(p.stem.split("-")[1]))
        except (IndexError, ValueError):
            continue
    return f"DSC-{highest + 1:04d}"


STOP_MEANING = {
    "converged": "an iteration read nothing new - the read corpus has nothing further on this",
    "iteration_cap": "the iteration limit was reached; the corpus was NOT shown to be exhausted",
    "time_budget": "the total time budget ran out; the corpus was NOT shown to be exhausted",
    "iteration_timeout": "an iteration hit its time limit; the corpus was NOT shown to be exhausted",
}


def render(res, did, gap_source, corpus):
    fm = {
        "id": did, "question": res.question, "gap_source": gap_source,
        "created": date.today().isoformat(), "engine": "extractive",
        "limits": res.limits, "stop_reason": res.stop_reason,
        "iterations_run": res.iterations, "elapsed_seconds": res.elapsed,
        "corpus_passages": res.corpus_passages, "passages_read": res.passages_read,
        "findings": len(res.findings), "divergent": len(res.divergent),
        "rejected_by_verifier": res.rejected, "residual_gap": res.residual,
    }
    out = ["---", yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip(), "---", ""]
    out += [f"# Discovery {did}", "", f"**Question:** {res.question}", "",
            "> Derived working document. **Not a claim and not citable.** Every finding below is a",
            "> verbatim sentence from material already read into the corpus. To put a finding in",
            "> the ledger, run `extract-claims` on its source record.", ""]

    out += ["## Condensed findings", ""]
    if not res.findings:
        out += ["_None. The read corpus contains nothing bearing on this question._" if
                res.corpus_passages else
                "_None. The read corpus is empty — no candidate has yet been read into a source "
                "record, so there is nothing to condense._", ""]
    for n, f in enumerate(sorted(res.findings, key=lambda f: (-len(f.citations), -f.score)), 1):
        srcs = sorted({s for pid, _ in f.citations
                       for p in corpus.passages if p.pid == pid for s in p.sources})
        groups = independent_groups(srcs, corpus.source_meta) if srcs else 0
        out.append(f"{n}. “{f.text}”")
        out.append(f"   - cited: {', '.join(pid for pid, _ in f.citations)}")
        out.append(f"   - rests on {len(srcs)} source(s), {groups} independent group(s)"
                   + ("  — independent confirmation" if groups >= 2 else ""))
    out.append("")

    out += ["## Divergent statements — route to `reconcile`", ""]
    if res.divergent:
        out += ["Same statement shape, different numbers. Kept apart rather than merged, because",
                "merging would hide a possible contradiction inside a condensed finding. This loop",
                "does not classify them; `reconcile` does.", ""]
        for d in res.divergent:
            out.append(f"- `{d['a'][0]}`: “{d['a'][1]}”")
            out.append(f"  vs `{d['b'][0]}`: “{d['b'][1]}”  (similarity {d['similarity']})")
        out.append("")
    else:
        out += ["_None found._", ""]

    out += ["## What the read corpus does not contain", ""]
    if res.residual:
        out += ["These parts of the question found no evidence in anything we have read. Each is",
                "a candidate for a named `missing_data` gap — but only once the unread candidates",
                "below have been read, since absence from the READ corpus is not absence from",
                "the field.", ""]
        out += [f"- {r}" for r in res.residual]
    else:
        out += ["_Every part of the question found some evidence._"]
    out.append("")

    out += ["## Unread candidates that may bear on this (NOT evidence)", ""]
    if res.read_next:
        out += ["Matched on title only. Nothing below has been read, and a title is not evidence.",
                "Read these with the `harvest` skill, then re-run this discovery.", ""]
        for c in res.read_next:
            ref = c.get("doi") or c.get("arxiv_id") or ""
            out.append(f"- `{c['id']}` ({c['venue_id']}) {c['title']}" + (f" — {ref}" if ref else ""))
    else:
        out += ["_No unread candidates match._"]
    out.append("")

    out += ["## Loop trace", "",
            f"Stopped: **{res.stop_reason}** — {STOP_MEANING.get(res.stop_reason, '')}.", "",
            f"Limits: {res.limits['max_iterations']} iterations max, "
            f"{res.limits['iteration_seconds']}s per iteration, "
            f"{res.limits['total_seconds']}s total, breadth {res.limits['breadth']}.", ""]
    for w in res.warnings:
        out.append(f"- limit warning: {w}")
    for step in res.trace:
        out.append(f"- iteration {step['iteration']}: {step['new_passages']} new passage(s)")
        for q in step["queries"]:
            out.append(f"  - `{q['query']}` -> {q['passages']} passage(s), "
                       f"{q['sentences']} sentence(s)")
    if res.rejected:
        out += ["", f"**{res.rejected} finding(s) rejected by the verifier** — a citation did not "
                    "appear verbatim in the passage it named. From the extractive engine this is "
                    "a bug and must be investigated."]
    return "\n".join(out) + "\n"


def question_for_gap(gap_id, conflicts_dir=CONFLICTS):
    path = Path(conflicts_dir) / f"{gap_id}.md"
    if not path.exists():
        raise FileNotFoundError(f"no conflict record {gap_id}")
    text = path.read_text(encoding="utf-8")
    fm = yaml.safe_load(text.split("---")[1]) if text.startswith("---") else {}
    q = fm.get("gap") or fm.get("resolution_trigger")
    if not q:
        raise ValueError(f"{gap_id} has no named gap to discover against")
    return q


def main():
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--question")
    src.add_argument("--gap", metavar="CFL-nnnn")
    src.add_argument("--all-gaps", action="store_true",
                     help=f"every live:data-absent conflict, at most {MAX_GAPS_PER_RUN} per run")
    ap.add_argument("--max-iterations", type=int)
    ap.add_argument("--iteration-seconds", type=int)
    ap.add_argument("--total-seconds", type=int)
    ap.add_argument("--breadth", type=int)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    overrides = {"max_iterations": a.max_iterations, "iteration_seconds": a.iteration_seconds,
                 "total_seconds": a.total_seconds, "breadth": a.breadth}

    jobs = []
    if a.question:
        jobs = [(a.question, "question")]
    elif a.gap:
        jobs = [(question_for_gap(a.gap), a.gap)]
    else:
        live = []
        for p in sorted(CONFLICTS.glob("CFL-*.md")):
            t = p.read_text(encoding="utf-8")
            fm = yaml.safe_load(t.split("---")[1]) if t.startswith("---") else {}
            if fm.get("state") == "live:data-absent" and fm.get("gap"):
                live.append((fm["gap"], p.stem))
        if len(live) > MAX_GAPS_PER_RUN:
            print(f"{len(live)} live gaps; processing the first {MAX_GAPS_PER_RUN} (per-run cap)")
        jobs = live[:MAX_GAPS_PER_RUN]
        if not jobs:
            print("no live:data-absent conflicts with a named gap - nothing to discover against")
            return 0

    corpus = load_corpus()
    DISCOVERIES.mkdir(exist_ok=True)
    for question, gap_source in jobs:
        res = run_loop(question, corpus, **overrides)
        did = next_discovery_id()
        for w in res.warnings:
            print(f"warning: {w}")
        print(f"{did}  stop={res.stop_reason}  iterations={res.iterations}  "
              f"read={res.passages_read}/{res.corpus_passages}  findings={len(res.findings)}  "
              f"divergent={len(res.divergent)}  residual={len(res.residual)}  "
              f"read_next={len(res.read_next)}  {res.elapsed}s")
        doc = render(res, did, gap_source, corpus)
        if a.dry_run:
            print(doc)
        else:
            (DISCOVERIES / f"{did}.md").write_text(doc, encoding="utf-8")
            print(f"  -> discoveries/{did}.md")
        if res.rejected:
            print(f"  !! {res.rejected} finding(s) failed verification - extractive engine bug")
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
