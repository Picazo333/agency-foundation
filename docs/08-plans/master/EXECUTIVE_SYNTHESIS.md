---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - AGENCY_MASTER_PLAN.md
  - RED_TEAM_REVIEW.md
  - INTEGRATION_PASS.md
---
# Executive Synthesis

> The final output required by Issue #2: what is decided, what is provisional, what is blocked, and
> what happens next. Written for the human project owner. Read `RED_TEAM_REVIEW.md` immediately
> after this.

## 1. The finding

Nine business archetypes were compared against the evidence. Four were killed outright, one was
demoted, and the survivors combine into a single recommended shape:

> **A diagnostic-led, vertical, productized studio.** Sell a paid diagnostic that measures where one
> specific kind of business loses revenue it has already paid to generate. Sell bounded, fixed-price
> builds that close the measured gaps. Sell an operated layer that keeps them closed and keeps
> measuring. Use AI to make this economically possible for one person. Never lead with it.

The recommendation rests on one property no other candidate has: **proof is a byproduct of the entry
offer.** The diagnostic captures a baseline in week one, so every engagement becomes a case study by
construction. For a supplier whose binding constraint is the absence of references, that matters more
than any other property a business model can have.

## 2. What is decided

Nothing. This plan proposes; the human owner decides
(`HUMAN_AUTHORITY.md`, `CANON_PROMOTION_RULE.md`). Every file carries `status: review`,
`authority: workbench`.

**What the reasoning establishes with reasonable confidence** — these conclusions do not depend on
any unvalidated number:

| # | Conclusion |
|---|---|
| 1 | A classic multidisciplinary agency is not viable from here: it is portfolio-gated and the portfolio does not exist |
| 2 | A generic AI/automation agency is the wrong category — it names the supplier's tools rather than the buyer's problem, and buyers hold no "AI" budget line |
| 3 | White-label subcontracting is a trap: it pays this month and forecloses every other model |
| 4 | A craft-led creative-technology studio is the best fit for the founder's taste and is unreachable today. It is a destination reachable in 18–36 months, not a starting point |
| 5 | Buyer *access*, not strategy quality, is the binding constraint, and it should be the first thing tested |
| 6 | Measurement-first is the only structure that produces proof fast enough to matter for a supplier with no references |

## 3. What is provisional

| Provisional | Resolved by | When |
|---|---|---|
| The business model (M8) | Six gates | D5 is decisive, day 60 |
| The vertical (multi-site clinic groups recommended) | Access gate + founder network | Day 30 |
| Every price | H-04; first real quotes | Day 60+ |
| The offer ladder | First delivery | Day 90 |
| The category label | H-11 | Day 45 |
| The recurring layer | H-09 | Day 180 |
| The brand/buyer relationship | H-08 + Gate 1 | After day 60 |

## 4. What is blocked

