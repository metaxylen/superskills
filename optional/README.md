# Optional skills (vendored)

Not part of the v1 sixteen in `skills/`. Link alongside superskills.

## Fleet and limits

| Skill | Use when |
|-------|----------|
| `codex-fleet` | Codex CLI (`codex exec`), parallel lanes, worktree writes, images |
| `limit` | Claude + Codex subscription usage before large delegate runs |

## Design and planning

| Skill | Use when |
|-------|----------|
| `grilling` | Relentless interview to stress-test a plan or design |
| `domain-modeling` | `GLOSSARY.md`, ADRs, ubiquitous language |
| `codebase-design` | Deep modules, seams, interface depth (shared vocabulary) |

## Engineering workflow

| Skill | Use when |
|-------|----------|
| `code-review` | Two-axis review since a fixed point (Standards + Spec, parallel sub-agents) |
| `diagnosing-bugs` | Hard bugs or perf after `systematic-debugging` stalls |
| `research` | Primary-source investigation saved as Markdown in the repo |

## Agent environment and docs

| Skill | Use when |
|-------|----------|
| `writing-for-agents` | Skills, `AGENTS.md`, pointers (app repos—not superskills catalog) |
| `retro` | Session retro: checks, navigation, AGENTS.md bloat (often slash-only) |
| `handoff` | Handoff doc for the next agent session |
| `wait-what` | Re-pitch last message in STE + glossary |
| `git-guardrails-claude-code` | Claude Code hooks blocking dangerous git commands |

`code-review` may reference an issue tracker workflow in the target repo; without one, use the Spec axis with a spec file path or commit messages only.

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
