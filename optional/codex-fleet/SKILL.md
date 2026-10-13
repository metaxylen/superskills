---
name: codex-fleet
description: >-
  Runs codex exec for requested CLI tasks, imagegen, and parallel fleets. Use
  when the user asks to run Codex CLI or delegate work through it. Do not use
  for a CLI explanation or native image generation without a CLI request.
---

# Codex Fleet — Standalone Action Runner

> A single self-contained skill for driving the [Codex CLI](https://github.com/openai/codex) from any agent (Claude Code, Cursor, or your own harness). No external control plane required — everything here runs against a plain local `codex` install. Drop this file into `.claude/skills/codex-fleet/SKILL.md` (or your agent's skills dir) and go.
>
> Built and battle-tested by [Avenox](https://avenox.lol). Share freely.

This skill does three things and ALWAYS executes them, never describes them:

1. **General Codex CLI tasks** — code review, refactor, multi-file edits, analysis, diagnosis, anything you'd hand to a peer-AI for parallel processing.
2. **Image generation** — real rendered images via Codex's built-in `gpt-image-2` tool: backgrounds, portraits, icons, sigils, banners, UI assets, sprites, mockups, photoreal, infographics.
3. **Fleets** — spawning many `codex exec` delegates in parallel (one lane or twenty), with worktree isolation for concurrent write lanes.

## CRITICAL: This is an ACTION skill, not commentary

When invoked you MUST:

1. **Actually invoke `codex exec` via the Bash tool.** Never write instructions for the user to run themselves.
2. **Default to background execution** (`run_in_background: true`) for any task likely to take >10s. This lets the main agent continue other work in parallel while Codex runs. The harness notifies on completion.
3. **Run independent jobs in parallel within the host and account limits.** Keep dependent jobs sequential and isolate concurrent write lanes.
4. **Summarize results from logs** after each background job completes — don't dump raw stdout unless asked.

If the user's request is "use codex to X" or "run codex on X", run `codex exec ... "X"`. Don't wrap, don't paraphrase, don't ask "should I proceed" — just go.

## Load only the needed workflow

Read [runtime and defaults](references/runtime.md) before execution. User instructions and the host's permission policy take precedence over these defaults. Resolve script paths from this skill's directory, not from `references/`.

| Requested job | Read before acting |
|---|---|
| General CLI task, review, analysis, edit, or resume | [General tasks](references/tasks.md) |
| Image generation or editing through Codex CLI | [Image generation](references/image-generation.md) |
| Passing `-i` images, reference chains, or series consistency | [Image inputs and chains](references/image-references.md) |
| Several delegated tasks with lane ownership and integration | [Fleets](references/fleets.md) and [general tasks](references/tasks.md) |

For image jobs with reference inputs, read both image documents. Do not load image guidance for a code-only fleet.

Check the installed CLI and imagegen instructions when flags or tool capabilities differ from these examples. Preserve the locked model and effort defaults unless the user changes them; do not silently switch to a billed API fallback.

## Completion

Read each job's exit status and log, verify its requested output or acceptance check, and report saved paths or changes. A delegate's success message alone is not verification.

## Credits

Merged and maintained by **Avenox** — [avenox.lol](https://avenox.lol). This is a distilled, dependency-free build of an internal Codex operations skill. Feedback and improvements welcome.
