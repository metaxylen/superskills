---
name: diagnosing-workflow
description: >-
  Diagnoses a bad agent session with evidence from transcripts—wrong skill,
  ignored plan, repeated work, false "done", or runaway cost. Use when the user
  says the session went wrong, wasted time, ignored the plan, used the wrong
  workflow, or wants a post-mortem on this or a past chat. Do not use for
  product bugs in application code—use systematic-debugging. Do not use when
  the user only wants to continue forward work—route with dev-router instead.
  Turkish cues: oturum kötü, yanlış skill, zaman kaybı, planı dinlemedi,
  post-mortem.
---

# Diagnosing workflow

## Done

- Problem statement: session id/path, turn range if known, expected vs actual, metric they care about (time, repeats, wrong skill).
- Findings cite `transcript-path:line` or command output — no citation, no finding.
- Report names **process** failures (routing, plan, verification, skill choice), not unfounded blame on model quality.
- Optional fixes point to skills (`writing-skills` for triggers, `dev-router` for routing gaps) — user decides.

## Intake (one question at a time)

Turn vague complaints into a statement:

- "Too long" → which phase? setup, search, retries, review?
- "Wrong skill" → which skill should have run?
- "Ignored plan" → which plan file and which step?

If the user is away, list open questions and stop — do not invent their expectations.

## Locate sessions

1. Current chat transcript under `~/.cursor/projects/<project>/agent-transcripts/<uuid>.jsonl`.
2. Past session: user provides id, date, or first message — confirm by quoting first user turn + timestamp.
3. Note subagent/Task transcripts if separate files exist.
4. Work in a scratch note in the repo or `/tmp` — **read-only** on transcript files.

**Context safety:** JSONL lines can be huge. Read with `sed`/`rg` ranges; never dump full tool results into chat.

## Analyze (read yourself first)

| Dimension | Look for |
|-----------|----------|
| Skill timeline | Which skills were available vs invoked; `dev-router` skipped? |
| Plan adherence | Plan/ledger paths; tasks redone after compaction |
| Repeated work | Same file edits, same failed command loops |
| Verification | "Done" without test output; skipped `verification-before-completion` |
| Stumbles | Tool errors ignored, wrong directory, sandbox surprises |
| Cost/time | Turn count, parallel subagents, oversized reads |

Split long transcripts by turn range. Discard analyst-style guesses without line cites.

## Report template

```markdown
## Problem statement
## Sessions (paths)
## Timeline (cited)
## Findings (path:line each)
## Likely process cause
## Suggested next action (skill or habit)
## What we cannot prove from transcript
```

## Hard rules

- Read-only on transcripts and git history unless user asks to change skills.
- Do not propose skill text edits in this skill — hand off to `writing-skills` with findings.
- Numbers (tokens, duration) only if present in logs or measured commands — never guess pricing.

## Boundaries

- **Always:** intake before deep reads; cite evidence.
- **Ask first:** exporting/sharing transcripts externally; filing issues upstream.
- **Never:** modify transcript files; diagnose application production incidents without codebase evidence.

## Output

Path to report file + three-line summary for the user.
