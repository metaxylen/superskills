---
name: using-agent-skills
description: >-
  Explains how skills work, which skill to choose, installation, and skill
  slash commands. Use when the user asks which skill or workflow to use, or how
  skills load or install. Do not use merely because a concrete task mentions skills or
  workflows; use the matching specialist, writing-skills for authoring, or
  dev-router for an unclear coding request. Turkish cues: hangi skill, skill
  nasıl çalışır, superskills, workflow sırası.
---

# Using agent skills

## Done

- The user knows which skill applies (or that `dev-router` handles ambiguity).
- The agent reads the project's nearest `AGENTS.md` for commands and boundaries.
- One primary skill is active for the current step; hand off when the job changes.
- This library's `SKILL.md` files are authoritative for superskills.

## How this library works

Skills live under `skills/<name>/SKILL.md`. Cursor loads **name** and **description** for every skill at session start. The body loads only after a skill is selected.

Install v1: `./scripts/link-all-skills.sh` (or per-host scripts in `scripts/README.md`). Optional extras: `optional/` + `./scripts/link-optional-skills.sh`. Plugin copy: `docs/plugins.md`. Do not duplicate plugin + symlink for the same names.

Progressive disclosure:

1. **Description** — routing signal only (what + when + when not).
2. **Body** — steps after the skill is active.
3. **references/** — optional; only when the body points to them.

Project commands (`test`, `build`, `lint`) belong in the **project** `AGENTS.md`, not inside skills.

## Catalog and routing

For the sixteen v1 roles, read [CONSOLIDATION.md](../CONSOLIDATION.md). For ambiguous coding requests, read the routing table in [dev-router](../dev-router/SKILL.md). Optional workflows are listed in [optional/README.md](../../optional/README.md).

## Choosing a skill

When multiple skills match:

1. **Process before implementation** (e.g. `systematic-debugging` before editing code for a failure).
2. **One primary skill** per step; hand off explicitly in one line, then follow that skill's body.
3. If still tied, ask **one** clarifying question with two concrete options; then stop.

Do **not** stack "mandatory on every message" behavior (that causes token bloat and wrong activations).

Read the selected skill when first needed. Reuse its loaded instructions during the task; re-read if the file changes or its contents are no longer available in context. Surface material assumptions and ask about conflicts that change the requested outcome.

## Boundaries

- **Always:** Prefer project `AGENTS.md` for tool commands; prefer one skill per step.
- **Ask first:** Adding a new skill to the v1 set; changing another skill's description for routing.
- **Never:** Bulk-import external skill catalogs into this repo; paste system prompts as skills; run destructive git commands unless the user asked.

## Output

When this skill is invoked to answer "which skill?":

```
Skill: <name>
Why: <one sentence>
Next: <read SKILL.md path or hand off to dev-router>
AGENTS.md: <path or "none — read package manifest">
```
