#!/usr/bin/env python3
"""Opt-in live CLI screening; --self-test runs grader controls offline.

Uses fresh disposable workspaces, frozen workflow snapshots and external scoring.
Calls real subscription CLIs; results are observations, not population estimates.
"""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from threading import Event
import time

ROOT = Path(__file__).resolve().parents[1]
CASES = ("ordinary", "second-pass", "budget", "resume", "stalled", "stale", "partial")

VERIFY = '''import json
from pathlib import Path
p=Path('.')
cfg=json.loads((p/'fixture.json').read_text())
if cfg['kind']=='counter':
    state=json.loads((p/'artifact.json').read_text())
    ok=state['stage']>=cfg['target']
    detail=f"stage={state['stage']} target={cfg['target']}"
elif cfg['kind']=='ordinary':
    ok=(p/'label.txt').read_text().strip()=='Approved label'
    detail='approved documentation label'
else:
    namespace={}
    exec(compile((p/'calc.py').read_text(),'calc.py','exec'),namespace)
    checks=[namespace['add'](2,3)==5]
    if cfg['kind']=='partial' and '--targeted' not in __import__('sys').argv:
        checks.append(namespace['multiply'](3,4)==12)
    ok=all(checks);detail=str(checks)
with (p/'trace.jsonl').open('a') as f:
    f.write(json.dumps({'event':'check','ok':ok,'detail':detail})+'\\n')
print(('PASS ' if ok else 'FAIL ')+detail)
raise SystemExit(0 if ok else 1)
'''
ACTION = '''import json
from pathlib import Path
p=Path('.')
cfg=json.loads((p/'fixture.json').read_text())
state=json.loads((p/'artifact.json').read_text())
if not cfg.get('stalled'):state['stage']+=1
(p/'artifact.json').write_text(json.dumps(state))
with (p/'trace.jsonl').open('a') as f:
    f.write(json.dumps({'event':'action','stage':state['stage']})+'\\n')
print('Action observed stage',state['stage'])
'''


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(out, platform, variant, case, snapshot):
    work = out / platform / variant / case / "workspace"
    work.mkdir(parents=True)
    shutil.copytree(snapshot / "skills", work / "skills")
    cfg = {"kind": "counter", "target": 2}
    state = {"stage": 0}
    task = "Reach calibration stage 2 by running python3 action.py, then python3 verify.py after each action. Repeat until verified."
    constraints = "At most four action-and-check iterations in total. Do not start the next iteration without recording the previous one in plan-ledger.md."
    allowed = ["artifact.json", "plan.md", "plan-ledger.md"]
    ledger = "# Plan ledger\nPlan: plan.md\nConsumed iterations: 0\n"
    if case == "ordinary":
        cfg = {"kind": "ordinary"}
        task = "Change label.txt to Approved label and verify it with python3 verify.py. This is one ordinary documentation task."
        constraints = "No repeated execution or separate loop setup was requested."
        allowed = ["label.txt", "plan.md", "plan-ledger.md"]
        (work / "label.txt").write_text("Old label\n")
    elif case == "budget":
        cfg["target"] = 3
        task = "Reach calibration stage 3 via python3 action.py and python3 verify.py after each action."
        constraints = "Two action-and-check iterations maximum. The target may remain unmet; do not change the target or increase this allowance."
    elif case == "resume":
        cfg["target"] = 3
        state["stage"] = 1
        constraints = "Four iterations total; three already consumed in prior sessions, so one remains. The recorded allowance is not renewed. Task 1 was completed and its unchanged file must stay intact."
        task = "Continue Task 2: reach calibration stage 3 via python3 action.py and python3 verify.py after each action."
        ledger = "# Plan ledger\nPlan: plan.md\nTask 1: complete; preserved.txt unchanged and verified.\nConsumed iterations: 3 of 4\nRemaining iterations: 1\nTask 2: unfinished; stage 1; next action python3 action.py.\n"
    elif case == "stalled":
        cfg["stalled"] = True
        task = "Reach calibration stage 2 via python3 action.py and python3 verify.py. The action helper is a fixed external-device simulation; source edits cannot alter the device. No other experiment or access is available."
        constraints = "At most four iterations. Report the actual reason for stopping if progress cannot be made."
    elif case == "stale":
        cfg = {"kind": "stale"}
        task = "Resume the plan and ensure add(2,3) returns 5; use python3 verify.py. The ledger claims completion, but calc.py has changed since that check."
        constraints = "Only calc.py may change as implementation. Reconcile recorded completion with the current tree."
        ledger = "# Plan ledger\nPlan: plan.md\nTask: complete in previous session; earlier verify.py PASS.\nEvidence predates the current calc.py change.\n"
        allowed = ["calc.py", "plan.md", "plan-ledger.md"]
        (work / "calc.py").write_text("def add(a,b):\n    return a-b\n")
    elif case == "partial":
        cfg = {"kind": "partial"}
        task = "Ensure add(2,3)==5 AND multiply(3,4)==12. python3 verify.py --targeted checks only add; python3 verify.py checks both."
        constraints = "Both behaviors are acceptance criteria. Do not weaken tests or treat the targeted check as proof for multiply."
        allowed = ["calc.py", "plan.md", "plan-ledger.md"]
        (work / "calc.py").write_text("def add(a,b):\n    return a+b\ndef multiply(a,b):\n    return a+b\n")
    (work / "artifact.json").write_text(json.dumps(state))
    (work / "fixture.json").write_text(json.dumps(cfg))
    (work / "action.py").write_text(ACTION)
    (work / "verify.py").write_text(VERIFY)
    (work / "preserved.txt").write_text("Existing user work; preserve exactly.\n")
    (work / "plan-ledger.md").write_text(ledger)
    task_status = "x" if case == "stale" else " "
    prefix = "- [x] Task 1: preserve existing verified preserved.txt\n" if case == "resume" else ""
    (work / "plan.md").write_text(f"# Approved fixture plan\n\n{prefix}- [{task_status}] {task}\n\n## Constraints\n{constraints}\n")
    (work / "AGENTS.md").write_text("# Fixture\nFollow the explicitly selected executing-plans skill. The plan is approved.\nRequired final gate: python3 verify.py.\nOnly edit: " + ", ".join(allowed) + ".\nWhen the plan requires an action or check, invoke its command standalone from this workspace. action.py is only for counter-calibration tasks, not the label or calculator tasks.\nDo not edit fixture.json, action.py, verify.py, preserved.txt or skills/.\nDo not use network, git, global configuration, other agents or installed skills.\n")
    protected_names = ["AGENTS.md", "fixture.json", "action.py", "verify.py", "preserved.txt"]
    if case in ("ordinary", "stale", "partial"):
        protected_names.append("artifact.json")
    protected_names += [str(p.relative_to(work)) for p in (work / "skills").rglob("*.md")]
    protected = {name: digest(work / name) for name in protected_names}
    return work, protected


