# Optional skills (vendored)

Not part of the v1 sixteen in `skills/`. Extra capabilities you can link alongside superskills.

| Skill | Use when |
|-------|----------|
| `codex-fleet` | Run Codex CLI (`codex exec`), parallel lanes, worktree-isolated writes, image generation |
| `limit` | Show Claude + Codex subscription usage before large delegate runs |

## Install

```bash
./scripts/link-optional-skills.sh
```

Links into `~/.cursor/skills/`, `~/.claude/skills/`, and `~/.agents/skills/` (skips missing parent dirs).

Uninstall symlinks only:

```bash
./scripts/link-optional-skills.sh --unlink
```

## License

Vendored content is MIT — see [LICENSE-MIT-vendor.txt](./LICENSE-MIT-vendor.txt). Do not merge these into the v1 catalog without updating routing tests.
