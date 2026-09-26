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

**Name:** `DIVINIVID · Agency Ecosystem · Strategy → Validation → Operations`

**Stable ID:** `AGY-ECOSYSTEM-ORCH-01`

**Conversation taxonomy:**  
`AGENCY_ECOSYSTEM / DIVINIVID / AGENCY_ECOSYSTEM / BUSINESS_OPERATING_SYSTEM / PRE_EVIDENCE_TO_REPEATABLE_DELIVERY / TRANSVERSAL_AGENCY_ORCHESTRATION / VALIDATION_FIRST_WITH_HUMAN_GATES`

**Skill taxonomy reused:**  
`cross-functional / orchestrator / transversal`

The conversation taxonomy is local descriptive metadata. It does **not** create or modify Skill Foundry taxonomy.

## Mission

Own the complete agency ecosystem as an orchestration and execution scope while keeping authority, evidence and dependencies separate.

The governing outcome is not “finish the plan.” It is to move the agency through:

`buyer evidence → payment → delivery → proof → repeatability`

with Brand, tooling, Asset Factory, technical foundations and Noema treated as supporting or parallel systems unless current evidence makes one of them a real blocker.

## Authority reconciliation

Current authority is:

1. current authoritative repo state;
2. approved ADRs / canon;
3. explicit current human statement;
4. current evidence;
5. migration checkpoints;
6. workbench / proposals;
7. historical chat.

A merge does not promote a proposal by itself.

### Approved ADR set

`ADR-0001` through `ADR-0005`, plus `ADR-0011` through `ADR-0015`, are currently approved.

### Still proposed

`ADR-0006` through `ADR-0010` remain **PROPOSED**:

- diagnostic-led vertical productized studio as working thesis;
- 75/25 two-segment validation;
- paid diagnostic as mandatory entry offer;
- defer price freeze until willingness-to-pay evidence;
- AI as delivery mechanism, not category.

They may be tested. They may not be described as agency decisions.

## AGENCY ECOSYSTEM STATE MAP

| Workstream | State | Authority | Current blocker | Next decision |
|---|---|---|---|---|
| Repo governance / authority | **CANON / APPROVED** | Source-of-truth + operating model + META_PLAN | None for this scope | Reuse; do not build another governance layer |
| Strategy / thesis / positioning | **PROPOSED / REVIEW + EXTERNAL-EVIDENCE DEPENDENT** | Agency Master Plan workbench + ADR-0006 proposed | Zero buyer evidence | Test hypotheses in field before freeze |
| ICP / segments | **PROPOSED / REVIEW + EXTERNAL-EVIDENCE DEPENDENT** | ICP workbench + ADR-0007 proposed | U-01..U-05 not recorded; no access evidence | Choose a reversible validation sample, not final ICP |
| Offer architecture | **PROPOSED / REVIEW + EXTERNAL-EVIDENCE DEPENDENT** | Offer workbench + ADR-0008 proposed | No buyer/problem/payment evidence | Test offer shape; do not assume paid diagnostic is canon |
| Pricing / economics | **EXTERNAL-EVIDENCE DEPENDENT** | Pricing workbench + ADR-0009 proposed | No founder recalibration, WTP, payment or delivery hours | Calibrate from real inputs and WTP |
| Field validation | **ACTIVE EXECUTION / EXTERNAL-EVIDENCE DEPENDENT** | Workbench instrumentation | Founder D0 unanswered, target ledger empty, no contact | Complete D0 → target → contact |
| Proof / case studies | **BLOCKED** | Workbench | No real delivery/outcome | Capture baseline and outcome from first engagement |
| Acquisition / sales | **ACTIVE EXECUTION SUPPORT READY** | Workbench instruments | No target list / targeting decision | Send first logged outreach batch |
| Delivery / lifecycle / ops / scorecard | **DEFERRED** | Workbench | No paid engagement | Activate minimum path after sale |
| Tooling / automation | **PROPOSED / REVIEW** | Requirements workbench | Vendor stack not decided/verified in repo | Select only against a live workflow |
| Brand / DIVINIVID | **ACTIVE EXECUTION** | Human-approved Brand canon + Brand workspace | P6 human review | PASS or bounded MUTATE in Brand scope |
| Asset Factory | **BLOCKED FOR ACTIVATION** | Integrated workbench architecture | Final expression + production matrix + golden-set pilot | Activate only after prerequisites |
| Neutral Technical Foundation | **CANON / APPROVED** | ADR-0011 + integrated foundation | None for baseline; production stack intentionally unresolved | Keep neutral until implementation need |
| MVS | **PROPOSED / REVIEW** | Web requirements workbench | Targeting/copy unvalidated | Build only minimum credibility surface if it improves contact |
| Brand Vertical Slice Prototype | **BLOCKED** | Brand operating scope | Final Expression Lock not reached | Owned by Brand scope after final lock |
| Production Website | **DEFERRED** | Downstream plan | Business + Brand + IA + stack gates | Do not start |
| Noema vNext agency adoption | **DEFERRED / REPO-SPECIFIC DECISION REQUIRED** | Noema for protocol; agency repo for domain | Agency migration not applied | Assess KEEP/MODIFY/ADD/DEFER before mutation |
| Skill Foundry relationship | **APPROVED EXTERNAL CAPABILITY SOURCE** | Skill Foundry | None for this scope | Reuse before new Skill |
| Legal / accounting | **EXTERNAL-EVIDENCE DEPENDENT** | External professionals | Jurisdiction-specific advice | Parallel setup; first SOW/invoice gates |

