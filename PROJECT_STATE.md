---
status: approved
owner: meta
updated: 2026-09-16
authority: canon
depends_on:
  []
---
# Project State

## Program goal
Build a serious agency from research -> decisions -> brand -> strategy -> validation -> asset production -> implementation -> launch, while keeping every important decision traceable and reversible.

## Current active work
1. **Brand Direction Lab (ChatGPT):** naming exploration, validation, identity systems V0, visual freeze V0.
2. **Agency Master Plan (Claude/CoWork):** **first full pass delivered** (GitHub Issue #2) —
   21 modules, 9 audit passes, red-team review and integration pass, proposed for review on a
   branch. Entry point: `docs/08-plans/master/AGENCY_MASTER_PLAN.md`. Status is `review`, not canon;
   five ADRs (`ADR-0005`…`ADR-0009`) await human decision. **Next: field validation, not more
   planning.**
3. **Asset Factory Architecture (Gemini):** design the future Gem/factory; do not mass-produce assets before Brand V1.
4. **Technical Foundation (Codex/Antigravity/Jules/Cursor):** neutral repo/tooling, sandboxes, token schema, SVG/motion pipeline, QA infrastructure.

## Frozen process decisions
- Repo-first / single source of truth.
- Research != decision.
- Workbench != canon.
- Main/canon changes require review.
- Brand V0 is provisional until Brand/Business Fit Review.
- Implementation will be split into Aesthetic / Functional / System spines.
- Build maturity: Visual -> Interactive -> Mock Data -> Backend Wired -> AI/MCP.

## Open decisions
- Agency name.
- Brand Direction V0.
- Agency archetype/business model — **proposal on the table** (`ADR-0005`: diagnostic-led vertical
  productized studio, as a *working thesis under validation*, not a freeze).
- Initial ICP — **candidates ranked and a selection procedure defined** (`ADR-0006`); the choice is
  made by evidence at the Day 30 access gate.
- Positioning — **proposal on the table** (`ADR-0009`: AI as mechanism, never category).
- Offer architecture and pricing — **architecture proposed** (`ADR-0007`); **all prices remain
  `INFERRED RANGE` and may not be published** (`ADR-0008`).
- Validation plan outcomes — plan exists; **no validation has been run**.
- Full Brand System V1.
- Production stack and final website architecture.

## Validation state

**Zero buyer contact has occurred.** No interviews, experiments or findings exist. This is the
single most important fact about the program's current state, and it caps the evidence grade of
every strategic conclusion in the repository
(`docs/02-strategy/thesis/EVIDENCE_AND_ASSUMPTIONS_REGISTER.md`, `E-09`).

A stop rule is proposed with `ADR-0005`: no further strategic planning artifact may be created
until 10 qualified buyer conversations are logged in `docs/06-validation/interviews/`.

## Next convergence gate
**Brand/Business Fit Review** after Brand Direction V0 + Agency Master Plan exist.
