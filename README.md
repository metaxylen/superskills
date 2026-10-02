# superskills

Personal [Agent Skills](https://agentskills.io/specification) library for Cursor: sixteen merged workflows for planning, implementation, testing, review, git, and meta skill authoring.

## Quick start

1. Clone this repo (or keep it at `~/Desktop/superskills`).
2. Install skills into Cursor:

   ```bash
   ./scripts/link-cursor-skills.sh
   ```

   This symlinks each folder under `skills/<name>/` into `~/.cursor/skills/<name>`. Restart Cursor or start a new agent chat so descriptions reload.

3. In any **application** project, add an `AGENTS.md` with test/build/lint commands. Skills read that file; they do not hardcode your stack.

## Layout

| Path | Purpose |
|------|---------|
| `skills/` | v1 skill set — one `SKILL.md` per folder; see `skills/CONSOLIDATION.md` |
| `docs/` | Sources, specs, and implementation plans for work tracked in this repo |
| `scripts/` | `link-cursor-skills.sh` and future tooling |
| `tests/` | Skill validation (frontmatter, routing) when added |
| `documentations/` | Personal archive — not part of the skill workflow |

## Routing

- Vague coding request → `dev-router`
- Unsure how skills fit together → `using-agent-skills`
- Bad session post-mortem → `diagnosing-workflow`

Full catalog: [skills/CONSOLIDATION.md](skills/CONSOLIDATION.md).

## Plans and specs (this repo)

When using superskills on itself or as a template:

- Plans: `docs/superskills/plans/YYYY-MM-DD-<feature>.md`
- Specs: `docs/superskills/specs/<feature>.md`

See [docs/README.md](docs/README.md).

## Provenance

Merged ideas from five public skill collections; see [docs/SOURCES.md](docs/SOURCES.md). Skill text in this repo is original English; upstream repos are reference only.

## License

Private personal repo unless you add a `LICENSE` file. Respect upstream licenses if you copy material from sources listed in `docs/SOURCES.md`.
