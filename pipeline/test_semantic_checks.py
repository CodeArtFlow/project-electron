"""Offline behavioral tests: no credentials or network."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
import yaml
from assess_quality import MODEL, validate_response
from semantic_checks import job, choice, noul, score, run, route, build_jobs, gate_failures, digest
from reconcile import independent

def answer(request):
    answers={}
    for key,q in request["questions"].items():
        if q["type"]=="noul":
            answers[key]={"type":"noul","noul":1}
        elif q["type"]=="choice":
            keys=list(q["criteria"])
            answers[key]={"type":"choice","choice":keys[0],"confidence":1,
                          "probabilities":{k:float(k==keys[0]) for k in keys}}
        else:
            levels=q["criteria"]
            answers[key]={"type":"score","score":0,"confidence":1,
                "legend":{str(i):v for i,v in enumerate(levels)},
                "probabilities":{str(i):float(i==0) for i in range(len(levels))}}
    return {"model":MODEL,"usage":{"input_tokens":1,"output_tokens":1},"answers":answers}

class SemanticTests(unittest.TestCase):
    def test_three_contracts(self):
        request=job("test","test",{},{"p":noul("yes?"),"s":score("quality",["low","high"]),
                                    "c":choice("which?",{"x":"x","y":"y"})})["request"]
        response=answer(request)
        validate_response(response,request)
        for key,field,value in [("p","noul",True),("p","noul",1.1),("s","score",0.5),
                               ("s","legend",{"0":"wrong","1":"high"})]:
            bad=copy.deepcopy(response);bad["answers"][key][field]=value
            with self.assertRaises(ValueError): validate_response(bad,request)

    def test_preview_and_budget_and_cache(self):
        jobs=[job(str(i),"test",{"n":i},{"p":noul("test")}) for i in range(2)]
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            calls=[]
            def api(req,timeout):
                self.assertLessEqual(timeout,30);calls.append(req);return answer(req)
            self.assertFalse(run(jobs,{},root,call=api)["complete"])
            self.assertEqual(calls,[])
            result=run(jobs,{},root,True,1,10,api)
            self.assertEqual(result["calls"],1)
            self.assertFalse(result["complete"])
            result=run(jobs,{},root,True,1,10,api)
            self.assertTrue(result["complete"])
            self.assertTrue(result["records"][0]["cached"])
            self.assertEqual(len(calls),2)

    def test_missing_evidence_suppresses_score(self):
        j=job("s","source_quality",{},{
            "method_available":noul("available?"),
            "method_detail":score("detail",["low","high"]),
            "access_consistent":choice("consistent?",{"consistent":"yes","unknown":"unknown"})})
        response=answer(j["request"]);response["answers"]["method_available"]["noul"]=0.1
        self.assertIn("method_detail",route(j,response)["suppressed_scores"])

    def test_no_independence_from_absence(self):
        a={"sources":["a"]};b={"sources":["b"]}
        self.assertFalse(independent(a,b,{}))
        self.assertFalse(independent(a,b,{"a":{"authors":["alice"],"affiliations":["one"]},
                                         "b":{"authors":["bob"],"affiliations":[]}}))
        self.assertTrue(independent(a,b,{"a":{"authors":["alice"],"affiliations":["one"]},
                                        "b":{"authors":["bob"],"affiliations":["two"]}}))

    def test_scope_and_provenance(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            (root/"corpus/candidates").mkdir(parents=True)
            (root/"corpus/candidates/CAND-1.yaml").write_text(yaml.safe_dump(
                {"id":"CAND-1","title":"semiconductors","secret_field":"not for model"}))
            jobs,coverage=build_jobs(root,"triage",1)
            self.assertEqual(len(jobs),1)
            self.assertNotIn("secret_field",json.dumps(jobs))
            self.assertTrue(coverage["author_evidence_missing"])
            self.assertFalse(jobs[0]["required"])

    def test_gate_recomputes_flags_and_rejects_stale(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            (root/"sota").mkdir()
            doc=root/"sota/MAT.md";doc.write_text("No read evidence.")
            jobs,coverage=build_jobs(root,"publication",0)
            def api(req,timeout):
                result=answer(req)
                result["answers"]["overstates"]["noul"]=1
                return result
            report=run(jobs,coverage,root,True,3,10,api)
            self.assertTrue(report["complete"])
            for r in report["records"]: r["publication_risk"]=False;r["flags"]=[]
            path=root/"run/typesafe-publication.json"
            path.write_text(json.dumps(report))
            self.assertTrue(any("overstatement" in f for f in gate_failures(root,True)))
            doc.write_text("Changed evidence.")
            self.assertIn("stale",gate_failures(root,True)[0])

    def test_missing_or_incomplete_audit_blocks(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            self.assertEqual(gate_failures(root),[])
            self.assertTrue(gate_failures(root,True))
            jobs,coverage=build_jobs(root,"publication",0)
            report=run(jobs,coverage,root)
            (root/"run").mkdir(exist_ok=True)
            (root/"run/typesafe-publication.json").write_text(json.dumps(report))
            self.assertTrue(gate_failures(root,True))

    def test_error_and_size_fail_closed(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            jobs=[job("x","test",{"x":"a"*41000},{"p":noul("yes?")})]
            def api(req,timeout): raise RuntimeError("Unavailable")
            report=run(jobs,{},root,True,1,10,api)
            self.assertFalse(report["complete"]);self.assertEqual(report["calls"],0)
            jobs=[job("y","test",{},{"p":noul("yes?")})]
            report=run(jobs,{},root,True,1,10,api)
            self.assertEqual(report["records"][0]["status"],"error")
            self.assertFalse(report["complete"])

if __name__=="__main__":
    unittest.main()
