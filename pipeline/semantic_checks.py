"""Evidence-bound TypeSafe semantic checks across the research pipeline.

No browsing, no free-text generation, no model-written source records.
Results are proposals with a separate publication-risk signal.
"""
import argparse
from collections import Counter
from datetime import date, datetime, timezone
import hashlib
import itertools
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

import yaml
from assess_quality import MODEL, PREFIX, encoded, evaluate, validate_response

ROOT = Path(__file__).resolve().parent.parent
VERSION = "semantic-v1"
MAX_BYTES = 40000
TOPICS = {
    "MAT":"Materials", "DEV":"Devices", "LITHO":"Lithography", "PROC":"Process",
    "PKG":"Packaging", "MEM":"Memory", "ARCH":"Architecture", "PHOT":"Photonics",
    "EDA":"Electronic design automation", "ECON":"Fab economics",
    "unknown":"Insufficient context or outside semiconductor scope",
}
RELATION = {
    "supports":"All substantive parts are supported by the supplied evidence, including qualifications.",
    "contradicts":"Supplied evidence directly opposes at least one substantive part.",
    "unsupported":"At least one substantive part is not established by the supplied evidence.",
    "unknown":"Insufficient or ambiguous context to decide.",
}
def choice(text, criteria):
    return {"type":"choice","instructions":PREFIX+text,"criteria":criteria}
def noul(text):
    return {"type":"noul","instructions":PREFIX+text}
def score(text, levels):
    return {"type":"score","instructions":PREFIX+text,"criteria":levels}
def stamp():
    return datetime.now(timezone.utc).isoformat()
def digest(value):
    return hashlib.sha256(encoded(value)).hexdigest()
def plain(value):
    # YAML dates become stable JSON strings, without silently stringifying arbitrary objects.
    return json.loads(json.dumps(value, default=lambda x:x.isoformat() if isinstance(x,date) else str(x)))
def yaml_file(path):
    obj=yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(obj,dict):
        raise ValueError(f"Expected mapping in {path.name}")
    return plain(obj)
def markdown_meta(text):
    if text.startswith("---"):
        return plain(yaml.safe_load(text.split("---",2)[1]) or {})
    return {}
def read_state(root):
    papers={p.stem:yaml_file(p) for p in sorted((root/"corpus/papers").glob("SRC-*.yaml"))}
    authors={p.stem:yaml_file(p) for p in sorted((root/"corpus/authors").glob("*.yaml"))}
    claims={}
    for p in sorted((root/"ledger/claims").glob("*.yaml")):
        for c in yaml_file(p).get("claims",[]):
            if c["id"] in claims: raise ValueError("Duplicate claim IDs")
            claims[c["id"]]=c
    return papers, authors, claims

def source_view(source):
    return {k:source[k] for k in (
        "id","title","url","access","reported","method_summary","limitations","evidence_type","grade"
    ) if k in source}

def job(key, stage, state, questions, required=False, missing=None):
    request={"model":MODEL,"state":state,"questions":questions}
    return {"id":key,"stage":stage,"request":request,"required":required,
            "missing":missing or [],"fingerprint":digest({"version":VERSION,"request":request})}