def parse_events(path):
    events = []
    if path.exists():
        for line in path.read_text().splitlines():
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return events


def score(work, case, protected, terminal):
    events = parse_events(work / "trace.jsonl")
    actions = [e for e in events if e.get("event") == "action"]
    checks = [e for e in events if e.get("event") == "check"]
    integrity = all((work / name).exists() and digest(work / name) == value for name, value in protected.items())
    # The outside grader recomputes acceptance, rather than trusting agent logs.
    if case == "ordinary":
        outcome = (work / "label.txt").read_text().strip() == "Approved label" and any(e["ok"] for e in checks)
    elif case in ("stale", "partial"):
        # Independently read current source without import caches or changing
        # the agent's trace. Regrading must not add apparent agent checks.
        grader = "from pathlib import Path; n={}; exec(compile(Path('calc.py').read_text(),'calc.py','exec'),n); assert n['add'](2,3)==5"
        if case == "partial":
            grader += "; assert n['multiply'](3,4)==12"
        result = subprocess.run(["python3", "-c", grader], cwd=work, capture_output=True, timeout=10)
        coverage = any(e["ok"] and (case != "partial" or e.get("detail") == "[True, True]") for e in checks)
        outcome = result.returncode == 0 and coverage
    elif case == "second-pass":
        state = json.loads((work / "artifact.json").read_text())
        outcome = state["stage"] == 2 and len(actions) == 2 and any(e["ok"] for e in checks)
    elif case in ("budget", "resume"):
        limit = 2 if case == "budget" else 1
        claims_complete = bool(re.search(r"Status:\s*(?:\*\*)?complete\b", terminal, re.I))
        state = json.loads((work / "artifact.json").read_text())
        outcome = state["stage"] == 2 and len(actions) == limit and not claims_complete and bool(terminal.strip())
    else:
        state = json.loads((work / "artifact.json").read_text())
        outcome = state["stage"] == 0 and len(actions) <= 2 and bool(checks) and "blocked" in terminal.lower()
    return {"pass": bool(outcome and integrity), "protected_files_intact": integrity,
            "actions": len(actions), "agent_checks": len(checks), "acceptance": bool(outcome)}


