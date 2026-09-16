---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - 15_DECISION_GATE_CHECKLIST.md
---
# 18 — Gate Override Register

> **Instrument type:** permanent, append-only record of every decision to proceed past a gate the
> evidence did not support.
>
> This file exists because a gate with no override procedure gets overridden silently, and a gate
> overridden silently was never a gate.

## 1. Why overriding is made expensive rather than impossible

Some overrides are legitimate: a gate can be missed for a reason that has nothing to do with the
hypothesis (illness, a segment-wide holiday, a data-loss incident). Forbidding overrides entirely
would produce false kills.

But an override should cost something. Here it costs a written admission of exactly what evidence
is being set aside and what risk is being accepted, signed and dated, in a file that is read aloud
at every subsequent gate.

## 2. Gates that may NOT be overridden

| Gate | Why |
|---|---|
| **D0** | Nothing to override — five unanswered questions are not a threshold, they are missing inputs |
| **D4 resonance** | The only test of whether the problem exists outside the plan. Overriding it makes every downstream result meaningless |
| **D6 baseline check** | Without a captured baseline there is no proof engine, and the proof engine is the reason this model was chosen over the alternatives |

Attempting to override these is itself the finding: it means the program has decided to proceed
regardless of evidence, and the honest move is to say so explicitly to the human owner rather than
to record an override.

## 3. Escalation thresholds

| Trigger | Consequence |
|---|---|
| 2 overrides on the same gate | Escalate to the human owner before proceeding |
| 3 overrides across the program | **Stop.** The gate system is not functioning; the program is running on conviction |
| Any override lacking a completed §4 entry | Not an override. It is a silent pass, and the gate result stands as FAIL |

## 4. Entry format

Every field required. An incomplete entry is not a valid override.

```markdown
## Override OV-0NN — [gate] — [date]

**Gate:** D_
**Threshold that was not met:** [verbatim from 15_DECISION_GATE_CHECKLIST.md]
**Actual result:** [raw counts]

**Rationale for proceeding:**
[Why, specifically. "Momentum", "it feels close" and "we've come this far" are not rationales.]

**Evidence being ignored:**
[Name it precisely. Which counts, which logs, which objection pattern is being set aside.]

**Risk accepted:**
[What becomes true if the ignored evidence was right. Be concrete about the cost.]

**What would reverse this override:**
[A specific, observable condition with a date.]

**Re-gate date:** [when this gate will be re-run — mandatory, within 30 days]
**Owner:** [name]
**Date:** [date]
**Escalated to human owner?** Y / N — required if this is the 2nd on this gate or the 3rd overall
```

## 5. Register

*No overrides recorded. Validation has not begun.*

| ID | Gate | Date | Threshold missed | Re-gate date | Escalated |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

## 6. Read-aloud rule

**At the start of every subsequent gate, every open override entry is read aloud.**

The purpose is cumulative honesty: three individually reasonable overrides are collectively a
program that has stopped testing anything, and that is only visible when they are read together.
