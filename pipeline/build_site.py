"""Build the static site from the ledger. Derived output only.

The site is a rendering of `digests/`, `sota/` and the open contradictions register. It is never
a source of truth, so this script only ever READS the research artifacts and writes to the output
directory. If the site and the ledger disagree, the ledger is right and the site is stale.

The publication gate runs first and a failure aborts the build. Deploying a site that the gate
rejected would make the gate advisory, and an advisory gate is not a gate.

AGENTS.md requires the open contradictions register to be a permanent top-level page linked from
the front page. That is enforced here structurally: the register page is always generated, always
linked, and the front page shows the live count even when it is zero.

Usage:
    python pipeline/build_site.py [--out _site] [--skip-gate]
"""

import argparse
import json
import re
import shutil
import sys
from datetime import date, datetime
from html import escape
from pathlib import Path

import markdown
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from publication_gate import load_claims, load_conflicts, run_gate  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DIGESTS = ROOT / "digests"
SOTA = ROOT / "sota"
REGISTER = ROOT / "ledger" / "open-contradictions.md"
REGISTRY = ROOT / "sources" / "registry.yaml"
AUDIT_PATH = ROOT / "run" / "typesafe-publication.json"

SITE_TITLE = "Project Electron"
SITE_TAGLINE = "Daily semiconductor research, with its contradictions on the front page"

TOPICS = {
    "MAT": "Materials", "DEV": "Devices", "LITHO": "Lithography",
    "PROC": "Process", "PKG": "Packaging", "MEM": "Memory",
    "ARCH": "Architecture", "PHOT": "Photonics", "EDA": "EDA", "ECON": "Economics",
}

