---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - ../FIELD_VALIDATION_PLAN.md
  - ../hypotheses/HYPOTHESIS_REGISTER.md
---
# 17 — Traceability Matrix

> **Pass 1 output.** Every hypothesis in `../FIELD_VALIDATION_PLAN.md` §2 mapped to the instrument
> that tests it, the **specific field** that records the evidence, and the gate that consumes it.
>
> A hypothesis with no field is not testable, however much prose surrounds it. This matrix exists
> to make that failure visible.

## 1. Coverage

| Hypothesis | Priority | Instrument | Evidence field | Gate | Status |
|---|---:|---|---|---|---|
| **H-01** buyer pays for diagnosis | 1 | `12_DIAGNOSTIC_SALES_ATTEMPT_LOG.md` | `payment_received` (cleared) ∧ `discount_offered=N` | **D5** | ✅ |
| **H-03** 8+ qualified conversations in 30 days | 2 | `02_TARGET_ACCOUNT_LEDGER.md` | `qualified_conversation` (strict 4-part test) + warm/cold split | **D3** | ✅ |
| **H-10** problem volunteered unprompted | 3 | `10_PROBLEM_RESONANCE_LOG.md` | `PC1..PC7 = VOLUNTEERED` ∧ `counts_in_denominator=Y` | **D4** | ✅ |
| **H-06** baseline capturable ≤ 2 weeks | 4 | `08_INTERVIEW_RECORD_TEMPLATE.md` §6 | "≥ 4 weeks reconstructable?" — aggregated ≥50% pass / <25% fail | **D5** (sample) + D6 (delivery) | ✅ |
| **H-04** price tolerance in range | 5 | `11_PRICE_SIGNAL_LOG.md` | `reaction_class` ∈ {engaged, counteroffer} ÷ total | **D5** | ✅ |
| **H-09** 40% recurring attachment | 6 | Engagement records | Offered day 21 of build | D9 (day 180) | ⏳ **out of window** |
| **H-03b** signer reachable | 7 | `08_INTERVIEW_RECORD_TEMPLATE.md` §6 Authority; ledger `committee_position` | signer role named; `signer_present` in sales log | D5 | ✅ |
| **H-07** no competitor in position | 8 | `03_ACCOUNT_RESEARCH_TEMPLATE.md` §3.9; interview §6 Competitive | named competitors + their positioning | D4 | ✅ |
| **H-08** distinctive work ≠ lower trust | 9 | `08_INTERVIEW_RECORD_TEMPLATE.md` §10b; X-05 | "which would you forward to your partner?" | Gate 1 | ✅ |
| **H-11** category language budgetable | 10 | `08_INTERVIEW_RECORD_TEMPLATE.md` §4 Phase 5 | **budget line named, verbatim** | D4 | ✅ |
| **H-12** delivery ≤ 130% of budget | 11 | Time log by phase (`DELIVERY_OS.md` §11); X-04 | actual vs budgeted hours; rework separate | D6 | ⏳ post-D5 |
| **H-05** cycle 30–60 days | 12 | `12_DIAGNOSTIC_SALES_ATTEMPT_LOG.md` | `days_quote_to_payment`; median weekly | informs D5 | ✅ |

⏳ = cannot be tested inside the 90-day window; capture location defined in
`13_EXPERIMENT_RUNBOOK.md` §2b so the absence is deliberate, not an oversight.

## 2. Gate → required inputs

| Gate | Day | Requires | From |
|---|---:|---|---|
| **D0** | 3 | U-01…U-05 + recalibration | `01_FOUNDER_INPUTS_U01_U05.md` |
| **D3** | 30 | Qualified-conversation count, warm/cold split, X-01 arms | Ledger, runbook |
| **D4** | 45 | Clean resonance denominator ≥ 10; volunteered count; verbatim per hit | Resonance log, interview records |
| **D5** | 60 | Cleared, undiscounted payments; objection distribution; price reactions | Sales log, price log |
| **D6** | 90 | Baseline captured day 1; hours vs budget; rework ratio; reference willingness | Delivery records, X-04 |
| **Gate 1** | after D5 | Brand V0 + H-08 reactions | Interview §10b, X-05 |

