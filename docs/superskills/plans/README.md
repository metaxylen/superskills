# Implementation plans

**Path pattern:** `docs/superskills/plans/YYYY-MM-DD-<feature>.md`

Created by the `writing-plans` skill after brainstorming or an approved spec. Executed by `executing-plans` (inline) or `subagent-driven-development` (per-task review).

## Required header

```markdown
# [Feature] implementation plan

**Goal:** …
**Architecture:** …
**Spec:** docs/superskills/specs/<feature>.md
**Executor:** executing-plans | subagent-driven-development

## Global constraints
- …

## Review focus
- …
```

## Tasks

Each task should be independently verifiable (test command or observable behavior). Include TDD steps when behavior changes.

## Ledger

During execution, agents may create `<plan-stem>-ledger.md` beside the plan (same basename, `-ledger` suffix) for rulings, resume state, and completed task lines. Do not commit ledgers unless they contain durable decisions worth keeping.

## Example filenames

- `2026-10-02-link-cursor-skills.md`
- `2026-10-15-skill-frontmatter-tests.md`
