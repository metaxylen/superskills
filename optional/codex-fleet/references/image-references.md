# Image inputs and reference chains


For both general codex tasks (passing images for analysis) AND image generation (passing reference images for style/character consistency), codex supports `-i, --image <FILE>...` to attach images to the prompt context.

### THE BUG: greedy `-i` parse eats your prompt

The `-i FILE...` flag is **variadic-greedy** — without termination it consumes the prompt itself as another `<FILE>` argument and codex falls through to stdin, which is empty, and errors out:

```
Reading prompt from stdin...
No prompt provided via stdin.
```

**WRONG (silently fails):**
```bash
codex exec [opts] -i ref1.png -i ref2.png "prompt text" > log 2>&1
```

**RIGHT (use `--` separator):**
```bash
codex exec [opts] -i ref1.png -i ref2.png -- "prompt text" > log 2>&1
```

The `--` terminates the `-i` flag's greedy parse and the prompt is correctly passed as a positional argument. This is the single most important pattern for any multi-reference image-gen workflow.

### Sequential reference chaining for series consistency

When generating a series of frames where each new frame must reference the previous one (key frames of a video sequence, multi-shot scenes, character continuity across beats), chain codex calls with `&&` so each call waits for the previous output to materialize before starting:

```bash
mkdir -p output/dir && \
  codex exec [opts] -i char_sheet.png \
    -- "frame1 prompt → save to output/dir/frame1.png" > /tmp/log1 2>&1 && \
  codex exec [opts] -i char_sheet.png -i output/dir/frame1.png \
    -- "frame2 prompt → save to output/dir/frame2.png" > /tmp/log2 2>&1 && \
  codex exec [opts] -i char_sheet.png -i output/dir/frame1.png -i output/dir/frame2.png \
    -- "frame3 prompt → save to output/dir/frame3.png" > /tmp/log3 2>&1
```

This guarantees temporal/visual continuity: frame N has frame N-1 (and earlier) loaded as visual references. Each frame's prompt explicitly tells codex which attached image is the "character bible" vs the "previous frame" so the model knows what to match.

Run the whole chain as ONE background bash call (`run_in_background: true`) — you get a single notification when the entire chain completes. Per-frame failures stop the chain via `&&` short-circuit.

### Parallel non-dependent generation

For independent assets with NO continuity needed (e.g., 5 different characters in 5 different scenes), use **5 separate background bash calls in a single message** instead of chaining — much faster (5x parallel rather than serial).

### Reference image hierarchy (recommended pattern)

For viral content, character drama, multi-shot work: build a reusable reference hierarchy. Three levels:

1. **Character bible (turnaround sheet)** — 3-pose model sheet on white background, locks body / material / proportion / wardrobe. The canonical reference for ALL downstream generations of that character.
2. **Key art** — single dramatic environment shot, locks the character's persona vibe in their canonical world. Optional secondary reference for tone-matching.
3. **Stage / scene frames** — actual story-beat frames generated using the bible + previous frames as references.

**Rule of thumb when adding `-i` flags to a generation call:**
- Need character consistency? Pass the character bible.
- Need scene/environment continuity from a previous beat? Pass that previous frame.
- Need multi-character scene? Pass each character's bible.
- For style-only continuity across different scenes? Pass an earlier frame from the series as a "production-style anchor."

The model will use whichever attached images are visually relevant to your prompt's instructions. Be explicit in the prompt about which attached image plays which role ("reference 1 is the character bible, reference 2 is the immediately preceding beat").