def build_jobs(root=ROOT, scope="all", candidate_limit=8):
    papers, authors, claims=read_state(root)
    jobs=[]
    # A claim check is against the read record, not a re-reading of its original paper.
    for cid,c in claims.items():
        if c.get("status") not in ("active","contested","challenged"): continue
        sources={sid:source_view(papers[sid]) for sid in c.get("sources",[]) if sid in papers}
        missing=[sid for sid in c.get("sources",[]) if sid not in sources]
        questions={
            "support":choice("How does sources relate to claim.statement? Do not fill gaps from the claim itself.",RELATION),
            "conditions":choice("Are ALL stated claim.conditions explicitly supported by sources? "
                "Similar conditions in another paper do not count. No conditions is unknown.",
                {"supported":"Every condition has support in these sources.",
                 "unsupported":"At least one condition is missing from or conflicts with the sources.",
                 "unknown":"No conditions or insufficient evidence."}),
            "atomic":noul("Does claim.statement contain exactly one independently falsifiable assertion?"),
            "evidence_type":choice("Which evidence type do sources establish for this specific claim?",
                {v:v for v in ("measured","simulated","projected","announced","rumored","mixed","unknown")}),
            "numbers":choice("Does claim.quantity.as_published faithfully represent the value AND its "
                "bound, approximation or uncertainty in sources? A bound must not become an equality. "
                "Do not perform unit conversion.", {
                    "faithful":"Value and qualifiers preserved.",
                    "distorted":"Value, direction of bound, ratio meaning or uncertainty changed.",
                    "not_applicable":"No quantity in this claim.",
                    "unknown":"Insufficient source text."}),
        }
        jobs.append(job("claim:"+cid,"extraction",{"claim":c,"sources":sources},questions,True,missing))
    if scope in ("all","publication"):
        for sid,s in papers.items():
            questions={
                "method_available":noul("Does source provide substantive method details to assess disclosure quality?"),
                "method_detail":score("Assuming substantive methods are present, rate method disclosure in source only.",[
                    "Methods lack key conditions needed to interpret the result.",
                    "Some conditions and method identified; major reproduction details absent.",
                    "Most conditions, controls and limitations disclosed.",
                    "Conditions, controls, uncertainty and reproduction details clearly disclosed."]),
                "limits_explicit":noul("Does source explicitly state limitations relevant to its conclusions?"),
                "access_consistent":choice("Is source.access consistent with its own oa_evidence and limitations?",
                    {"consistent":"No internal inconsistency in claimed access.",
                     "inconsistent":"Record claims access contradicted by its own text.",
                     "unknown":"Cannot determine from record alone."}),
            }
            # Include OA text so this tests actual access assertions, never URL availability.
            state={"source":dict(source_view(s),oa_evidence=s.get("oa_evidence"))}
            jobs.append(job("source:"+sid,"source_quality",state,questions))
        for aid,a in authors.items():
            # Author records must explicitly supply read professional evidence; no guessed lineage.
            evidence=a.get("evidence",[])
            if not isinstance(evidence,list) or not evidence or any(
                    not isinstance(e,dict) or not all(isinstance(e.get(k),str) and e[k].strip()
                    for k in ("excerpt","source_url","locator")) or not e.get("read_at")
                    for e in evidence):
                jobs.append(job("group:"+aid,"group_quality",{"target_id":aid}, {},
                                missing=["No complete professional evidence with excerpt, source_url, locator and read_at"]))
                continue
            questions={
                "identity_supported":noul("Does evidence establish the identity and membership of target?"),
                "track_record_available":noul("Does evidence describe target's past research outcomes beyond citations or prestige?"),
                "track_record":score("Given outcome evidence, rate target's record of results holding up.",[
                    "Documented results have unresolved substantive failures.",
                    "Limited outcome history; no independent verification established.",
                    "Multiple outcomes have independent confirmation.",
                    "Sustained independently confirmed outcomes across years."]),
                "lineage_documented":noul("Does evidence explicitly document advisor or research-group lineage for target?"),
                "integrity":choice("What integrity conclusion is established by evidence for target?",
                    {"unknown":"No adequate integrity review evidence.",
                     "concern_documented":"Documented, attributable integrity concern; not guilt inferred from a correction.",
                     "resolved_concern":"Concern and resolution both documented.",
                     "no_concern_in_reviewed_record":"Bounded reviewed record reports no concern, not proof none exists."}),
            }
            jobs.append(job("group:"+aid,"group_quality",{"target":a.get("id",aid),"evidence":evidence},questions))
        # Compare semantically even when condition labels differ; include qualitative same-topic pairs.
        live=[c for c in claims.values() if c.get("status") in ("active","contested","challenged")]
        for a,b in itertools.combinations(live,2):
            if a.get("topic")!=b.get("topic"): continue
            qa=(a.get("quantity") or {}).get("quantity")
            qb=(b.get("quantity") or {}).get("quantity")
            if qa and qb and qa!=qb: continue
            sources={sid:papers[sid] for sid in sorted(set(a.get("sources",[])+b.get("sources",[]))) if sid in papers}
            questions={
                "comparability":choice("Do a and b describe the same result under genuinely comparable conditions?",
                    {"comparable":"Same metric, subject, baseline and conditions.",
                     "different_scope":"Different baseline, operating point, object or scope.",
                     "unknown":"Missing conditions or ambiguous comparison."}),
                "contradiction":noul("Do a and b assert mutually incompatible things under the SAME conditions? Different scopes are not contradictions."),
                "shared_group":noul("Do supplied source author records explicitly establish a shared author or research group? "
                                    "Missing affiliations do not establish independence."),
                "classification":choice("Which preliminary discrepancy classification best fits the supplied evidence? "
                    "This is only a review proposal.",
                    {"D":"Unit/definition mismatch","C1":"Can be scoped to different conditions",
                     "C2":"Genuine incompatible claims with specified resolving evidence missing",
                     "A":"Our statement misrepresents its own source","none":"No demonstrated discrepancy",
                     "unknown":"Needs further examination"}),
            }
            jobs.append(job("pair:"+a["id"]+":"+b["id"],"reconciliation",
                            {"a":a,"b":b,"sources":sources},questions,True))
        for folder in ("digests","sota","discoveries"):
            for p in sorted((root/folder).glob("*.md")):
                text=p.read_text(encoding="utf-8")
                ids=sorted(set(re.findall(r"\bCLM-[A-Z]+-\d{4}\b",text)))
                cited={cid:claims[cid] for cid in ids if cid in claims}
                # Synthesis may name no CLM IDs; compare to the whole ledger plus honest coverage.
                if not ids and folder=="sota": cited=claims
                state={"document":text,"claims":cited,"coverage":{
                    "source_count":len(papers),"claims_by_topic":dict(Counter(c.get("topic") for c in claims.values())),
                    "candidate_count":len(list((root/"corpus/candidates").glob("CAND-*.yaml")))}}
                if folder=="discoveries":
                    state["sources"]={sid:source_view(s) for sid,s in papers.items()}
                questions={
                    "faithful":choice("Does document preserve the substantive meaning, conditions and uncertainty "
                        "of supplied claims/evidence? Counts and descriptions of this pipeline are not scientific claims.",RELATION),
                    "overstates":noul("Does document portray missing corpus coverage as settled knowledge of the field, "
                                      "or simulations/single-group results as independently established measurements?"),
                    "gap_visible":noul("Where supplied claims are challenged/contested or document describes a data gap, "
                        "does document clearly disclose that uncertainty? If no such claims/gaps, answer yes."),
                }
                jobs.append(job("document:"+folder+"/"+p.name,"discovery" if folder=="discoveries" else "publication",
                                state,questions,folder!="discoveries",
                                [cid for cid in ids if cid not in claims]))
        for p in sorted((root/"ledger/conflicts").glob("CFL-*.md")):
            text=p.read_text(encoding="utf-8")
            meta=markdown_meta(text)
            questions={
                "resolution_supported":choice("Does conflict's recorded explanation follow from the supplied claims "
                    "and sources? Do not accept its conclusion merely because it says resolved.",RELATION),
                "gap_specific":noul("If conflict names missing evidence, is it specific enough to say what would resolve it? "
                    "If no missing-data resolution is used, answer yes."),
            }
            refs={cid:claims[cid] for cid in meta.get("claims",[]) if cid in claims}
            sids={sid for c in refs.values() for sid in c.get("sources",[])}
            jobs.append(job("conflict:"+p.stem,"reconciliation",{"conflict":text,"claims":refs,
                            "sources":{sid:source_view(papers[sid]) for sid in sorted(sids) if sid in papers}},questions,True))
    coverage={"candidate_total":0,"candidate_selected":0,"author_records":len(authors),
              "author_evidence_missing":not authors}
    if scope in ("all","triage"):
        paths=sorted((root/"corpus/candidates").glob("CAND-*.yaml"), reverse=True)
        coverage.update(candidate_total=len(paths),candidate_selected=min(candidate_limit,len(paths)))
        for p in paths[:candidate_limit]:
            c=yaml_file(p)
            state={"candidate":{k:c.get(k) for k in ("id","title","primary_topic","venue_id","relevance")},
                   "limitation":"Unread metadata only: route for reading; no scientific assertions can be made."}
            questions={
                "relevance":choice("Does candidate metadata suggest a semiconductor research reading priority?",
                    {"core":"Direct semiconductor stack topic","adjacent":"Related devices/materials/fabrication",
                     "out_of_scope":"Different domain","unknown":"Not enough metadata"}),
                "layer":choice("Which primary semiconductor stack layer is suggested by candidate metadata?",TOPICS),
                "priority":score("How directly does candidate metadata suggest useful semiconductor research?",[
                    "No apparent connection","Indirect connection","Relevant adjacent work","Directly addresses a stack layer"]),
            }
            jobs.append(job("candidate:"+p.stem,"triage",state,questions))
    if scope=="triage": jobs=[j for j in jobs if j["stage"]=="triage"]
    return jobs,coverage