CSS = """
:root {
  --bg: #fbfbfa; --surface: #ffffff; --border: #e3e1dc; --text: #1a1a18;
  --muted: #6b6862; --accent: #7a4a2b; --accent-soft: #f2ebe4;
  --warn-bg: #fdf4e6; --warn-border: #e0b374; --warn-text: #7a4e14;
  --mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
  --sans: ui-sans-serif, -apple-system, "Segoe UI", Inter, Helvetica, Arial, sans-serif;
  --serif: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #14140f; --surface: #1c1c18; --border: #33322c; --text: #eceae4;
    --muted: #9a968c; --accent: #d9a87c; --accent-soft: #2a241d;
    --warn-bg: #2b2114; --warn-border: #7a5a28; --warn-text: #e8c489;
  }
}
:root[data-theme="dark"] {
  --bg: #14140f; --surface: #1c1c18; --border: #33322c; --text: #eceae4;
  --muted: #9a968c; --accent: #d9a87c; --accent-soft: #2a241d;
  --warn-bg: #2b2114; --warn-border: #7a5a28; --warn-text: #e8c489;
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--bg); color: var(--text);
  font-family: var(--sans); line-height: 1.65; font-size: 16px;
  -webkit-font-smoothing: antialiased;
}
.wrap { max-width: 46rem; margin: 0 auto; padding: 0 16px 6rem; }
header.site { border-bottom: 1px solid var(--border); margin-bottom: 2.5rem; }
header.site .wrap { padding-top: 2.5rem; padding-bottom: 1.25rem; }
header.site h1 { font-family: var(--serif); font-size: 1.6rem; margin: 0 0 .25rem; letter-spacing: -.01em; }
header.site h1 a { color: var(--text); text-decoration: none; }
header.site p { margin: 0; color: var(--muted); font-size: .92rem; }
nav.site { margin-top: 1.1rem; display: flex; flex-wrap: wrap; gap: 1.1rem; }
nav.site a { color: var(--muted); text-decoration: none; font-size: .88rem; }
nav.site a:hover, nav.site a[aria-current] { color: var(--accent); }
h2 { font-family: var(--serif); font-size: 1.28rem; margin: 2.5rem 0 .75rem; letter-spacing: -.01em; }
h3 { font-size: 1.02rem; margin: 1.75rem 0 .5rem; }
a { color: var(--accent); }
p { margin: 0 0 1rem; }
code, .mono { font-family: var(--mono); font-size: .86em; }
.card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 10px; padding: 1.1rem 1.25rem; margin-bottom: 1rem;
}
.card h3 { margin-top: 0; }
.meta { color: var(--muted); font-size: .84rem; }
.banner {
  border: 1px solid var(--warn-border); background: var(--warn-bg); color: var(--warn-text);
  border-radius: 10px; padding: 1rem 1.25rem; margin: 0 0 1.5rem;
}
.banner strong { display: block; margin-bottom: .2rem; }
.count { font-family: var(--serif); font-size: 2rem; line-height: 1; }
.pill {
  display: inline-block; font-family: var(--mono); font-size: .74rem;
  padding: .12rem .5rem; border-radius: 999px;
  background: var(--accent-soft); color: var(--accent); border: 1px solid var(--border);
}
.stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(7rem, 1fr)); gap: .75rem; margin: 1rem 0; }
.stat { background: var(--surface); border: 1px solid var(--border); border-radius: 10px; padding: .9rem 1rem; }
.stat .count { display: block; margin-bottom: .15rem; }
.stat .label { color: var(--muted); font-size: .8rem; }
.table-wrap { overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 1rem 0; }
.table-wrap table { margin: 0; }
table { border-collapse: collapse; width: 100%; font-size: .9rem; margin: 1rem 0; }
th, td { text-align: left; padding: .5rem .6rem; border-bottom: 1px solid var(--border); vertical-align: top; }
th { color: var(--muted); font-weight: 600; font-size: .8rem; text-transform: uppercase; letter-spacing: .04em; }
ul.plain { list-style: none; padding: 0; margin: 0; }
ul.plain li { padding: .6rem 0; border-bottom: 1px solid var(--border); }
ul.plain li:last-child { border-bottom: 0; }
blockquote { margin: 1rem 0; padding: .1rem 0 .1rem 1rem; border-left: 3px solid var(--border); color: var(--muted); }
footer.site { border-top: 1px solid var(--border); margin-top: 4rem; }
footer.site .wrap { padding-top: 1.5rem; color: var(--muted); font-size: .84rem; }
.empty { color: var(--muted); font-style: italic; }
.tabs { display: flex; flex-wrap: wrap; gap: .35rem; margin: 1.25rem 0 1.5rem; }
.tabs button {
  font: inherit; font-size: .84rem; cursor: pointer; padding: .35rem .7rem;
  border-radius: 999px; border: 1px solid var(--border); background: var(--surface);
  color: var(--muted);
}
.tabs button[aria-selected="true"] { background: var(--accent-soft); color: var(--accent); border-color: var(--accent); }
.tabs button .n { font-family: var(--mono); font-size: .76em; opacity: .75; margin-left: .35rem; }
.panel[hidden] { display: none; }
.panel h2:first-child { margin-top: 0; }
.timeline { list-style: none; padding: 0; margin: 1rem 0; }
.timeline li { display: grid; grid-template-columns: 4.2rem 1fr; gap: .6rem; padding: .45rem 0; border-bottom: 1px solid var(--border); align-items: baseline; }
.timeline .t { font-family: var(--mono); font-size: .8rem; color: var(--accent); text-align: right; }
.timeline .d { font-size: .88rem; }
.timeline .sub { color: var(--muted); font-size: .8rem; }
.bar { height: 5px; background: var(--accent); border-radius: 3px; margin-top: .3rem; min-width: 2px; }
.badge { font-family: var(--mono); font-size: .72rem; padding: .1rem .42rem; border-radius: 4px; border: 1px solid var(--border); color: var(--muted); }
.badge.ok { color: var(--accent); border-color: var(--accent); }
.badge.wait { color: var(--warn-text); border-color: var(--warn-border); background: var(--warn-bg); }
@media (max-width: 480px) { .wrap { padding-left: 16px; padding-right: 16px; } }
"""


def page(title, body, active="", depth=0):
    up = "../" * depth
    nav = [("Home", "index.html"), ("Digests", "digests/index.html"),
           ("State of the art", "sota/index.html"),
           ("The field", "synthesis.html"),
           ("Open contradictions", "contradictions.html"),
           ("Pipeline run", "run.html"),
           ("Research checks", "checks.html"),
           ("Methodology", "methodology.html")]
    links = "".join(
        f'<a href="{up}{href}"{" aria-current=\'page\'" if label == active else ""}>{label}</a>'
        for label, href in nav)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} — {SITE_TITLE}</title>
