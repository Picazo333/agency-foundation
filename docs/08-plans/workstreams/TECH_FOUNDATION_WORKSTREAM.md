---
status: approved
owner: tech
updated: 2026-09-15
authority: canon
depends_on:
  []
---
# Workstream — Neutral Technical Foundation

## Current executor
Jules, governed by Issue #4 and the branch `tech/jules-technical-foundation`.

## Mission
Prepare neutral implementation infrastructure without prematurely building the production website.

## Early tasks
- token schema with Brand values TBD
- SVG optimization/validation/sanitization/componentization pipeline
- visual/motion/interaction sandboxes
- CSS/SVG/GSAP/scroll experiments only where justified
- reduced-motion behavior
- responsive/accessibility/performance harness
- visual regression/test baseline
- asset provenance integration
- S0-S4 maturity contract and entry/exit criteria

## Boundaries
- Experiments stay isolated in `labs/` or clearly experimental technical areas.
- Production code enters `apps/`/`packages/` only after approved specs.
- This workstream must not duplicate Issue #6 repo-hardening/CI scope except for narrow integration dependencies.
- Brand V0 values remain placeholders/TBD until approved.
- Antigravity may be used later for specialized experimentation, but it is not required to complete this foundation package.
