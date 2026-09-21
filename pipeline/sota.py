"""Stages 5-6: derive the per-layer state of the art, the cross-stack synthesis, and the digest.

Everything here is DERIVED. Not one sentence is composed freehand. AGENTS.md forbids
"connective tissue" prose that quietly introduces unsourced facts, so the safest implementation
is one that structurally cannot: every statement below is either a claim from the ledger, a
count of claims, or a statement about what the ledger does NOT contain.

That is also why there is no `sota` or `digest` skill. A skill would exist to write prose, and
prose is exactly the attack surface. The ledger already holds the assertions; these renderers
arrange them.

  sota      one document per topic code: the standing position, its numbers in display units,
            live contradictions inline, and what is missing
  synthesis the whole field: coverage, evidence quality, contradictions across layers, and an
            explicit statement of what we cannot yet say
  digest    what changed since the previous digest

Usage:
    python pipeline/sota.py --sota --synthesis --digest
"""

import argparse
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import date, datetime, timezone
from pathlib import Path

import yaml

from bounds import scrutiny
from candidates import unread_candidates

ROOT = Path(__file__).resolve().parent.parent
CLAIMS = ROOT / "ledger" / "claims"
CONFLICTS = ROOT / "ledger" / "conflicts"
PAPERS = ROOT / "corpus" / "papers"
CANDIDATES = ROOT / "corpus" / "candidates"
SOTA = ROOT / "sota"
DIGESTS = ROOT / "digests"

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

TOPICS = {
    "MAT": "Materials", "DEV": "Devices", "LITHO": "Lithography", "PROC": "Process",
    "PKG": "Packaging", "MEM": "Memory", "ARCH": "Architecture", "PHOT": "Photonics",
    "EDA": "EDA", "ECON": "Economics",
}
GRADE_RANK = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}


def load_claims():
    out = []
    for p in sorted(CLAIMS.glob("*.yaml")):
        doc = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        out.extend(doc.get("claims", []) or [])
    return [c for c in out if c.get("id")]


def load_conflicts():
    out = []
    for p in sorted(CONFLICTS.glob("CFL-*.md")):
        t = p.read_text(encoding="utf-8")
        if t.startswith("---"):
            fm = yaml.safe_load(t.split("---")[1])
            if isinstance(fm, dict):
                out.append(fm)
    return out


def load_sources():
    return {p.stem: (yaml.safe_load(p.read_text(encoding="utf-8")) or {})
            for p in PAPERS.glob("SRC-*.yaml")}


def qty(c):
    q = c.get("quantity") or {}
    d = q.get("display") or {}
    if d.get("value") is None:
        return None
    v = d["value"]
    txt = f"{v:g}" if isinstance(v, (int, float)) else str(v)
    unit = d.get("unit", "")
    if unit == "dimensionless":
        unit = "\u00d7" if q.get("quantity") == "energy_advantage_ratio" else ""
    # A published bound is rendered as one. "up to 5.3x" must never read as a measured 5.3x.
    prefix = {"upper_bound": "\u2264 ", "lower_bound": "\u2265 "}.get(q.get("bound", "exact"), "")
    if q.get("approximate"):
        prefix += "\u2248"
    return f"{prefix}{txt} {unit}".strip()


def conds(c):
    cd = c.get("conditions") or {}
    return ", ".join(f"{k} {v}" for k, v in cd.items()) if cd else ""


def claim_line(c, conflicts_by_claim):
    bits = [f"**{qty(c)}**" if qty(c) else "", c.get("statement", "")]
    line = " — ".join(b for b in bits if b)
    meta = [f"`{c['id']}`", f"grade {c.get('grade')}", f"credibility {c.get('credibility')}",
            str(c.get("evidence_type")), f"as of {c.get('as_of')}"]
    if conds(c):
        meta.insert(1, conds(c))
    out = [f"- {line}", f"  - {' · '.join(meta)}",
           f"  - sources: {', '.join(c.get('sources', []) or []) or '_none_'}"]
    if c.get("extraction", {}).get("method") == "automated-extractive":
        x = c["extraction"]
        out.append(f"  - \u2699 automated extraction ({x.get('model')}; {x.get('verified_quotes')} "
                   f"quote(s) verified verbatim against the paper)")
    # Derived from the sourced constants at render time and never stored on the claim, so a flag
    # cannot go stale when a definition or a bound is corrected. A prompt to look harder, not a verdict.
    for flag in scrutiny(c):
        out.append(f"  - \u2691 **scrutiny** ({flag['id']}): {flag['message']}")
    flags = conflicts_by_claim.get(c["id"], [])
    if flags:
        out.append(f"  - **live contradiction:** {', '.join(flags)} — see the open register")
    if c.get("status") != "active":
        out.append(f"  - status: **{c.get('status')}**")
    return out


