---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - ../FIELD_VALIDATION_PLAN.md
  - ../../02-strategy/thesis/EVIDENCE_AND_ASSUMPTIONS_REGISTER.md
  - ../../02-strategy/thesis/DECISION_TREE.md
---
# 01 — Founder Inputs: U-01 to U-05

> **Instrument type:** one-time input form. **Time to complete: 10–15 minutes.**
> **Gate:** `DECISION_TREE.md` D0. Nothing else in the kit runs until this is filled in.
>
> **This file does not contain answers and must not be answered by anyone but the founder.**
> These are the five questions that move more of the plan than any further analysis could.

## How to use this

1. Copy this file to `docs/06-validation/findings/FOUNDER_INPUTS_ANSWERED.md`.
2. Fill in the **ANSWER** line under each question. One sitting. Do not research; state what you know.
3. Work through §7 (recalibration worksheet) — about 10 minutes, and it is the part that matters.
4. Run §8 (exit routing) to find out which D0 exit you are on.
5. Commit the answered copy. Then open `16_VALIDATION_LAUNCH_CHECKLIST.md`.

**Do not skip §7.** The answers are only useful once the numbers downstream of them have been
changed. An answered form with an unrevised model has produced nothing.

---

## U-01 — Geography, jurisdiction, operating language, entity status

> Where are you physically and legally? Which country/metro? What language will you sell in?
> Do you have a registered business entity today, or are you operating personally?

**ANSWER:**

