---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - ../FIELD_VALIDATION_PLAN.md
  - ../../08-plans/master/AGENCY_MASTER_PLAN.md
---
# 00 — Field Validation Execution Kit

> **This is the operational entry point for validation.**
> `../FIELD_VALIDATION_PLAN.md` says *what* must be tested and why. This kit is *how*, with the
> instruments filled in. It changes no threshold, no hypothesis and no decision rule.
>
> **To start tomorrow morning: open `16_VALIDATION_LAUNCH_CHECKLIST.md` and work down it.**

## The loop

```text
  TARGET ──► RESEARCH ──► TEARDOWN ──► OUTREACH ──► CONVERSATION ──► QUALIFY
                                                                        │
                                            ┌───────────────────────────┘
                                            ▼
                                    OFFER ──► LOG EVIDENCE ──► WEEKLY REVIEW
                                                                        │
                                                                        ▼
                                                    DECISION GATE ──► CONTINUE / PIVOT / STOP
```

## Step by step

| Step | Open | Produces | Tests | Do NOT conclude |
|---|---|---|---|---|
| **0. Founder inputs** | `01_FOUNDER_INPUTS_U01_U05.md` | Answers to U-01…U-05 + recalibrated numbers | D0 | That the answers validate anything — they *constrain* the plan |
| **1. Target** | `02_TARGET_ACCOUNT_LEDGER.md` → `data/target_account_ledger.csv` | 40–60 accounts with reasons | H-03 | That a long list is a pipeline |
| **2. Research** | `03_ACCOUNT_RESEARCH_TEMPLATE.md` | Observations classified OBSERVABLE / INFERENCE / QUESTION | H-03, H-07 | Anything about their revenue or performance. You cannot see it |
| **3. Teardown** | `04_TEARDOWN_SOP.md` + `05_TEARDOWN_TEMPLATE.md` | One-page teardown + 5-min video | H-03, X-01 | That a good teardown means they have the problem |
| **4. Outreach** | `06_OUTREACH_SEQUENCE.md` | 4 touches, then stop | H-03, H-03b | That a reply means interest, or interest means demand |
| **5. Conversation** | `07_BUYER_INTERVIEW_GUIDE.md` | 40-min interview, 12 min sealed | **H-10**, H-06, H-11, H-07 | Anything from agreement obtained after you named the problem |
| **6. Record** | `08_INTERVIEW_RECORD_TEMPLATE.md` | Verbatim separated from interpretation | all | That your summary is their words |
| **7. Classify resonance** | `10_PROBLEM_RESONANCE_LOG.md` | VOLUNTEERED / PROMPTED / AGREED | **H-10 → D4** | That PROMPTED or AGREED counts. Only VOLUNTEERED does |
| **8. Qualify** | `09_QUALIFICATION_SCORECARD.md` | QUALIFIED / WITH RISK / NOT YET / DISQUALIFIED | D3, D5 | That "they liked it" qualifies anyone |
| **9. Offer** | `11_PRICE_SIGNAL_LOG.md` + `12_DIAGNOSTIC_SALES_ATTEMPT_LOG.md` | Price reaction; payment or not | **H-01, H-04 → D5** | That verbal intent is a sale. Only cleared money is |
| **10. Experiments** | `13_EXPERIMENT_RUNBOOK.md` | X-01…X-06 results | various | "Statistically significant" — no experiment here has the sample |
| **11. Weekly review** | `14_WEEKLY_VALIDATION_REVIEW.md` | Learning-log entry + one decision | all | That a week with nothing wrong was a good week |
| **12. Gate** | `15_DECISION_GATE_CHECKLIST.md` | PASS / PARTIAL / FAIL + next action | D0, D3, D4, D5, D6 | That a near miss is a pass. Use `18_GATE_OVERRIDE_REGISTER.md` and pay the cost |

## The four rules the whole kit exists to enforce

| # | Rule | Enforced in |
|---|---|---|
| 1 | **Only VOLUNTEERED counts for resonance.** The problem must be described by the buyer before it is described to them | Interview guide §0 sealed phase · resonance log · interview record §1 integrity header |
| 2 | **Only cleared money is `FACT`.** Interest, verbal intent and signatures are worth zero | Price log §1 ladder · sales log §2 · gate D5 |
| 3 | **Observation and inference are never mixed.** You cannot see a business's performance from outside | Research template §2 · teardown prohibitions · interview record §4–§8 |
| 4 | **Gates are run on their due date, counted before they are discussed, and failed out loud** | Gate checklist §0 · override register |