## Verified commercial evidence

The repo currently contains **no buyer evidence** beyond empty instrumentation:

- `docs/06-validation/interviews/` contains only its README;
- `interview_index.csv` is header-only;
- `target_account_ledger.csv` is header-only;
- `resonance_log.csv` is header-only;
- `price_signal_log.csv` is header-only;
- `sales_attempt_log.csv` is header-only.

Therefore the current observed state is:

- qualified buyer conversations: **0**;
- target accounts logged: **0**;
- price signals: **0**;
- sales attempts: **0**;
- cleared payments: **0**.

This is the binding commercial fact.

## Critical path

The current critical path is:

`Founder D0 facts → reversible validation sampling → target list → first outreach → qualified conversations → problem resonance → payment → delivery → measured proof → repeatability`.

The exact downstream D3/D4/D5/D6 mechanics remain workbench instruments until the associated strategy is promoted, but their evidence discipline is useful now.

### What does **not** currently belong on the commercial critical path

- finishing Brand;
- activating the Asset Factory;
- selecting the full AI/tool stack;
- production-site implementation;
- more strategic research;
- Noema vNext migration;
- technical polish.

Those may proceed only as bounded parallel work when they do not consume the attention needed to create external evidence.

## Parallel tracks

### 1. Brand

The Brand workstream can close P6 in parallel. It is not allowed to hold buyer validation hostage.

Agency Ecosystem only tracks the dependency. Detailed visual execution remains owned by:

`docs/09-handoffs/DIVINIVID_CONTEXT_HANDOFF_BRAND_IDENTITY_VERTICAL_SLICE_2026-09-25.md`.

### 2. Legal / accounting

Start jurisdiction-specific setup in parallel. Legal restrictions may alter outreach; contract review blocks the first SOW; accounting/tax setup blocks the first compliant invoice. Neither should be allowed to become generic planning work.

### 3. MVS credibility support

The MVS is an early commercial credibility/validation artifact. It is **not**:

- the Brand Vertical Slice;
- the Production Website;
- final IA.

Build only the smallest surface that materially helps contact. A full site is not required to learn whether buyers will talk.

### 4. Neutral technical foundation

The baseline is already integrated and approved through ADR-0011. Do not confuse a neutral lab with a production stack.

### 5. Asset Factory

The architecture exists on `main` through PR #17. Mass production remains gated. The open Issue #3 is tracking residue, not evidence that the architecture is missing.

## Human / external gates

### Founder-only

`U-01..U-05` must be answered by the founder. They cover:

- geography / jurisdiction / operating language / entity status;
- real weekly hours;
- runway and minimum draw;
- warm network;
- verifiable prior delivery work.

No agent should fabricate these.

### Buyer-only / market-only

Desk research cannot establish:

- whether the buyer volunteers the proposed problem;
- whether the buyer gives access;
- whether the offer resonates;
- willingness to pay;
- cleared payment.

### Runtime / delivery

No plan can establish:

- real delivery hours;
- rework rate;
- integration friction;
- realized outcome;
- repeatability.

### Professional

Local counsel/accounting are needed for jurisdiction-specific contracting, tax/invoicing and any material healthcare/data restrictions.

### Brand

P6 is a human gate in the separate Brand workspace.

