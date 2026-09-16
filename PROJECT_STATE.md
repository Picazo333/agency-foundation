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
1. **Brand Direction Lab (ChatGPT + human):** naming validation, identity systems V0, visual freeze V0.
2. **Agency Master Plan (Claude Code):** **first full pass delivered** (GitHub Issue #2) — 21 modules, 9 audit passes, red-team review and integration pass, proposed for review on a branch. Entry point: `docs/08-plans/master/AGENCY_MASTER_PLAN.md`. Status is `review`, not canon; five ADRs (`ADR-0006`…`ADR-0010`) await human decision. **Next: field validation, not more planning.**
3. **Asset Factory Architecture (Jules):** design a generator-agnostic future asset factory; do not mass-produce final assets before Brand V1. Governing Issue #3; execution branch `asset/jules-asset-factory-architecture`.
4. **Neutral Technical Foundation (Jules):** token schema, isolated visual/motion/SVG/interaction labs, performance/accessibility/provenance foundations and S0-S4 contract. Governing Issue #4; execution branch `tech/jules-technical-foundation`.
5. **Repo Hardening (Jules):** repo hygiene, CI, documentation validation and agentic-work safety. Governing Issue #6; branch `tech/jules-repo-hardening`.

## Executor simplification decision
Active workstreams are defined by **capability and contract**, not by the tool originally proposed to execute them. Gemini CLI and Antigravity are no longer required dependencies for the current foundation phase. Their former workstreams were reassigned to Jules to reduce setup/coordination complexity without reducing scope or quality requirements.

Gemini may still be used later as an asset-generation engine after Brand V1. Antigravity may still be used later for experimentation when its unique interaction model adds enough value to justify the setup cost.

## Frozen process decisions
- Repo-first / single source of truth.
- Research != decision.
- Workbench != canon.
- Main/canon changes require review.
- Capability contracts outlive executor/tool substitutions.
- One concurrent task/workstream -> isolated branch/task environment -> PR review.
- Brand V0 is provisional until Brand/Business Fit Review.
- Implementation will be split into Aesthetic / Functional / System spines.
- Build maturity: Visual -> Interactive -> Mock Data -> Backend Wired -> AI/MCP.

## Open decisions
- Agency name.
- Brand Direction V0.
- Agency archetype/business model — **proposal on the table** (`ADR-0006`: diagnostic-led vertical
  productized studio, as a *working thesis under validation*, not a freeze).
- Initial ICP — **candidates ranked and a selection procedure defined** (`ADR-0007`); the choice is
  made by evidence at the Day 30 access gate.
- Positioning — **proposal on the table** (`ADR-0010`: AI as mechanism, never category).
- Offer architecture and pricing — **architecture proposed** (`ADR-0008`); **all prices remain
  `INFERRED RANGE` and may not be published** (`ADR-0009`).
- Validation plan outcomes — plan exists; **no validation has been run**.
- Full Brand System V1.
- Production stack and final website architecture.
- Whether Gemini, Antigravity, Codex or another executor becomes useful again in later implementation stages.

## Validation state

**Zero buyer contact has occurred.** No interviews, experiments or findings exist. This is the
single most important fact about the program's current state, and it caps the evidence grade of
every strategic conclusion in the repository
(`docs/02-strategy/thesis/EVIDENCE_AND_ASSUMPTIONS_REGISTER.md`, `E-09`).

A stop rule is proposed with `ADR-0006`: no further strategic planning artifact may be created
until 10 qualified buyer conversations are logged in `docs/06-validation/interviews/`.

## Next convergence gate
**Brand/Business Fit Review** after Brand Direction V0 + Agency Master Plan exist.