<meta name="description" content="{escape(SITE_TAGLINE)}">
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
<header class="site"><div class="wrap">
<h1><a href="{up}index.html">{SITE_TITLE}</a></h1>
<p>{escape(SITE_TAGLINE)}</p>
<nav class="site">{links}</nav>
</div></header>
<main class="wrap">
{body}
</main>
<footer class="site"><div class="wrap">
<p>Every statement here traces to a claim in the ledger. Built {date.today().isoformat()}
from the repository state at that time. The ledger is the source of truth; if this page and the
ledger disagree, this page is stale.</p>
</div></footer>
</body>
</html>
"""


def md(text):
    """Render Markdown, wrapping tables so a wide one scrolls instead of breaking the layout."""
    html = markdown.markdown(text, extensions=["tables", "fenced_code", "toc"])
    return re.sub(r"(<table>.*?</table>)", r'<div class="table-wrap">\1</div>',
                  html, flags=re.S)


def parse_conflicts():
    out = []
    for c in load_conflicts():
        if str(c.get("state", "")).startswith("live:"):
            out.append(c)
    return out


def digest_entries():
    entries = []
    for p in sorted(DIGESTS.glob("*.md"), reverse=True):
        text = p.read_text(encoding="utf-8")
        title = next((l.lstrip("# ").strip() for l in text.splitlines()
                      if l.startswith("# ")), p.stem)
        entries.append({"slug": p.stem, "title": title, "text": text, "path": p})
    return entries


def sota_entries():
    entries = []
    for p in sorted(SOTA.glob("*.md")):
        if p.stem.upper() == "SYNTHESIS":
            continue
        code = p.stem.upper()
        text = p.read_text(encoding="utf-8")
        entries.append({"code": code, "name": TOPICS.get(code, code),
                        "text": text, "path": p})
    # Stack order, not alphabetical: a reader moves down the stack from materials to economics,
    # and TOPICS is declared in that order.
    order = list(TOPICS)
    entries.sort(key=lambda e: order.index(e["code"]) if e["code"] in order else 99)
    return entries


def build(out_dir, skip_gate=False):
    out = Path(out_dir)
    if out.exists():
        shutil.rmtree(out)
    (out / "assets").mkdir(parents=True)
    (out / "digests").mkdir()
    (out / "sota").mkdir()
    (out / "assets" / "style.css").write_text(CSS, encoding="utf-8")

    claims = load_claims()
    live = parse_conflicts()
    digests = digest_entries()
    sotas = sota_entries()

    # ---------------- front page ----------------
    n_live = len(live)
    banner = f"""<div class="banner">
<strong>{n_live} open contradiction{"" if n_live == 1 else "s"}</strong>
Claims the evidence cannot currently settle. Each names the specific data that would resolve it.
<a href="contradictions.html">Read the register</a>.
</div>""" if n_live else """<div class="card">
<h3>No open contradictions</h3>
<p class="meta">Nothing in the ledger is currently in dispute. This section appears on every
page of this site whether or not it is empty &mdash; an empty register is a finding, and a
register that is <em>never</em> non-empty would be a warning sign about our own rigour.</p>
<p><a href="contradictions.html">Open the register</a></p>
</div>"""

    if digests:
        d = digests[0]
        latest = f"""<h2>Latest digest</h2>
<div class="card">
<h3><a href="digests/{escape(d['slug'])}.html">{escape(d['title'])}</a></h3>
<p class="meta">{escape(d['slug'])}</p>
</div>"""
    else:
        latest = """<h2>Latest digest</h2>
<div class="card"><p class="empty">No digests published yet. The harvest stage has not run,
so the corpus is empty and there is nothing to report. This page will say so until that
changes rather than showing placeholder content.</p></div>"""

    tiles = [("Claims", len(claims)), ("Open contradictions", n_live),
             ("Digests", len(digests)), ("Topic reviews", len(sotas))]
    stats = ('<h2>Ledger</h2><div class="stats">'
             + "".join(f'<div class="stat"><span class="count">{v}</span>'
                       f'<span class="label">{escape(k)}</span></div>' for k, v in tiles)
             + "</div>")

    intro = """<p>Project Electron reads new open-access semiconductor literature every day,