## Asset Factory state

Two facts must remain separate:

1. **Architecture exists.** PR #17 integrated the reviewed generator-agnostic Asset Factory contracts on `main`.
2. **Activation is blocked.** Current canon still requires sufficient final identity specification, an executable production matrix and a passing golden-set factory pilot before mass production.

Do not reopen the architecture merely because Issue #3 is still open.

## Neutral Technical Foundation state

ADR-0011 is approved and PR #18 integrated the neutral foundation:

- neutral token schema;
- visual/motion/interaction/SVG labs;
- accessibility/performance baseline;
- provenance consumer contract;
- S0–S4 maturity model;
- security notes and technical experiments.

This does **not** mean a production framework, production sanitizer, visual-regression stack or hosting platform has been selected.

## Tooling / automation state

The repository currently has **requirements, not vendor decisions**.

`TOOLING_AUTOMATION_REQUIREMENTS.md` defines capability categories and selection criteria: CRM, project management, e-signature, invoicing/accounting, files, secrets, orchestration, analytics, communication, AI tooling and repository/knowledge needs.

No repo evidence currently establishes approved/configured/verified choices for CRM, automation orchestration, analytics, Workspace or hosting.

Therefore:

`REQUIREMENT ≠ VENDOR DECISION ≠ CONFIGURED ≠ VERIFIED ≠ PROVEN VALUE`.

Do not promote external tool choices into agency state without current evidence.

## Website boundary

### MVS

Early commercial credibility/validation support. Proposed in workbench. It may be plain and minimal.

### Brand Vertical Slice Prototype

High-fidelity proof of the finished Brand expression. Owned by the Brand workspace after Final Expression Lock.

### Production Website

Later business/system implementation with validated IA/copy, CRM/booking/analytics wiring, runtime evidence and production QA.

These three artifacts are intentionally non-interchangeable.

## Noema vNext reconciliation

Upstream Noema vNext is released and post-merge verified in the Noema repository.

That does **not** mean this agency repo has migrated.

Current agency evidence still says:

- `noema.project.yaml`: `x-noema-adoption: selective-rc0-migration`;
- Noema ecosystem registry: agency status `rc0-configured-domain-gated`;
- Project State: vNext transversal migration not yet executed here.

Disposition: **DEFER mutation.** A bounded agency-specific adoption assessment must precede any vNext change. It is not on the commercial critical path.

## Operating architecture selected by the scope Skill

The `workspace-operating-contract-orchestrator` resolves this workspace primarily through **REUSE**:

- governance → existing repo authority;
- acceptance → existing validation and human gates;
- schemas → existing field-kit, Asset Factory and Noema contracts;
- execution → Field Validation Execution Kit;
- context/recovery → active handoff + Noema manifest + these workspace artifacts;
- evaluation → domain-owned validation/Brand/delivery gates;
- security → ADR-0011 + existing governance/security checklist;
- observability → evidence logs + state artifacts;
- completion → evidence-backed gates, never narrative completion.

No new Skill, orchestrator layer, schema framework or MCP is justified merely to run this conversation.

## Maximum 3 next actions

### 1. Complete founder D0 inputs

Create:

`docs/06-validation/findings/FOUNDER_INPUTS_ANSWERED.md`

from `field-kit/01_FOUNDER_INPUTS_U01_U05.md`, filled by the founder only.

This is the first hard blocker because it changes jurisdiction, available capacity, runway, warm access and proof posture.

### 2. Launch the first external validation batch

Immediately after D0 constraints are known:

- choose a reversible validation sample;
- populate the target ledger;
- research the first accounts;
- send the first logged outreach;
- preserve the sealed interview phase;
- log evidence within the field kit.

Do not delay this for Brand, Asset Factory or full website work.

### 3. Close Brand P6 in parallel

Use the Brand conversation to return either:

- `PASS`; or
- `MUTATE: <one concrete translation failure>`.

This removes a parallel Brand blocker without turning Brand into the agency’s commercial critical path.

## Stop rules

Stop desk work when the missing fact requires:

- buyer conversation;
- payment;
- delivery;
- runtime;
- legal/accounting advice;
- production telemetry.

Do not create another strategy document unless it changes a live decision or directly enables external contact.

Do not build out the vendor stack before an active workflow requires it.

Do not activate Asset Factory mass production or the Production Website before their gates.

Do not silently promote ADR-0006 through ADR-0010.
