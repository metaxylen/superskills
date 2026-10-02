# docs/

Documentation for the superskills repo and conventions used by its skills.

## Index

| Document | Description |
|----------|-------------|
| [plugins.md](./plugins.md) | Cursor plugin install vs symlink |
| [marketplace.md](./marketplace.md) | Publish checklist (optional) |
| [templates/AGENTS.example.md](./templates/AGENTS.example.md) | Copy into application repos |
| [superskills/plans/README.md](./superskills/plans/README.md) | Implementation plan format and location |
| [superskills/specs/README.md](./superskills/specs/README.md) | Feature spec format and location |

## Relationship to skills

- `writing-plans` writes to `docs/superskills/plans/`.
- `spec-driven-development` expects specs under `docs/superskills/specs/` unless the project defines another path.
- `executing-plans` and `subagent-driven-development` consume plans and optional ledgers.

Application projects may mirror this layout or override paths in chat; document overrides in the project `AGENTS.md`.
