---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - ../../02-strategy/sales/SALES_SYSTEM.md
  - ../../02-strategy/icp/ICP_FRAMEWORK.md
  - 08_INTERVIEW_RECORD_TEMPLATE.md
---
# 09 — Qualification Scorecard

> **Instrument type:** categorical gate. Run **after** every interview, from the record — never
> from memory and never during the call.
> **Implements:** `SALES_SYSTEM.md` §3 (Q1–Q4) and `ICP_FRAMEWORK.md` §6.7.
> **Feeds:** ledger field 24, D3/D5 counting, `12_DIAGNOSTIC_SALES_ATTEMPT_LOG.md`.

## 1. Why this is categorical, not scored

A weighted score lets a strong "they seemed keen" compensate for a missing signer. It cannot. There
is no amount of enthusiasm that substitutes for someone who can authorise spend.

So: **gates, not points.** Each gate is pass or fail on an observable condition, and the conditions
are written so that *"they liked the idea"* satisfies none of them.

> **Enthusiasm is not a gate and appears nowhere in this instrument.** If you find yourself wanting
> to record it, put it in §7 of the interview record where it belongs — as your interpretation.

## 2. Hard disqualifiers — check first

Any one → `DISQUALIFIED`. Stop; do not run the gates.

| # | Disqualifier | Source |
|---|---|---|
| D-a | Will not grant read access to booking/enquiry data, and will not instrument | `RF-8`, loss code `L-09` |
| D-b | Wants clinical / patient-record integration in the first engagement | `RF-7`, `DNS-9` — ⚖️ blocked pending counsel |
| D-c | Wants ad management as the primary deliverable | `RF-2`, `DNS-1` |
| D-d | Wants results-based / revenue-share pricing | `DNS-11` |
| D-e | Under contract with an incumbent whose scope this duplicates, with no intent to change | `ICP_FRAMEWORK.md` §6.7 |
| D-f | Price-shopping against a named cheaper competitor at first contact | `DNS-3` dynamics |
| D-g | Signer will not join any call, ever | `SALES_SYSTEM.md` Q3 |
| D-h | Outside the segment definition and not a deliberate hedge/rotation test | `ICP_FRAMEWORK.md` §6.1 |
| D-i | Has opted out of contact | Binding, permanent |

## 3. The gates

Each gate: **PASS / RISK / FAIL**. `RISK` means unresolved but resolvable, with a named next action.

### Q1 — Business fit
| Result | Condition |
|---|---|
| PASS | Meets `ICP_FRAMEWORK.md` §6.1 size band (3+ locations, or 2 with a third planned in 12 months); in-segment; no disqualifier |
| RISK | In-segment but at the size boundary, or the planned third site is unconfirmed |
| FAIL | Outside the segment or the size band |

### Q2 — Problem  *(the gate that does the most work)*
| Result | Condition |
|---|---|
| PASS | The buyer described a commercial problem **in their own words, unprompted, in Phase 2 or nominated in Phase 4** — and `resonance_contaminated = N` |
| RISK | They described the problem only **after** I raised it, but described it concretely and with specifics of their own |
| FAIL | No problem described, or agreement only (`"yes, that's a problem for us"` with nothing behind it), or `resonance_contaminated = Y` with nothing volunteered |

> **"They agreed it was a problem" is a FAIL.** Agreement is the cheapest response available to a
> polite person in a conversation they did not initiate.

### Q3 — Authority
| Result | Condition |
|---|---|
| PASS | The signer is **named by role** and has been in at least one conversation; any additional approvers and the spend threshold are known |
| RISK | Signer named and reachable but not yet spoken to; or a partnership threshold exists and the approval cadence is known but slow |
| FAIL | Signer unknown, unreachable, or "the managing partner is keen" with no detail (`AUD-05-02`) |

### Q4 — Measurement access
| Result | Condition |
|---|---|
| PASS | Confirmed willingness to grant read access within 5 business days |
| RISK | Willing in principle; access owned by a third party (software vendor, incumbent agency) and not yet confirmed |
| FAIL | Unwilling, or unwilling to instrument where no baseline exists → `D-a` |

