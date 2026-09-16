---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - ../../02-strategy/thesis/DECISION_TREE.md
  - ../FIELD_VALIDATION_PLAN.md
  - 18_GATE_OVERRIDE_REGISTER.md
---
# 15 — Decision Gate Checklists

> **Instrument type:** operator checklists for D0, D3, D4, D5, D6 (+ Gate 1 timing).
> **Thresholds are reproduced verbatim from `DECISION_TREE.md` and `FIELD_VALIDATION_PLAN.md`.
> This file changes none of them.**
>
> A gate is run **on its due date**, from the logs, out loud, with the result written down before
> any discussion of what to do about it.

## 0. Rules for running any gate

| # | Rule |
|---|---|
| G-1 | Run the gate **on the due date**, not when it feels ready. Late gates are always passed |
| G-2 | Count from the logs. Not from memory, not from impression |
| G-3 | **Write the raw count before discussing what it means.** Reversing this order is how a fail becomes a partial |
| G-4 | Contaminated, calibration and warm-only data are reported separately, never merged to reach a threshold |
| G-5 | A gate result is recorded even when it is a fail. Especially then |
| G-6 | An override requires a completed entry in `18_GATE_OVERRIDE_REGISTER.md`. A gate cannot be overridden by deciding it was "basically passed" |
| G-7 | Two overrides on the same gate, or three across the program, escalate to the human owner |

---

## D0 — Founder context
**Due:** day 3. **Owner:** founder.

**INPUTS REQUIRED**
- [ ] `01_FOUNDER_INPUTS_U01_U05.md` answered
- [ ] §7 recalibration worksheet completed (R-1…R-12)
- [ ] Assumptions updated in `EVIDENCE_AND_ASSUMPTIONS_REGISTER.md`

**MINIMUM EVIDENCE:** all five answered; the recalibration done, not just read.

| Result | Condition |
|---|---|
| **PASS** | All five answered; worksheet complete; a D0 exit selected |
| **PARTIAL** | Answered but not recalibrated → **finish the worksheet before proceeding.** An answered form with an unrevised model has produced nothing |
| **FAIL** | Unanswered → **the program cannot start.** Everything downstream depends on numbers derived from these |

**NEXT ACTION:** route via `01_FOUNDER_INPUTS_U01_U05.md` §8.
**ASSUMPTIONS CHANGED:** `A-01`, `A-02`, `A-03`, `A-06`, `A-18`; break-even; validation window.
**ADR REQUIRED?** No. **HUMAN DECISION REQUIRED?** Yes — only the founder can answer.
**OVERRIDE ALLOWED?** **No.** This gate cannot be overridden; there is nothing to override, only
questions to answer.

---

## D3 — ACCESS GATE
**Due:** day 30. **Hypothesis:** H-03. **Threshold: ≥ 8 qualified conversations in the primary segment.**

**INPUTS REQUIRED**
- [ ] `02_TARGET_ACCOUNT_LEDGER.md` current
- [ ] Every conversation tested against the strict four-part definition (§4 of the ledger)
- [ ] Warm / cold split computed
- [ ] X-01 arm results available

**MINIMUM EVIDENCE:** a count of conversations meeting *all four* criteria — ≥20 min, DM or direct
influencer, in-segment business, about their operations.

**COUNT FIRST, THEN READ:**
```
Primary qualified: ___   (warm ___ / cold ___)
Hedge qualified:   ___
Contacts:  ___    Reply rate: ___%
```

| Result | Condition | Next action |
|---|---|---|
| **PASS** | ≥ 8 in primary | → D4. Reduce hedge to 10% effort |
| **PARTIAL** | 4–7 in primary | Diagnose channel vs segment. If one channel produced nearly all, double down and re-test in 15 days. If spread thin, treat as **fail** |
| **SWAP** | < 4 primary **and** ≥ 8 hedge | Hedge becomes primary → D4. This is the two-segment design working, not a failure |
| **FAIL** | < 4 in both | → D3b rotation (max 2). **Before rotating, answer: was it the segment, the channel, or the message?** |

**The warm/cold caveat — mandatory at this gate:**
> If ≥ 6 of 8 qualified conversations came from warm contacts, **H-03 has not been tested.** You
> have measured your network, not the segment's reachability. Record `PASS (warm-dependent)` and
> treat cold access as still open. Do not report a clean pass.

**ASSUMPTIONS CHANGED:** `U-04` (network yield), channel mix, outreach hours per conversation.
**ADR REQUIRED?** No — unless rotating segment away from the `ADR-0007` portfolio, which needs a
note against that ADR.
**HUMAN DECISION REQUIRED?** On rotation, yes.
**OVERRIDE ALLOWED?** Yes, with a register entry — but note that overriding D3 means continuing to
spend on a channel that has not produced access.

---

