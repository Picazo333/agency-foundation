# Jules Handoff — Issue #4 (Neutral Technical Foundation)

## Issue / objective completed
GitHub Issue #4 — Neutral technical foundation + labs.

## Inputs used
- `docs/09-handoffs/jules/START_PROMPT_TECH_FOUNDATION.md`
- `docs/08-plans/workstreams/TECH_FOUNDATION_WORKSTREAM.md`

## Outputs produced

### STABLE_FOUNDATION
- Neutral design-token schema established (`packages/design-tokens/src/schema.json`) with all unresolved values kept as `TBD`.
- Implementation-facing asset provenance consumer contract created (`packages/assets/provenance.json`) and aligned to the Asset Factory license-state vocabulary.
- Security notes baseline extended (`infra/SECURITY_NOTES.md`).
- Performance/accessibility strategy documented (`docs/tech/PERFORMANCE_A11Y_STRATEGY.md`) using current Core Web Vitals terminology and WCAG 2.2 AA as the production baseline.
- Visual-regression strategy documented (`docs/tech/VISUAL_REGRESSION.md`).
- S0-S4 maturity model defined (`docs/tech/MATURITY_MODEL.md`), with S4 explicitly optional rather than a mandatory endpoint.
- `ADR-0011-neutral-technical-foundation-baseline.md` records the approved baseline and its reopen conditions.

### EXPERIMENTAL
- Visual Lab (`labs/visual/index.html`) demonstrating neutral token mapping.
- SVG Lab (`labs/svg/`) plus a deliberately limited inspection POC (`scripts/tech-labs/svg-optimizer.js`). The regex demo is explicitly **not** a production SVG sanitizer.
- Motion Lab (`labs/motion/index.html`) validating CSS motion and reduced-motion behavior.
- Interaction Lab (`labs/interaction/index.html`) for framework-neutral behavior experiments.

### REJECTED / DEFERRED
- Production framework selection remains deferred.
- Heavy E2E/performance suites (for example Playwright/Lighthouse CI as required gates) remain deferred until an actual application/runtime exists.
- Regex-based SVG sanitization is rejected as a production security control; a vetted parser/sanitizer policy is still required.

### BLOCKED_BY_BRAND_STRATEGY
- Final token values (color, typography, spacing semantics, etc.) remain unresolved until Brand V1 approval.
- Final production UI components remain blocked on architecture/implementation decisions.

## Files changed
- `packages/design-tokens/`
- `packages/assets/provenance.json`
- `labs/visual/`, `labs/svg/`, `labs/motion/`, `labs/interaction/`
- `scripts/tech-labs/svg-optimizer.js`
- `docs/tech/`
- `infra/SECURITY_NOTES.md`
- `infra/testing/lighthouserc.json` (non-enforced stub)
- `docs/07-decisions/ADR-0011-neutral-technical-foundation-baseline.md`
- this handoff

## Intentionally not changed
- Brand or Strategy decisions.
- Production framework or component library.
- Root dependency manifest / production dependencies.
- Brand token values.

## Validation / review notes
- Lab files are experimental evidence, not production artifacts.
- The SVG POC demonstrates only the included fixtures; it does not confer a security guarantee.
- Performance/a11y guidance was updated during review to current LCP/INP/CLS and WCAG 2.2 terminology.
- The ADR was renumbered to `ADR-0011` to avoid collision with the already-integrated Agency Master Plan ADR range `0006-0010`.

## PR / integration
Original Jules task PR: #13, targeting the prepared technical-foundation branch. Final integration to `main` must preserve the current mainline ADR index and other concurrently merged governance work.

## Risks / gaps
- Lab HTML/JS will likely be replaced or ported after production architecture selection.
- The production SVG sanitizer/optimizer remains unselected.
- Synthetic performance targets are not yet calibrated against a real preview/runtime.
- Asset provenance schemas must remain aligned with the generator-agnostic Asset Factory contract as that contract evolves.

## Recommended next action
- Keep these labs as neutral evidence while Brand V0/V1 evolves.
- After Brand V1 and web requirements converge, select the production frontend architecture and promote only proven patterns through an explicit implementation PR.
