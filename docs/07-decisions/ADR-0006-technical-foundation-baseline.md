# ADR 0006: Technical Foundation Baseline & Labs

## Status
Accepted

## Context
We need to establish a neutral technical foundation (Issue #4) that prepares the repository for a future website implementation without prematurely locking into a specific JavaScript framework, styling solution, or finalizing brand identity. We need safe spaces to experiment with visuals, motion, and interaction.

## Decision
1. **Neutral Labs:** We will use plain HTML/CSS/JS for initial lab environments (`labs/visual`, `labs/motion`, `labs/interaction`, `labs/svg`) to ensure zero lock-in and minimal dependencies while validating concepts.
2. **SVG Sanitization:** All SVGs entering the system must pass a sanitization pipeline (stripping `<script>` and inline event handlers) before optimization. A Node.js proof-of-concept (`scripts/tech-labs/svg-optimizer.js`) demonstrates this requirement.
3. **No Premature Architecture:** We will defer installing heavy E2E (Playwright) or CI (Lighthouse) tools until a primary web framework is selected, opting instead to document the intended strategy (`PERFORMANCE_A11Y_STRATEGY.md`, `VISUAL_REGRESSION.md`).
4. **Token Schema:** We define the structure for design tokens (`packages/design-tokens/src/schema.json`) but explicitly set all values to "TBD" until Brand V1 is approved.

## Consequences
- **Positive:** We maintain a lean repository. The team can experiment safely. Brand and strategy teams are not blocked by technical assumptions.
- **Negative:** Lab components built in plain HTML/JS will eventually need to be rewritten or adapted into the chosen framework (e.g., React/Vue) once architecture is finalized.
