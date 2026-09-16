# Performance and Accessibility Strategy

This document defines the neutral foundation's current quality targets without prematurely binding the project to a production framework or heavy test stack.

## Performance baseline

Use the current Core Web Vitals model:

- **LCP (Largest Contentful Paint):** target `<= 2.5s` at the 75th percentile.
- **INP (Interaction to Next Paint):** target `<= 200ms` at the 75th percentile.
- **CLS (Cumulative Layout Shift):** target `<= 0.1` at the 75th percentile.

These are production-facing goals, not claims that the current labs satisfy field metrics. Field data should take precedence over synthetic scores once traffic exists.

### Synthetic / CI targets
- Lighthouse categories should target strong results (initially `>= 0.90`) once a stable preview URL and repeatable CI environment exist.
- Do **not** turn the current `infra/testing/lighthouserc.json` stub into a required merge gate until the app URL/start command, runtime and variance budget are defined.
- Asset formats, dimensions and compression should be selected to meet actual delivery needs; prefer modern raster formats where appropriate and sanitize/validate SVG before production use.

## Accessibility baseline

Production surfaces should target **WCAG 2.2 AA**.

Minimum expectations include:
- semantic HTML before ARIA;
- full keyboard operability for interactive controls;
- visible and intentional focus states;
- accessible names/instructions for controls;
- sufficient color contrast;
- responsive text/layout without loss of content or function;
- `prefers-reduced-motion` behavior for non-essential animation and a non-motion equivalent where motion communicates state;
- touch targets and interaction patterns appropriate to target devices.

Accessibility is a design/implementation requirement, not a final audit-only phase.

## Tooling (future implementation)

Tooling remains conditional on the selected production architecture:

1. **Lighthouse CI** — synthetic performance/accessibility/best-practice regression checks against a stable preview.
2. **axe-core + Playwright** — automated accessibility checks inside browser/E2E coverage where a browser test stack exists.
3. **Framework-specific linting** (for example `eslint-plugin-jsx-a11y` in React ecosystems) — only if relevant to the chosen stack.
4. **Real-user monitoring / field CWV** — preferred once production traffic is sufficient.

The chosen stack must include local reproduction instructions, failure thresholds, false-positive handling and an explicit removal/update path.