reduces it to atomic claims with their measurement conditions, and reconciles those claims
against everything it has previously asserted.</p>
<p>Its organising constraint is that the corpus must never contradict itself. Where a
contradiction survives, it survives only because the evidence to settle it is missing &mdash; and
the missing evidence is named, dated, and shown here rather than smoothed away.</p>"""

    (out / "index.html").write_text(
        page("Home", banner + intro + latest + stats, active="Home"), encoding="utf-8")

    # ---------------- open contradictions register ----------------
    if REGISTER.exists():
        register_html = md(REGISTER.read_text(encoding="utf-8"))
    else:
        register_html = "<p class='empty'>The register has not been generated yet.</p>"
    note = """<p class="meta">This page is generated from the conflict records in
<code>ledger/conflicts/</code>. A contradiction appears here if and only if the data to resolve
it is absent, and that absence is named. Nothing is listed here because we ran out of time to
investigate it &mdash; that state exists, it is called <code>live:unexamined</code>, and it
blocks publication outright.</p>"""
    (out / "contradictions.html").write_text(
        page("Open contradictions", "<h2>Open contradictions</h2>" + note + register_html,
             active="Open contradictions"), encoding="utf-8")

    # ---------------- digests ----------------
    if digests:
        items = "".join(
            f'<li><a href="{escape(d["slug"])}.html">{escape(d["title"])}</a>'
            f'<div class="meta">{escape(d["slug"])}</div></li>' for d in digests)
        body = f'<h2>Digests</h2><ul class="plain">{items}</ul>'
    else:
        body = ('<h2>Digests</h2><p class="empty">None yet. The pipeline has not run a '
                'harvest, so there is nothing to summarise.</p>')
    (out / "digests" / "index.html").write_text(
        page("Digests", body, active="Digests", depth=1), encoding="utf-8")

    for d in digests:
        (out / "digests" / f"{d['slug']}.html").write_text(
            page(d["title"], md(d["text"]), active="Digests", depth=1), encoding="utf-8")

    # ---------------- state of the art: one tab per layer ----------------
    claims_by_topic = {}
    for c in claims.values() if isinstance(claims, dict) else claims:
        if c.get("status") in ("active", "challenged", "contested"):
            claims_by_topic[c.get("topic")] = claims_by_topic.get(c.get("topic"), 0) + 1

    if sotas:
        tabs, panels = [], []
        for i, s in enumerate(sotas):
            n = claims_by_topic.get(s["code"], 0)
            sel = "true" if i == 0 else "false"
            tabs.append(
                f'<button role="tab" aria-selected="{sel}" aria-controls="p-{s["code"]}" '
                f'id="t-{s["code"]}">{escape(s["name"])}<span class="n">{n}</span></button>')
            panels.append(
                f'<div class="panel" role="tabpanel" id="p-{s["code"]}" '
                f'aria-labelledby="t-{s["code"]}"{"" if i == 0 else " hidden"}>'
                f'{md(s["text"])}</div>')
        script = """<script>