## 3. Experiment → hypothesis → decision

| Exp | Hypothesis | Decision it changes | Recorded in |
|---|---|---|---|
| X-01 teardown response | H-03 | Whether a D3 fail is *message* or *segment* | Ledger `notes` (arm), reply rate |
| X-02 price probe | H-04 | Pricing §4 re-derivation; T-11 | Price log `x02_arm` |
| X-03 message frame | H-11 | Positioning language; Brand input | Interview §4 Phase 5 |
| X-04 concierge pilot | H-06, H-12 | D6; `A-13`/`A-14` calibration | Time log; delivery record |
| X-05 brand register | H-08 | Gate 1 PASS/MUTATE | Interview §10b |
| X-06 partner probe | CH-3 viability | Whether pivot P-C is available | Ledger `source=partner` |

## 4. Assumption → evidence route

| Assumption | Calibrated by | Instrument |
|---|---|---|
| `A-07` buyer pays for diagnosis | H-01 | Sales log |
| `A-08` 30% diagnostic→core | post-D5 | Sales log |
| `A-09` 20% qualified→diagnostic | H-01 | Sales + ledger |
| `A-10` cycle 30–60 days | H-05 | Sales log |
| `A-11` 40% L3 attachment | H-09 | ⏳ out of window |
| `A-13` 20% rework | H-12 | Time log, rework separate |
| `A-14` 20 unbilled sales hours | observation | Time log per opportunity |
| `A-01`…`A-06`, `A-18` | U-01…U-05 | Founder inputs §7 |
| `U-07` WTP | H-04 | Price log |
| `U-08` baseline availability | H-06 | Interview §6 |
| `U-09` buying committee | H-03b | Interview §6 Authority |
| `U-12` competitive density | H-07 | Research §3.9 + interview §6 |

## 5. Scorecard metric → source

| Metric | Source field |
|---|---|
| M-01 contacts | ledger `touch_count ≥ 1` |
| M-02 reply rate | ledger `reply ≠ none` |
| **M-03 qualified conversations** | ledger `qualified_conversation = Y` |
| M-04 teardown → conversation | ledger `teardown_status=sent` ∧ `conversation_held` |
| M-05 conversation → qualified | ledger `qualification_status` |
| M-06 qualified → diagnostic sold | sales log `payment_received` |
| M-10 unbilled sales hours | time log per opportunity |
| M-17 loss distribution | ledger `loss_code` |
| M-36 baseline capture rate | delivery records |

## 6. Orphan check

| Check | Result |
|---|---|
| Hypotheses with no instrument | **0** |
| Hypotheses with no evidence field | **0** |
| Hypotheses with no gate or interpretation rule | **0** |
| Instruments testing no hypothesis | **0** — `14`, `15`, `16`, `17`, `18` are procedural and are consumers, not producers |
| Gates with an unsourced input | **0** |
| Fields recording nothing that changes a decision | **0** after the Pass 5 information-efficiency audit (`19_KIT_AUDIT_LOG.md`) |

## 7. Known coverage limits — stated, not hidden

1. **H-09 cannot be tested in 90 days.** It needs three delivered cores. `A-11` — the plan's most
   consequential unvalidated assumption — remains unvalidated at the end of this kit's window.
2. **H-12 is n=1 at D6.** One delivery is an existence proof of feasibility, not of repeatability.
   Repeatability is D8, at day 120.
3. **H-07 relies on buyer report and desk search.** No systematic competitive census exists. A
   competitor no buyer mentions and no search surfaces stays invisible.
4. **H-08 at n=8 is qualitative reaction only.** It cannot measure conversion effect.
5. **Warm-sourced conversations do not test cold reachability.** If D3 passes on warm contacts, H-03
   is supported only for warm access — enforced as a mandatory caveat at the gate.
