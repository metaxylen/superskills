# Claude Code

The same `skills/<name>/SKILL.md` files work in **Claude Code** (terminal or desktop). Cursor install scripts do not apply.

## Personal install (recommended)

```bash
./scripts/link-claude-skills.sh
```

Targets `~/.claude/skills/<name>/` on macOS.

If the skills folder was empty when Claude Code started, run **`/reload-skills`** or restart the app. Check with **`/skills`**.

## Project-scoped skills

Alternatively, symlink or copy into **your app repo**:

`.claude/skills/<name>/SKILL.md`

Only that repository’s sessions see them.

## Usage

- Implicit: Claude matches your message to each skill `description` (including Turkish cues).
- Explicit: `/skill-name` when supported (see Claude Code skills docs).

## Application projects

Use [templates/AGENTS.example.md](./templates/AGENTS.example.md) in app repos for test/build commands.

## One source, multiple hosts

| Tool | Script | Target |
|------|--------|--------|
| Cursor | `link-cursor-skills.sh` | `~/.cursor/skills/` |
| Claude Code | `link-claude-skills.sh` | `~/.claude/skills/` |
| Codex app | `link-codex-skills.sh` | `~/.agents/skills/` |

All point at this repo’s `skills/` directory.