## D4 — PROBLEM-RESONANCE GATE
**Due:** day 45. **Hypothesis:** H-10. **Threshold: ≥ 5 of 10 volunteered unprompted.**

**INPUTS REQUIRED**
- [ ] `10_PROBLEM_RESONANCE_LOG.md` complete for every interview
- [ ] Every classification made **from transcript or recording**, ≥1 h after the interview
- [ ] Contaminated interviews excluded from the denominator
- [ ] Calibration interviews excluded
- [ ] Verbatim quote present for every VOLUNTEERED
- [ ] **`PC-8` unanticipated problems tallied by theme** — a cluster of ≥3 of the same one is a
      D4b reframe candidate even when the headline ratio passes

**MINIMUM EVIDENCE:** denominator ≥ 10 clean interviews. **Below 10, the gate is not decidable** —
do not call it in either direction.

**COUNT FIRST:**
```
Clean denominator: ___   Volunteered: ___   Ratio: ___
Excluded: contaminated ___ · calibration ___
Classified from memory (low quality): ___
Most frequent category: PC-__
Unanticipated problems (PC-8): ___
```

| Result | Condition | Next action |
|---|---|---|
| **PASS** | ≥ 5/10 | → D5. Harvest the verbatim corpus; replace all provisional copy (`POSITIONING_ARCHITECTURE.md` §3) |
| **PARTIAL** | 2–4/10 | → D4b reframe, **once**, around the problem they *did* volunteer. Re-enter D4 with a 15-day window |
| **FAIL** | ≤ 1/10 | The thesis' core problem claim is false in this segment → D3b (different segment) or D7 if rotations exhausted |
| **NOT DECIDABLE** | denominator < 10 | Keep interviewing. Do not call it |

**The pattern that looks like a pass and is not:**
> High `AGREED AFTER FRAMING`, low `VOLUNTEERED` = you are selling a problem rather than finding
> one. If that is the shape of the log, the correct response is to lengthen Phase 2, not to argue
> the classifications.

**ASSUMPTIONS CHANGED:** the thesis' core problem claim; the messaging corpus; possibly the wedge.
**ADR REQUIRED?** On a D4b reframe, yes — amend `AGENCY_THESIS.md` §1 and note it against `ADR-0006`.
**HUMAN DECISION REQUIRED?** Yes on reframe or rotation.
**OVERRIDE ALLOWED?** **No.** This gate may not be overridden. It is the only test of whether the
problem exists outside the plan; an override here makes every downstream result meaningless.

---

## D5 — MONETISATION GATE *(decisive)*
**Due:** day 60. **Hypotheses:** H-01, H-04. **Threshold: ≥ 2 paid diagnostics from ≤ 20 qualified conversations.**

**INPUTS REQUIRED**
- [ ] `12_DIAGNOSTIC_SALES_ATTEMPT_LOG.md` complete
- [ ] `11_PRICE_SIGNAL_LOG.md` complete
- [ ] Payment cleared, verified against the bank — not against a signature
- [ ] Discounted sales identified and excluded
- [ ] Objection distribution computed

**MINIMUM EVIDENCE:** **cleared funds.** Verbal intent, signed proposals and "invoice me" all count
as zero.

**COUNT FIRST:**
```
Qualified conversations: ___
Attempts (qualified + priced): ___
PAID, undiscounted, cleared: ___   (warm ___ / cold ___)
Verbal-yes-unpaid: ___   ← reported separately, never added
Objections: price ___ trust ___ problem ___ authority ___ timing ___
```

| Result | Condition | Path |
|---|---|---|
| **PASS** | ≥ 2 paid | **A** — thesis holds as designed → D6 |
| **PARTIAL** | 1 paid | Extend 15 days. Still 1 → treat as fail and run the diagnosis |
| **FALLBACK** | 0 paid, but ≥1 core sold after a free teardown | **B** — `A-07` false. Free wedge, with stated costs. Model mutates to M3+M6 → D6 |
| **FAIL** | 0 paid, 0 cores, from ≥ 20 qualified | **C** → diagnosis below, then D7 |
| **NOT DECIDABLE** | < 20 qualified conversations | Do not call it early in either direction |

**Path C diagnosis — required before any action** (dominant objection decides the remedy):
price → re-test lower before killing · trust → get one pilot at ≥60% with a case-study agreement ·
problem → thesis wrong, D7 · authority → qualification failure, tighten Q3 and re-run 15 days.

**The warm caveat:**
> If both paid diagnostics came from warm contacts, **H-01 is supported for warm buyers only.**
> Record it that way. The cold arm remains untested and the acquisition model is unproven.

**ALSO EVALUATE (H-06) — do this at D5, not D6.** By day 60 roughly 12 buyers have been asked what
data they hold, which is the sample `FIELD_VALIDATION_PLAN.md` §3 specifies:

```
Buyers with ≥ 4 weeks reconstructable data: ___ / ___ asked  = ___%
```