(function(){
  var tl=document.querySelector('.tabs');
  if(!tl) return;
  tl.addEventListener('click',function(e){
    var b=e.target.closest('button[role=tab]'); if(!b) return;
    tl.querySelectorAll('button[role=tab]').forEach(function(x){
      x.setAttribute('aria-selected', String(x===b));
      var p=document.getElementById('p-'+x.id.slice(2));
      if(p) p.hidden = (x!==b);
    });
  });
})();
</script>"""
        body = ('<h2>State of the art, by layer</h2>'
                '<p class="meta">One living document per layer of the stack. The number on each '
                'tab is how many claims the ledger holds for that layer &mdash; a zero means '
                'nothing has been read for it yet, not that the layer is quiet.</p>'
                f'<div class="tabs" role="tablist">{"".join(tabs)}</div>'
                f'{"".join(panels)}{script}')
    else:
        listed = "".join(f'<li>{escape(name)} <span class="pill">{code}</span></li>'
                         for code, name in TOPICS.items())
        body = (f'<h2>State of the art</h2><p class="empty">No topic reviews written yet.</p>'
                f'<ul class="plain">{listed}</ul>')
    (out / "sota" / "index.html").write_text(
        page("State of the art", body, active="State of the art", depth=1), encoding="utf-8")

    for s in sotas:
        (out / "sota" / f"{s['code']}.html").write_text(
            page(s["name"], md(s["text"]), active="State of the art", depth=1), encoding="utf-8")

    # ---------------- cross-stack synthesis ----------------
    syn = SOTA / "SYNTHESIS.md"
    syn_html = md(syn.read_text(encoding="utf-8")) if syn.exists() else         "<p class='empty'>Not generated yet.</p>"
    (out / "synthesis.html").write_text(
        page("The field", syn_html, active="The field"), encoding="utf-8")

    # ---------------- pipeline run ----------------
    run_file = ROOT / "run" / "timings.json"
    if run_file.exists():
        import json as _json
        r = _json.loads(run_file.read_text(encoding="utf-8"))
        steps = [s for s in r.get("steps", []) if not s.get("skipped")]
        worst = max([s.get("seconds", 0) for s in steps] or [1]) or 1
        rows = []
        for s in steps:
            secs = s.get("seconds", 0)
            state = ("ok" if s.get("ok") else "wait")
            label = "ok" if s.get("ok") else ("blocked" if s.get("blocked") else "fail")
            rows.append(
                f'<li><span class="t">{secs:.2f}s</span>'
                f'<span class="d"><strong>{escape(s["stage"])}</strong> '
                f'<span class="badge {state}">{label}</span>'
                f'<div class="sub">{escape(s.get("description", ""))} '
                f'&middot; <code>{escape(s.get("command", ""))}</code></div>'
                f'<div class="bar" style="width:{max(2, int(100 * secs / worst))}%"></div>'
                f'</span></li>')
        pend = r.get("pending_reading_stages", [])
        pend_html = ""
        if pend:
            items = "".join(
                f'<li><strong>{escape(p["stage"])}</strong> '
                f'<span class="badge wait">waiting on reading</span>'
                f'<div class="sub">{escape(p["why"])} &middot; skill: '
                f'<code>{escape(p["skill"])}</code></div></li>' for p in pend)
            pend_html = ('<h2>Stages waiting on reading</h2>'
                         '<p class="meta">These require comprehension &mdash; reading a paper, '
                         'classifying a contradiction. A script doing them would be fabricating, '
                         'so the pipeline reports them rather than faking them.</p>'
                         f'<ul class="plain">{items}</ul>')
        before, after = r.get("before", {}), r.get("after", {})
        deltas = "".join(
            f'<tr><td>{escape(k)}</td><td>{before.get(k, 0)}</td><td>{v}</td></tr>'
            for k, v in after.items())
        body = (f'<h2>Pipeline run</h2>'
                f'<p class="meta">{escape(str(r.get("run_started")))} &middot; '
                f'{r.get("total_seconds")}s total across {len(steps)} automatic stage(s). '
                f'Every stage below is deterministic code.</p>'
                f'<ul class="timeline">{"".join(rows)}</ul>'
                f'{pend_html}'
                f'<h2>Corpus before and after</h2>'
                f'<div class="table-wrap"><table><tr><th>Artifact</th><th>Before</th>'
                f'<th>After</th></tr>{deltas}</table></div>')
    else:
        body = '<h2>Pipeline run</h2><p class="empty">No run recorded yet.</p>'
    (out / "run.html").write_text(page("Pipeline run", body, active="Pipeline run"),
                                  encoding="utf-8")

    # ---------------- methodology ----------------
    reg = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    counts = {"true": 0, "review": 0, "false": 0}
    for section, rows in reg.items():
        if not isinstance(rows, list) or section in ("removed", "excluded_paywalled"):
            continue
        for e in rows:
            if isinstance(e, dict):
                v = e.get("verified")
                key = "true" if v is True else "false" if v is False else "review"
                counts[key] += 1

    method = f"""<h2>Methodology</h2>
<p>How to read anything on this site.</p>