def route(j,response):
    """Provisional review signals, not calibrated truth probabilities or conflict resolutions."""
    answers=response["answers"]
    flags=[]
    for key,a in answers.items():
        if a["type"]=="choice" and a["confidence"]<0.9:
            flags.append(key+": uncertain")
    if j["stage"]=="extraction":
        if answers["support"]["choice"]!="supports": flags.append("Claim support needs review")
        if j["request"]["state"]["claim"].get("conditions") and answers["conditions"]["choice"]!="supported":
            flags.append("Conditions not established")
        if answers["atomic"]["noul"]<0.9: flags.append("Atomicity uncertain")
        expected=j["request"]["state"]["claim"].get("evidence_type")
        if answers["evidence_type"]["choice"]!=expected: flags.append("Evidence type mismatch/uncertain")
        if answers["numbers"]["choice"] not in ("faithful","not_applicable"): flags.append("Numeric qualifier needs review")
    if j["stage"] in ("publication","discovery"):
        if answers["faithful"]["choice"]!="supports": flags.append("Document fidelity needs review")
        if answers["overstates"]["noul"]>0.1: flags.append("Possible overstatement")
        if answers["gap_visible"]["noul"]<0.9: flags.append("Uncertainty may be hidden")
    if j["stage"]=="reconciliation":
        if "contradiction" in answers and answers["contradiction"]["noul"]>0.1:
            flags.append("Potential conflict: classify from evidence")
        if "resolution_supported" in answers and answers["resolution_supported"]["choice"]!="supports":
            flags.append("Recorded conflict resolution needs review")
    if j["stage"]=="source_quality" and answers["access_consistent"]["choice"]!="consistent":
        flags.append("Access assertion needs review")
    if j["stage"]=="group_quality":
        if answers["identity_supported"]["noul"]<0.9: flags.append("Identity not established")
        if answers["integrity"]["choice"]=="concern_documented": flags.append("Documented concern requires review")
    # An unavailable premise suppresses a speculative score; never replace absence with zero.
    suppressed=[]
    for premise,value in (("method_available","method_detail"),("track_record_available","track_record"),("identity_supported","track_record")):
        if premise in answers and answers[premise]["noul"]<0.9:
            suppressed.append(value)
    if j["missing"]: flags.append("Missing evidence: "+", ".join(j["missing"]))
    return {"status":"needs_review" if flags else "model_checked",
            "flags":flags,"suppressed_scores":suppressed,
            "publication_risk":bool(flags) and j["required"],
            "note":"Uncalibrated model signal; no claim, credibility tier or conflict status was changed."}

