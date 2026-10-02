# Upstream workflow (mandatory)

Before changing **any** `skills/*/SKILL.md`, **plugin manifest**, install scripts, or consolidation docs, scan all five source repos and note what you merged or intentionally skipped.

## Repositories

| Repo | URL | Quick paths |
|------|-----|-------------|
| obra/superpowers | https://github.com/obra/superpowers | `skills/`, `.cursor-plugin/plugin.json`, `hooks/` |
| mattpocock/skills | https://github.com/mattpocock/skills | `skills/engineering/`, `.claude-plugin/plugin.json` |
| addyosmani/agent-skills | https://github.com/addyosmani/agent-skills | `skills/`, `plugin.json`, `hooks/` |
| anthropics/skills | https://github.com/anthropics/skills | `skills/`, `template/`, `spec/` |
| avenoxai/avenoxskills | https://github.com/avenoxai/avenoxskills | `skills/`, `tests/` |

## Checklist (every change batch)

1. **Find counterparts** — same job name or closest skill in each repo (use GitHub search or `rg` on a local clone).
2. **Diff intent** — description routing, steps, boundaries, gotchas.
3. **Merge decision** — take, adapt, or skip; write one line in commit message or plan ledger.
4. **Overlap** — ensure `do not use when` still points to the right v1 neighbor (`CONSOLIDATION.md`).
5. **Run** `./tests/skill-frontmatter.sh` after skill or plugin JSON edits.

## Local clones (optional)

```bash
./scripts/check-upstream.sh          # remote HEAD pointers + manifest versions
./scripts/check-upstream.sh --clone  # shallow clone under .upstream/ (gitignored)
```

## When skipping upstream

Allowed only for pure typo fixes or Turkish cue tweaks that do not change English workflow. Everything else: at least open the superpowers + anthropic counterpart on the web.
