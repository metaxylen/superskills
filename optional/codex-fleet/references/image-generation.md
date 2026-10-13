# Image generation

## Contents

- [CRITICAL — Always force the imagegen tool](#critical--always-force-the-imagegen-tool)
- [Base command (image generation)](#base-command-image-generation)
- [Output handling](#output-handling)
- [Parallelization (default for ≥2 assets)](#parallelization-default-for-2-assets)
- [Sizes (gpt-image-2)](#sizes-gpt-image-2)
- [Quality (gpt-image-2)](#quality-gpt-image-2)
- [Prompt craft (gpt-image-2)](#prompt-craft-gpt-image-2)
- [Transparency](#transparency)
- [CLI fallback — when to use it](#cli-fallback--when-to-use-it)
- [Common failures and fixes](#common-failures-and-fixes)
- [End-to-end template (single asset, built-in tool)](#end-to-end-template-single-asset-built-in-tool)
- [End-to-end template (parallel batch, built-in tool)](#end-to-end-template-parallel-batch-built-in-tool)
- [End-to-end template (CLI fallback, batch from JSONL)](#end-to-end-template-cli-fallback-batch-from-jsonl)
- [Quality bar / acceptance check](#quality-bar--acceptance-check)
- [Known limits](#known-limits)


Generate real rendered images via Codex CLI's built-in `image_gen` tool, defaulting to **`gpt-image-2`** (snapshot `gpt-image-2-2026-04-21`). This is for actual painted/rendered output — backgrounds, portraits, sigils, banners, sprites, icons, hero images, photorealistic shots, mockups, infographics. Studio-grade when invoked correctly.

### CRITICAL — Always force the imagegen tool

Codex defaults to writing Python+PIL when asked to "generate an image" or "make pixel art." That produces low-fidelity procedural output (10–20KB files, no real artistic rendering). To get the real `image_gen` tool (gpt-image-2), the prompt MUST contain something like:

```
TOOL DIRECTIVE: You MUST use the built-in image generation tool (image_gen / gpt-image-2).
DO NOT write Python. DO NOT use PIL/Pillow/canvas/sharp/any drawing library.
DO NOT generate procedurally with code.
You MAY use shell commands (cp, mv, ls, find) to relocate the resulting file from
~/.codex/generated_images/ to the target output path.
If the image gen tool is unavailable, refuse and say so explicitly.
```

That last line about `cp/mv` is essential — without it, Codex over-interprets the constraint and refuses to copy the generated PNG out of its cache directory, leaving the asset orphaned.

**Alternative trigger:** Codex 0.128+ supports `$imagegen` as an explicit skill marker. Including the literal string `$imagegen` in the prompt biases Codex to invoke the official imagegen skill workflow. Use both together for maximum reliability.

### Base command (image generation)

```bash
codex exec --skip-git-repo-check --ephemeral -s danger-full-access \
  -m gpt-6-astra \
  -c model_reasoning_effort=high \
  --color never \
  "<PROMPT>" 2>&1
```

Flag breakdown:
- `-s danger-full-access` — required to write files. Image-gen tool needs this sandbox level to copy the result to disk.
- `-m gpt-6-astra` — agent model that decides to call `image_gen`. Best prompt-following for image workflows.
- `-c model_reasoning_effort=high` — default per skill policy. `xhigh`/`max` only on explicit request.
- `--ephemeral` — fresh session each call, no history pollution between image jobs.
- Respect user and project execpolicy rules; `--ignore-rules` disables those rules and is not part of the default recipe.
- `--skip-git-repo-check` — runs anywhere.
- `--color never` — clean stdout for log parsing.

### Output handling

The built-in `image_gen` tool does NOT take a target file path. Generated images land at:

```
~/.codex/generated_images/<session-id>/ig_<hash>.png
```

(`$CODEX_HOME` is `~/.codex` by default; respect `$CODEX_HOME` if the user has overridden it.)

Two ways to get them where you want them:

1. **Let Codex copy them itself.** Include the target path in your prompt and explicitly authorize `cp/mv` (see the directive block above). Codex will `find` the result and `cp` it.
2. **Find and copy yourself afterwards.** If Codex refuses to copy (over-cautious), the files are still in the cache:
   ```bash
   find ~/.codex/generated_images -type f -name '*.png' -mmin -5
   ```
   …then `cp` them to where you need them. This is the reliable fallback.

### Parallelization (default for ≥2 assets)

For multiple assets, fire each as a separate `codex exec` Bash call with `run_in_background: true`. Don't serialize — Codex sessions are independent.

```
Single message with 4 Bash tool calls, all run_in_background: true:
  codex exec [...flags...] "PROMPT_BG"        > /tmp/codex-bg.log 2>&1
  codex exec [...flags...] "PROMPT_PORTRAITS" > /tmp/codex-portraits.log 2>&1
  codex exec [...flags...] "PROMPT_SIGIL"     > /tmp/codex-sigil.log 2>&1
  codex exec [...flags...] "PROMPT_BANNER"    > /tmp/codex-banner.log 2>&1
```

After each completes, inspect the log to confirm the image-gen tool was invoked (look for `ig_<hash>.png` in the log — that's the cache path indicator) and confirm the target file exists.

**Default rule:** if generating ≥2 distinct assets, always parallelize. ONE prompt per `codex exec` call — do not stuff multiple unrelated assets into a single prompt; quality drops and recovery is harder.

**Note on `n`:** the underlying API supports `n` (1–10) for **variants of the same prompt**. Don't use `n` as a substitute for separate prompts when you want different assets — that's what parallel `codex exec` calls are for.

### Sizes (gpt-image-2)

`gpt-image-2` accepts `auto` or any `WIDTHxHEIGHT` that meets ALL of:

- Max edge ≤ **3840px**
- Both edges multiples of **16px**
- Long-edge / short-edge ratio ≤ **3:1**
- Total pixels between **655,360** and **8,294,400**
- Outputs above **2560×1440** are technically supported but flagged as experimental — quality variance is higher

Popular sizes (use these unless there's a reason not to):

| Use | Size |
|---|---|
| Square (default fast) | `1024x1024` |
| Landscape | `1536x1024` |
| Portrait | `1024x1536` |
| 2K square | `2048x2048` |
| 2K landscape (widescreen) | `2048x1152` |
| 4K landscape | `3840x2160` |
| 4K portrait | `2160x3840` |
| Auto | `auto` |

Square is fastest. Don't ask for tiny output (e.g. `256x256`) — the tool will reject it (below min-pixels). Generate at a supported size and downscale with `sips` afterwards (Windows: `pwsh -NoProfile -File skills/codex-fleet/scripts/Resize-Image.ps1 -Path in.png -Out out.png -Width 512`).

### Quality (gpt-image-2)

Four levels: `low`, `medium`, `high`, `auto`.

- `low` — fast drafts, thumbnails, candidate sweeps, "show me the rough idea"
- `medium` — fine for most preview/draft work
- `high` — **default for finals.** Final assets, dense text inside the image, tight composition, identity-sensitive edits, large outputs
- `auto` — let the model pick

The built-in tool doesn't expose `--quality` directly to the prompt, but you can ask for it ("high quality, fine detail") and the tool tends to honor it. For deterministic quality control, use the CLI fallback (see below).

### Prompt craft (gpt-image-2)

The OpenAI prompting guide is explicit: **structure prompts as scene/backdrop → subject → key details → constraints**, and state intended use to set polish level. gpt-image-2 rewards specificity in this rough order:

1. **Use case / intended surface** — "landing page hero," "tarot card icon," "game faction crest," "infographic frame"
2. **Subject + composition** — what's centered, what's around it, camera angle
3. **Material / medium** — "obsidian shard," "bronze cupped hands," "filigree gold ornament," "matte ceramic," "35mm film"
4. **Lighting / mood** — "deep amber inner glow," "cold sapphire light bleeding from cracks," "soft studio softbox"
5. **Style anchor** — "Octopath Traveler / Triangle Strategy / Disco Elysium portrait icon caliber" — these references work consistently. For photoreal: avoid "studio polish" language; prompt as if capturing a real moment.
6. **Palette** — give hex codes when colors matter: `warm orange (#ff6a3d), sapphire (#4a8eff), jade (#3dd47b)`
7. **Negative space** — "leave the upper third calm for UI overlay readability"
8. **Background instruction** — "deep midnight starfield" / "flat #00ff00 chroma-key for removal" / "warm sunset gradient"
9. **Constraints / avoid list** — "no text, no watermark, no logos" / for edits: "change only X; keep Y unchanged"

For game-asset icons / sigils: ask for "tarot card icon" or "videogame faction crest" — these style references reliably produce iconic centered compositions with ornate frames.

For atmospheric backgrounds: cinematic + painterly + name a specific game or visual ref. Avoid "pure pixel art" — you'll get blocky low-fi. Instead: "high-fidelity digital painting in the visual language of detailed pixel art" gets you the polished JRPG-screenshot look.

For text inside the image (gpt-image-2 is strong at this): put the literal text in **straight quotes**, specify font style and placement, and use `quality: high`. For tricky words: spell letter-by-letter and demand verbatim rendering.

### Transparency

For the built-in tool, request a transparent background and preserve the generated alpha. Inspect the output; do not assume the built-in path has the same limitations as a particular API model.

If an older host returns a solid background, consult its installed imagegen instructions. Use chroma-key processing or a different API model only when the user requested or confirmed that path; do not substitute it automatically.

### CLI fallback — when to use it

Use the installed imagegen CLI only when the user explicitly requests or confirms CLI/API/model controls. It requires `OPENAI_API_KEY`; built-in generation uses the subscription. File destinations, normal size or quality requests, and the word "batch" do not by themselves authorize switching to the API.

Locate the installed `image_gen.py` and read its CLI help before using the examples below. For `gpt-image-1.5`, obtain the user's agreement unless they explicitly requested that model.

Setup:

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export IMAGE_GEN="$CODEX_HOME/skills/.system/imagegen/scripts/image_gen.py"
```

Quick generate:

```bash
python "$IMAGE_GEN" generate \
  --prompt "A cozy alpine cabin at dawn" \
  --size 1024x1024 \
  --quality high \
  --out output/imagegen/alpine-cabin.png
```

Edit:

```bash
python "$IMAGE_GEN" edit \
  --image input.png \
  --prompt "Replace only the background with a warm sunset" \
  --quality high \
  --out output/imagegen/sunset-edit.png
```

True transparency (only after user confirms):

```bash
python "$IMAGE_GEN" generate \
  --model gpt-image-1.5 \
  --prompt "A clean product cutout on a transparent background" \
  --background transparent \
  --output-format png \
  --out output/imagegen/product-cutout.png
```

**Never modify `image_gen.py`.** It's bundled and updated by Codex; changes get clobbered. If something seems missing, ask the user.

**Subcommands:** `generate`, `edit`, `generate-batch`. `--dry-run` prints the API payload without calling the API or needing the key.

### Common failures and fixes

| Symptom | Cause | Fix |
|---------|-------|-----|
| Tiny PNG (5–20KB), looks like procedural pixel grid | Codex went the Python/PIL path | Add the TOOL DIRECTIVE block + `$imagegen` marker; re-fire |
| "I generated it but couldn't save to that path" | Codex refused `cp` because directive said "no drawing library" too strictly | Add `You MAY use shell commands (cp, mv) to relocate` to the directive |
| Image has a solid background instead of transparency | The host did not satisfy the request | Check the alpha channel and installed imagegen guidance; retry the built-in request before proposing another workflow |
| Empty cache directory after run | Codex refused or errored silently | Check the log file (`/tmp/codex-X.log`) — image gen may have hit content policy or rate limit |
| Wrong aspect ratio | Tool didn't honor exact dimensions | Re-prompt with one of the popular sizes (`1024x1024`, `1536x1024`, etc.); crop with `sips` if needed, or `scripts/Resize-Image.ps1 -Crop` on Windows |
| Multiple assets in one prompt — only some land on disk | Codex generated all but only copied first | Split into separate `codex exec` calls (recommended). Don't use `n` for distinct assets — `n` is for variants of one prompt |
| "size must be auto or WIDTHxHEIGHT, multiples of 16" error from CLI | Bad size for gpt-image-2 | Both edges must be multiples of 16, total pixels in [655,360 .. 8,294,400], aspect ≤ 3:1, max edge ≤ 3840 |
| "transparent backgrounds are not supported in gpt-image-2" | Tried `--background transparent` with default model | Either chroma-key workflow, or `--model gpt-image-1.5 --background transparent --output-format png` (after user confirms) |
| `input_fidelity` errors | gpt-image-2 doesn't accept it | Drop the flag — gpt-image-2 always uses high fidelity for image inputs |

### End-to-end template (single asset, built-in tool)

```bash
codex exec --skip-git-repo-check --ephemeral -s danger-full-access \
  -m gpt-6-astra \
  -c model_reasoning_effort=high \
  --color never \
  "\$imagegen
TOOL DIRECTIVE: You MUST use the built-in image generation tool (image_gen / gpt-image-2). DO NOT write Python. DO NOT use PIL/Pillow/canvas/sharp/any drawing library. DO NOT generate procedurally with code. You MAY use shell commands (cp, mv, ls, find) to relocate the resulting file from ~/.codex/generated_images/ to the target output path. If the image gen tool is unavailable, refuse explicitly.

Generate one image, save to <ABSOLUTE_TARGET_PATH>. Size: 1024x1024.

Use case: <product-mockup | ui-mockup | illustration-story | stylized-concept | photorealistic-natural | etc>
Subject: <SUBJECT>.
Composition: <COMPOSITION>.
Style: <STYLE_REFERENCE>.
Lighting/mood: <LIGHTING>.
Palette: <PALETTE_HEXES>.
Background: <BG_INSTRUCTION>.
Constraints: no text, no watermark, no logos.

Use the image generation tool. Save the PNG to the path above." \
  > /tmp/codex-asset.log 2>&1
```

(Note: the `$imagegen` marker is escaped as `\$imagegen` inside the bash double-quoted string so the shell doesn't try to expand it as a variable.)

### End-to-end template (parallel batch, built-in tool)

```bash
# Fire N jobs in parallel — one prompt per call
codex exec [...flags...] "PROMPT_BG"        > /tmp/codex-bg.log 2>&1 &
codex exec [...flags...] "PROMPT_PORTRAITS" > /tmp/codex-portraits.log 2>&1 &
codex exec [...flags...] "PROMPT_SIGIL"     > /tmp/codex-sigil.log 2>&1 &
codex exec [...flags...] "PROMPT_BANNER"    > /tmp/codex-banner.log 2>&1 &
wait

# If any didn't land in target path, recover from cache:
find ~/.codex/generated_images -type f -name '*.png' -mmin -10
# View candidates, then `cp` to target paths.
```

In an agent harness, the equivalent is to invoke each `codex exec` via Bash with `run_in_background: true`, then proceed with other work. You'll be notified per completion. Inspect each log to confirm the tool path was taken (look for `ig_<hash>.png` in the log) and confirm the target file exists.

### End-to-end template (CLI fallback, batch from JSONL)

For high-volume work where you want explicit control + API pricing:

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export IMAGE_GEN="$CODEX_HOME/skills/.system/imagegen/scripts/image_gen.py"
export OPENAI_API_KEY="<key>"

# JSONL: one job per line, each with prompt + size + quality + out
cat > tmp/imagegen/jobs.jsonl <<'EOF'
{"prompt":"alpine cabin at dawn","size":"1536x1024","quality":"high","out":"output/imagegen/cabin.png"}
{"prompt":"forest path in mist","size":"1536x1024","quality":"high","out":"output/imagegen/forest.png"}
{"prompt":"coastal cliff at sunset","size":"1536x1024","quality":"high","out":"output/imagegen/coast.png"}
EOF

python "$IMAGE_GEN" generate-batch \
  --jobs tmp/imagegen/jobs.jsonl \
  --concurrency 5
```

`--dry-run` to preview payloads without spending. Defaults: model `gpt-image-2`, concurrency 5, max 500 jobs per batch.

### Quality bar / acceptance check

After generation, always:

1. Confirm the tool invocation succeeded and the target is a readable image. File size alone does not prove generation quality.
2. View the PNG visually before declaring success — confirm composition matches the prompt.
3. If any asset is off, re-fire **that single prompt** with tightened wording rather than re-running the whole batch.

### Known limits

- **Transparency** — request it from the built-in tool; verify alpha. API-model capabilities are a separate question.
- **Text rendering** — quote literal text, specify font/placement, and visually check the output.
- **Content policy** — follow the active tool's response; do not infer refusal from a broad subject category.
- **One asset per prompt** — don't chain multiple unrelated assets into one prompt; quality drops and recovery is harder. Use parallel `codex exec` calls.
- **`input_fidelity` is fixed high** in gpt-image-2 — don't try to set it.
- **Cost awareness** — API fallback is separately billed and needs user agreement. Consult current pricing and account usage instead of cached cost or limit multipliers.
