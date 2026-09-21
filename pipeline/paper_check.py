"""Check a paper's extracted claims against EXCERPTS OF THE PAPER ITSELF, with TypeSafe. Advisory only.

The existing audit (semantic_checks.py) judges a claim against our source RECORD, a summary of the
paper, so it cannot see a record that repeats a wrong abstract or words the extraction added that the
paper never wrote. This sends TypeSafe the parts of the paper each claim rests on (excerpts.py) with the
claims and the rubric derived from the packet the reader stored (question_packets.py). One request per
paper: TypeSafe evaluates every question against the state in parallel, at a documented $0.042 per
million input tokens, so a paper costs well under a tenth of a cent.

TypeSafe stores nothing. The answers are written beside the packet as
corpus/questions/SRC-nnnnn.answers.json, in git, together with the EXACT questions asked. They are
uncalibrated review signals, not verification. This never changes a claim, a grade, a credibility tier
or a conflict.

  * the paper is re-fetched and its hash compared with the one recorded; a paper that has changed is
    recorded `stale` and NOT sent;
  * every excerpt is the paper's own text and says where it came from. Excerpts are never trimmed to
    fit: if a claim's own evidence does not fit, the paper is recorded `too_long` and NOT sent;
  * a claim whose quotes cannot be found in the text is not sent, and is recorded as `unlocated`;
  * because these are excerpts, an answer never means "the paper says nothing about X". The answers
    file records `coverage: excerpts`;
  * a transport failure is not recorded, so a later run retries it; a missing key is a visible skip.

Usage:
    python pipeline/paper_check.py                    # preview: sizes and status, no calls, no writes
    python pipeline/paper_check.py --live             # needs TYPESAFE_API_KEY
    python pipeline/paper_check.py --validate         # shape-check the stored packets and answers
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from assess_quality import MODEL, encoded, evaluate  # noqa: E402
from excerpts import build_excerpts  # noqa: E402
from fetch_text import fetch_arxiv  # noqa: E402
from question_packets import (RUBRIC_VERSION, answers_path, build_request, load_packets,  # noqa: E402
                              text_sha256, validate_packet)

ROOT = Path(__file__).resolve().parent.parent
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

ANSWERS_VERSION = "paper-answers-v2"
DEFAULTS = {"max_papers": 10, "seconds": 240}
CEILINGS = {"max_papers": 25, "seconds": 600}
TERMINAL = ("checked", "stale", "too_long", "unlocated")
# Documented price (docs.typesafe.ai/models, read 2026-09-21): $42 per billion input tokens, output free.
PRICE_PER_MTOK = 0.042
LEAN = 0.5            # a provisional cut: below this the model leans against a yes/no statement. Uncalibrated.
NOTE = ("Advisory, uncalibrated. Judged against excerpts of the paper's own text, by a model: a prompt for a "
        "human look, not verification. Excerpts are parts of the paper, so no answer means the paper is "
        "silent elsewhere. No claim, grade, credibility tier or conflict was changed.")


def today_utc():
    return datetime.now(timezone.utc).date().isoformat()


def load_claims(root):
    claims = {}
    for f in sorted((Path(root) / "ledger" / "claims").glob("*.yaml")):
        for c in (yaml.safe_load(f.read_text(encoding="utf-8")) or {}).get("claims", []):
            if c.get("status") in ("active", "challenged", "contested"):
                claims[c["id"]] = c
    return claims


def _noul(answers, key):
    a = answers.get(key)
    return a["noul"] if a else None


def _choice(answers, key):
    a = answers.get(key)
    return a["choice"] if a else None


def flags_for(answers, packet_claims, ledger_claims):
    """Per claim, the reasons the answers say it needs a human look. Provisional cuts only.

    Every reason is worded about the EXCERPTS, never "the paper": an excerpt not establishing something is
    a reason to look, not a finding that the paper lacks it."""
    flags = {}
    for cid, entry in packet_claims.items():
        if not any(k.startswith(f"{cid}.") for k in answers):
            continue                                                  # this claim was not sent
        claim, out = ledger_claims.get(cid) or {}, []
        s = _choice(answers, f"{cid}.support")
        if s not in (None, "supports"):
            out.append(f"the excerpts do not clearly support the statement (support: {s})")
        p = _noul(answers, f"{cid}.is_result")
        if p is not None and p < LEAN:
            out.append(f"the excerpts do not show the value is a reported result rather than an input, "
                       f"assumed or baseline value (p={p:.2f})")
        p = _noul(answers, f"{cid}.unit")
        if p is not None and p < LEAN:
            out.append(f"the excerpts do not show the unit is the unit of this value (p={p:.2f})")
        et = _choice(answers, f"{cid}.evidence_type")
        if et and claim.get("evidence_type") and et not in (claim["evidence_type"], "unknown"):
            out.append(f"the excerpts suggest {et} evidence, the claim says {claim['evidence_type']}")
        p = _noul(answers, f"{cid}.atomic")
        if p is not None and p < LEAN:
            out.append(f"the statement may assert more than one thing (p={p:.2f})")
        for key in sorted(k for k in answers if k.startswith(f"{cid}.cond.")):
            if answers[key]["noul"] < LEAN:
                out.append(f"condition {key.split('.cond.', 1)[1]} is not established by the excerpts "
                           f"(p={answers[key]['noul']:.2f})")
        for key in sorted(k for k in answers if k.startswith(f"{cid}.term.")):
            n = int(key.rsplit(".", 1)[1])
            terms = entry.get("terms") or []
            if answers[key]["noul"] < LEAN and n <= len(terms):
                out.append(f'the term "{terms[n - 1]}" is not established for this subject by the excerpts '
                           f"(p={answers[key]['noul']:.2f})")
        flags[cid] = out
    return flags


def prepare(root, sid, packet, fetch, ledger_claims):
    """(status, request or None, detail, info) for one packet: fetch, verify, cut, and decide if it may be sent."""
    got = fetch(packet.get("arxiv_id"))
    if not got.ok:
        return "error", None, got.error or "the paper could not be fetched", {}
    if text_sha256(got.text) != packet["text_sha256"]:
        return "stale", None, (f"the paper's text is not the text the packet hashed (now {got.chars:,} "
                               f"characters, then {packet['text_chars']:,}); not sent"), {}
    live = {cid: e for cid, e in packet["claims"].items() if cid in ledger_claims}
    if not live:
        return "no_claims", None, "none of the packet's claims is in the ledger any more", {}
    excerpts, info = build_excerpts(got.text, {cid: e["evidence_spans"] for cid, e in live.items()},
                                    packet.get("extra_quotes") or [])
    if excerpts is None:
        return "too_long", None, (f"the claims' own evidence needs {info['chars']:,} characters even with no "
                                  f"context, over the budget; not sent and not cut"), info
    if not any(info["located"].get(cid) for cid in live):
        return "unlocated", None, "no claim's quotes could be found in the text; not sent", info
    request = build_request(packet, ledger_claims, excerpts, MODEL, info["located"])
    return "ready", request, "", {**info, "excerpts": [{"id": e["id"], "from": e["from"], "to": e["to"],
                                                         "chars": e["to"] - e["from"]} for e in excerpts]}


def check_one(root, sid, packet, ledger_claims, fetch, call, key, live, today):
    """One paper. Returns (answers_doc or None, usage or None, note). None means: record nothing."""
    status, request, detail, info = prepare(root, sid, packet, fetch, ledger_claims)
    base = {"answers_version": ANSWERS_VERSION, "source": sid, "checked": today, "model": MODEL,
            "rubric_version": RUBRIC_VERSION, "coverage": "excerpts", "text_sha256": packet["text_sha256"],
            "text_chars": packet["text_chars"], "note": NOTE}
    if status in ("stale", "too_long", "unlocated"):
        return {**base, "status": status, "detail": detail}, None, detail
    if status in ("error", "no_claims"):
        return None, None, detail
    unlocated = sorted(cid for cid, n in info["located"].items() if not n)
    if not live:
        return None, None, (f"ready: {len(request['questions'])} questions over {len(info['excerpts'])} excerpts "
                            f"({info['chars']:,} characters), {len(encoded(request)):,} bytes")
    response = call(request, key)
    answers = response["answers"]
    doc = {**base, "status": "checked", "request_bytes": len(encoded(request)),
           "excerpts": info["excerpts"], "context": info["context"], "extra_quotes_dropped": info["dropped_extra"],
           "quotes_not_found": info["not_found"], "unlocated_claims": unlocated,
           "questions": request["questions"], "usage": response.get("usage"), "answers": answers,
           "flags": flags_for(answers, packet["claims"], ledger_claims)}
    n = sum(1 for f in doc["flags"].values() if f)
    return doc, response.get("usage"), f"checked: {n} of {len(doc['flags'])} claim(s) flagged"


def run(root, key, live, max_papers, seconds, only=None, recheck=False, fetch=fetch_arxiv, call=None,
        sleep=time.sleep, clock=time.monotonic, today=None):
    today = today or today_utc()
    call = call or (lambda request, k: evaluate(request, k, timeout=(5, 90)))
    started = clock()
    summary = {"date": today, "live": live, "papers": [], "counts": {}, "tokens": {"input": 0, "output": 0},
               "invalid": [], "stop_reason": "queue_exhausted"}
    packets = load_packets(root)
    ledger_claims = load_claims(root)
    todo = []
    for sid, packet in packets.items():
        problems = validate_packet(packet)
        if problems:
            summary["invalid"].append({"source": sid, "problems": problems})
            continue
        if only and sid != only:
            continue
        done = answers_path(sid, root)
        if not recheck and done.exists() and json.loads(done.read_text(encoding="utf-8")).get("status") in TERMINAL:
            continue
        todo.append(sid)
    failures = 0
    for i, sid in enumerate(todo[:max_papers]):
        if clock() - started >= seconds:
            summary["stop_reason"] = "time_budget"
            break
        if i:
            sleep(3.0)                                  # arXiv asks for at most one request per 3 seconds
        try:
            doc, usage, note = check_one(root, sid, packets[sid], ledger_claims, fetch, call, key, live, today)
        except RuntimeError as e:                       # a transport or HTTP failure: record nothing, retry later
            failures += 1
            summary["papers"].append({"source": sid, "status": "error", "detail": str(e)[:200]})
            summary["counts"]["error"] = summary["counts"].get("error", 0) + 1
            if any(code in str(e) for code in ("HTTP 401", "HTTP 403")) or failures >= 3:
                summary["stop_reason"] = "api_error"
                break
            continue
        status = doc["status"] if doc else ("preview" if not live else "skipped")
        if doc and live:
            answers_path(sid, root).write_text(
                json.dumps(doc, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
        if usage:
            summary["tokens"]["input"] += usage.get("input_tokens", 0)
            summary["tokens"]["output"] += usage.get("output_tokens", 0)
        summary["counts"][status] = summary["counts"].get(status, 0) + 1
        summary["papers"].append({"source": sid, "status": status, "detail": note, "flags": (doc or {}).get("flags")})
    else:
        if len(todo) > max_papers:
            summary["stop_reason"] = "paper_cap"
    summary["queued"] = len(todo)
    summary["estimated_cost_usd"] = round(summary["tokens"]["input"] * PRICE_PER_MTOK / 1e6, 6)
    summary["errors"] = summary["counts"].get("error", 0)
    return summary


def validate_answers(root):
    """Shape problems in stored answers, checked against the packets they answer. [] when fine."""
    problems = []
    packets = load_packets(root)
    for sid in packets:
        path = answers_path(sid, root)
        if not path.exists():
            continue
        doc = json.loads(path.read_text(encoding="utf-8"))
        if doc.get("answers_version") != ANSWERS_VERSION or doc.get("source") != sid:
            problems.append(f"{sid}: not a {ANSWERS_VERSION} answers file for this source")
        if doc.get("status") == "checked":
            missing = [k for k in (doc.get("questions") or {}) if k not in (doc.get("answers") or {})]
            if missing:
                problems.append(f"{sid}: answers missing for {missing[:3]}")
            if doc.get("coverage") != "excerpts":
                problems.append(f"{sid}: answers must say coverage: excerpts")
        if doc.get("text_sha256") != packets[sid]["text_sha256"]:
            problems.append(f"{sid}: answers were made against a different text than the packet's")
    return problems


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--live", action="store_true", help="send to TypeSafe (needs TYPESAFE_API_KEY) and write answers")
    ap.add_argument("--require-key", action="store_true", help="fail (not skip) without TYPESAFE_API_KEY")
    ap.add_argument("--max-papers", type=int)
    ap.add_argument("--seconds", type=int)
    ap.add_argument("--source", help="check only this source id")
    ap.add_argument("--recheck", action="store_true", help="check papers that already have answers")
    ap.add_argument("--validate", action="store_true", help="shape-check stored packets and answers, then exit")
    a = ap.parse_args()

    if a.validate:
        bad = 0
        for sid, p in load_packets(ROOT).items():
            for problem in validate_packet(p):
                bad += 1
                print(f"  {sid}: {problem}")
        for problem in validate_answers(ROOT):
            bad += 1
            print("  " + problem)
        print(f"packets and answers: {bad} problem(s)")
        return 1 if bad else 0

    limits = dict(DEFAULTS)
    for k, v in (("max_papers", a.max_papers), ("seconds", a.seconds)):
        if v is not None:
            limits[k] = min(max(1, v), CEILINGS[k])
    key = os.environ.get("TYPESAFE_API_KEY", "")
    if a.live and not key:
        msg = "TYPESAFE_API_KEY is not set; nothing was checked"
        if a.require_key:
            sys.exit("error: " + msg)
        print("::warning::" + msg)
        return 0

    summary = run(ROOT, key, a.live, limits["max_papers"], limits["seconds"], a.source, a.recheck)
    for bad in summary["invalid"]:
        print(f"INVALID PACKET {bad['source']}: {bad['problems']}")
    print(f"{'checked' if a.live else 'previewed'} {len(summary['papers'])} of {summary['queued']} queued paper(s); "
          f"{summary['counts']}; stopped: {summary['stop_reason']}")
    if a.live:
        print(f"  tokens in/out: {summary['tokens']['input']:,}/{summary['tokens']['output']:,}"
              f"  (~${summary['estimated_cost_usd']:.4f} at TypeSafe's documented $0.042 per million input tokens)")
    for p in summary["papers"]:
        print(f"  {p['source']}: {p['status']} - {p['detail']}")
        for cid, fl in (p.get("flags") or {}).items():
            for f in fl:
                print(f"      {cid}: {f}")
    if not a.live:
        print("preview: nothing was sent and nothing was written")
    if a.live:
        (ROOT / "corpus" / "questions").mkdir(parents=True, exist_ok=True)
        (ROOT / "corpus" / "questions" / "_last_paper_check.json").write_text(
            json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    return 1 if summary["invalid"] else (2 if summary["errors"] else 0)


if __name__ == "__main__":
    sys.exit(main())
