---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - PRICING_AND_ECONOMICS_MODEL.md
  - SALES_SYSTEM.md
  - DELIVERY_OS.md
---
# Agency Scorecard and Measurement System

> **Module 17 of the Agency Master Plan** (Issue #2 Phase 14). Metric definitions, review cadence
> and decision thresholds. A metric without a definition is an argument; a metric without a
> threshold is decoration.

## 1. Design rules

1. **Every metric has an exact definition.** "Conversion rate" means nothing until numerator,
   denominator and time basis are fixed.
2. **Every metric has a threshold and a named action.** If nothing happens at any value, the metric
   is not measured.
3. **Fewer metrics, reviewed seriously.** A solo operator who tracks 40 metrics reviews none.
4. **Leading before lagging during validation.** Revenue at month 2 tells you nothing; qualified
   conversations tell you everything.
5. **Metrics calibrate assumptions.** Each links back to an `A-##` in the evidence register.
6. **Effective yield per founder hour is the master metric.** Everything else explains it.

## 2. The master metric

> **Effective Yield = total revenue recognised in the period ÷ total founder hours worked in the
> period (delivery + sales + admin).**

Not revenue, not margin, not utilisation. In a business whose only real input is founder hours
(`E-25`), this is the number that says whether the business is working.

| Phase | Target (`INFERRED RANGE`) |
|---|---|
| Ramp (months 1–6) | USD 30–50/h — depressed by unbillable validation work, and that is correct |
| Establishing (7–12) | USD 60–90/h |
| Established (13–24) | USD 90–130/h |
| Specialist (24+) | USD 130+/h |

**Trigger T-5:** below USD 50/h for two consecutive months after month 6 → stop and re-plan.

## 3. Metric definitions

### 3.1 Pipeline and acquisition

| ID | Metric | Definition | Target | Action threshold | Calibrates |
|---|---|---|---|---|---|
| M-01 | Contacts initiated | Distinct businesses receiving touch 1 | 15–20/wk | <10/wk → capacity or discipline problem | — |
| M-02 | Reply rate | Replies ÷ contacts, any reply | ≥ 8% | <8% after 60 → rewrite message (`ACQUISITION_MARKETING_SYSTEM.md` CH-1) | — |
| M-03 | **Qualified conversations** | ≥20 min with a DM or direct influencer at an ICP-fitting business | ≥ 2/wk | <8 by day 30 → D3 | H-03 |
| M-04 | Teardown → conversation | Conversations ÷ teardowns delivered | ≥ 15% | <15% after 10 → L0 is consuming capacity (`OFFER_ARCHITECTURE.md` §2) | — |
| M-15 | Referral rate | Referrals received ÷ delivered clients | ≥ 0.5 | <0.3 after 4 clients → the ask is not being made, or delivery is not remarkable | — |
| M-16 | Inbound conversations | Conversations from content/site/referral without outbound | Rising from month 6 | Flat at month 9 → content is not working | — |

### 3.2 Sales

| ID | Metric | Definition | Target | Action threshold | Calibrates |
|---|---|---|---|---|---|
| M-05 | Conversation → qualified | Passing Q1–Q4 ÷ conversations | ≥ 40% | <40% → targeting is wrong | — |
| M-06 | Qualified → diagnostic sold | Diagnostics sold ÷ qualified | 20% | <10% after 15 → H-01 failing → D5 | `A-09` |
| M-07 | **Diagnostic → core** | Cores sold ÷ diagnostics delivered | 30% | 3 consecutive non-conversions → T-10 | `A-08` |
| M-08 | Core proposal win rate | Cores won ÷ core proposals | 30–60% | **>70% → raise price (T-3)**; <20% after 8 → T-4 | — |
| M-09 | Sales-cycle length | Days, first contact → signature, by offer | 30–60 d | >90 d → qualification or authority failure | `A-10` |
| M-10 | **Unbilled sales hours per close** | Sales+admin hours on won opportunities ÷ closes | ≤ 20 | >40 → T-7 | `A-14` |
| M-17 | Loss-reason distribution | Count by code (`SALES_SYSTEM.md` §8) | — | 3 consecutive L-07 → D4 resonance failure | — |

### 3.3 Revenue and economics

| ID | Metric | Definition | Target | Action |
|---|---|---|---|---|
| M-18 | Cash collected | Actually received in period | Per scenario | Below worst case for 2 months → D7 |
| M-19 | Revenue mix | % by offer tier | L3 rising | L3 <15% at month 12 → structural weakness |
| M-20 | **Effective yield** | §2 | Per phase | T-5 |
| M-21 | Average core value | Mean core contract value | Rising | Falling → price erosion or scope shrinkage |
| M-22 | Contribution margin | (Revenue − direct costs) ÷ revenue | >85% | <75% → cost base out of control |
| M-23 | Client concentration | Largest client ÷ trailing-3-month revenue | <40% | >40% → T-8 |
| M-24 | Tax reserve adequacy | Reserved ÷ estimated obligation | ≥ 100% | <100% → correct immediately |

### 3.4 Delivery

| ID | Metric | Definition | Target | Action | Calibrates |
|---|---|---|---|---|---|
| M-25 | Hours vs budget | Actual ÷ budgeted delivery hours | ≤ 110% | >130% twice → T-1 | §2.1 pricing model |
| M-26 | **Rework ratio** | Hours logged as rework ÷ total delivery hours | ≤ 20% | >35% → T-2 | `A-13` |
| M-27 | On-time milestone rate | Milestones met ÷ total, excluding client-caused delay | ≥ 85% | <70% → estimation failure | — |
| M-28 | Defects at client review | Count per engagement | ≤ 2 | >5 → internal QA failed | — |
| M-29 | Change orders | Count and value per engagement | 1–2 | **0 → silent absorption**; >4 → under-scoping | — |
| M-30 | Template reuse | Reused components ÷ total | Rising | Flat → productization not happening (D8 risk) | — |
| M-31 | Time to first outcome | Launch → first outcome record | ≤ 30 d | >45 d → proof engine slipping | — |

### 3.5 Client health and retention

| ID | Metric | Definition | Target | Action | Calibrates |
|---|---|---|---|---|---|
| M-11 | **L3 attachment** | Cores with L3 attached within 60 d ÷ cores delivered | 40% | <20% after 5 → T-6 | `A-11` |
| M-12 | L3 retention | 1 − (accounts churned ÷ accounts at period start) | ≥ 95%/mo | Any churn <90 d → diagnose, do not discount (D9) | `A-12` |
| M-32 | Report engagement | % monthly reports opened/discussed | ≥ 80% | <50% → **the strongest churn predictor** |  — |
| M-33 | Expansion rate | Expansion revenue ÷ total client revenue | ≥ 15% by month 12 | Low → QBR not happening | — |
| M-34 | Reference willingness | Clients agreeing to act as a reference ÷ delivered | ≥ 60% | <40% → delivery quality problem | — |
| M-35 | Net revenue retention | (Start + expansion − churn) ÷ start, on operated accounts | >100% | <90% → churn exceeds expansion | — |

### 3.6 Proof and capability

| ID | Metric | Definition | Target | Action |
|---|---|---|---|---|
| M-36 | Baseline capture rate | Engagements with a day-1 baseline ÷ total | **100%** | Any miss is a process failure, investigated |
| M-37 | Outcome capture rate | Engagements with an outcome record ÷ completed | **100%** | Same |
| M-38 | Case studies published | Cumulative | 1 by month 6, 3 by month 12 | Behind → proof engine stalled |
| M-39 | Benchmark dataset size | Rows with complete fields | n≥5 by month 9 | Enables T3 claims |

### 3.7 Founder and operations

| ID | Metric | Definition | Target | Action |
|---|---|---|---|---|
| M-40 | Founder hours worked | Logged weekly | ≈ `A-03` | Persistently >40 → unsustainable; the model is mis-sized |
| M-41 | Hour allocation | % delivery / sales / admin | Per `PRICING_AND_ECONOMICS_MODEL.md` §2 | Sales <10% for 3 weeks → **protected block broken** |
| M-42 | WIP | Active engagements by type | ≤ limits (`OPERATING_MODEL.md` §5) | Over limit → stop selling |
| M-43 | **Founder dependency** | % of delivery hours only the founder can perform | Falling from month 9 | Flat → delegation not progressing |
| M-44 | Admin hours | Weekly | ≤ 2 | >4 → delegate |

## 4. Review cadence

| Cadence | Metrics | Duration | Output |
|---|---|---|---|
| **Weekly** (Mon) | M-01…M-03, M-40…M-42, WIP, pipeline | 45 min | Week's plan |
| **Monthly** (1st week) | All, plus assumption calibration and trigger check | 2 h | Written monthly review |
| **Quarterly** | All, plus strategy, pricing, offers, hiring triggers, ADR review | Half day | Quarterly decision memo |

### 4.1 Monthly review agenda
1. Scorecard vs targets.
2. **Trigger check** — any T-1…T-11 fired? (`PRICING_AND_ECONOMICS_MODEL.md` §11)
3. **Assumption calibration** — which `A-##` gained evidence? Update the register with the *grade of
   evidence obtained*, not with optimism.
4. Loss-reason review.
5. Client health review.
6. One decision, recorded.

**Rule:** the monthly review produces at least one written decision or an explicit "no change,
because…". A review that produces nothing was a status report.

## 5. Validation-phase scorecard *(days 0–90)*

During validation most metrics have no data and chasing them is noise. Track only these:

| Metric | Day 30 | Day 60 | Day 90 |
|---|---|---|---|
| Qualified conversations (M-03) | **≥ 8** | ≥ 16 | ≥ 22 |
| Problem volunteered unprompted | — | **≥ 5/10** | — |
| Diagnostics sold | 0–1 | **≥ 2** | ≥ 3 |
| Cores sold | 0 | 0–1 | **≥ 1** |
| Cash collected | 0 | ≥ 2,400 | ≥ 8,000 |
| Buyer phrases logged | ≥ 10 | ≥ 25 | ≥ 40 |
| Teardowns delivered | ≥ 8 | ≥ 16 | ≥ 20 |

Bold values are `DECISION_TREE.md` gate thresholds. Missing a bold value triggers the gate's
failure branch — it is not a stretch target to be rationalised.

## 6. Anti-metrics

Deliberately **not** tracked, because they consume attention and change no decision:

| Not tracked | Why |
|---|---|
| Social followers / impressions | Not correlated with revenue at this scale |
| Website traffic (before month 6) | Volume is meaningless without intent |
| Proposals sent | Rewards speculative proposals — the exact behaviour `SALES_SYSTEM.md` §5.1 prohibits |
| Hours worked as a success measure | Rewards inefficiency; M-20 already captures the real question |
| Number of tools or automations built | Activity, not outcome |
| NPS at current client volume | n<10 makes it noise. Use M-34 (reference willingness), which is behavioural |

## 7. Data collection

| Source | Feeds | Method |
|---|---|---|
| CRM | Pipeline, sales, loss codes | Automated on stage change |
| Time tracking | Hours, rework, yield | **Manual, logged as worked** |
| Accounting | Cash, margin, concentration | Monthly, with bookkeeper |
| Engagement records | Delivery, proof | At gates |
| Client systems | Outcomes | Automated where possible |
| Interview log | Buyer phrases, resonance | Manual, after each conversation |

**The weak link is time tracking**, and it is the input to the master metric. Reconstructed hours
systematically under-report rework, which is precisely the variable that decides whether the
pricing model holds. Log as worked, or the scorecard is fiction.
