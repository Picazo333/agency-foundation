# Visual Regression Strategy

This document outlines the foundation's approach to visual regression testing, ensuring UI stability across updates without installing heavy dependencies during the neutral foundation phase.

## Core Principles

1. **Deterministic Rendering:** Tests must run against mocked data and consistent environments to prevent false positives caused by dynamic content (e.g., dates, random images).
2. **Component & Page Level:** Visual regressions should be captured at both the individual component level (e.g., via Storybook) and the critical page level (via E2E tests).
3. **Cross-Browser Verification:** Tests must cover target browsers (Chromium, WebKit, Firefox) as defined by the eventual browser support matrix.

## Intended Architecture

Once the production stack is chosen and component implementation begins, the following stack is recommended:

- **Playwright:** For orchestrating page navigation, state setup, and capturing screenshots. Playwright's built-in visual comparison (`toHaveScreenshot`) serves as an excellent starting point.
- **Percy / Chromatic (Optional):** If the team scales and requires advanced visual review workflows (approvals, branch diffing, DOM snapshotting instead of just pixels), a dedicated service like Percy or Chromatic (if Storybook is used) should be evaluated.

## Implementation Guidelines

- Store baseline screenshots in a dedicated directory (e.g., `__snapshots__`) committed to version control, unless a third-party service manages them.
- Use a `.gitignore` to prevent committing failed test diff artifacts.
- Ensure the CI environment (e.g., GitHub Actions) uses a stable OS and browser version to prevent rendering discrepancies between local and CI runs.