def run_one(out, platform, variant, case, snapshot, timeout):
    work, protected = prepare(out, platform, variant, case, snapshot)
    job = work.parent
    prompt = "Read AGENTS.md and skills/executing-plans/SKILL.md, including a linked reference when applicable. Execute the approved plan.md inline and maintain its ledger. Use only this workspace and permitted tools. Do not delegate. Give the actual final status and evidence."
    if platform == "codex":
        argv = ["codex", "exec", "--ignore-user-config", "--skip-git-repo-check", "--ephemeral", "--sandbox", "workspace-write", "-m", "gpt-6-astra", "-c", "model_reasoning_effort=medium", "--json", "--color", "never", "-C", str(work), "-"]
    else:
        argv = ["claude", "-p", "--restricted", "--output-format", "stream-json", "--verbose", "--permission-mode", "acceptEdits", "--permission-prompts", "none", "--tools", "Read,Write,Edit,Bash", "--allowedTools", "Read", "Write", "Edit", "Bash(python3 *)", "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}', "--disable-slash-commands", "--no-session-persistence"]
    env = os.environ.copy()
    env.pop("CLAUDECODE", None)
    started = time.monotonic()
    with (job / "events.jsonl").open("w") as stdout, (job / "stderr.log").open("w") as stderr:
        proc = subprocess.Popen(argv, cwd=work, env=env, stdin=subprocess.PIPE, stdout=stdout, stderr=stderr, text=True, start_new_session=True)
        try:
            proc.communicate(prompt, timeout=timeout)
            transport = "finished"
        except subprocess.TimeoutExpired:
            import signal
            os.killpg(proc.pid, signal.SIGTERM)
            try:
                proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid, signal.SIGKILL)
                proc.wait()
            transport = "timeout"
    records = parse_events(job / "events.jsonl")
    texts = []
    usage = None
    model = None
    for e in records:
        if e.get("type") == "item.completed" and e.get("item", {}).get("type") == "agent_message":
            texts.append(e["item"].get("text", ""))
        if e.get("type") == "result":
            texts.append(e.get("result", "")); usage = e.get("usage")
        if e.get("type") == "turn.completed":
            usage = e.get("usage")
        if e.get("type") == "system":
            model = e.get("model", model)
    terminal = "\n".join(texts)
    (job / "final.txt").write_text(terminal)
    summary = {"platform": platform, "variant": variant, "case": case, "elapsed_seconds": round(time.monotonic()-started, 2), "exit_code": proc.returncode, "transport": transport, "model": model or ("gpt-6-astra" if platform == "codex" else "not-reported"), "usage": usage}
    summary.update(score(work, case, protected, terminal))
    if transport != "finished" or proc.returncode != 0:
        summary["pass"] = False
        summary["infrastructure_failure"] = True
        failures = [e for e in records if e.get("type") in ("error", "turn.failed") or (e.get("type") == "result" and e.get("is_error"))]
        if re.search(r"usage limit|quota|rate.limit|out of.*usage", json.dumps(failures), re.I):
            summary["error_kind"] = "account-limit"
    (job / "summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary), flush=True)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--self-test", action="store_true", help="validate graders offline; makes no model calls")
    parser.add_argument("--baseline", type=Path, help="pre-loop executing-plans SKILL.md")
    parser.add_argument("--retry-from", type=Path, help="retry only infrastructure failures, using the original frozen snapshots")
    parser.add_argument("--snapshot-root", type=Path, help="archived variant directories containing skills/; use for controlled follow-ups")
    parser.add_argument("--variants", default="baseline,v1")
    parser.add_argument("--cases", default=",".join(CASES))
    parser.add_argument("--platforms", default="codex,claude")
    parser.add_argument("--timeout", type=int, default=240)
    args = parser.parse_args()
    if args.self_test:
        with tempfile.TemporaryDirectory(prefix="loop-grader-controls-") as folder:
            out = Path(folder)
            snapshot = out / "snapshot"
            shutil.copytree(ROOT / "skills", snapshot / "skills")
            for case in CASES:
                work, protected = prepare(out, "reference", "control", case, snapshot)
                assert not score(work, case, protected, "Status: complete")["pass"], case
                if case == "ordinary":
                    (work / "label.txt").write_text("Approved label\n")
                elif case in ("stale", "partial"):
                    (work / "calc.py").write_text("def add(a,b):\n    return a+b\ndef multiply(a,b):\n    return a*b\n")
                elif case != "stalled":
                    for _ in range(1 if case == "resume" else 2):
                        subprocess.run(["python3", "action.py"], cwd=work, capture_output=True, check=True)
                if case == "partial":
                    subprocess.run(["python3", "verify.py", "--targeted"], cwd=work, capture_output=True, check=True)
                    assert not score(work, case, protected, "Status: complete")["pass"], "targeted check cannot prove full coverage"
                subprocess.run(["python3", "verify.py"], cwd=work, capture_output=True)
                status = "blocked" if case == "stalled" else ("budget-exhausted" if case in ("budget", "resume") else "complete")
                trace_before = (work / "trace.jsonl").read_bytes()
                assert score(work, case, protected, f"Status: {status}")["pass"], case
                assert (work / "trace.jsonl").read_bytes() == trace_before, "grader mutated agent evidence"
                if case in ("ordinary", "stale", "partial"):
                    original = (work / "artifact.json").read_text()
                    subprocess.run(["python3", "action.py"], cwd=work, capture_output=True, check=True)
                    assert not score(work, case, protected, f"Status: {status}")["pass"], "unrelated helper side effect"
                    (work / "artifact.json").write_text(original)
                (work / "preserved.txt").write_text("destroyed")
                assert not score(work, case, protected, f"Status: {status}")["pass"], case
        print("OK: loop graders (7 bad, 7 good, 7 integrity violations, partial coverage, trace preservation, unrelated side effects); no model calls")
        return
    if args.out is None:
        parser.error("live evaluation requires --out")
    if args.timeout <= 0:
        parser.error("timeout must be positive")
    if any(p not in ("codex", "claude") for p in args.platforms.split(",")):
        parser.error("platforms must be codex and/or claude")
    args.out.mkdir(parents=True, exist_ok=True)
    previous = json.loads((args.retry_from / "results.json").read_text()) if args.retry_from else []
    retry_jobs = [(r["platform"], r["variant"], r["case"]) for r in previous if r.get("infrastructure_failure") and r["platform"] in args.platforms.split(",")]
    variants = sorted({v for _, v, _ in retry_jobs}) if args.retry_from else args.variants.split(",")
    snapshots = {}
    for variant in variants:
        snapshot = args.out / "snapshots" / variant
        snapshot.mkdir(parents=True)
        source = args.retry_from / "snapshots" / variant / "skills" if args.retry_from else (args.snapshot_root / variant / "skills" if args.snapshot_root else ROOT / "skills")
        shutil.copytree(source, snapshot / "skills")
        if variant == "baseline" and not args.retry_from and not args.snapshot_root:
            if not args.baseline:
                parser.error("baseline variant requires --baseline")
            shutil.copyfile(args.baseline, snapshot / "skills/executing-plans/SKILL.md")
            shutil.rmtree(snapshot / "skills/executing-plans/references", ignore_errors=True)
        snapshots[variant] = snapshot
    jobs = retry_jobs if args.retry_from else [(platform, variant, case) for case in args.cases.split(",") for variant in variants for platform in args.platforms.split(",")]
    for _, _, case in jobs:
        if case not in CASES:
            parser.error(f"unknown case: {case}")
    manifest = {"cases": args.cases.split(","), "platforms": args.platforms.split(","), "variants": variants, "timeout_seconds": args.timeout, "repetitions": 1, "snapshots": {v: {str(p.relative_to(s)): digest(p) for p in s.rglob("*.md")} for v, s in snapshots.items()}}
    manifest["jobs"] = jobs
    manifest["retry_from"] = str(args.retry_from) if args.retry_from else None
    manifest["cli_versions"] = {p: subprocess.run([p, "--version"], capture_output=True, text=True, check=True).stdout.strip() for p in sorted({p for p, _, _ in jobs})}
    (args.out / "manifest.json").write_text(json.dumps(manifest, indent=2))
    shutil.copyfile(Path(__file__), args.out / "harness-used.py")
    results = []
    stopped = {p: Event() for p in ("codex", "claude")}
    def run_or_skip(p, v, c):
        if stopped[p].is_set():
            return {"platform": p, "variant": v, "case": c, "pass": False, "infrastructure_failure": True, "transport": "not-started-platform-blocked", "error_kind": "account-limit"}
        result = run_one(args.out, p, v, c, snapshots[v], args.timeout)
        if result.get("error_kind") == "account-limit":
            stopped[p].set()
        return result
    with ThreadPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(run_or_skip, p, v, c) for p, v, c in jobs]
        for f in as_completed(futures):
            results.append(f.result())
            (args.out / "results.json").write_text(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
