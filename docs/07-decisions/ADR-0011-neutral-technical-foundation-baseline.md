# ADR-0011 — Neutral technical foundation baseline and labs

Status: APPROVED
Date: 2026-09-16

## Context
Issue #4 requires a technical foundation that can support later web implementation, interaction, motion, asset handling and AI/MCP work without prematurely locking the project to a production framework or to unresolved Brand decisions.

The foundation must be useful now, reversible later, and explicitly separate experimental proofs of concept from production-grade implementation.

## Decision
1. **Neutral labs first.** Use isolated plain HTML/CSS/JS labs for early visual, motion, interaction and SVG experiments. Lab output is evidence, not production code.
2. **No premature framework lock-in.** Do not select React/Vue/Svelte, a component library, Storybook, Playwright, Lighthouse CI or similar production tooling until the implementation requirements justify the dependency.
3. **Design-token structure without Brand values.** Maintain a neutral token schema with unresolved values marked `TBD` until Brand V1 supplies approved values and semantic mappings.
4. **SVGs are untrusted input.** Any third-party/generated SVG intended for production must pass a vetted parser/sanitizer and validation pipeline before optimization or component conversion. The current regex script is a lab-only proof of concept and must never be treated as a production sanitizer for hostile SVG.
5. **Current accessibility baseline.** Production surfaces should target WCAG 2.2 AA, semantic HTML, keyboard/focus behavior and reduced-motion support appropriate to each interaction.
6. **Current performance baseline.** Use the current Core Web Vitals model (LCP, INP, CLS) and establish enforceable budgets only once a stable preview/runtime exists. Early lab targets are directional, not release gates.
7. **Maturity is capability-based.** S0-S3 describe progressive implementation maturity where applicable. S4 (AI/MCP) is optional and applies only to surfaces that actually require agentic/model integrations; it is not a mandatory final stage for every component.

## Consequences
### Positive
- Preserves architectural optionality while Brand and business requirements converge.
- Gives design/motion/interaction work a safe experimental home.
- Establishes explicit accessibility, provenance and security expectations early.
- Avoids dependency churn and false production maturity.

### Negative / trade-offs
- Some lab work will be discarded or ported once the production stack is selected.
- Plain HTML/CSS/JS experiments are not proof that a future framework implementation will have identical behavior or performance.
- Production SVG sanitization, visual regression and performance tooling remain intentionally unresolved dependencies.

## Non-regression requirements
- `labs/` must remain clearly experimental.
- No `TBD` token value may be presented as approved Brand canon.
- Regex-based SVG cleaning must not be promoted to a production security control.
- Accessibility/performance guidance must be refreshed when standards or production architecture change.
- AI/MCP capability must not be added to a surface merely to advance a maturity label.

## Reopen if
- Brand V1 freezes token values or materially changes the token model;
- the production framework/toolchain is selected;
- a real implementation requires stronger accessibility, security, performance or browser-support guarantees;
- the asset pipeline adopts a production sanitizer/optimizer contract;
- the S0-S4 model proves misleading for actual delivery work.
