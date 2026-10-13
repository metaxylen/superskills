# General Codex tasks


### Base command

```bash
codex exec --skip-git-repo-check \
  -m gpt-6-astra \
  -c model_reasoning_effort=high \
  --sandbox read-only \
  "<PROMPT>" 2>&1
```

### Sandbox quick reference

| Use case | Flags |
|---|---|
| Read-only review / analysis / diagnosis (default) | `--sandbox read-only` |
| Apply local edits | `--approve-for-me` (alone — do NOT add `--sandbox`/`-s`) |
| Network access or broad system access | `--sandbox danger-full-access` (confirm with user first) |

> **Version-dependent flags:** use `codex exec --help` from the installed CLI rather than assuming `--full-auto` or `--approve-for-me` is available. Use `--approve-for-me` alone when selecting its automatically reviewed workspace-write mode; do not combine it with `--sandbox`/`-s`.

For a working dir other than CWD: add `-C <DIR>`.
For escalated reasoning: replace `model_reasoning_effort=high` with `=xhigh` or `=max` (explicitly heavy lanes only).

### Background-first invocation pattern

Run any non-trivial codex task in the background. Don't block the main thread:

```
Bash tool call:
  command: codex exec --skip-git-repo-check -m gpt-6-astra \
           -c model_reasoning_effort=high \
           --sandbox read-only \
           "Review src/foo.ts for race conditions and report findings." 2>&1
  run_in_background: true
```

Then continue other work. When the background notification fires, read the log/output and summarize.

For tasks where you genuinely need the result before doing anything else (rare), run foreground.

### Parallelization (the default for multiple jobs)

If the user asks for N independent codex investigations, run separate background jobs within the available concurrency and account limits. Jobs that depend on each other stay sequential.

Example: "have codex review the contracts AND the backend AND the frontend" → 3 parallel codex jobs, not sequential.

### Resume

To continue a previous session (preserves model, reasoning, sandbox of the original):

```bash
echo "follow-up prompt" | codex exec --skip-git-repo-check resume --last 2>&1
```

When resuming, **do not pass `-m`, `-c model_reasoning_effort`, or `--sandbox`** — they inherit. Only add flags if the user is explicitly changing the configuration.

### Critical evaluation of Codex output

Codex runs on OpenAI's models with their own training cutoffs. Treat it as a peer, not an authority:

- Trust your own knowledge when confident; push back on Codex claims you know to be wrong.
- Verify via web search or live docs when uncertain — especially for model names, recent library versions, post-cutoff API changes.
- For substantive disagreements, resume and discuss as a peer:
  ```bash
  echo "I disagree with [X] because [Y]. What's your take?" \
    | codex exec --skip-git-repo-check resume --last 2>&1
  ```
- Frame as discussion, not correction. Either AI can be wrong. If genuine ambiguity remains, surface it to the user.

### Error handling

- If `codex --version` or `codex exec` exits non-zero, stop and report. Do not retry blindly.
- High-impact flags (`--approve-for-me`, `--sandbox danger-full-access`, `--dangerously-bypass-approvals-and-sandbox`) require explicit user OK before first use in a session — after that you can keep using them within the same task scope.
