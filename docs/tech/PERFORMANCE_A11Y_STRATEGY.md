# Performance and Accessibility Strategy

This document outlines the foundation's approach to enforcing performance and accessibility (a11y) standards without prematurely burdening the repository with heavy dependencies.

## Performance Budget

- **Core Web Vitals:** We target "Good" scores across LCP (<2.5s), FID (<100ms), and CLS (<0.1).
- **Lighthouse Score:** A minimum score of 90 across all categories (Performance, Accessibility, Best Practices, SEO) in CI.
- **Asset Size:** Image assets must be optimized (e.g., WebP/AVIF where possible) and SVGs must pass the sanitization pipeline.

## Accessibility Baseline

- **WCAG 2.1 AA Compliance:** All components must meet this standard.
- **Reduced Motion:** The `@media (prefers-reduced-motion: reduce)` media query must be implemented for all animations and transitions.
- **Semantic HTML & ARIA:** Strict adherence to semantic HTML elements before reaching for ARIA attributes.

## Tooling (Future Implementation)

We avoid installing full dependency suites until the core application framework is chosen. The intended tooling stack includes:

1. **Lighthouse CI:** To run against preview deployments. (Configuration stubbed in `infra/testing/lighthouserc.json`).
2. **Axe-core / Playwright:** For component-level a11y testing during the E2E phase.
3. **eslint-plugin-jsx-a11y:** If a React-like framework is chosen.
