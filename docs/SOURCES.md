# Upstream sources (reference)

Superskills v1 was consolidated from these public collections. **This repo’s `SKILL.md` files are rewritten English text** — not verbatim copies. Use upstream repos for history, examples, and license terms when borrowing scripts or long excerpts.

| Repository | URL | What we took |
|------------|-----|----------------|
| obra/superpowers | https://github.com/obra/superpowers | Process skills: brainstorming, plans, executing, TDD, debugging, verification, worktrees, subagent SDD, writing-skills, diagnosing |
| mattpocock/skills | https://github.com/mattpocock/skills | Routing and teaching tone; trimmed domain-specific skills |
| addyosmani/agent-skills | https://github.com/addyosmani/agent-skills | Breadth scan; avoided duplicating one-off domain packs in v1 |
| anthropics/skills | https://github.com/anthropics/skills | Agent Skills spec alignment; `skill-creator` patterns in `writing-skills` |
| avenoxai/avenoxskills | https://github.com/avenoxai/avenoxskills | Parallel / fleet ideas lightly reflected in `subagent-driven-development` |

## Specification

- [Agent Skills specification](https://agentskills.io/specification) — `name`, `description`, folder layout.

## Consolidation rules (v1)

1. Find counterparts in all five repos before writing a new skill.
2. One primary job per skill; explicit **do not use when** pointing to the owning neighbor.
3. Sixteen skills only unless `CONSOLIDATION.md` is deliberately expanded.
4. Commands and stack live in project `AGENTS.md`, not in skills.

## Attribution when copying

If you paste scripts, prompts, or large sections from an upstream repo into this tree, add a short note in the file header or `references/` with repo name, path, and license. Prefer linking to upstream for maintenance-heavy assets.
