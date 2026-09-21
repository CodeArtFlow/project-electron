"""Authenticated API contract check using a labelled synthetic fixture, not research evidence."""
import json
import os
from pathlib import Path
import time
from assess_quality import MODEL, evaluate

def main():
    key = os.environ.get("TYPESAFE_API_KEY")
    if not key:
        raise SystemExit("Missing TYPESAFE_API_KEY Actions secret")
    request = {
        "model": MODEL,
        "state": {"fixture": "Synthetic connection test. No research paper, author history, or replication data is supplied."},
        "questions": {
            "evidence_available": {
                "type": "choice",
                "instructions": "Using only the supplied fixture, is there evidence to assess a research group's track record?",
                "criteria": {"unknown": "No research evidence was supplied.", "available": "Research track-record evidence was supplied."}
            }
        }
    }
    started = time.monotonic()
    response = evaluate(request, key)
    passed = response["answers"]["evidence_available"]["choice"] == "unknown"
    report = {"kind": "synthetic_connection_test", "passed": passed,
              "seconds": round(time.monotonic()-started,3), "response": response}
    output = Path("run/typesafe-smoke.json")
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(json.dumps(report,indent=2))
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary,"a",encoding="utf-8") as handle:
            handle.write("# TypeSafe authenticated check\n\n"
                         + ("PASS" if passed else "FAIL")
                         + ": synthetic evidence-absence test. This is not research-quality calibration.\n\n"
                         + f"Model: {response['model']}; elapsed: {report['seconds']}s.\n")
    if not passed:
        raise SystemExit("API authenticated but synthetic evidence-absence check failed")

if __name__=="__main__":
    main()
