# Optional skills (vendored)

Not part of the v1 sixteen in `skills/`. Link alongside superskills.

| Skill | Use when |
|-------|----------|
| `codex-fleet` | Codex CLI (`codex exec`), parallel lanes, worktree writes, images |
| `limit` | Claude + Codex subscription usage before large delegate runs |
| `grilling` | Relentless interview to stress-test a plan or design |
| `git-guardrails-claude-code` | Claude Code hooks blocking dangerous git commands |

## Install

```bash
./scripts/link-optional-skills.sh
```

Links into `~/.cursor/skills/`, `~/.claude/skills/`, and `~/.agents/skills/`.

```bash
./scripts/link-optional-skills.sh --unlink
```

## License

MIT vendored components: [LICENSE-MIT-vendor.txt](./LICENSE-MIT-vendor.txt), [LICENSE-MIT-mattpocock.txt](./LICENSE-MIT-mattpocock.txt).
