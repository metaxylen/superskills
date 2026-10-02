# Skill mechanics (reference)

Distilled rules for authoring skills in this repo. Full prose lives in optional `writing-for-agents` if installed.

## Invocation

| Mode | YAML | When |
|------|------|------|
| Model-invoked | default (`description` only) | Agent should discover from routing; other skills may hand off |
| User-invoked | `disable-model-invocation: true` | Slash-only; zero description load; human remembers the name |

Use model-invoked for v1 superskills routing. Use user-invoked for long slash workflows (triage, wayfinder-style) that must not bloat every turn.

## Description as pointer

- Front-load the leading verb or noun agents match on.
- One branch per distinct trigger; collapse synonyms.
- **Use when** + **Do not use when** pointing at the owning neighbor skill.

## Information hierarchy

1. In-file steps (what to do, in order).
2. In-file reference (rules consulted during steps).
3. Disclosed reference (`references/` files loaded on demand).

Push detail down the ladder so descriptions stay under 1024 characters.

## Router skills

One user-invoked router can list slash skills the human must remember. Model-invoked `dev-router` is the autonomous equivalent for vague chat.