def build_sota(claims, conflicts):
    SOTA.mkdir(exist_ok=True)
    live = [c for c in conflicts if str(c.get("state", "")).startswith("live:")]
    by_claim = defaultdict(list)
    for cf in live:
        for cid in cf.get("claims", []) or []:
            by_claim[cid].append(cf["id"])

    by_topic = defaultdict(list)
    for c in claims:
        by_topic[c.get("topic", "MAT")].append(c)

    written = []
    for code, name in TOPICS.items():
        topic_claims = [c for c in by_topic.get(code, [])
                        if c.get("status") in ("active", "challenged", "contested")]
        superseded = [c for c in by_topic.get(code, []) if c.get("status") == "superseded"]
        lines = [f"# {name} — state of the art", "",
                 f"Topic code `{code}`. Last reviewed {date.today().isoformat()}.", "",
                 "> Derived from the claim ledger. Every statement traces to a claim; nothing "
                 "here is composed freehand.", ""]

        if not topic_claims:
            lines += ["## Current position", "",
                      "_No claims in the ledger for this layer._", "",
                      "This is a statement about our corpus, not about the field. It means "
                      "nothing has been read and extracted for this layer yet — not that the "
                      "field is quiet.", ""]
        else:
            lines += ["## Current position", ""]
            groups = defaultdict(list)
            for c in topic_claims:
                groups[(c.get("quantity") or {}).get("quantity") or "qualitative"].append(c)
            for qname, group in sorted(groups.items()):
                lines += [f"### {qname.replace('_', ' ')}", ""]
                for c in sorted(group, key=lambda x: (GRADE_RANK.get(x.get("grade"), 9),
                                                      str(x.get("as_of")))):
                    lines += claim_line(c, by_claim)
                lines.append("")

            topic_live = [cf for cf in live
                          if any(cid in {c["id"] for c in topic_claims}
                                 for cid in cf.get("claims", []) or [])]
            lines += ["## Live contradictions in this layer", ""]
            if topic_live:
                lines += ["Shown here, not in an appendix: a reader of this page must see the "
                          "disagreement without navigating elsewhere.", ""]
                for cf in topic_live:
                    lines += [f"- `{cf['id']}` — {cf.get('quantity', '')}: "
                              f"{cf.get('gap', '_unexamined; classification pending_')}",
                              f"  - claims: {', '.join(cf.get('claims', []))}",
                              f"  - missing data: `{cf.get('missing_data', 'not yet named')}`"]
                lines.append("")
            else:
                lines += ["_None._", ""]

            if superseded:
                lines += ["## Superseded", "",
                          "Retained for history. Not the current position.", ""]
                for c in superseded:
                    lines.append(f"- `{c['id']}` {c.get('statement', '')[:100]} "
                                 f"(superseded by {c.get('superseded_by')})")
                lines.append("")

        grades = Counter(c.get("grade") for c in topic_claims)
        lines += ["## Evidence base", "",
                  f"- claims: {len(topic_claims)}",
                  f"- grades: {dict(grades) if grades else 'none'}",
                  f"- distinct sources: "
                  f"{len({s for c in topic_claims for s in c.get('sources', []) or []})}", ""]
        path = SOTA / f"{code}.md"
        path.write_text("\n".join(lines), encoding="utf-8")
        written.append(code)
    return written


