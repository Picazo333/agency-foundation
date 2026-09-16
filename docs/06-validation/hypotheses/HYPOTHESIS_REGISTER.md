---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - FIELD_VALIDATION_PLAN.md
---
# Hypothesis Register

> Live tracking table for the hypotheses defined in `../FIELD_VALIDATION_PLAN.md` §2.
> **Instruments that produce this evidence:** [`../field-kit/00_README.md`](../field-kit/00_README.md).
> Which instrument and which field feeds each hypothesis:
> [`../field-kit/17_TRACEABILITY_MATRIX.md`](../field-kit/17_TRACEABILITY_MATRIX.md).
> **This file is updated as evidence arrives.** Status may only advance on the grade of evidence
> actually obtained (`EVIDENCE_AND_ASSUMPTIONS_REGISTER.md` §5 rule 2): interviews produce
> `SIGNAL`; only money received produces `FACT`.

## Status vocabulary

`OPEN` — no evidence · `TESTING` — test running · `SUPPORTED (SIGNAL)` — qualitative support ·
`SUPPORTED (FACT)` — money or measurement confirms · `FALSIFIED` · `PARTIAL` · `DEFERRED`

## Register

| ID | Hypothesis | Priority | Gate | Status | Evidence | Kill criterion | Updated |
|---|---|---:|---|---|---|---|---|
| H-01 | Buyer pays for a diagnostic before implementation | 1 | D5 | `OPEN` | — | 0 sales from 20 qualified | 2026-09-16 |
| H-03 | 8+ qualified conversations reachable in 30 days | 2 | D3 | `OPEN` | — | <4 after two rotations | 2026-09-16 |
| H-03b | The signer is directly reachable | 7 | D5 | `OPEN` | — | Signer unreachable in >70% of cases | 2026-09-16 |
| H-04 | Price tolerance within modelled ranges | 5 | D5 | `OPEN` | — | >70% immediate dismissal at base price | 2026-09-16 |
| H-05 | Sales cycle 30–60 days | 12 | D5 | `OPEN` | — | Median >120 days | 2026-09-16 |
| H-06 | Usable baseline capturable in ≤2 weeks | 4 | D6 | `OPEN` | — | <25% have reconstructable data | 2026-09-16 |
| H-07 | No local competitor occupies this position | 8 | D4 | `OPEN` | — | Established local competitor with references | 2026-09-16 |
| H-08 | Distinctive visual work does not reduce trust | 9 | Gate 1 | `OPEN` | — | Consistent negative reaction in 8 buyers | 2026-09-16 |
| H-09 | 40% of cores attach an operated layer | 6 | D9 | `DEFERRED` | Requires 3 delivered cores | 0 of 3 attach | 2026-09-16 |
| H-10 | Buyers recognise the problem unprompted | 3 | D4 | `OPEN` | — | ≤1 of 10 unprompted | 2026-09-16 |
| H-11 | Category language is comprehensible and budgetable | 10 | D4 | `OPEN` | — | No buyer can name a budget line | 2026-09-16 |
| H-12 | Delivery fits hour budget within 130% | 11 | D6 | `DEFERRED` | Requires 1 delivered core | >150% on two engagements | 2026-09-16 |

## Assumption linkage

| Hypothesis | Calibrates |
|---|---|
| H-01 | `A-07` |
| H-03 | Access viability; `U-04` |
| H-04 | `U-07`, converts `INFERRED RANGE` → `PRICE SIGNAL`, fires T-11 |
| H-05 | `A-10` |
| H-06 | `U-08` |
| H-07 | `U-12` |
| H-08 | `U-11`, `E-24` |
| H-09 | `A-11` |
| H-10 | Thesis core claim |
| H-12 | `A-13`, §2.1 of the pricing model |

## Update protocol

1. After each interview, update the Evidence column with the interview file reference — never with
   a summary judgement.
2. Advance status only at the defined sample size, not at the first encouraging conversation.
3. On falsification, follow the action in `FIELD_VALIDATION_PLAN.md` §6 **and** record it in
   `../findings/LEARNING_LOG.md` within 7 days.
4. Falsified hypotheses stay in the register. Deleting them erases the reasoning that made the next
   decision correct.
