# Parallel fleets


A **fleet** is N `codex exec` delegates working at once. Each lane is a plain background `codex exec` process. This is pure local orchestration — you (the orchestrator agent) spawn the lanes, hand each a self-contained brief, watch their logs, and integrate their output. No control plane required.

### Operator defaults for delegate lanes

| Setting | Default | Why |
|---|---|---|
| Model | `gpt-6-astra` (`-m gpt-6-astra`) | The fleet workhorse since 2026-09-05 (replaced `gpt-5.6-sol`). Never silently downgrade. |
| Reasoning | `high` for hard/precision lanes, `medium` for routine lanes (`-c model_reasoning_effort=high`) | `xhigh`/`max` only for an explicitly heavy lane (gnarly refactors, deep debugging, gate review); `low` for cheap read lanes. astra is frontier-tier, so medium/high carries most work. |
| Sandbox | `--approve-for-me` (alone, no `-s`) for write lanes; `--sandbox read-only` for read/review lanes | Write lanes need to edit their claimed files. Only grant what the lane needs. |
| Working dir | `-C <lane dir>` | Anchor each lane in its claimed directory or worktree. |

### Spawn recipe (one lane)

```bash
caffeinate -i codex exec --skip-git-repo-check --approve-for-me \
  -C <LANE_DIR> \
  -m gpt-6-astra \
  -c model_reasoning_effort=high \
  "<SELF-CONTAINED LANE BRIEF>" > /tmp/lane-A.log 2>&1
```

Fire it with `run_in_background: true`. The brief is the lane's **entire contract** — it must state the goal, the exact files the lane OWNS, the files it must NOT touch (and which sibling owns them), the acceptance check, and how to report done/failed. A delegate can't see your conversation; everything it needs goes in the brief.

> **`caffeinate -i` (macOS).** Idle sleep can interrupt a mid-flight lane (you'll see ~5KB of output, zero edits). Wrap every spawn in `caffeinate -i` to inhibit idle sleep during the fleet; this does not guarantee operation with a closed lid. A respawn with the same brief is safe when `git status` shows no partial work.
>
> **Windows equivalent.** `caffeinate` does not exist there. Start the bundled sentinel once, in the background, *before* spawning lanes — the sleep block is thread-scoped, so wrapping each lane would release it the moment that lane exits:
>
> ```bash
> pwsh -NoProfile -File skills/codex-fleet/scripts/Invoke-KeepAwake.ps1 -Minutes 90 &
> ```
>
> The sentinel prevents idle sleep, not explicit sleep or closing the lid (see [Microsoft documentation](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate)).
>
> It prints `KEEPAWAKE_ON until=... pid=<PID>`. Kill that PID when the fleet is done, or let it expire.

### Fleet patterns (3–20 lanes)

- **Stagger the spawns** (2–5s apart): firing every lane's first model call simultaneously is a thundering herd. In a live 23-lane run, 2 lanes wedged on dead connections at startup and sat silent for 30 minutes. The stagger costs a minute; a zombie costs half an hour.
- **Real ceiling ≈ 20 concurrent `codex exec` processes** — that's RAM + OpenAI rate limits, not orchestration. Beyond that, tier and queue.
- **Tier the lanes**: quick read/explore lanes → `low`/`medium` read-only; standard write lanes → `high` `--approve-for-me`; deep refactor / gnarly debugging / review-gate lanes → `max` (`xhigh` if you want a cheaper heavy tier). One model id for the whole fleet; the tier is the effort, not the model.
- **Read lanes stay read-only**: give review/analysis lanes `--sandbox read-only` so they physically cannot edit. Escalate to a write lane if edits are needed — don't tell a read lane to patch.
- **Liveness check from the surface side**: a codex lane whose log file hasn't grown for many minutes with zero tool calls is dead regardless of the process table. Respawn it with the same brief.
- **Completions are claims, not evidence.** "Succeeded" from a lane means it *thinks* it's done. Run the lane's acceptance check yourself (targeted typecheck / lint / tests in its dir) before integrating.

### Concurrent WRITE lanes — worktree isolation (the key trick)

When multiple lanes must WRITE to the same repo at once, they'll clobber each other's saves in a shared checkout. Two proven shapes:

**A. Worktree-per-lane + one commit per lane + orchestrator cherry-picks** (best for lanes carving disjoint regions of the SAME file, or any risk of live collisions):

```bash
# Per lane, at a pinned base commit:
git worktree add --detach ../fleet-lane-A <BASE_SHA>
# (install deps / build as needed inside the worktree)
# Spawn the lane with -C ../fleet-lane-A ; brief tells it to make ONE commit when done.
# Orchestrator then cherry-picks each lane's commit onto main in completion order,
# gating (build+typecheck+test) at each pick.
```

No live collisions, linear history with each lane's commit preserved, orchestrator gates every pick. Prove the mechanics on a baseline worktree whose gate is GREEN before any lane spawns. Conflicts concentrate in append zones (import blocks, guard-list arrays) and resolve as unions; for moved code, resolve by OWNERSHIP — grep the lane's target file for the moved decl before deleting anything.

**B. Shared tree with explicit OWNS / DO-NOT-TOUCH lists** (works when lanes touch clearly disjoint files):

- Each lane brief carries an explicit OWNS list and a DO-NOT-TOUCH list naming which sibling owns what. Lanes then self-report fouls ("sibling edits present, left intact") instead of "fixing" them.
- **Shared files (barrels, CLI entry, validators) are declared append-only.** Allocate each shared file to exactly one commit at integration time.
- **Lanes never run the repo-root gate or git** — targeted tests + per-package typecheck only. The orchestrator runs the single full gate (test+typecheck+build) after ALL lanes settle, repairs cross-lane breakage (expect ~1–2 pinned-literal test failures when one lane reshapes source another lane's test pins), then commits per coherent unit.
- **A lane adding shared exports can break every other lane's build mid-flight.** If one lane edits a barrel/type file everyone imports, rebuild that package (`<your build for that package>`) so downstream lanes resolve. For long fleets, run a quiet rebuild loop (~every 2 min) so the outage window stays bounded.

### What makes a fleet run good

- The brief embeds the full contract: goal, OWNS, DO-NOT-TOUCH (+ sibling owner), acceptance check, and report format. The delegate follows the brief verbatim — put everything in it.
- **Re-verify "already fixed" claims live.** A lane that verifies a fix only against an in-memory/demo store has verified nothing — FK ordering, contention, and real-data edge cases exist only against the real backend.
- **Honest failure beats a cheerful lie.** A lane reporting "failed: sibling's mid-flight edit broke cross-package typecheck" is often fine — read the failure note; "outside my lane" usually means integrate normally and verify at the gate.
- **Expect other work on the machine.** Only act on your own fleet's lanes/logs; never reap processes you didn't spawn without inspecting them first.
