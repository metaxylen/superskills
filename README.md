# superskills

Personal [Agent Skills](https://agentskills.io/specification) library for Cursor: sixteen merged workflows for planning, implementation, testing, review, git, and meta skill authoring.

## Quick start

1. Clone this repo (or keep it at `~/Desktop/superskills`).
2. Install into Cursor — **choose one**:

   **Plugin (recommended for “real” install):**

   ```bash
   ./scripts/install-cursor-plugin.sh
   ```

   Copies `.cursor-plugin/` and `skills/` to `~/.cursor/plugins/local/superskills/`. Reload the Cursor window.

   **Symlink (recommended while editing skills here):**

   ```bash
   ./scripts/link-cursor-skills.sh
   ```

   Links `skills/<name>/` into `~/.cursor/skills/<name>`. Do not use both methods at once for the same names.

   Details: [docs/plugins.md](docs/plugins.md).

3. In any **application** project, add an `AGENTS.md` with test/build/lint commands. Skills read that file; they do not hardcode your stack.

## Layout

| Path | Purpose |
|------|---------|
| `skills/` | v1 skill set — one `SKILL.md` per folder; see `skills/CONSOLIDATION.md` |
| `docs/` | Plugin install, specs, and implementation plans for this repo |
| `.cursor-plugin/` | Cursor Plugin manifest (`plugin.json`) |
| `scripts/` | `install-cursor-plugin.sh`, `link-cursor-skills.sh` |
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

## Quality check

```bash
./tests/run-all.sh
```

Manual Cursor routing: [tests/routing-manual-test.md](tests/routing-manual-test.md). App `AGENTS.md` template: [docs/templates/AGENTS.example.md](docs/templates/AGENTS.example.md).

## License

Private personal repo unless you add a `LICENSE` file.