| | |
|---|---|
| Changes assumptions | `A-01` (market = MX metro, low confidence) · `A-02` (modelling currency USD) · `A-18` (overhead) |
| Modules depending on it | `PRICING_AND_ECONOMICS_MODEL.md` (all figures) · `GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §1, §4, §6 · `ICP_FRAMEWORK.md` §6.1 (geography field) · `ACQUISITION_MARKETING_SYSTEM.md` (channel legality) |
| Recalculations required | Convert every `INFERRED RANGE` to local currency and re-anchor against local norms; recompute `A-18`; re-scope the legal checklist to the actual jurisdiction |
| Gates affected | D0 · D2 (segment density) · D5 (price reaction is jurisdiction-relative) |
| Can trigger | **Repricing** (different anchor) · **Narrowing** (legal constraints on healthcare outreach, `M-03`) · **Pivot** (if local anchors cannot support the economics — `RED_TEAM_REVIEW.md` RT-07) |
| Blocks | First invoice (needs compliant invoicing) · first SOW (needs jurisdiction-correct contracts) |

---

## U-02 — Weekly hours available

> Realistically, how many productive hours per week does this business get — not hours at a desk,
> hours of focused work? If it varies, give the low week and the good week.

**ANSWER:** low week ______ h · typical ______ h · good week ______ h

| | |
|---|---|
| Changes assumptions | `A-03` (30 h/week) — the input to every capacity figure in the plan |
| Modules depending on it | `PRICING_AND_ECONOMICS_MODEL.md` §2, §2.2, §9, §10 · `OPERATING_MODEL.md` §2, §5, §6 · `FIELD_VALIDATION_PLAN.md` §9 |
| Recalculations required | Annual delivery ceiling (currently 780 h at 50% allocation) · WIP limits · every revenue scenario · the validation-phase load (16–21 h/week = 55–70% of `A-03`) |
| Gates affected | D0 · D3 (outreach volume is hours-bound) · D6 (delivery capacity) |
| Can trigger | **Narrowing** (single-offer, single-segment micro-version) · **Stop/defer** if below 15 h/week |
| Hard rule | **< 15 h/week → the plan as written does not fit.** Say so explicitly and re-scope rather than silently under-delivering (`NO_SILENT_DOWNGRADE.md`) |

---

## U-03 — Runway and minimum monthly draw

> How many months can you cover your personal costs without income from this?
> What is the minimum you must take out of the business each month once it starts?

**ANSWER:** runway ______ months · minimum monthly draw ______

| | |
|---|---|
| Changes assumptions | Break-even logic (`PRICING_AND_ECONOMICS_MODEL.md` §10) · validation-window length |
| Modules depending on it | Pricing §5.1 (cash timeline), §9 (scenarios), §10 (break-even) · `DECISION_TREE.md` D0, D7 |
| Recalculations required | Break-even at *your* draw, **multiplied by 1.35–1.45 for the tax reserve** (`AUD-04-03`, F-02). A USD 4,000 draw needs ~USD 6,600–7,100 monthly contribution, not USD 4,935 |
| Gates affected | D0 · D5 (how long you can wait for the first sale) · D7 |
| Can trigger | **Stop** · **Pivot P-D** (employment/contract work to fund a slower build — a legitimate outcome, not a defeat) · **Compressed validation** (45 days instead of 90) |
| Hard rules | **< 3 months → ramp not survivable.** Take the bounded runway exception in parallel, capped at 20% of hours, compress validation to 45 days, and **do not abandon validation to do billable work** — that is how the business becomes a subcontract shop permanently.<br>**< 6 months → the plan is tight.** The model reaches meaningful positive cash in month 3–4 *at the earliest*, and only if D5 passes on schedule |

> **Read this one honestly.** If your minimum draw is around USD 6,000/month, the plan's base case
> *is* the break-even case — no buffer, no room for a failed engagement, no slow quarter
> (`PRICING_AND_ECONOMICS_MODEL.md` §10). That is a finding, not a reason to inflate the forecast.

---

## U-04 — Warm network

> Who can you contact **this month** without cold outreach? Name them. Count them.
> For each: what business, what segment, and would they take a 20-minute call as a favour?

**ANSWER:** total reachable ______ · largest single-segment cluster: ______ (segment: ______, count: ______)

| Name / business | Segment | Relationship | Would take a call? |
|---|---|---|---|
| | | | |
| | | | |

| | |
|---|---|
| Changes assumptions | `U-04` itself · channel mix in `ACQUISITION_MARKETING_SYSTEM.md` (CH-1 vs CH-2 weighting) |
| Modules depending on it | `ICP_FRAMEWORK.md` §5 (ranking) and §7 · `ACQUISITION_MARKETING_SYSTEM.md` CH-2 · `DECISION_TREE.md` D0, D2 |
| Recalculations required | Outreach volume needed to hit 8 qualified conversations. Warm conversations cost ~0.5–1 founder hour each; cold cost 2–4 |
| Gates affected | **D2 (segment selection) · D3 (access)** |
| Can trigger | **ICP override** — see the hard rule below |
| Hard rule | **≥ 15 reachable businesses in one segment → that segment becomes primary at D2, overriding the desk ranking in `ICP_FRAMEWORK.md` §5.** Fifteen warm doors beat a better-scoring segment behind a cold one (`E-23`) |

> **Count honestly.** "I could probably get introduced to some clinics" is zero. A name you could
> message today is one.

---

## U-05 — Verifiable prior delivery work

> What have you actually built or delivered for a paying client that you could show or reference?
> For each: what, when, for whom, can it be named publicly, and would they take a reference call?

**ANSWER:** referenceable engagements ______ · nameable publicly ______ · reference calls available ______

| Work | When | Client nameable? | Reference call? | Measured outcome available? |
|---|---|---|---|---|
| | | | | |

| | |
|---|---|
| Changes assumptions | `A-06` (no significant client roster or referenceable case studies) |
| Modules depending on it | `PROOF_STRATEGY.md` §2 (which ladder rung you start on) · `PRICING_AND_ECONOMICS_MODEL.md` §3 (yield phase and therefore price) · `POSITIONING_ARCHITECTURE.md` §8.1 (claim tier) |
| Recalculations required | Starting proof rung (P0/P1/P2 if nothing, higher if references exist) · price phase (ramp USD 50–70/h vs established USD 80–110/h) |
| Gates affected | D5 (trust objections) · Gate 1 indirectly |
| Can trigger | **Repricing upward** if genuine references exist · **proof-ladder shortcut** (skip straight to P5/P6) |
| Claim discipline | Prior work in *another* sector is still `A-06` for **this** sector. It raises general credibility, not sector credibility, and must be described that way (`EC-3`) |

---

## 6. What this form must NOT do

| Prohibited | Why |
|---|---|
| Being answered by anyone other than the founder | These are facts about one person's situation |
| Being estimated optimistically | An inflated hours or runway figure propagates into every downstream number and produces a plan that fails quietly |
| Being filled in and then ignored | §7 is the point of the exercise |
| Being used to justify a decision the evidence does not support | These answers constrain the plan; they do not validate it |

---

## 7. Recalibration worksheet *(do this immediately, ~10 min)*

| # | Recalculate | Source | New value |
|---|---|---|---|
| R-1 | Weekly hours → monthly hours (`U-02` × 4.33) | `A-03` | |
| R-2 | Annual delivery ceiling (monthly × 12 × 50%) | Pricing §2.2 | |
| R-3 | Cores deliverable per year (ceiling ÷ ~152 h) | Pricing §2.1 | |
| R-4 | Validation load as % of capacity (16–21 h ÷ `U-02`) | Validation §9 | |
| R-5 | Monthly break-even = fixed costs + draw | Pricing §10 | |
| R-6 | **Break-even including tax reserve = R-5 × 1.35–1.45** | `AUD-04-03` | |
| R-7 | Months of runway vs months to first cash (3–4 minimum) | Pricing §5.1 | |
| R-8 | Warm-sourced conversations available vs 8 needed at D3 | `ICP_FRAMEWORK.md` §7 | |
| R-9 | Cold outreach volume required = (8 − R-8) ÷ 0.05 contacts | Scorecard M-02, M-05 | |
| R-10 | Does R-9 fit inside 8–10 outreach hours/week? | Acquisition CH-1 | |
| R-11 | Starting proof rung and therefore claim tier | `PROOF_STRATEGY.md` §2 | |
| R-12 | Price phase (ramp / establishing) and therefore the L1 quote you will actually use | Pricing §3, §4 | |

**If R-10 is "no":** the outreach plan does not fit the hours. Fix it before starting, by narrowing
the target list, raising the warm ratio, or accepting a longer access window — **and record which
you chose.** Do not start an outreach plan you cannot sustain for four weeks.

---

## 8. D0 exit routing

Work down this list and stop at the first row that matches.

| Condition | Exit | Action |
|---|---|---|
| `U-02` < 15 h/week | **Re-scope or defer** | Single-offer, single-segment micro-version. State the downgrade explicitly |
| `U-03` runway < 3 months | **Compressed + funded** | 45-day validation window; bounded runway exception ≤20% of hours; validation continues |
| `U-03` runway 3–6 months | **Proceed, tight** | Full plan, no slack. Review at D3 rather than D5 |
| `U-04` ≥ 15 in one segment | **ICP override** | That segment is primary at D2 regardless of the desk ranking |
| `U-01` shows a legal blocker to healthcare outreach | **Narrow or swap** | Route to `GOVERNANCE_RISK_SECURITY_CHECKLIST.md` `M-03` ⚖️ before contacting clinics |
| `U-05` shows ≥ 2 nameable references with outcomes | **Proof shortcut + reprice** | Start higher on the proof ladder; consider the establishing price phase |
| None of the above | **Proceed as planned** | → D1, then `16_VALIDATION_LAUNCH_CHECKLIST.md` |

---

## 9. Sign-off

| Field | Value |
|---|---|
| Completed on | |
| Completed by | |
| Recalibration worksheet done? | ☐ Yes |
| D0 exit selected | |
| Assumptions updated in `EVIDENCE_AND_ASSUMPTIONS_REGISTER.md`? | ☐ Yes — list IDs: |
| Next file to open | `16_VALIDATION_LAUNCH_CHECKLIST.md` |
