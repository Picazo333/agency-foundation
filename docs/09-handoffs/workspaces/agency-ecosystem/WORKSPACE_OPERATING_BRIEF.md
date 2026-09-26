---
status: active
owner: meta
created: 2026-09-25
authority: operating_scope_contract
scope: agency_ecosystem
derived_from_skill: workspace-operating-contract-orchestrator
---

# Workspace Operating Brief — DIVINIVID Agency Ecosystem

## Proposed conversation name and taxonomy

**Name:** `DIVINIVID · Agency Ecosystem — Strategy → Validation → Operating System`

**Stable ID:** `AGY-ECOSYSTEM-CORE-01`

**Taxonomy:**  
`AGENCY_ECOSYSTEM / DIVINIVID / PROGRAM / AGENCY_ECOSYSTEM / VALIDATION_TO_LAUNCH / BUSINESS_SYSTEM_END_TO_END / ORCHESTRATION_WITH_HUMAN_EXTERNAL_GATES`

## Mission

Own the global agency dependency graph, current evidence, decisions and next actions across strategy,
validation, offers, pricing, proof, sales, delivery, operations, tooling, Brand dependencies, Asset
Factory, technical foundation, web/system implementation and Noema integration.

This workspace coordinates the ecosystem; it does **not** imply that every workstream is authorized to
execute simultaneously.

## Authority boundary

Authority order remains:

`current repo state > approved ADR/canon > explicit current human statement > current evidence > migration checkpoints > workbench/proposals > historical chat`.

Key consequences:

- `META_PLAN.md` is canon.
- `AGENCY_MASTER_PLAN.md` and its roadmap/field-kit modules are workbench/review.
- ADR-0006 through ADR-0010 remain **PROPOSED**.
- A merged proposal is not automatically an agency decision.
- Noema represents context/conformance; it does not own agency strategy.
- Brand/DIVINIVID visual execution is a separate workstream with its own cursor.

## Reconciled operating state

The current commercial system is **pre-validation** in authoritative evidence.

The repository contains **no qualified buyer interview records** beyond the interviews directory README
and no cleared-payment evidence. Therefore buyer access, resonance and willingness to pay remain the
binding uncertainties.

The Brand workstream is active at `P6_HUMAN_REVIEW_GATE`, but Brand progress is not market validation.

The Neutral Technical Foundation baseline is approved and Issue #4 is documented as completed. It
should remain a parallel evidence foundation until a real runtime justifies production architecture
decisions.

Asset Factory architecture exists as a governed workstream, but its current spec area remains
workbench/draft and mass production is blocked until the identity/production matrix is mature and a
golden-set pilot passes.

Tooling/automation currently has a requirements specification, not an approved vendor stack. No CRM,
analytics, Workspace, automation or production-hosting vendor is treated as verified merely because it
is desirable or available.

Noema vNext is **not yet executed in the agency repo**. The repo still declares protocol
`0.1.0-rc.0` and preserves pre-vNext checkpoints for migration.

## Critical path

`Founder inputs → human strategy gate → minimum validation instruments → outreach → qualified conversations → resonance → cleared payment → delivery → delivery economics`.

Brand, Asset Factory, tool experiments and production-site polish are parallel until evidence makes one
of them blocking.

Desk work stops when the next uncertainty requires buyer conversation, payment, delivery, runtime,
legal/accounting advice or production telemetry.

## MVS / Brand Vertical Slice / Production Website

These are three different artifacts:

1. **MVS** — early commercial credibility/validation artifact. Minimum viable, provisional and fast.
2. **Brand Vertical Slice Prototype** — high-fidelity proof that the finished Brand works in use.
3. **Production Website** — later functional/system implementation with CRM, analytics, legal and runtime gates.

The second does not substitute for the first or authorize the third.

## Human / external gates

Human-owned now:

- complete U-01…U-05 and D0 recalibration;
- adjudicate ADR-0006…ADR-0010, especially 0006/0007/0008;
- Brand P6 decision in the Brand workspace.

External-reality gates:

- qualified buyer conversations;
- cleared money;
- first delivery;
- accountant/counsel where legally required;
- production telemetry once runtime exists.

## Maximum-leverage next actions

1. **Complete U-01…U-05 + D0 recalibration.** These five founder facts move more downstream decisions than more research.
2. **Adjudicate ADR-0006…ADR-0010, prioritizing 0006/0007/0008.** This resolves the working thesis, segment allocation and entry-offer semantics without pretending they are market-validated.
3. **Launch the minimum validation loop to first qualified conversations.** Build only the target list, method/credibility surface, teardown and outreach assets needed to make contact.

## Operating architecture from the scope-orchestration skill

The minimum sufficient architecture is **reuse-heavy**:

- governance: existing repo authority + ADRs + active handoff;
- acceptance: existing D0/D3/D4/D5/D6 and convergence gates;
- context recovery: handoff + PROJECT_STATE + Noema manifest + this contract;
- evals: field gates, Brand/Business Fit, implementation readiness and launch readiness;
- execution: capability-first workstreams and minimum-necessary mutation;
- security: existing governance checklist until production/client-data risk appears;
- tooling: defer vendor selection until a concrete requirement needs an executor.

No new top-level Skill, agent framework, schema family or MCP layer is justified for this workspace.

## Stop rule

Do not create more strategic planning artifacts merely to improve confidence in questions already
blocked on buyer evidence.

Specialist execution should split into bounded workspaces whenever its own cursor, authority or artifact
load would otherwise overload Agency Ecosystem.