def worker_call(request,timeout):
    proc=subprocess.run([sys.executable,str(Path(__file__).resolve()),"--worker"],
        input=json.dumps(request),text=True,capture_output=True,timeout=timeout,
        encoding="utf-8")
    if proc.returncode: raise RuntimeError("TypeSafe worker failed: "+proc.stderr.strip()[:600])
    return json.loads(proc.stdout)

def run(jobs,coverage,root=ROOT,live=False,max_calls=64,seconds=180,call=worker_call):
    if not 1<=max_calls<=100 or not 1<=seconds<=300:
        raise ValueError("Limits: 1-100 requests, 1-300 seconds")
    started=time.monotonic()
    records=[]
    calls=0
    cache_dir=root/"run/typesafe-cache"
    if live: cache_dir.mkdir(parents=True,exist_ok=True)
    for j in jobs:
        rec={k:j[k] for k in ("id","stage","required","fingerprint")}
        rec["request"]=j["request"]
        if not j["request"]["questions"]:
            rec.update(status="unknown",missing=j["missing"])
        elif len(encoded(j["request"]))>MAX_BYTES:
            rec.update(status="pending",reason="Input exceeds 40 KB; not silently truncated")
        elif not live:
            rec.update(status="pending",reason="Preview: no API call")
        else:
            cache=cache_dir/(j["fingerprint"]+".json")
            response=None
            try:
                if cache.exists():
                    response=json.loads(cache.read_text(encoding="utf-8"))
                    validate_response(response,j["request"])
                    rec["cached"]=True
                else:
                    left=seconds-(time.monotonic()-started)
                    if calls>=max_calls or left<1:
                        rec.update(status="pending",reason="Run request/time budget reached")
                        records.append(rec)
                        continue
                    calls+=1
                    tick=time.monotonic()
                    response=call(j["request"],min(30,left))
                    validate_response(response,j["request"])
                    rec["seconds"]=round(time.monotonic()-tick,3)
                    cache.write_text(json.dumps(response,ensure_ascii=False),encoding="utf-8")
                    rec["cached"]=False
                rec.update(route(j,response),response=response,request=j["request"])
            except (RuntimeError,ValueError,subprocess.TimeoutExpired,OSError) as exc:
                rec.update(status="error",reason=type(exc).__name__+": "+str(exc)[:650])
        records.append(rec)
    report={"schema_version":1,"version":VERSION,"model":MODEL,"created":stamp(),
        "plan_hash":digest([j["fingerprint"] for j in jobs]),"scope_coverage":coverage,
        "mode":"live" if live else "preview","elapsed_seconds":round(time.monotonic()-started,3),
        "calls":calls,"max_http_attempts":calls*3,"records":records,
        "status_counts":dict(Counter(r["status"] for r in records)),
        "calibration":"not_calibrated; provisional review thresholds only"}
    report["complete"]=not any(r["status"] in ("pending","error") for r in records)
    return report