## What this kit will NOT do for you

- It will not tell you whether the business is good. It shortens the time to finding out.
- It will not make the first cold conversation comfortable.
- It will not stop you rationalising a failed gate — it only makes it expensive and visible.
- It produces `SIGNAL`, not proof. Twelve interviews are thematic saturation, never significance.

## Files

| File | Type |
|---|---|
| `00_README.md` | This map |
| `01_FOUNDER_INPUTS_U01_U05.md` | Input form — **start here** |
| `02_TARGET_ACCOUNT_LEDGER.md` | Ledger spec |
| `03_ACCOUNT_RESEARCH_TEMPLATE.md` | Per-account research |
| `04_TEARDOWN_SOP.md` · `05_TEARDOWN_TEMPLATE.md` | Teardown production |
| `06_OUTREACH_SEQUENCE.md` | Messages + reply handling |
| `07_BUYER_INTERVIEW_GUIDE.md` | Interview script |
| `08_INTERVIEW_RECORD_TEMPLATE.md` | Evidence record |
| `09_QUALIFICATION_SCORECARD.md` | Categorical gates |
| `10_PROBLEM_RESONANCE_LOG.md` | H-10 classification |
| `11_PRICE_SIGNAL_LOG.md` | H-04 price evidence |
| `12_DIAGNOSTIC_SALES_ATTEMPT_LOG.md` | H-01 decisive log |
| `13_EXPERIMENT_RUNBOOK.md` | X-01…X-06 |
| `14_WEEKLY_VALIDATION_REVIEW.md` | Weekly procedure |
| `15_DECISION_GATE_CHECKLIST.md` | Gate operator checklists |
| `16_VALIDATION_LAUNCH_CHECKLIST.md` | **Day-0 sequence** |
| `17_TRACEABILITY_MATRIX.md` | Hypothesis → instrument → field → gate |
| `18_GATE_OVERRIDE_REGISTER.md` | Append-only override record |
| `19_KIT_AUDIT_LOG.md` | The eight quality passes run on this kit |
| `data/` | CSV templates, headers only |
| `tests/` | Three synthetic fixtures — **NOT EVIDENCE** |

## What happens after a diagnostic is sold

This kit ends where validation ends: at cleared payment. From that point the operator moves to the
delivery instruments, which already exist in the plan and are **not** duplicated here:

| Next | Where |
|---|---|
| Deliver the diagnostic (18-day phased process) | `DELIVERY_OS.md` §4 |
| Capture the baseline **on day 1** — gated, non-skippable | `PROOF_STRATEGY.md` §10 |
| Onboarding, access, clock-pause clause | `CLIENT_LIFECYCLE.md` §2 |
| Log hours by phase, rework separately | `DELIVERY_OS.md` §11 — calibrates `A-13`, feeds H-12 |
| Run X-04 on the first delivery | `13_EXPERIMENT_RUNBOOK.md` |
| D6 delivery gate at day 90 | `15_DECISION_GATE_CHECKLIST.md` |

**Validation does not stop when the first sale lands.** The D5 gate still needs a second payment,
and the outreach cadence must survive the first delivery — that is the exact point at which solo
operators let the pipeline empty (`OPERATING_MODEL.md` §6.1, the protected sales block).

## Rules of use

1. **Log within 24 hours.** Verbatim quality collapses after that.
2. **Classify from transcripts, not memory.** Memory systematically upgrades.
3. **Never mix warm and cold** in the D3 count, or you will measure your network and call it a market.
4. **Never merge verbal intent with payment** in any report.
5. **Synthetic examples are marked and must be deleted before use.** None may ever enter an evidence log.
6. **No personal contact data in this repository** (`data/README.md`).
7. **The stop rule is active:** no further strategic planning artifact until 10 qualified buyer
   conversations are logged (`AGENCY_THESIS.md` §11).

## Status

`review` / `workbench`. This kit is instrumentation, not canon. It implements
`../FIELD_VALIDATION_PLAN.md` without changing it, and it assumes `ADR-0006`…`ADR-0010` are
**PROPOSED** — it does not depend on their approval to be executed, except that `ADR-0007` sets the
segment portfolio and `ADR-0008` sets the paid-diagnostic entry offer.
