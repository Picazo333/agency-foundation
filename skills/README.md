# Project Skills Registry

This directory contains **governed capability adapters**, not an unrestricted plugin sandbox.

## Why this exists
The project should be able to reuse proven external Skills without depending on conversational memory or silently trusting whatever version happens to be latest upstream.

Each approved Skill is:
- tied to an original upstream source;
- pinned to an exact commit/version;
- assigned a narrow authority and allowed use cases;
- subordinate to `AGENTS.md`, project canon, and task/workstream scope;
- safe-by-default: executable behavior is disabled unless explicitly approved.

See `docs/00-meta/capability-governance.md` before adding or updating capabilities.

## Layout
- `registry.yaml` — machine/human-readable inventory and provenance.
- `approved/<skill>/SKILL.md` — local adapter defining how this project may use the pinned upstream Skill.

The adapters intentionally do **not** copy arbitrary upstream executables or auto-run installers. They direct agents to the exact pinned upstream Skill and define local safety/authority boundaries.

## Invocation modes
1. **Reference mode (default):** read/apply the pinned upstream methodology; do not execute its installer, shell, binary, MCP, OAuth, or external upload flows.
2. **Execution mode:** allowed only after explicit human approval under the Tier 3 intake rules.

## Update rule
Never replace a pinned commit with `latest` automatically. Review upstream changes first, then update `registry.yaml` and the adapter in a dedicated PR.
