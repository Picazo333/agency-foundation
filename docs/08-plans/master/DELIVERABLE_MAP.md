---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - AGENCY_MASTER_PLAN.md
---
# Deliverable Map

> Maps every deliverable name required by **GitHub Issue #2** and by
> `docs/08-plans/workstreams/CLAUDE_MASTER_PLAN_WORKSTREAM.md` to its actual path, and records the
> naming reconciliation between the two contracts.

## 1. Why this file exists

Two governing documents specify deliverables under **different filenames**:

| Source | Named deliverables |
|---|---|
| `CLAUDE_MASTER_PLAN_WORKSTREAM.md` (status `approved`, authority `canon`) | 13 files, including `PRICING_MODEL.md`, `ECONOMIC_MODEL.md`, `90_DAY_ROADMAP.md` |
| **GitHub Issue #2** (the governing task) | 22 files, including `PRICING_AND_ECONOMICS_MODEL.md`, `30_60_90_180_365_ROADMAP.md`, and nine outputs the workstream spec does not name |

Issue #2 is the later and more specific contract and supersedes the earlier filename list. Rather
than edit a canonical document to match a task (which `CANON_PROMOTION_RULE.md` discourages), the
reconciliation is recorded here and flagged for the human owner in `CLAUDE_HANDOFF.md`.

Logged as contradiction `C-05` in `INTEGRATION_PASS.md`.

## 2. Issue #2 required outputs → actual paths

| # | Required name | Path | Status |
|---:|---|---|---|
| 1 | `AGENCY_MASTER_PLAN.md` | `docs/08-plans/master/AGENCY_MASTER_PLAN.md` | ✅ |
| 2 | `STRATEGY_RECONCILIATION.md` | `docs/02-strategy/thesis/STRATEGY_RECONCILIATION.md` | ✅ |
| 3 | `EVIDENCE_AND_ASSUMPTIONS_REGISTER.md` | `docs/02-strategy/thesis/EVIDENCE_AND_ASSUMPTIONS_REGISTER.md` | ✅ |
| 4 | `DECISION_TREE.md` | `docs/02-strategy/thesis/DECISION_TREE.md` | ✅ |
| 5 | `ICP_FRAMEWORK.md` | `docs/02-strategy/icp/ICP_FRAMEWORK.md` | ✅ |
| 6 | `POSITIONING_ARCHITECTURE.md` | `docs/02-strategy/positioning/POSITIONING_ARCHITECTURE.md` | ✅ |
| 7 | `OFFER_ARCHITECTURE.md` | `docs/02-strategy/offers/OFFER_ARCHITECTURE.md` | ✅ |
| 8 | `PRICING_AND_ECONOMICS_MODEL.md` | `docs/02-strategy/pricing/PRICING_AND_ECONOMICS_MODEL.md` | ✅ |
| 9 | `PROOF_STRATEGY.md` | `docs/02-strategy/proof/PROOF_STRATEGY.md` | ✅ |
| 10 | `ACQUISITION_MARKETING_SYSTEM.md` | `docs/02-strategy/sales/ACQUISITION_MARKETING_SYSTEM.md` | ✅ |
| 11 | `SALES_SYSTEM.md` | `docs/02-strategy/sales/SALES_SYSTEM.md` | ✅ |
| 12 | `CLIENT_LIFECYCLE.md` | `docs/04-operations/client-lifecycle/CLIENT_LIFECYCLE.md` | ✅ |
| 13 | `DELIVERY_OS.md` | `docs/04-operations/delivery/DELIVERY_OS.md` | ✅ |
| 14 | `OPERATING_MODEL.md` | `docs/04-operations/OPERATING_MODEL.md` | ✅ ⚠️ see §4 |
| 15 | `TOOLING_AUTOMATION_REQUIREMENTS.md` | `docs/04-operations/tooling/TOOLING_AUTOMATION_REQUIREMENTS.md` | ✅ |
| 16 | `GOVERNANCE_RISK_SECURITY_CHECKLIST.md` | `docs/04-operations/GOVERNANCE_RISK_SECURITY_CHECKLIST.md` | ✅ |
| 17 | `AGENCY_SCORECARD.md` | `docs/04-operations/AGENCY_SCORECARD.md` | ✅ |
| 18 | `FIELD_VALIDATION_PLAN.md` | `docs/06-validation/FIELD_VALIDATION_PLAN.md` | ✅ |
| 19 | `BRAND_BUSINESS_INTERFACE.md` | `docs/02-strategy/BRAND_BUSINESS_INTERFACE.md` | ✅ ⚠️ see §4 |
| 20 | `WEB_BUSINESS_REQUIREMENTS.md` | `docs/02-strategy/WEB_BUSINESS_REQUIREMENTS.md` | ✅ ⚠️ see §4 |
| 21 | `30_60_90_180_365_ROADMAP.md` | `docs/08-plans/master/30_60_90_180_365_ROADMAP.md` | ✅ |
| 22 | Updated `RISK_REGISTER.md` / open questions | `RISK_REGISTER.md`, `OPEN_QUESTIONS.md` | ✅ |
| 23 | Final executive synthesis | `docs/08-plans/master/EXECUTIVE_SYNTHESIS.md` | ✅ |

