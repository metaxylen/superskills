# docs/

Documentation for the superskills repo and conventions used by its skills.

## Index

| Document | Description |
|----------|-------------|
| [plugins.md](./plugins.md) | Cursor plugin install vs symlink |
| [claude-code.md](./claude-code.md) | Claude Code install (`~/.claude/skills`) |
| [codex.md](./codex.md) | Codex app install (`~/.agents/skills`) |
| [marketplace.md](./marketplace.md) | Publish checklist (optional) |
| [templates/AGENTS.example.md](./templates/AGENTS.example.md) | Copy into application repos |
| [superskills/plans/README.md](./superskills/plans/README.md) | Implementation plan format and location |
| [superskills/specs/README.md](./superskills/specs/README.md) | Feature spec format and location |
| [superskills/research/2026-10-12-skill-simplification.md](./superskills/research/2026-10-12-skill-simplification.md) | Sources, per-change rationale, and validation for the skill cleanup |
| [superskills/research/2026-10-12-loop-control.md](./superskills/research/2026-10-12-loop-control.md) | Sources, scope, and evaluation cases for bounded plan execution |
| [superskills/research/2026-10-12-loop-engineering-evaluation.md](./superskills/research/2026-10-12-loop-engineering-evaluation.md) | Deeper primary-source research, implementation review, live Codex/Claude comparisons and limitations |
| [superskills/research/2026-10-12-cost-aware-delegation.md](./superskills/research/2026-10-12-cost-aware-delegation.md) | Why no new skill is needed, source-backed delegation gates, shared budgets and a native review observation |

## Relationship to skills

- `writing-plans` follows the project's plan path; in this repo it uses `docs/superskills/plans/`.
- `spec-driven-development` expects specs under `docs/superskills/specs/` unless the project defines another path.
- `executing-plans` and `subagent-driven-development` consume plans and optional ledgers.

Application projects may mirror this layout or override paths in chat; document overrides in the project `AGENTS.md`.
