---
name: writing-skills
description: >-
  Creates, edits, or validates skills in this repository. Use to fix skill
  triggers, tune descriptions, or validate SKILL.md. Do not use for
  application features or product debugging; use incremental-implementation or
  systematic-debugging. Turkish cues: skill yaz, skill oluştur, description
  düzelt, tetikleyici.
---

# Writing skills

## Done

- `skills/<name>/SKILL.md` validates: `name` matches folder; required frontmatter; body under ~500 lines.
- `description` states the job, activation conditions, and nearest exclusion without overlapping other v1 skills (see `CONSOLIDATION.md`).
- Optional **Turkish cues:** comma-separated triggers in `description` only (English body).
- User approved text before commit; `./tests/run-all.sh` passes.
- Update installation docs only when the install surface or layout changes.

## Spec ([agentskills.io](https://agentskills.io/specification))

```text
skills/<name>/
├── SKILL.md          # required
├── references/       # optional, on demand
├── scripts/          # optional
└── assets/           # optional
```

Frontmatter: `name`, `description` (≤1024 chars, third person). Optional: `license`, `compatibility`, `metadata`.

Use **Done**, a process, and **Boundaries** where useful. Add examples, gotchas, or an output template only when they resolve a concrete ambiguity.

Commands and stack belong in project `AGENTS.md`, not in skills unless tool-specific.

See [references/mechanics.md](references/mechanics.md) for invocation and description mechanics. For full agent-doc style (pointers, pruning) in **application** repos, link optional `writing-for-agents` after `./scripts/link-optional-skills.sh`.

## Description rules

- One primary job per skill.
- When excluding an adjacent job, name its owning skill; omit exhaustive lists of unrelated jobs.
- Never "required on every message" unless `disable-model-invocation: true` and user invokes `/skill`.
- No pasted system prompts or bulk-imported foreign skill trees.

## Before you edit

Read `CONSOLIDATION.md`, the descriptions once, and the bodies of overlapping skills. Establish a routing or behavior failure the edit should fix; keep the review scoped to those overlaps.

## Authoring loop (TDD for docs)

1. **RED** — Record one observed failure or a clearly labeled untested scenario; do not invent a failed agent run.
2. **GREEN** — Write minimal `description` + body fixing that failure.
3. **REFACTOR** — Tighten wording; add gotcha; re-check overlap with `dev-router` and cousins.

For description tuning: try phrasing against the other fifteen descriptions; adjust until one winner per vague phrase.

## Eval loop (optional)

- Check prompts that should activate the skill and near misses that should not; update the routing TSVs when descriptions change.
- Run `./tests/run-all.sh`. Its substring and synthetic routing checks do not prove live model selection; report manual or model evaluations separately.

## Install path

- Canonical source: `skills/<name>/` in this repo.
- Cursor: `scripts/install-cursor-plugin.sh` (plugin) or `scripts/link-cursor-skills.sh` (symlink dev). See `docs/plugins.md`.
- Plugin manifest: `.cursor-plugin/plugin.json` (skills auto-discovered from `skills/`).

## Boundaries

- **Always:** user approval before merge; English in repo skills unless user requests locale-specific triggers in YAML only.
- **Ask first:** new v1 skill count >16; copying entire external skill catalogs.
- **Never:** install foreign skill trees into `~/.cursor/skills`; commit secrets in fixtures.

## Output

```
Skill: skills/<name>/SKILL.md
Description: <one line summary>
Overlap check: pass | adjusted <skill>
Tests: <command or manual>
Next: commit + symlink instructions
```
