---
status: approved
owner: meta
updated: 2026-09-15
authority: canon
depends_on:
  []
---
# Project State

## Program goal
Build a serious agency from research -> decisions -> brand -> strategy -> validation -> asset production -> implementation -> launch, while keeping every important decision traceable and reversible.

## Current active work
1. **Brand Direction Lab (ChatGPT + human):** naming validation, identity systems V0, visual freeze V0.
2. **Agency Master Plan (Claude Code):** strategy reconciliation, ICP, positioning, offer, pricing, proof, sales, delivery, economics and validation roadmap.
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
- Agency archetype/business model.
- Initial ICP.
- Positioning.
- Offer architecture and pricing.
- Validation plan outcomes.
- Full Brand System V1.
- Production stack and final website architecture.
- Whether Gemini, Antigravity, Codex or another executor becomes useful again in later implementation stages.

## Next convergence gate
**Brand/Business Fit Review** after Brand Direction V0 + Agency Master Plan exist.
