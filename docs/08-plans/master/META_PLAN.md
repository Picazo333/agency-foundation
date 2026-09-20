---
status: approved
owner: meta
updated: 2026-09-20
authority: canon
depends_on:
  []
---
# Agency Meta-Plan

## Goal
Parallelize high-value work without allowing tools to make conflicting decisions or contaminate each other's domains.

## 2026-09-20 DIVINIVID visual-program update
The detailed Brand visual-universe -> Asset Factory sequence is now governed by:
`docs/08-plans/master/DIVINIVID_VISUAL_UNIVERSE_META_PLAN_V2.md`.

ADR-0013 supersedes the older visual-phase sequencing only for the DIVINIVID visual workstream. Business validation, repo-first governance, capability-first execution and the existing Asset Factory architecture remain in force.

Noema provides cross-project governance/conformance and Skill Foundry may consume high-signal Project Harvest candidates; neither system owns DIVINIVID domain canon.

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

## Wave 3 — Full Brand System / Visual Universe industrialization
DIVINIVID follows the Visual Universe Meta-Plan V2: archive and classify the explored corpus, build the visual canon/lineage registry, execute the contracted expansion program, audit coverage, then translate the universe into production specifications.

## Wave 4 — Asset Factory activation
Activate the approved Asset Factory architecture only after the Visual Spec/Matrix/Ontology exist and the golden-set factory pilot passes. The generation provider is selected at execution time; Gemini is the intended first executor, not a dependency.

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
