# tests/

```bash
./tests/run-all.sh    # frontmatter + routing + offline loop grader controls
npm test              # same
```

| File | Role |
|------|------|
| `skill_frontmatter.py` | YAML, plugin.json, trigger files |
| `routing_eval.py` | EN/TR triggers, unique Turkish tokens |
| `routing-triggers.tsv` | Turkish substring checks |
| `routing-triggers-en.tsv` | English substring checks |
| `routing-manual-test.md` | Phrases to try in Cursor |
| `optional-routing-triggers.tsv` | Optional skill description substrings |
| `router_integrity.py` | dev-router table → existing `skills/` / `optional/` |
| `routing_scenarios.py` | Synthetic Fixit Corp path walkthrough (no LLM) |
| `loop_agent_eval.py` | Offline grader controls; opt-in live Codex/Claude screening |

Add a tab-separated row when you change a v1 or optional skill `description`.

## Live loop screening (opt-in)

The default suite makes no model calls. Live screening consumes CLI account
usage and requires authenticated `codex` and/or `claude` installations. Check
the installed CLI flags before use. Each trial uses a fresh temporary fixture,
a frozen skill snapshot, a 240-second process timeout, and outside scoring.

```bash
python3 tests/loop_agent_eval.py --self-test
python3 tests/loop_agent_eval.py --out /tmp/loop-screen-current --variants current --platforms codex,claude
# Compare an archived pre-loop executing-plans file with the current reference:
python3 tests/loop_agent_eval.py --out /tmp/loop-screen-comparison --baseline /path/to/archived/SKILL.md --variants baseline,current --platforms codex,claude
# Resume only infrastructure failures; completed trials and frozen instructions stay intact:
python3 tests/loop_agent_eval.py --out /tmp/loop-screen-retry --retry-from /tmp/loop-screen-current --platforms codex,claude
```

Use a new output directory for each run. Results include manifests, JSONL CLI
traces, final responses and per-trial summaries. Traces remain local; inspect
them before sharing. Cases select `executing-plans` explicitly, so they test
behavior after loading, not automatic skill routing. Seven small cases with
one trial per cell screen regressions; they do not measure general
productivity or interruption recovery. Interpret environments separately.
An account-limit error stops newly queued jobs for that platform; already
running jobs may also fail. Preserve those records as infrastructure failures.