def build_synthesis(claims, conflicts, sources):
    live = [c for c in conflicts if str(c.get("state", "")).startswith("live:")]
    unexamined = [c for c in live if c.get("state") == "live:unexamined"]
    by_topic = Counter(c.get("topic") for c in claims
                       if c.get("status") in ("active", "challenged", "contested"))
    grades = Counter(c.get("grade") for c in claims)
    etypes = Counter(c.get("evidence_type") for c in claims)
    cands = len(unread_candidates(CANDIDATES))

    covered = [t for t in TOPICS if by_topic.get(t)]
    missing = [t for t in TOPICS if not by_topic.get(t)]

    lines = ["# The field, as our corpus knows it", "",
             f"Generated {date.today().isoformat()} from the claim ledger.", "",
             "> **Read this as a description of our corpus, not of the field.** Every number "
             "below counts what we have read and extracted. A layer with no claims means we "
             "have not read anything for it — never that nothing is happening there.", "",
             "## Coverage", "",
             "| Layer | Claims | Read |", "|---|---|---|"]
    for code, name in TOPICS.items():
        n = by_topic.get(code, 0)
        lines.append(f"| {name} (`{code}`) | {n} | {'yes' if n else '**nothing yet**'} |")
    lines += ["",
              f"{len(covered)} of {len(TOPICS)} layers have any claim at all. "
              f"{len(sources)} source record(s) read; {cands} candidate(s) queued unread.", ""]

    lines += ["## Evidence quality", "", "| Grade | Claims |", "|---|---|"]
    for g in ("A", "B", "C", "D", "E"):
        lines.append(f"| {g} | {grades.get(g, 0)} |")
    lines += ["", "| Evidence type | Claims |", "|---|---|"]
    for k, v in etypes.most_common():
        lines.append(f"| {k} | {v} |")
    lines.append("")

    lines += ["## Where the corpus disagrees with itself", ""]
    if unexamined:
        lines += [f"**{len(unexamined)} conflict(s) are unexamined.** Reconciliation is "
                  "unfinished, so the picture below is provisional and publication is blocked.",
                  ""]
    absent = [c for c in live if c.get("state") == "live:data-absent"]
    if absent:
        lines += ["These survive because the evidence to settle them is missing, and the missing "
                  "evidence is named:", ""]
        for cf in absent:
            lines.append(f"- `{cf['id']}` ({cf.get('quantity', '')}): {cf.get('gap', '')} "
                         f"— `{cf.get('missing_data')}`")
        lines.append("")
    elif not unexamined:
        lines += ["No live contradictions. With a corpus this small that is unremarkable: "
                  "contradictions need overlapping claims, and there are few claims to overlap.",
                  ""]

    lines += ["## What we cannot yet say", ""]
    if missing:
        lines += [f"- Nothing about **{', '.join(TOPICS[m] for m in missing)}** — no claims "
                  "extracted for those layers.", ""]
    if cands:
        lines += [f"- {cands} candidate(s) sit unread. Until they are read, absence of a claim "
                  "here is absence of reading, not absence of evidence.", ""]
    lines += ["- Nothing about any paper with no legal open-access copy. That exclusion is a "
              "property of our access policy, and it is tracked as `access-blocked`.", ""]

    (ROOT / "sota" / "SYNTHESIS.md").write_text("\n".join(lines), encoding="utf-8")
    return len(covered), len(missing)


DIGEST_CORRECTIONS = ROOT / "ledger" / "digest-corrections.yaml"


def today_utc():
    """The date used for digests: UTC, never the machine's local date.

    CI runs in UTC and a developer's machine does not. On 2026-09-20 local time it was already
    2026-09-21 in CI, so the same pipeline would have dated a digest differently depending on where
    it ran, and a local run could have collided with (or rewritten) the digest CI produced.
    """
    return datetime.now(timezone.utc).date().isoformat()


class DigestAlreadyPublished(Exception):
    """The digest for this date is already committed, and rebuilding it would change it."""


def published_and_different(path, content, root=ROOT):
    """True if `path` is tracked by git (so it is OUT) and `content` would change it.

    A committed digest has been published: CI deploys main. AGENTS.md says errors in a published
    digest are corrected in the NEXT digest with a dated note, never by rewriting it. The builder
    used to overwrite whatever was on disk. Outside a git checkout, or for a path outside `root`
    (tests use temp directories), nothing counts as published.
    """
    try:
        rel = Path(path).resolve().relative_to(Path(root).resolve()).as_posix()
        tracked = subprocess.run(["git", "ls-files", "--error-unmatch", rel], cwd=root,
                                 capture_output=True).returncode == 0
        if not tracked:
            return False
        committed = subprocess.run(["git", "show", "HEAD:" + rel], cwd=root, capture_output=True,
                                   text=True, encoding="utf-8").stdout
    except (ValueError, OSError):
        return False
    return committed.replace("\r\n", "\n").strip() != content.replace("\r\n", "\n").strip()


def _digest_date(path):
    return path.stem            # digests are named YYYY-MM-DD.md, which sorts as a date


def collect_corrections(claims, since, digest_corrections_file=DIGEST_CORRECTIONS):
    """Corrections a reader has not yet been told about: dated after the previous digest.

    Two kinds. A claim that changed AFTER it was published (`public: true`), and a digest that
    itself was wrong. Both are stated plainly rather than edited away.
    """
    out = []
    for c in claims:
        for corr in c.get("corrections", []) or []:
            if corr.get("public") is True and (since is None or str(corr["date"]) > since):
                fields = ", ".join(corr.get("fields", []) or []) or "see reason"
                out.append((str(corr["date"]), f"`{c['id']}` corrected ({fields}): {corr['reason']}"))
    try:
        doc = yaml.safe_load(Path(digest_corrections_file).read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError):
        doc = {}
    for corr in doc.get("corrections", []) or []:
        if since is None or str(corr.get("date")) > since:
            out.append((str(corr["date"]),
                        f"Digest {corr.get('digest')}: {corr.get('text')}"))
    return [text for _, text in sorted(out)]


