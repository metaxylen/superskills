# Cursor plugin (superskills)

This repo is a **Cursor Plugin**: manifest at `.cursor-plugin/plugin.json`, skills at `skills/<name>/SKILL.md`. Manifest includes `"skills": "./skills/"` (same pattern as [obra/superpowers](https://github.com/obra/superpowers)); Cursor discovers each folder with `SKILL.md`. We do not ship superpowers-style `hooks` in v1.

When changing packaging, run `./scripts/check-upstream.sh` and read [UPSTREAM-WORKFLOW.md](./UPSTREAM-WORKFLOW.md).

## Install (plugin path)

```bash
./tests/skill-frontmatter.sh          # optional but recommended
./scripts/install-cursor-plugin.sh
```

Then **Developer: Reload Window** and open **Customize → Skills**. You should see the `superskills` plugin and its skills.

Enterprise: admins may need **Allow Local Plugin Imports** enabled.

### Uninstall

```bash
./scripts/install-cursor-plugin.sh --remove
```

Reload Cursor afterward.

## Install (symlink path — development)

While editing skills in this repo, symlinks update Cursor immediately without recopying:

```bash
./scripts/link-cursor-skills.sh
```

Targets `~/.cursor/skills/<name>` → `skills/<name>` in the repo.

## Pick one method

| Method | Path | Best for |
|--------|------|----------|
| **Plugin copy** | `~/.cursor/plugins/local/superskills/` | Testing the real plugin layout; marketplace-like install |
| **Symlink** | `~/.cursor/skills/` | Daily development on this repo |

Using **both** for the same skill names can duplicate skills in the UI and confuse routing. Unlink or remove the other install before switching.

## What we removed (v1)

Empty stubs for other assistants (`.claude-plugin`, `.codex-plugin`, etc.) were deleted. **Cursor-only** packaging for v1; portable `skills/` remain standard [Agent Skills](https://agentskills.io/specification) markdown.

## Marketplace (later)

Publishing to Cursor Marketplace is a separate step (team marketplace, versioning, review). Local install above is enough for personal use.