### Q5 — Baseline availability *(informational; does not gate)*
| Result | Condition |
|---|---|
| PASS | ≥ 4 weeks reconstructable history exists |
| RISK | No history, but willing to instrument → **O-0 pre-phase required**, timeline extends to 5–6 weeks and must be said at the point of sale |
| FAIL | No history and unwilling to instrument → `D-a`, `DISQUALIFIED` |

Q5 feeds **H-06** and changes what you sell, not whether you sell.

### Q6 — Timing realism *(informational)*
| Result | Condition |
|---|---|
| PASS | They named a timeframe, or a trigger event is live |
| RISK | Interested, no timeframe |
| FAIL | Explicitly deferred beyond 6 months → `nurture`, loss code `L-06` |

## 4. Outcome

| Outcome | Exact condition |
|---|---|
| **QUALIFIED** | Q1, Q2, Q3, Q4 all `PASS`. No disqualifier |
| **QUALIFIED WITH RISK** | Q1 and Q2 `PASS`; **at most two** of Q3/Q4 at `RISK`; none `FAIL`; every risk has a named next action and date |
| **NOT YET QUALIFIED** | Any gate at `FAIL` that could plausibly change (typically Q3 signer not yet reached, or Q4 access unconfirmed). Requires a specific next action |
| **DISQUALIFIED** | Any hard disqualifier, or Q1/Q2 `FAIL` with no realistic path |

**Rules that make this stick:**

1. **Only `QUALIFIED` and `QUALIFIED WITH RISK` may receive a diagnostic quote.** Quoting a
   `NOT YET` is what turns 20 unbilled sales hours into 80 (`PRICING_AND_ECONOMICS_MODEL.md` §8.3).
2. **Q2 `FAIL` can never be upgraded by enthusiasm, seniority, or company size.**
3. A `RISK` without a named next action and date is a `FAIL`.
4. Re-running the scorecard requires **new evidence from a new interaction**, recorded. Re-reading
   the same notes more optimistically is not new evidence.
5. The scorecard is completed from the written record, at least one hour after the call.

## 5. Record block

```markdown
## Qualification — A-0NN / I-0NN
date: ____   run_by: ____   basis: interview record I-0NN (not memory)

Hard disqualifiers: none | D-_ (which)

| Gate | Result | Evidence (quote or fact from the record) |
|---|---|---|
| Q1 Fit        | PASS/RISK/FAIL | |
| Q2 Problem    | PASS/RISK/FAIL | verbatim: "…"  · volunteered? Y/N · contaminated? Y/N |
| Q3 Authority  | PASS/RISK/FAIL | signer role: ___ · spoken? Y/N · threshold: ___ |
| Q4 Access     | PASS/RISK/FAIL | |
| Q5 Baseline   | PASS/RISK/FAIL | ≥4 weeks? Y/N · system: ___ |
| Q6 Timing     | PASS/RISK/FAIL | |

OUTCOME: QUALIFIED | QUALIFIED_WITH_RISK | NOT_YET | DISQUALIFIED
Risks + next action + date:
Quote permitted? YES / NO     (YES only if QUALIFIED or QUALIFIED_WITH_RISK)
Ledger updated: ☐
```

## 6. The self-deception check

Before recording the outcome, answer these. They exist because the founder is the most motivated
person in the process and therefore the least reliable grader.

1. Am I upgrading a gate because of how the conversation *felt*?
2. Would a second operator reading only the record reach the same outcome?
3. For Q2 — can I point to the **exact verbatim line**? If not, it is not a PASS.
4. For Q3 — do I know the signer's **role**, or only that "someone signs things off"?
5. Am I recording `QUALIFIED WITH RISK` because it is true, or because `NOT YET` feels like failure?
6. If this account never buys, will this record explain why?

> **`NOT YET QUALIFIED` is a normal, healthy outcome.** At the access stage most conversations
> should land there. A pipeline where most interviews produce `QUALIFIED` means the gates are being
> applied loosely — and the D5 gate will then fail with no explanation of why.