## 3. Workstream-spec names → where the content lives

| `CLAUDE_MASTER_PLAN_WORKSTREAM.md` name | Superseded by | Path |
|---|---|---|
| `AGENCY_MASTER_PLAN.md` | same | as above |
| `STRATEGY_RECONCILIATION.md` | same | as above |
| `DECISION_TREE.md` | same | as above |
| `ICP_FRAMEWORK.md` | same | as above |
| `OFFER_ARCHITECTURE.md` | same | as above |
| `PRICING_MODEL.md` | `PRICING_AND_ECONOMICS_MODEL.md` | merged |
| `ECONOMIC_MODEL.md` | `PRICING_AND_ECONOMICS_MODEL.md` | merged — pricing and unit economics are one model, and splitting them produced duplication |
| `PROOF_STRATEGY.md` | same | as above |
| `SALES_SYSTEM.md` | split into `ACQUISITION_MARKETING_SYSTEM.md` (demand) + `SALES_SYSTEM.md` (conversion) | Issue #2 Phases 8 and 9 are distinct |
| `DELIVERY_OS.md` | same | as above |
| `FIELD_VALIDATION_PLAN.md` | same | as above |
| `90_DAY_ROADMAP.md` | `30_60_90_180_365_ROADMAP.md` | superset |
| `RISK_REGISTER.md` | updated in place | root |

Also produced beyond both contracts, because the audits required them:
`AGENCY_THESIS.md` (Issue Phase 2 had no named output) · `MASTER_PLAN_AUDITS.md` ·
`RED_TEAM_REVIEW.md` · `INTEGRATION_PASS.md` · `HYPOTHESIS_REGISTER.md` · `LEARNING_LOG.md` ·
`DELIVERABLE_MAP.md` · five ADR proposals.

## 4. Placement notes

| Doc | Placement decision |
|---|---|
| `OPERATING_MODEL.md` | Placed at `docs/04-operations/`. **Name collides conceptually** with `docs/00-meta/operating-model.md` (program governance). The filename is fixed by the Issue #2 contract; the collision is disambiguated in the document's own header. Renaming is a human decision — see `CLAUDE_HANDOFF.md` |
| `BRAND_BUSINESS_INTERFACE.md` | Placed under `docs/02-strategy/`, **not** `docs/03-brand/`. It states commercial requirements for the brand; `docs/03-brand/` is the Brand workstream's territory and was not touched (`OWNERSHIP_MATRIX.md`) |
| `WEB_BUSINESS_REQUIREMENTS.md` | Placed under `docs/02-strategy/`, **not** `docs/05-product-web/`. Those READMEs state they are populated after strategy and brand convergence, which has not occurred |
| `AGENCY_SCORECARD.md`, `GOVERNANCE_RISK_SECURITY_CHECKLIST.md`, `OPERATING_MODEL.md` | Placed at `docs/04-operations/` root rather than in a subfolder, because each spans several subfolder concerns |

## 5. Ownership compliance

`AGENTS.md` and `OWNERSHIP_MATRIX.md` grant Claude/CoWork write access to `docs/02-strategy/`,
`docs/04-operations/`, `docs/06-validation/` and `docs/08-plans/`, plus handoffs and proposals.

| Area | Written? | Authorised? |
|---|---|---|
| `docs/02-strategy/` | Yes | ✅ |
| `docs/04-operations/` | Yes | ✅ |
| `docs/06-validation/` | Yes | ✅ |
| `docs/08-plans/master/` | Yes | ✅ |
| `docs/09-handoffs/claude/` | Yes | ✅ (own handoff) |
| `docs/07-decisions/` | Yes — **PROPOSED** ADRs only | ✅ per `CLAUDE_KICKSTART.md` workflow rule 5 |
| `RISK_REGISTER.md`, `OPEN_QUESTIONS.md`, `PROJECT_STATE.md`, `CHANGELOG.md` | Yes — additive updates | ✅ required by Issue #2 |
| `docs/03-brand/` | **No** | Forbidden — untouched |
| `docs/01-research/` | **No** | Read only |
| `docs/05-product-web/` | **No** | Other workstream |
| `apps/`, `packages/`, `labs/`, `infra/`, `scripts/`, `asset-factory/`, `assets/` | **No** | Other workstreams |
| `docs/00-meta/` | **No** | Canon, other owner |
| `docs/08-plans/workstreams/` | **No** | See §1 — reconciliation recorded here instead |