| Result | Consequence |
|---|---|
| ≥ 50% | H-06 supported. L1 sells as specified, 2–3 weeks to findings |
| 25–49% | Mixed. **O-0 instrumentation must be quoted as an option on every proposal** |
| < 25% | **H-06 fails.** O-0 becomes mandatory; time-to-findings extends to 5–6 weeks, and that must be priced and disclosed at the point of sale (`OFFER_ARCHITECTURE.md` §3.2) |

Evaluating this at D5 rather than waiting for D6 matters: it changes **what you sell and what you
quote**, and waiting until after the first delivery means selling the wrong shape of engagement to
everyone in between.

**ALSO OBSERVE (H-05):** median days from first contact to cleared payment. Compare against
`A-10` (30–60 days). A materially longer cycle extends the cash timeline and tightens the runway
question from `U-03` — record it even when the gate passes.

**ASSUMPTIONS CHANGED:** `A-07`, `A-08`, `A-09`, `A-10`, `U-07`; fires **T-11** (re-derive pricing §4).
**ADR REQUIRED?** **Yes on path B or C** — a superseding ADR naming the selected pivot, **written
within 7 days** (`FIELD_VALIDATION_PLAN.md` §6).
**HUMAN DECISION REQUIRED?** Yes.
**OVERRIDE ALLOWED?** Yes, with a register entry — but an override here is the specific behaviour
the plan was built to prevent: *"let's give it another month,"* three times, is how a 90-day
validation becomes an 18-month drift. The register entry must name the evidence being ignored.

---

## D6 — DELIVERY GATE
**Due:** day 90. **Hypotheses:** H-06, H-12.

**INPUTS REQUIRED**
- [ ] First diagnostic delivered
- [ ] Baseline record captured **on day 1** of the engagement
- [ ] Hours logged **as worked**, by phase, rework separate
- [ ] X-04 concierge result recorded
- [ ] Baseline record exists as a **dated, immutable artifact** stored with the engagement
      (`PROOF_STRATEGY.md` §10). "We know roughly what it was" does not satisfy this check —
      the artifact either exists with a date or it does not

| Check | Threshold | If failed |
|---|---|---|
| Baseline captured at kickoff | yes/no | `P-1` falsified → O-0 pre-phase mandatory; re-price and re-time |
| Actual vs budgeted delivery hours | ≤ 130% | Trigger **T-1**: re-scope or raise price 15–20% before the next sale |
| Rework vs `A-13` (20%) | ≤ 30% | Trigger **T-2**: change control failed; fix before selling another |
| Client would give a reference | yes/no | Diagnose before scaling. An unreferenceable delivery is a broken product |

| Result | Next action |
|---|---|
| **PASS** (all four) | → D8 |
| **PARTIAL** | Fix the specific mechanism, deliver one more, re-gate |
| **FAIL** | **Do not sell a third engagement with a known-broken delivery model** |

**ASSUMPTIONS CHANGED:** `A-13`, `A-14`, hour table §2.1, `U-08`.
**ADR REQUIRED?** No, unless the offer structure changes materially.
**OVERRIDE ALLOWED?** Yes for the hours check; **no** for the baseline check — without a baseline
there is no proof engine, and the proof engine is why this model was chosen over the alternatives.

---

## Gate 1 — Brand/Business Fit *(timing only)*
**Earliest:** after D5. **Inputs:** Brand V0 + H-08 (X-05) evidence.
**Owned by:** `BRAND_BUSINESS_FIT_REVIEW.md` and `BRAND_BUSINESS_INTERFACE.md` §7. Not run from
this kit; listed so it is not forgotten, and so that **Brand V1 is not mistaken for a validation
prerequisite** — it is not.

---

## Gate result block

```markdown
## Gate [D_] result — [date]
Due date: ____   Run on: ____   (late? Y/N — if Y, why)

RAW COUNTS (written before discussion):

RESULT: PASS | PARTIAL | FAIL | SWAP | NOT DECIDABLE
Caveats (warm-dependent / contaminated excluded / small denominator):
Next action:
Assumptions changed:
ADR required? Y/N — which:
Human decision required? Y/N
Override used? Y/N → register entry ID:
Logged in HYPOTHESIS_REGISTER? ☐   LEARNING_LOG? ☐
```

## Summary

| Gate | Day | Threshold | Override? |
|---|---|---|---|
| D0 | 3 | U-01…U-05 answered + recalibrated | **No** |
| D3 | 30 | ≥ 8 qualified in primary | Yes, with register |
| D4 | 45 | ≥ 5/10 volunteered, clean denominator ≥ 10 | **No** |
| D5 | 60 | ≥ 2 paid, cleared, undiscounted | Yes, with register |
| D6 | 90 | Baseline + ≤130% hours + reference | Partial — baseline check is **not** overridable |
