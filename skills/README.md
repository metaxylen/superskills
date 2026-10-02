# skills/

Sixteen active skills for v1. Each directory contains exactly one authoritative `SKILL.md`.

## Catalog

See [CONSOLIDATION.md](./CONSOLIDATION.md) for names and roles (Turkish summary table).

## Authoring

- New or changed skills: read `writing-skills/SKILL.md` and [agentskills.io](https://agentskills.io/specification).
- Before adding a seventeenth skill, update `CONSOLIDATION.md` and resolve routing overlap with `dev-router` and cousins.

## Install

From repo root (see [docs/plugins.md](../docs/plugins.md)):

```bash
./scripts/install-cursor-plugin.sh   # Cursor plugin copy
# or
./scripts/link-cursor-skills.sh      # dev symlinks — not both at once
```

Only directories listed in `CONSOLIDATION.md` are part of the plugin.