def build_digest(claims, conflicts, sources, digests_dir=None, candidates_dir=None, today=None,
                 digest_corrections_file=DIGEST_CORRECTIONS):
    digests_dir = Path(digests_dir or DIGESTS)
    candidates_dir = Path(candidates_dir or CANDIDATES)
    digests_dir.mkdir(exist_ok=True)
    today = today or today_utc()

    # PREVIOUS digests only: strictly before today. An earlier version read every file in the
    # directory, so a second run on the same day counted today's own digest as history, saw every
    # claim as "already reported", and overwrote the digest with "Nothing new" - the live
    # 2026-09-20 digest said nothing was new while the ledger held seven claims. Excluding
    # today's file makes a same-day rebuild produce the same digest, so it is idempotent.
    prior = sorted(p for p in digests_dir.glob("*.md") if _digest_date(p) < today)
    since = _digest_date(prior[-1]) if prior else None
    seen_ids = set()
    for p in prior:
        seen_ids |= set(re.findall(r"\bCLM-[A-Z]+-\d{4}\b", p.read_text(encoding="utf-8")))

    new_claims = [c for c in claims if c["id"] not in seen_ids]
    live = [c for c in conflicts if str(c.get("state", "")).startswith("live:")]
    unexamined = [c for c in live if c.get("state") == "live:unexamined"]
    by_claim = defaultdict(list)
    for cf in live:
        for cid in cf.get("claims", []) or []:
            by_claim[cid].append(cf["id"])

    lines = [f"# Digest \u2014 {today}", "",
             "> Every claim below is in the ledger. Nothing is asserted here that is not.", ""]

    # Corrections come first: a reader should learn what we got wrong before what is new.
    corrections = collect_corrections(claims, since, digest_corrections_file)
    lines += ["## Corrections", ""]
    if corrections:
        lines += ["Errors in what we previously published, stated plainly and not edited away.", ""]
        lines += [f"- {text}" for text in corrections]
    else:
        lines += ["_None since the previous digest._"]
    lines.append("")

    if not new_claims:
        lines += ["## Nothing new", "",
                  "No claims were added since the previous digest. Reporting that plainly is "
                  "the point: a padded digest is how low-grade material enters the ledger.", ""]
    else:
        lines += [f"## {len(new_claims)} new claim(s)", ""]
        by_topic = defaultdict(list)
        for c in new_claims:
            by_topic[c.get("topic", "MAT")].append(c)
        for code, group in sorted(by_topic.items()):
            lines += [f"### {TOPICS.get(code, code)}", ""]
            for c in sorted(group, key=lambda x: GRADE_RANK.get(x.get("grade"), 9)):
                lines += claim_line(c, by_claim)
            lines.append("")

    lines += ["## Open contradictions", ""]
    if unexamined:
        lines += [f"**{len(unexamined)} unexamined.** Reconciliation is unfinished; these block "
                  "publication until classified.", ""]
        for cf in unexamined:
            lines.append(f"- `{cf['id']}` \u2014 {', '.join(cf.get('claims', []))}")
        lines.append("")
    absent = [c for c in live if c.get("state") == "live:data-absent"]
    if absent:
        for cf in absent:
            lines.append(f"- `{cf['id']}` ({cf.get('quantity', '')}): {cf.get('gap', '')} "
                         f"\u2014 missing: `{cf.get('missing_data')}`")
        lines.append("")
    if not live:
        lines += ["_None._ An empty section here is a finding, not an omission.", ""]

    unread = len(unread_candidates(candidates_dir))
    lines += ["## Corpus", "",
              f"- source records read: {len(sources)}",
              f"- claims in ledger: {len(claims)}",
              f"- candidates queued unread: {unread}", ""]

    path = digests_dir / f"{today}.md"
    content = "\n".join(lines)
    if published_and_different(path, content, ROOT):
        raise DigestAlreadyPublished(str(path))
    path.write_text(content, encoding="utf-8")
    return path, len(new_claims)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sota", action="store_true")
    ap.add_argument("--synthesis", action="store_true")
    ap.add_argument("--digest", action="store_true")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    if not any((a.sota, a.synthesis, a.digest, a.all)):
        ap.print_help()
        return 0

    claims, conflicts, sources = load_claims(), load_conflicts(), load_sources()
    if a.sota or a.all:
        written = build_sota(claims, conflicts)
        print(f"sota: {len(written)} topic document(s) -> sota/")
    if a.synthesis or a.all:
        covered, missing = build_synthesis(claims, conflicts, sources)
        print(f"synthesis: {covered} layer(s) with claims, {missing} with none -> sota/SYNTHESIS.md")
    if a.digest or a.all:
        try:
            path, n = build_digest(claims, conflicts, sources)
            print(f"digest: {n} new claim(s) -> {path.relative_to(ROOT)}")
        except DigestAlreadyPublished as exc:
            # Not an error: today's digest is out and is left alone. Anything added since then is
            # picked up by the next digest, which lists every claim no earlier digest has cited.
            print(f"digest: {Path(str(exc)).name} is already published and would change; left "
                  f"untouched. New claims will appear in the next digest.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