def gate_failures(root=ROOT,required=False):
    path=root/"run/typesafe-publication.json"
    if not path.exists(): return ["TypeSafe publication audit is missing"] if required else []
    try:
        report=json.loads(path.read_text(encoding="utf-8"))
        jobs,_=build_jobs(root,"publication",0)
        if report.get("mode")!="live" or report.get("plan_hash")!=digest([j["fingerprint"] for j in jobs]):
            return ["TypeSafe publication audit is stale or preview-only; rerun it"]
        if not report.get("complete"): return ["TypeSafe publication audit is incomplete"]
        records=report["records"]
        if len(records)!=len(jobs) or {r["id"] for r in records}!={j["id"] for j in jobs}:
            return ["TypeSafe audit record coverage does not match current plan"]
        by_id={r["id"]:r for r in records}
        failures=[]
        for j in jobs:
            r=by_id[j["id"]]
            if not j["request"]["questions"]: continue
            if r.get("request")!=j["request"]: return ["TypeSafe audit evidence mismatch"]
            validate_response(r["response"],j["request"])
            result=route(j,r["response"])
            if result["publication_risk"]: failures.append(j["id"]+": "+", ".join(result["flags"]))
        return failures
    except (ValueError,KeyError,TypeError,OSError): return ["TypeSafe publication audit is invalid"]


def render_summary(report):
    lines=["# TypeSafe research checks","",
        "Model judgments over supplied local evidence. Not verified scientific conclusions.","",
        f"Mode: {report['mode']}; model: {report['model']}; elapsed: {report['elapsed_seconds']}s;",
        f"requests: {report['calls']}; complete within selected scope: {report['complete']}.","",
        "## Coverage","",json.dumps(report["scope_coverage"],sort_keys=True),"",
        "## Review signals",""]
    for r in report["records"]:
        lines.append(f"- {r['id']}: **{r['status']}**")
        for flag in r.get("flags",[]): lines.append("  - "+flag)
        for key,a in r.get("response",{}).get("answers",{}).items():
            value=a.get(a["type"])
            if key in r.get("suppressed_scores",[]): value="withheld: supporting evidence unavailable"
            confidence="" if a["type"]=="noul" else f"; confidence={a['confidence']}"
            lines.append(f"  - {key}: {value}{confidence}")
        lines.append(f"  - API time: {r.get('seconds',0)}s; cached: {r.get('cached',False)}")
        if r.get("reason"): lines.append("  - "+r["reason"])
        if r.get("missing"): lines.append("  - Missing: "+", ".join(r["missing"]))
    return "\n".join(lines)+"\n"

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--scope",choices=("all","publication","triage"),default="all")
    ap.add_argument("--live",action="store_true")
    ap.add_argument("--worker",action="store_true",help=argparse.SUPPRESS)
    ap.add_argument("--max-calls",type=int,default=64)
    ap.add_argument("--seconds",type=int,default=180)
    ap.add_argument("--candidate-limit",type=int,default=8)
    args=ap.parse_args()
    if args.worker:
        key=os.environ.get("TYPESAFE_API_KEY")
        if not key: raise ValueError("Missing TYPESAFE_API_KEY")
        print(json.dumps(evaluate(json.load(sys.stdin),key)))
        return 0
    if not 0<=args.candidate_limit<=100: raise ValueError("candidate-limit must be 0-100")
    if args.live and not os.environ.get("TYPESAFE_API_KEY"): raise ValueError("Missing TYPESAFE_API_KEY")
    jobs,coverage=build_jobs(ROOT,args.scope,args.candidate_limit)
    report=run(jobs,coverage,ROOT,args.live,args.max_calls,args.seconds)
    folder=ROOT/"run"
    folder.mkdir(exist_ok=True)
    output=folder/("typesafe-"+args.scope+".json")
    output.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    summary=render_summary(report)
    output.with_suffix(".md").write_text(summary,encoding="utf-8")
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"],"a",encoding="utf-8") as handle: handle.write(summary)
    print(f"{output.name}: {len(jobs)} jobs; {report['status_counts']}; {report['calls']} calls; {report['elapsed_seconds']}s")
    return 2 if args.live and not report["complete"] else 0

if __name__=="__main__":
    try: raise SystemExit(main())
    except (ValueError,RuntimeError,OSError) as exc: raise SystemExit(str(exc))