<h3>Evidence grades</h3>
<p>Semiconductor discourse mixes measured silicon with marketing at identical rhetorical
confidence. Every claim carries a grade describing <em>what kind of evidence</em> stands behind
it.</p>
<div class="table-wrap"><table>
<tr><th>Grade</th><th>Meaning</th></tr>
<tr><td class="mono">A</td><td>Peer-reviewed measurement with the method disclosed</td></tr>
<tr><td class="mono">B</td><td>Preprint or conference abstract carrying data</td></tr>
<tr><td class="mono">C</td><td>Vendor or foundry technical disclosure containing actual data</td></tr>
<tr><td class="mono">D</td><td>Press release or roadmap slide with no data</td></tr>
<tr><td class="mono">E</td><td>Analyst note, trade journalism, rumour</td></tr>
</table></div>
<p>Grade D and E material is never stated as fact here. It is attributed &mdash; &ldquo;X states
that&hellip;&rdquo; &mdash; and it never overrides a grade A or B claim.</p>

<h3>Source credibility</h3>
<p>Separate from grade. A preprint from a group with a decade of replicated results is not the
same as a preprint from an unknown group, and neither is the same as a peer-reviewed paper.
Credibility can lower confidence in a claim; it can never raise it above what the evidence grade
allows.</p>

<h3>Units</h3>
<p>Every comparison is performed in coherent SI base units. Numbers are displayed in the
convention the field actually uses &mdash; mobility in cm&sup2;/(V&middot;s), pressures in mTorr
&mdash; but the value underneath is SI, and the figure as the source published it is kept
verbatim so any citation can be checked without arithmetic.</p>
<p>Process node names are treated as product names, never as physical dimensions, and are never
compared across foundries.</p>

<h3>Sources</h3>
<p>Open access only. {counts['true']} venues are fully verified, {counts['review']} are reachable
but require a per-article open-access check, and {counts['false']} could not be verified and are
not harvested. Verification is reproducible from the repository, not a one-time judgement.</p>

<h3>When claims conflict</h3>
<p>A contradiction is allowed to persist only when the evidence that would settle it does not
exist or cannot be reached &mdash; and that missing evidence must be named specifically.
&ldquo;The sources disagree&rdquo; is not a reason. &ldquo;No one has measured this on a
production-maturity process&rdquo; is.</p>
<p>Contradictions we have not finished investigating are a different state entirely, and they
block publication rather than appearing here as caveats.</p>
"""
    (out / "methodology.html").write_text(
        page("Methodology", method, active="Methodology"), encoding="utf-8")

    from semantic_checks import render_summary
    audit_path = AUDIT_PATH
    if audit_path.exists():
        audit = json.loads(audit_path.read_text(encoding="utf-8"))
        checks_body = "<h2>Research checks</h2><pre>" + escape(render_summary(audit)) + "</pre>"
    else:
        checks_body = "<h2>Research checks</h2><p>No current TypeSafe audit is available in this build.</p>"
    (out / "checks.html").write_text(
        page("Research checks", checks_body, active="Research checks"), encoding="utf-8")

    (out / ".nojekyll").write_text("", encoding="utf-8")

    return {"claims": len(claims), "live_contradictions": n_live,
            "digests": len(digests), "sota": len(sotas),
            "files": sum(1 for _ in out.rglob("*") if _.is_file())}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "_site"))
    ap.add_argument("--skip-gate", action="store_true",
                    help="build without the publication gate. For local preview only - CI never "
                         "passes this, and a site built this way must not be deployed.")
    args = ap.parse_args()

    if args.skip_gate:
        print("WARNING: publication gate skipped. This build must not be deployed.\n")
    else:
        results, counts = run_gate()
        failed = [r for r in results if not r["passed"]]
        if failed:
            print("publication gate FAILED - refusing to build:\n")
            for r in failed:
                print(f"  [{r['check']}] {r['name']}")
                for problem in r["failures"]:
                    print(f"      - {problem}")
            return 1
        print(f"publication gate passed ({counts['claims']} claims, "
              f"{counts['conflicts']} conflicts, {counts['digests']} digests)")

    stats = build(args.out, skip_gate=args.skip_gate)
    print(f"built {stats['files']} files -> {args.out}")
    print(f"  claims {stats['claims']} | live contradictions {stats['live_contradictions']} "
          f"| digests {stats['digests']} | sota {stats['sota']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
