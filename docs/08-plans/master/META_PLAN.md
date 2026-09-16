---
status: approved
owner: meta
updated: 2026-09-16
authority: canon
depends_on:
  []
---
# Agency Meta-Plan

## Goal
Parallelize high-value work without allowing tools to make conflicting decisions or contaminate each other's domains.

## Cross-cutting sidecar — Project Harvest
Across all waves, meaningful PRs, ADRs, milestones, experiments, incidents, and deliveries may produce a lightweight Project Harvest record for reusable organizational knowledge.

Project Harvest is deliberately **non-blocking** and does not alter existing gates, ownership, or workstream sequencing. It captures evidence/lessons once and may later route them to story/media, Skill candidates, SOPs, templates, evals, reusable components/assets, case studies/proof, or benchmarks.

It does not auto-publish, does not make research/candidates canonical, and does not couple this project to Noema, Skill Foundry, or another downstream tool.

Protocol: `docs/10-knowledge-harvest/PROJECT_HARVEST_PROTOCOL.md`.

## Operating principle — capability first, executor second
Workstreams are defined by their **capability contract, scope, outputs and Definition of Done**, not by a specific AI product. Executor changes are allowed when they reduce operational friction without reducing required quality.

A tool substitution must preserve:
- governing Issue;
- scope and forbidden scope;
- branch/task isolation;
- required artifacts;
- validation/audit requirements;
- PR review before `main`.

## Wave 0 — Foundation
Repository baseline, governance, research import, workstream contracts, handoffs and CI health checks.

## Wave 1 — Parallel workstreams
### A — Brand Direction (ChatGPT + human)
Naming -> shortlist/validation -> identity systems V0 -> Visual Direction Freeze V0.

### B — Agency Master Plan (Claude Code)
Strategy reconciliation -> thesis/category -> ICP -> positioning -> offer -> pricing -> proof -> sales -> delivery -> economics -> field validation -> dependency-aware roadmap.

### C — Asset Factory Architecture (Jules)
Design a generator-agnostic factory: schemas, categories, QA, provenance, generation contracts, lifecycle and handoff rules. Do not mass-produce final assets before Brand V1.

Current governing Issue: #3. Current execution branch: `asset/jules-asset-factory-architecture`.

Gemini is no longer required to design this architecture. It remains a possible generation engine after Brand V1.

### D — Neutral Technical Foundation (Jules)
Neutral token schema, visual/motion/SVG/interaction labs, SVG pipeline, accessibility/performance foundations, provenance integration and S0-S4 maturity contract. Do not build the final production site prematurely.

Current governing Issue: #4. Current execution branch: `tech/jules-technical-foundation`.

Antigravity is no longer required for this foundation phase. It remains an optional later experimentation surface when the incremental benefit justifies setup complexity.

### E — Repo Hardening (Jules)
Repo hygiene, CI, documentation validation, secret hygiene and multi-agent work safety.

Current governing Issue: #6. Current execution branch: `tech/jules-repo-hardening`.

## Parallelism rule for Jules
Jules may execute multiple workstreams concurrently only when each task is isolated by Issue + branch/task environment + explicit write scope. No cross-workstream edits unless a narrow integration dependency is documented.

## Gate 1 — Brand/Business Fit Review
Inputs: Brand V0 + Agency Master Plan.
Test whether name, personality and visual system fit the business model/ICP/price/offer without constraining future expansion.

## Wave 2 — Strategic convergence
Freeze serious agency structure while marking unresolved field-validation dependencies.

## Wave 3 — Full Brand System V1
Start in a clean brand-system workstream/conversation using approved business strategy + Brand V0.

## Wave 4 — Asset Factory activation
Activate the approved Asset Factory architecture using Brand V1. The generation provider is selected at execution time; Gemini is an option, not a dependency.

## Wave 5 — Implementation
Parallel spines:
- Aesthetic
- Functional
- System

Maturity stages:
`S0 Visual -> S1 Interactive -> S2 Mock Data -> S3 Backend Wired`

`S4 AI/MCP` is an **optional capability stage** only for surfaces that actually require model/tool-mediated behavior. It is not a mandatory endpoint or a quality badge.

## Wave 6 — Field validation
Validate WTP, access, buyer language, offer clarity, pricing, objections and proof.

## Wave 7 — Integration + launch
Website, social, proposal/deck, CRM, sales workflow, automations, onboarding, proof capture and analytics.

## Wave 8 — Measure + iterate
Use evidence; reopen frozen decisions only through an ADR.
