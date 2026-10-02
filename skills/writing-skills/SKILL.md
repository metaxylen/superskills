---
name: writing-skills
description: >-
  Creates or edits skills in this repo per Agent Skills spec with testable
  descriptions and concise bodies. Use when adding a skill to superskills,
  changing a description for routing, or authoring references scripts. Use when
  the user asks to create a skill, fix skill triggers, or validate SKILL.md.
  Do not use for normal application feature work or debugging product code—use
  incremental-implementation or systematic-debugging instead. Turkish cues: skill yaz,
  skill oluştur, description düzelt, tetikleyici.
---

# Writing skills

## Done

- `skills/<name>/SKILL.md` validates: `name` matches folder; required frontmatter; body under ~500 lines.
- `description` has **use when** and **do not use when** without overlapping other v1 skills (see `CONSOLIDATION.md`).
- Optional **Turkish cues:** comma-separated triggers in `description` only (English body).
- User approved text before commit; `tests/skill-frontmatter` or manual checklist run when available.
- Symlink target documented in root `README.md` when skill should load in Cursor.

## Spec ([agentskills.io](https://agentskills.io/specification))

```text
skills/<name>/
├── SKILL.md          # required
├── references/       # optional, on demand
├── scripts/          # optional
└── assets/           # optional
```

Frontmatter: `name`, `description` (≤1024 chars, third person). Optional: `license`, `compatibility`, `metadata`.

Body sections (this repo): **Done**, **Steps** or process, **Boundaries**, **Gotchas**, **Output**.

Commands and stack belong in project `AGENTS.md`, not in skills unless tool-specific.

## Description rules (avoid Superpowers overlap bugs)

- One primary job per skill.
- **Do not use when** must point to the skill that owns the adjacent job.
- Never "required on every message" unless `disable-model-invocation: true` and user invokes `/skill`.
- No pasted system prompts or whole third-party catalogs.

## Authoring loop (TDD for docs)

1. **RED** — Note how an agent fails without the skill (one scenario).
2. **GREEN** — Write minimal `description` + body fixing that failure.
3. **REFACTOR** — Tighten wording; add gotcha; re-check overlap with `dev-router` and cousins.

For description tuning: try phrasing against the other fifteen descriptions; adjust until one winner per vague phrase.

## Anthropic skill-creator alignment

- Draft → test prompts → revise → expand tests when stable.
- Evals are optional for personal sets; required before adding to shared v1 list.

## Install path

- Canonical: `~/Desktop/superskills/skills/` (this repo).
- Cursor loads: symlink or copy into `~/.cursor/skills/<name>` (see `scripts/link-cursor-skills.sh` when implemented).

## Boundaries

- **Always:** user approval before merge; English in repo skills unless user requests locale-specific triggers in YAML only.
- **Ask first:** new v1 skill count >16; copying licensed repos verbatim.
- **Never:** dump Osmani/Pocock trees into `~/.cursor/skills`; commit secrets in fixtures.

## Output

```
Skill: skills/<name>/SKILL.md
Description: <one line summary>
Overlap check: pass | adjusted <skill>
Tests: <command or manual>
Next: commit + symlink instructions
```
