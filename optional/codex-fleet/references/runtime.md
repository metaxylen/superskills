# Runtime and defaults

## Prerequisites

- Codex CLI installed and authenticated. Check `codex --version` and `codex exec --help` for supported flags; model and effort availability depend on the account and installed version.
- For the image-gen **CLI fallback** and `gpt-image-1.5` transparency path only: `OPENAI_API_KEY`. The built-in `image_gen` tool uses your Codex subscription and needs no key.

## Platform notes

Everything in this file is written as bash and assumes a Unix-shaped shell. That holds on
macOS and Linux natively, and on Windows through Git Bash — `/tmp`, `~`, `find -mmin`,
redirections and `$CODEX_HOME` all resolve there. Remove the macOS-only `caffeinate -i` prefix from each Windows spawn and start the sentinel below first. Linux users must also omit that prefix and supply their own sleep inhibitor if needed.

Two macOS binaries used below have no Windows equivalent. This skill ships replacements:

| Need | macOS | Windows |
|---|---|---|
| Stop the machine sleeping mid-fleet | `caffeinate -i` | `scripts/Invoke-KeepAwake.ps1` |
| Downscale / centre-crop a render | `sips -z` / `sips -c` | `scripts/Resize-Image.ps1` |

Both replacements are plain PowerShell against the .NET base library
(`SetThreadExecutionState`, `System.Drawing`) — no install, no ImageMagick, no persistent
system setting changed. Run either with `-?` for full help. They are additive: every macOS
instruction in this file is unchanged, and macOS users should keep using `caffeinate` and
`sips`.

Windows also needs `pwsh` (PowerShell 7+) on PATH for the two scripts. The rest of the skill
needs only Codex CLI and Git Bash.

## Defaults (locked in)

| Setting | Value | When to override |
|---|---|---|
| Model | `gpt-6-astra` | `-m <model>` only if user specifies. History: gpt-5.5 → gpt-5.6-sol → gpt-6-astra (2026-09-05) |
| Reasoning effort | `high` for hard/precision lanes, `medium` for routine lanes | `xhigh`/`max` ONLY for an explicitly heavy lane ("use xhigh", "max reasoning", "deep"); `low` for cheap read lanes; `ultra` is opt-in because it enables OpenAI's automatic task delegation |
| Service tier | **standard — fast is OFF** | see the note below; opt in per-call only |
| Sandbox | `read-only` | `workspace-write` for edits; `danger-full-access` for image gen or network (ask first) |
| `--skip-git-repo-check` | always | always |
| Diagnostics | preserve stdout and stderr in the job log | redact secrets before summarizing |
| `--color never` | recommended | when you need to grep stdout cleanly |

Reasoning levels available on `gpt-6-astra`: `low`, `medium`, `high`, `xhigh`, `max`, `ultra`. astra is a frontier-tier model, so `medium`/`high` is enough for most lanes; reserve `xhigh`/`max` for a lane whose brief justifies it. The model's own cache default is `medium`, so always pass the effort explicitly.

**Generation-6 lineup.** All three tiers moved to generation 6; `-m` any of them:

| Model | Successor of | Use it for |
|---|---|---|
| `gpt-6-astra` | `gpt-5.6-sol` as fleet default | **the default** — every lane unless the user names another model |
| `gpt-6-sol` | `gpt-5.6-sol` | the sol tier, when the user asks for sol by name |
| `gpt-6-luna` | `gpt-5.6-luna` | the cheap read tier — context gathering, inventory sweeps, mechanical edits against a verified spec |

Smoke-verified 2026-09-26 on codex-cli 0.155.0: all three answer `codex exec -m <id>`, and an unknown `gpt-6-*` id is rejected with HTTP 400, so a green smoke means the id is real. The `gpt-5.6-sol` / `gpt-5.6-luna` ids are still served, but pin the generation-6 ids in new briefs.

> **Fast tier is OFF by default — do not add it.** `-c service_tier=fast -c fast_default_opt_out=false` buys ~1.5× speed at ~2.5× rate cost. That trade is wrong for how this skill is used: everything here is background-first and parallel, so nobody is staring at a single lane's latency, and burning 2.5× rate on twenty lanes drains your limits for no wall-clock gain. Standard tier gives you the same quality plus rate-limit headroom. Every example in this file omits it deliberately. Opt in per-call only when a human is actively blocked on one foreground result — never for fleets, never as a global default.