| Blocked | Blocked by | Owner |
|---|---|---|
| Any commercial commitment | Zero buyer contact (`E-09`) | Founder |
| Pricing decisions | No price observation exists (`E-22`) | Field |
| Contract signature | Legal templates ⚖️ | External counsel |
| First invoice | Entity, tax and invoicing setup ⚖️ | External accountant |
| Healthcare ICP viability | Data-protection obligations (`U-10`) ⚖️ | Data-protection counsel |
| Production website | Brand V1 + validated message | Brand + technical |
| Asset factory | Brand V1 | Asset Factory workstream (Issue #3) |
| Brand/Business Fit Review | Brand V0 + H-08 evidence | Brand + founder |
| **Almost everything else** | Five founder questions | **Founder, this week** |

## 5. The five questions that gate the plan

`U-01`–`U-05`. Answerable in one sitting, and they move more of the model than any further analysis
could:

1. **Where are you, legally and physically?** Sets currency, legal checklist, channel mix, ICP
   density.
2. **How many hours per week does this get?** Every capacity and break-even figure is derived from
   it.
3. **How many months of runway, and what is your minimum monthly draw?** Determines whether a
   diagnostic-led ramp is survivable at all. **If the answer is under 6 months, the plan changes
   shape.**
4. **Who can you contact this month without cold outreach — by name, with a count?** May override
   the entire ICP ranking. Fifteen warm doors beat a better-scoring segment behind a cold one.
5. **What have you actually delivered for a paying client, that could be referenced?** Sets the
   starting rung of the proof ladder and the price ceiling.

## 6. The single most important finding

> **This program has never spoken to a customer.**

It has a governance system, an ADR register, four workstream contracts, a canon/workbench firewall
and, now, twenty-one strategy modules. It has zero conversations with a potential buyer.

The quality of the planning is real, and it is the risk. Planning of this standard is satisfying,
produces visible artifacts, and carries no risk of rejection. Outreach produces nothing to look at
and a great deal of rejection. Without a structural constraint, a capable systems thinker will
choose the first indefinitely and call it preparation.

**Recommendation:** approve `ADR-0006`, which activates a binding stop rule — *no further strategic
planning artifact until ten qualified buyer conversations are logged* — and begin outreach within
seven days.

## 7. What the Red Team could not answer

Seven exposures survived the adversarial pass and are carried openly:

1. Planning has substituted for market contact for the life of this program.
2. There is **no evidence the founder can sell**, and the plan depends on it entirely.
3. The core problem may be supplier-invented; the frame is a planner's, not a buyer's.
4. There is **no defensibility for 18–24 months**; the benchmark-data moat arrives after the period
   in which it is most needed.
5. The AI capability advantage is depreciating while the plan is being written.
6. The geography and price assumptions may invalidate the economics entirely.
7. **The founder's skills may be worth more employed, contracted, or applied to a product** than to
   a solo agency. The base case is roughly USD 6,350/month in year one, achieved only if six
   sequential gates pass with no slack. That comparison is a founder's judgement, and the plan's job
   was to state it rather than argue past it.

Full argument: `RED_TEAM_REVIEW.md`.

## 8. Decisions required before this plan can be executed

| # | Decision | Where |
|---|---|---|
| 1 | Approve, amend or reject the working thesis | `ADR-0006` |
| 2 | Confirm the two-segment validation portfolio | `ADR-0007` |
| 3 | Confirm the paid-diagnostic entry offer | `ADR-0008` |
| 4 | Confirm that no price is published before evidence | `ADR-0009` |
| 5 | Confirm AI as mechanism, never category | `ADR-0010` |
| 6 | Answer `U-01`–`U-05` | §5 |
| 7 | Engage an accountant and a lawyer ⚖️ | `GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §12 |
| 8 | Accept or reject the stop rule | `AGENCY_THESIS.md` §11 |

## 9. What happens in the next 90 days

| Days | What |
|---|---|
| 0–3 | Answer the five questions |
| 0–7 | Approve or amend the ADRs; engage accountant and lawyer |
| 3–18 | Method document, five-page site, teardown template, target list of 40–60 |
| 18–30 | Outreach at 15–20/week; 8+ teardowns → **D3: 8 qualified conversations** |
| 31–45 | Resonance testing → **D4: 5 of 10 volunteer the problem** |
| 45–60 | Diagnostic sales → **D5: 2 paid diagnostics** |
| 61–90 | First delivery; baseline captured; hours calibrated → **D6** |

## 10. The plan in one paragraph

> Answer five questions about yourself in three days. Spend two weeks building a method document, a
> five-page website and a teardown template. Spend six weeks talking to sixteen multi-site clinic
> operators, leading every conversation with something you measured about their business rather than
> with anything about yours. Sell two paid diagnostics. Deliver one properly, capture the baseline on
> day one, and find out whether the numbers in this plan bear any resemblance to reality. Everything
> else in this repository is either support for that or a distraction from it.

## 11. Honest statement of what this plan is worth

It cannot tell you whether this business will work. Nobody can, from a desk, with no market contact
and no primary data.

What it does is make the question **cheap and fast to answer**: six gates, ninety days, near-zero
cash, and a defined exit at every failure point — including one that says taking a job is a
legitimate outcome rather than a defeat.

Its most valuable content is not the recommendation. It is the refusal lists, the kill criteria and
the stop rule — the parts that cost something to honour.
