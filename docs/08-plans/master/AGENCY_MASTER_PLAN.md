---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - META_PLAN.md
  - CLAUDE_MASTER_PLAN_WORKSTREAM.md
  - ADR-0004
---
# Agency Master Plan

> **The entry point to the Claude/CoWork Agency Master Plan** (GitHub Issue #2).
> This document is the index, the executive argument and the navigation layer. The substance lives
> in the twenty-one modules listed in §3; this file does not duplicate them.
>
> **Status: proposal, not canon.** Per `CANON_PROMOTION_RULE.md`, nothing here is a decision until
> reviewed and recorded in an ADR. Five ADRs are proposed for that purpose (§7).

## 1. What this plan is, and what it is not

| It is | It is not |
|---|---|
| A decision architecture with dated gates and defined failure branches | A business plan asserting what will happen |
| A reasoning artifact | A research artifact |
| A set of execution contracts for offers, delivery, sales and operations | A set of commitments |
| An explicit map of what is unknown and what will resolve it | A forecast |

**The honest boundary** (`EVIDENCE_AND_ASSUMPTIONS_REGISTER.md` §6): the defensible content of this
plan is its comparative logic, its execution contracts, its risk exposure and its validation design.
Its non-defensible content is **every quantity**. The plan is structured so quantities can be
replaced without rebuilding the structure.

## 2. The argument in one page

**Where the program stands.** Three research corpora were ingested and closed (`E-01`, `E-03`), but
the raw archives are not in the repository, so no claim traces to a primary source (`E-02`). The
governance system is real and working (`E-12`). **Zero buyer conversations have occurred** (`E-09`).
No name, ICP, offer, price or model has been decided (`E-10`).

**What the evidence rules out.** A classic multidisciplinary agency is portfolio-gated and the
portfolio does not exist. A horizontal AI/automation agency names the supplier's tools rather than
the buyer's problem and competes on a commoditising axis (`E-17`). A consultancy is credential-gated
and produces nothing countable inside an engagement. White-label subcontracting pays this month and
forecloses every other model. A craft-led creative-technology studio is the best fit for the
founder's taste (`E-07`) and is unreachable without a portfolio — it is a destination, not a start.

**What survives.** A **diagnostic-led, vertical, productized studio**: a paid diagnostic that
measures where a specific kind of business loses revenue it has already paid to generate; bounded,
fixed-price builds that close the measured gaps; an operated layer that keeps them closed and keeps
measuring. AI is the mechanism that makes this viable for one person. It is never the pitch.

**Why this shape and not another.** Because it is the only candidate where **proof is a byproduct of
the entry offer**. The diagnostic captures a baseline in week one; every subsequent engagement is a
case study by construction. For a supplier whose binding constraint is the absence of references
(`A-06`), that is worth more than any other property a business model can have.

**What must be true.** Four propositions, none verified
(`STRATEGY_RECONCILIATION.md` §5): the buyer has a countable problem baselineable in days; the buyer
will pay something to have it diagnosed; a reachable vertical exists; and distinctive craft does not
repel that buyer.

**What happens next.** Five founder questions in three days. A method document, a five-page site and
a teardown template in eighteen. Sixteen clinic-group conversations and two sold diagnostics in
sixty. Six gates over one hundred and eighty days, each with a threshold and a failure branch.

**The largest risk is not the market.** It is that this program plans superbly and never makes
contact (`RED_TEAM_REVIEW.md` RT-01). A binding stop rule addresses it: no further strategic
planning artifact may be created until ten qualified buyer conversations are logged.

## 3. Module index

| # | Module | Document | Issue phase |
|---:|---|---|---|
| 1 | Evidence and assumptions | [`docs/02-strategy/thesis/EVIDENCE_AND_ASSUMPTIONS_REGISTER.md`](../../02-strategy/thesis/EVIDENCE_AND_ASSUMPTIONS_REGISTER.md) | 1 |
| 2 | Strategy reconciliation | [`docs/02-strategy/thesis/STRATEGY_RECONCILIATION.md`](../../02-strategy/thesis/STRATEGY_RECONCILIATION.md) | 1 |
| 3 | Agency thesis / market architecture | [`docs/02-strategy/thesis/AGENCY_THESIS.md`](../../02-strategy/thesis/AGENCY_THESIS.md) | 2 |
| 4 | Decision tree | [`docs/02-strategy/thesis/DECISION_TREE.md`](../../02-strategy/thesis/DECISION_TREE.md) | 1–2 |
| 5 | ICP framework | [`docs/02-strategy/icp/ICP_FRAMEWORK.md`](../../02-strategy/icp/ICP_FRAMEWORK.md) | 3 |
| 6 | Positioning architecture | [`docs/02-strategy/positioning/POSITIONING_ARCHITECTURE.md`](../../02-strategy/positioning/POSITIONING_ARCHITECTURE.md) | 4 |
| 7 | Offer architecture | [`docs/02-strategy/offers/OFFER_ARCHITECTURE.md`](../../02-strategy/offers/OFFER_ARCHITECTURE.md) | 5 |
| 8 | Pricing and unit economics | [`docs/02-strategy/pricing/PRICING_AND_ECONOMICS_MODEL.md`](../../02-strategy/pricing/PRICING_AND_ECONOMICS_MODEL.md) | 6 |
| 9 | Proof strategy | [`docs/02-strategy/proof/PROOF_STRATEGY.md`](../../02-strategy/proof/PROOF_STRATEGY.md) | 7 |
| 10 | Acquisition system | [`docs/02-strategy/sales/ACQUISITION_MARKETING_SYSTEM.md`](../../02-strategy/sales/ACQUISITION_MARKETING_SYSTEM.md) | 8 |
| 11 | Sales operating system | [`docs/02-strategy/sales/SALES_SYSTEM.md`](../../02-strategy/sales/SALES_SYSTEM.md) | 9 |
| 12 | Client lifecycle | [`docs/04-operations/client-lifecycle/CLIENT_LIFECYCLE.md`](../../04-operations/client-lifecycle/CLIENT_LIFECYCLE.md) | 10 |
| 13 | Delivery operating system | [`docs/04-operations/delivery/DELIVERY_OS.md`](../../04-operations/delivery/DELIVERY_OS.md) | 10 |
| 14 | Agency operating model | [`docs/04-operations/OPERATING_MODEL.md`](../../04-operations/OPERATING_MODEL.md) | 11 |
| 15 | Tooling and automation | [`docs/04-operations/tooling/TOOLING_AUTOMATION_REQUIREMENTS.md`](../../04-operations/tooling/TOOLING_AUTOMATION_REQUIREMENTS.md) | 12 |
| 16 | Governance, risk, security | [`docs/04-operations/GOVERNANCE_RISK_SECURITY_CHECKLIST.md`](../../04-operations/GOVERNANCE_RISK_SECURITY_CHECKLIST.md) | 13 |
| 17 | Agency scorecard | [`docs/04-operations/AGENCY_SCORECARD.md`](../../04-operations/AGENCY_SCORECARD.md) | 14 |
| 18 | Field validation plan | [`docs/06-validation/FIELD_VALIDATION_PLAN.md`](../../06-validation/FIELD_VALIDATION_PLAN.md) | 15 |
| 19 | Brand / business interface | [`docs/02-strategy/BRAND_BUSINESS_INTERFACE.md`](../../02-strategy/BRAND_BUSINESS_INTERFACE.md) | 16 |
| 20 | Web business requirements | [`docs/02-strategy/WEB_BUSINESS_REQUIREMENTS.md`](../../02-strategy/WEB_BUSINESS_REQUIREMENTS.md) | 17 |
| 21 | Roadmap 30/60/90/180/365 | [`30_60_90_180_365_ROADMAP.md`](30_60_90_180_365_ROADMAP.md) | 18 |

**Supporting:**
[`MASTER_PLAN_AUDITS.md`](MASTER_PLAN_AUDITS.md) (passes 1–8) ·
[`RED_TEAM_REVIEW.md`](RED_TEAM_REVIEW.md) (pass 9) ·
[`INTEGRATION_PASS.md`](INTEGRATION_PASS.md) ·
[`EXECUTIVE_SYNTHESIS.md`](EXECUTIVE_SYNTHESIS.md) ·
[`DELIVERABLE_MAP.md`](DELIVERABLE_MAP.md) ·
[`docs/06-validation/hypotheses/HYPOTHESIS_REGISTER.md`](../../06-validation/hypotheses/HYPOTHESIS_REGISTER.md) ·
[`docs/06-validation/findings/LEARNING_LOG.md`](../../06-validation/findings/LEARNING_LOG.md) ·
[`docs/09-handoffs/claude/CLAUDE_HANDOFF.md`](../../09-handoffs/claude/CLAUDE_HANDOFF.md)

## 4. Reading paths

| If you are | Read |
|---|---|
| The human owner, deciding whether to approve | `EXECUTIVE_SYNTHESIS.md` → `RED_TEAM_REVIEW.md` → §7 below → `ADR-0005` |
| About to start executing | `30_60_90_180_365_ROADMAP.md` §11 → §3 → `FIELD_VALIDATION_PLAN.md` |
| Checking the reasoning | Modules 1 → 2 → 3 → 4 in order |
| The Brand workstream | `BRAND_BUSINESS_INTERFACE.md`, then `POSITIONING_ARCHITECTURE.md` §5, §11 |
| The technical workstream | `WEB_BUSINESS_REQUIREMENTS.md`, then `TOOLING_AUTOMATION_REQUIREMENTS.md` |
| Sceptical | `RED_TEAM_REVIEW.md` first |

## 5. The gates

| Gate | Day | Question | Threshold |
|---|---:|---|---|
| D0 | 3 | Do we know the founder's constraints? | `U-01`–`U-05` answered |
| D3 | 30 | Can we reach them? | 8 qualified conversations |
| D4 | 45 | Is the problem real to them? | 5/10 volunteer it unprompted |
| **D5** | **60** | **Will they pay?** | **2 paid diagnostics** |
| D6 | 90 | Can we deliver profitably? | Baseline captured; ≤130% of budgeted hours |
| D8 | 120 | Is it a product? | 3 cores, ≤±25% variance |
| D9 | 180 | Does it stick? | 1 operated account past 90 days |
| Gate 1 | after D5 | Does the brand fit the buyer? | `BRAND_BUSINESS_INTERFACE.md` §7 |

Full specification: `DECISION_TREE.md`.

## 6. What this plan does not decide

Per `STOP_RULE.md`, `OWNERSHIP_MATRIX.md` and `HUMAN_AUTHORITY.md`:

- **The agency name and visual identity** — Brand workstream. `docs/03-brand/` is untouched.
- **The actual vertical** — proposed and ranked; selected by evidence at D2/D3.
- **Any price** — modelled; no price is a commitment.
- **Legal, tax and jurisdiction questions** — qualified local professionals only.
- **Whether the business should exist** — `RED_TEAM_REVIEW.md` RT-09 states the case against;
  the decision is the founder's.

## 7. Decisions requiring human approval

| ADR | Decision | Consequence of approving |
|---|---|---|
| [`ADR-0005`](../../07-decisions/ADR-0005-diagnostic-led-vertical-thesis.md) | Adopt the diagnostic-led vertical productized studio as the **working thesis under validation** | Authorises 90 days of validation effort; activates the stop rule. Does **not** freeze the model |
| [`ADR-0006`](../../07-decisions/ADR-0006-two-segment-validation-portfolio.md) | Validate two segments (75/25) rather than committing to one | Sets the outreach allocation and the D3 swap rule |
| [`ADR-0007`](../../07-decisions/ADR-0007-paid-diagnostic-entry-offer.md) | Make a paid diagnostic the mandatory entry offer; no speculative proposals | Accepts a harder first sale in exchange for funded qualification and baseline-driven proof |
| [`ADR-0008`](../../07-decisions/ADR-0008-defer-pricing-freeze.md) | Treat all prices as `INFERRED RANGE` until WTP evidence exists | No price may be published or frozen before H-04 |
| [`ADR-0009`](../../07-decisions/ADR-0009-ai-as-mechanism-not-category.md) | AI is a delivery mechanism, never the category or the headline | Forfeits AI-budget and novelty-seeking demand deliberately |

## 8. Definition of Done — evidence

Against `CLAUDE_KICKSTART.md` "Definition of Done" and Issue #2 "Required Master Outputs":

| Required | Where |
|---|---|
| What business models deserve consideration | Module 2 |
| Which ICPs deserve validation | Module 5 |
| What could be sold | Module 7 |
| How it could be priced | Module 8 |
| How demand could be generated | Module 10 |
| How proof would be created | Module 9 |
| How delivery would work | Modules 12, 13 |
| What economics need to hold | Module 8 |
| What must be validated in the real market | Module 18 |
| What should happen over the next 90 days | Module 21 |
| Which decisions wait for the Brand/Business Fit Review | Module 19, §6 above |
| Evidence discipline maintained throughout | Module 1, enforced by citation |
| Nine audit passes | `MASTER_PLAN_AUDITS.md`, `RED_TEAM_REVIEW.md` |
| Contradictions resolved or logged | `INTEGRATION_PASS.md` §4 |
| Cross-document dependencies | `INTEGRATION_PASS.md` §2; front-matter `depends_on` |
| Executive synthesis | `EXECUTIVE_SYNTHESIS.md` |
| Handoff | `docs/09-handoffs/claude/CLAUDE_HANDOFF.md` |

Full deliverable-name mapping: `DELIVERABLE_MAP.md`.
