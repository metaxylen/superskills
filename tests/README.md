# tests/

```bash
./tests/run-all.sh    # frontmatter + routing
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

Add a tab-separated row when you change a v1 or optional skill `description`.
