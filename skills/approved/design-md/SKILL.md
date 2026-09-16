---
name: project-design-md-adapter
description: Safe project adapter for the pinned upstream DESIGN.md skill. Use only after approved design-language evidence exists to create an agent-readable implementation contract.
license: MIT (upstream)
---
# DESIGN.md — Project Adapter

## Upstream source
- Repository: `nolly-studio/agent-skills`
- Commit: `2008e7f671eb9f55989b73f9e33cbe06e74c428a`
- Path: `skills/design-md/SKILL.md`
- License: MIT

Execution mode: `REFERENCE_ONLY`.

## Local authority
Authority: **design-language documentation for implementation**, downstream of approved Brand V1 and actual implementation evidence. It may audit existing tokens/components/docs, classify document/merge/propose mode, and prepare a living `DESIGN.md` contract.

It may NOT:
- create a design language before visual-route selection;
- restyle existing components merely to match documentation;
- overwrite Brand canon or specialist guidelines;
- copy another product's design language without approval.

## DIVINIVID use
Activate at Brand System V1 / implementation handoff. `DESIGN.md` should be one-hop discoverable by agents and express concrete tokens, budgets, typography, surfaces, motion and per-page verification rules that trace to approved Brand artifacts or real code.

## Security note
The upstream skill may reference installation workflows. This adapter does not authorize CLI/package execution or file writes outside the current approved task.