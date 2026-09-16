---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - OFFER_ARCHITECTURE.md
  - EVIDENCE_AND_ASSUMPTIONS_REGISTER.md
---
# Pricing and Unit-Economics Model

> **Module 8 of the Agency Master Plan** (Issue #2 Phase 6).
>
> ## Mandatory reading before any number below
>
> This program holds **zero `PUBLIC PRICE` records and zero `PRICE SIGNAL` records** (`E-22`).
> No competitor price, no buyer quote, no market benchmark has been observed. Every currency
> figure in this document is an **`INFERRED RANGE`** constructed bottom-up from capacity and cost
> logic under the assumptions in `EVIDENCE_AND_ASSUMPTIONS_REGISTER.md` §4.
>
> These are **modelling instruments, not prices**. Their purpose is to expose which variables the
> business is sensitive to, so that the first real market contact produces maximum information.
> A reader who extracts a number from this document and quotes it to a buyer has misused it.

Modelling currency: USD (`A-02`). Client-facing quoting may be in MXN; conversion and local anchor
calibration are blocked on `U-01`.

## 1. Pricing philosophy

Three rules, in priority order:

1. **Price against the quantified loss, never against a rate card.** The L1 diagnostic exists to
   produce the number that anchors the L2 price. "This gap costs you ~X per month; closing it costs
   Y once" is a fundamentally different negotiation from "our rate is Z per hour." This is the
   single largest pricing lever in the model and the main commercial reason the diagnostic exists.
2. **Fixed price, fixed scope, written exclusions.** Hourly billing transfers estimation risk to
   the client and caps upside at the clock. Fixed price transfers the risk to the agency and
   rewards the AI-leverage advantage (`E-21`) — which is exactly where this business is
   differentiated. The cost of that choice is `A-13` rework exposure, managed in §9.
3. **Never discount price; reduce scope.** A discount permanently re-anchors the relationship and,
   through referrals, the market. See §7 and `DNS-13`.

## 2. Capacity model — the real constraint

The binding constraint is **founder hours**, not cash and not demand (`A-03`, `A-04`, `E-25`).

**Base: `A-03` = 30 productive hours/week ≈ 130 hours/month ≈ 1,560 hours/year.**

| Allocation | Steady state | During an active core build | Ramp (months 1–3) |
|---|---|---|---|
| Delivery | 50% (65 h/mo) | 70% (91 h/mo) | 25% (33 h/mo) |
| Sales / marketing / validation | 30% (39 h/mo) | 12% (16 h/mo) | 55% (72 h/mo) |
| Admin / internal / tooling | 20% (26 h/mo) | 18% (23 h/mo) | 20% (26 h/mo) |

**The oscillation problem, made explicit.** During an active core build, sales capacity drops from
39 to 16 hours/month — a 59% reduction. Pipeline generated at 39 h/mo dries up at 16 h/mo, arriving
empty exactly when the build ends. This is the classic solo-operator feast/famine cycle, and it is
visible directly in the table above.

**The structural answer is the offer ladder, not discipline.** L0 teardowns (3 h) and L1 diagnostics
(36 h) are small and schedulable; they can be produced during a build, whereas a core build cannot.
The ladder therefore keeps the pipeline alive through delivery periods. This is the strongest
economic argument for the diagnostic-led model and is independent of whether the diagnostic sells
profitably.

### 2.1 Delivery-hour estimates (`INFERRED RANGE`)

Including `A-13` rework at 20%.

| Offer | Base hours | + rework | + unbilled sales (`A-14`) | Total founder hours |
|---|---:|---:|---:|---:|
| L0 Teardown | 3 (capped) | — | — | 3 |
| L1 Diagnostic | 30 | 36 | 8 | 44 |
| O-0 Instrumentation sprint | 12 | 14 | 2 | 16 |
| L2 C-1 Conversion Path Rebuild | 110 | 132 | 20 | 152 |
| L2 C-2 Revenue Operations Build | 130 | 156 | 20 | 176 |
| L2 C-3 Full Commercial System | 220 | 264 | 28 | 292 |
| L3 Monitored | 3/mo | 3.5/mo | — | 3.5/mo |
| L3 Operated | 8/mo | 9/mo | — | 9/mo |
| L3 Partnered | 14/mo | 16/mo | — | 16/mo |
| L4 X-1 Location rollout | 20 | 24 | 2 | 26 |
| L4 X-3 Reactivation system | 30 | 36 | 3 | 39 |

### 2.2 Annual capacity ceiling, solo

At 1,560 h/year with 50% delivery allocation ≈ **780 delivery hours/year**.

| Mix | Consumption | Fits? |
|---|---|---|
| 6 diagnostics + 4 cores | 216 + ~576 = 792 h | At the ceiling |
| 8 diagnostics + 3 cores | 288 + 432 = 720 h | Fits, with L3 headroom |
| 10 diagnostics + 5 cores | 360 + 720 = 1,080 h | **Requires contractors** |

> **Hard finding:** a solo founder at 30 h/week can deliver roughly **3–5 core engagements per
> year**. Every revenue scenario below is bounded by this, and no amount of demand changes it
> without contractors. This is the number that determines whether the business is viable at the
> founder's required income (`U-03`).

## 3. Price derivation method

For each offer: `price = total founder hours × target effective yield`, where target yield rises
with proof accumulation.

| Phase | Proof state | Target effective yield (`INFERRED RANGE`) |
|---|---|---|
| Ramp (engagements 1–3) | No references | USD 50–70/h |
| Established (4–10) | 2–3 case studies | USD 80–110/h |
| Specialist (11+) | Benchmark data, referral flow | USD 120–180/h |

The yield ladder is an `INFERRED RANGE` with no observed basis. It is calibrated by `U-01`
(geography sets the local anchor) and H-04 (observed WTP).

## 4. Price model — ramp phase

| Offer | Hours | Low | **Base** | High | Implied yield at base |
|---|---:|---:|---:|---:|---:|
| L0 Teardown | 3 | — | **Free** | — | Acquisition cost |
| O-0 Instrumentation | 16 | 600 | **900** | 1,400 | 56/h |
| **L1 Diagnostic** | 44 | 1,800 | **2,400** | 3,500 | 55/h |
| L2 C-1 | 152 | 9,000 | **12,000** | 16,000 | 79/h |
| L2 C-2 | 176 | 11,000 | **15,000** | 20,000 | 85/h |
| L2 C-3 *(locked until D8)* | 292 | 20,000 | **26,000** | 34,000 | 89/h |
| L3 Monitored | 3.5/mo | 400 | **550** | 700 | 157/h |
| L3 Operated | 9/mo | 900 | **1,400** | 1,800 | 156/h |
| L3 Partnered | 16/mo | 2,000 | **2,600** | 3,500 | 163/h |
| L4 X-1 | 26 | 2,000 | **2,900** | 4,500 | 112/h |
| L4 X-3 | 39 | 3,000 | **4,200** | 6,000 | 108/h |

**Structural observations:**

- The diagnostic yields the *least* per hour of any paid offer. This is by design
  (`AGENCY_THESIS.md` §5): it is bought as acquisition, not as revenue. Its return is qualification,
  anchoring and proof.
- The recurring layer yields roughly **twice** the core build per hour. This is the entire
  quantitative argument for `A-11`, and the reason L3 attachment is the highest-leverage
  unvalidated assumption in the plan.
- L4 expansion yields ~40% more per hour than a core build, purely from the absence of acquisition
  cost. This is the quantified case for the S2 multi-site ICP.

## 5. Payment and cash structure

| Offer | Structure | Rationale |
|---|---|---|
| L1 Diagnostic | 100% on signature | Small enough not to be a barrier; eliminates collection risk on the acquisition instrument |
| L2 Core | 50% deposit / 25% at mid-milestone / 25% on acceptance | Deposit funds the work; final tranche small enough that it cannot be used as leverage in an acceptance dispute |
| L2 ≥ USD 20,000 | 40 / 30 / 30 | Smooths the client's cash |
| L3 Operated | Monthly in advance, 6-month initial term | Advance billing is non-negotiable for a solo operator |
| L4 Expansion | 50 / 50 | — |
| L5 Custom | 50% deposit, then bi-weekly against a written cap | — |

**Non-negotiables:** no work begins before the deposit clears; late payment pauses work after 10
days' written notice; no net-60 terms (a solo operator cannot finance a client's working capital).

### 5.1 Cash-flow timeline (base case)

| Month | Event | Cumulative cash |
|---|---|---|
| 0 | Validation begins; no revenue | Negative (tooling ~USD 350/mo) |
| 1 | Teardowns + outreach; no revenue | Negative |
| 2 | First diagnostics sell (D5) | +USD 2,400–4,800 |
| 3 | First core deposit | +USD 6,000–7,500 |
| 4–5 | Core delivery; mid-milestone | +USD 3,000–4,000 |
| 5–6 | Core acceptance + first L3 | +USD 3,000 + recurring |
| 7+ | Second cycle overlapping | — |

> **Runway requirement:** the model reaches meaningful positive cash in **month 3–4 at the earliest**,
> and that assumes the D5 gate passes on schedule. `U-03` must show **at least 6 months of runway**,
> ideally 9. If it shows less, `DECISION_TREE.md` D0 routes to the bounded M7 runway exception or
> to pivot P-D. This is not a detail; it is a go/no-go input.

## 6. Cost model

### 6.1 Fixed monthly (`A-15`, `A-18`)

| Category | Low | Base | High |
|---|---:|---:|---:|
| CRM / pipeline | 30 | 60 | 120 |
| Automation / orchestration | 30 | 70 | 150 |
| Analytics / dashboarding | 0 | 40 | 100 |
| Proposal / e-signature | 20 | 30 | 50 |
| Project management | 0 | 25 | 60 |
| Password / secrets management | 10 | 20 | 40 |
| AI tooling (base subscriptions) | 60 | 100 | 200 |
| Hosting / domains / misc | 20 | 40 | 80 |
| **Tooling subtotal** | **170** | **385** | **800** |
| Accounting / legal / banking / insurance (`A-18`, post-formalisation) | 300 | 550 | 800 |
| **Total fixed** | **470** | **935** | **1,600** |

### 6.2 Variable

| Item | Basis | Range |
|---|---|---|
| AI / compute per active engagement (`A-16`) | Per engagement/month | USD 40–120 |
| Client-specific tools | Passed through where possible | Variable |
| Contractor hours (`A-17`) | When used | USD 25–60/h |
| Payment processing | Per transaction | 2.5–4% |

### 6.3 Contribution margin, base case

| Offer | Price | Direct cost (tools + AI + processing) | Contribution | % |
|---|---:|---:|---:|---:|
| L1 Diagnostic | 2,400 | ~180 | 2,220 | 93% |
| L2 C-1 | 12,000 | ~700 | 11,300 | 94% |
| L2 C-2 | 15,000 | ~850 | 14,150 | 94% |
| L3 Operated (monthly) | 1,400 | ~90 | 1,310 | 94% |

**These percentages are misleading and must not be quoted as margins.** They exclude the founder's
own labour, which is the only real cost in the business. The meaningful metric is **effective yield
per founder hour** (§4), not contribution margin. A services business with 94% contribution margin
and 780 sellable hours has a hard revenue ceiling, and the ceiling is what matters.

## 7. Discount and pilot policy

**Discounting is prohibited.** Permitted responses to price resistance, in order:

1. **Re-anchor** on the quantified loss from the diagnostic.
2. **Reduce scope** — remove a named deliverable, reduce location count, drop a channel. Price falls
   because the work falls.
3. **Restructure payment** — extend the schedule. Total price unchanged.
4. **Phase** — sell the first half now, the second as a separate engagement.
5. **Walk away.**

### 7.1 The pilot exception

At most **two** pilot engagements, before the third delivered core, priced at **no less than 60% of
base**, and only with a **written case-study agreement**: named attribution, publication rights,
before/after metrics, and a reference call commitment. The reduction is *consideration for the
case study*, and the agreement says so.

**This is not a discount**, because something of real value is exchanged, and because its
boundaries are contractual. The distinction matters: a discount teaches the market the price is
soft; a pilot agreement teaches it that proof has value.

## 8. Sensitivity analysis

Base: C-1 at USD 12,000, 110 base delivery hours, 20 hours unbilled sales.

### 8.1 Rework sensitivity (`A-13`) — the largest controllable risk

| Rework % | Delivery h | Total h | Effective yield | Change |
|---:|---:|---:|---:|---:|
| 0% | 110 | 130 | USD 92/h | +16% |
| **20% (base)** | **132** | **152** | **USD 79/h** | — |
| 40% | 154 | 174 | USD 69/h | −13% |
| 60% | 176 | 196 | USD 61/h | −23% |
| 100% | 220 | 240 | USD 50/h | −37% |

### 8.2 Price sensitivity

| Price | Total h (base rework) | Effective yield | Change |
|---:|---:|---:|---:|
| 9,000 (−25%) | 152 | USD 59/h | −25% |
| 10,800 (−10%) | 152 | USD 71/h | −10% |
| **12,000** | **152** | **USD 79/h** | — |
| 14,400 (+20%) | 152 | USD 95/h | +20% |

> **The finding that should change behaviour:** a **20% discount destroys as much yield as tripling
> the rework rate** (79 → 63/h vs 79 → 61/h). Discounting is quantitatively equivalent to
> catastrophic scope failure, and it happens in one sentence during a sales call.
> Print this and put it next to the phone.

### 8.3 Unbilled-sales sensitivity (`A-14`)

| Unbilled sales hours per closed core | Effective yield |
|---:|---:|
| 10 | USD 85/h |
| **20 (base)** | **USD 79/h** |
| 40 | USD 70/h |
| 80 | USD 57/h |

At 80 unbilled hours per close — entirely plausible with long cycles, multiple stakeholders and
speculative proposals — the business earns less per hour than a competent freelancer. **This is the
quantitative justification for the qualification gates in `SALES_SYSTEM.md` §3 and for the refusal
to write speculative proposals.** Sales discipline is not a preference; it is 28% of yield.

### 8.4 Diagnostic-conversion sensitivity (`A-08`)

Per 10 diagnostics sold (440 founder hours, USD 24,000 revenue):

| Conversion to core | Cores | Core revenue | Total | Total hours | Blended yield |
|---:|---:|---:|---:|---:|---:|
| 10% | 1 | 12,000 | 36,000 | 592 | USD 61/h |
| 20% | 2 | 24,000 | 48,000 | 744 | USD 65/h |
| **30% (base)** | **3** | **36,000** | **60,000** | **896** | **USD 67/h** |
| 50% | 5 | 60,000 | 84,000 | 1,200 | USD 70/h |

Note what this shows: blended yield is **remarkably insensitive** to conversion rate, because the
diagnostic is roughly cost-neutral. What conversion rate actually governs is **whether the capacity
ceiling is hit at all** — at 50% conversion, 10 diagnostics consume 1,200 hours against a 780-hour
ceiling. **High conversion is a capacity problem, not a revenue windfall**, and it arrives as a
contractor decision rather than a celebration.

## 9. Scenarios — year 1

Assumes Day 0 = validation start, solo, `A-03` = 30 h/week.

### Worst case — validation partially fails
| Line | Volume | Revenue |
|---|---:|---:|
| Diagnostics | 4 | 9,600 |
| Cores | 1 | 12,000 |
| Operated | 0 | 0 |
| Expansion | 0 | 0 |
| **Revenue** | | **21,600** |
| Costs (tooling only, unformalised) | | (5,000) |
| **Contribution** | | **16,600** |

≈ USD 1,380/month. **Not survivable as a sole income.** Triggers `DECISION_TREE.md` D7.

### Base case — gates pass on schedule
| Line | Volume | Revenue |
|---|---:|---:|
| Diagnostics | 7 | 16,800 |
| Cores (C-1/C-2 mix) | 4 | 54,000 |
| Operated (2 accounts, avg 6 months) | — | 16,800 |
| Expansion | 2 | 5,800 |
| **Revenue** | | **93,400** |
| Fixed costs (935 × 12) | | (11,220) |
| Variable + contractors | | (6,000) |
| **Contribution** | | **76,180** |

≈ USD 6,350/month founder draw. Delivery hours consumed ≈ 790 — **exactly at the solo ceiling**.
The base case is capacity-bound, not demand-bound, which is the defining characteristic of this
business.

### Best case — strong validation + contractor leverage
| Line | Volume | Revenue |
|---|---:|---:|
| Diagnostics | 12 | 30,000 |
| Cores | 6 | 85,000 |
| Operated (5 accounts) | — | 45,000 |
| Expansion | 5 | 15,000 |
| **Revenue** | | **175,000** |
| Fixed costs | | (14,000) |
| Contractors (~500 h @ 45) | | (22,500) |
| Variable | | (8,000) |
| **Contribution** | | **130,500** |

Requires contractors from month 5 and a functioning delegation model
(`OPERATING_MODEL.md` §7). Not reachable solo.

### Scenario comparison
| | Worst | Base | Best |
|---|---:|---:|---:|
| Revenue | 21,600 | 93,400 | 175,000 |
| Contribution | 16,600 | 76,180 | 130,500 |
| Monthly draw | 1,380 | 6,350 | 10,875 |
| Cores delivered | 1 | 4 | 6 |
| Recurring at year end | 0 | 2,800/mo | 7,000/mo |
| Requires contractors | No | Marginal | Yes |

## 10. Break-even

**Fixed monthly:** USD 935 (base) + founder minimum draw (`U-03`, unknown).

> **Tax correction (`AUD-04-03`).** The table below is stated in pre-tax contribution. Because
> F-02 requires reserving 25–30% of contribution against an unconfirmed tax obligation ⚖️, the
> revenue needed to deliver a given **take-home** draw is roughly **1.35–1.45×** the figures shown.
> A USD 4,000 monthly draw therefore implies approximately USD 6,600–7,100 of monthly contribution,
> not USD 4,935. Apply this multiplier before treating any break-even figure as survivable.

| Founder minimum draw | Monthly break-even | Annual | Minimum viable volume |
|---:|---:|---:|---|
| 1,500 | 2,435 | 29,220 | 2 cores + 3 diagnostics |
| 2,500 | 3,435 | 41,220 | 3 cores + 3 diagnostics |
| 4,000 | 4,935 | 59,220 | 4 cores + 4 diagnostics, or 3 cores + 2 operated |
| 6,000 | 6,935 | 83,220 | Base case, fully achieved — no margin for error |

> **The critical reading:** if the founder's minimum draw is USD 6,000/month, the base case *is* the
> break-even case. There is no buffer, no room for a failed engagement, and no capacity for a slow
> quarter. In that situation the correct response is to secure part-time income alongside the build
> (`DECISION_TREE.md` D7 pivot P-D), not to price more aggressively into an unvalidated market.
> `U-03` therefore determines the shape of the entire first year and must be answered in Week 1.

**Recurring revenue is the break-even lever.** Four operated accounts at base (USD 5,600/month)
covers a USD 4,000 draw plus fixed costs *before any project revenue*. This is why `A-11` is the
most consequential unvalidated assumption in the model: it is the difference between a business
that must sell every month and one that does not.

## 11. Repricing and redesign triggers

| ID | Trigger | Action |
|---|---|---|
| T-1 | Delivery hours exceed 130% of budget on 2 consecutive engagements | Re-scope the offer or raise price 15–20% before the next sale |
| T-2 | Rework exceeds 35% on any engagement | Halt selling that offer; fix change control (`DELIVERY_OS.md` §6) first |
| T-3 | Win rate above 70% on core proposals | **Price is too low.** Raise 15–25% on the next proposal. A high win rate is a pricing failure, not a sales success |
| T-4 | Win rate below 20% after 8 qualified proposals | Diagnose price vs positioning vs qualification before cutting price (`DECISION_TREE.md` D5 diagnostic) |
| T-5 | Effective yield below USD 50/h for 2 consecutive months | Structural problem. Stop and re-plan |
| T-6 | L3 attachment below 20% after 5 delivered cores | `A-11` failing. Redesign L3 value delivery; do not discount (D9) |
| T-7 | Unbilled sales hours exceed 40 per close | Qualification failure. Tighten `SALES_SYSTEM.md` §3 gates |
| T-8 | Any single client exceeds 40% of trailing-3-month revenue | Concentration risk. Prioritise new-logo acquisition over expansion for one quarter |
| T-9 | Contractor cost exceeds 30% of revenue without a yield increase | Delegation is not working. Re-examine what is being delegated |
| T-10 | Three consecutive diagnostics fail to convert | Either the diagnostic is not producing compelling findings or qualification is wrong. Audit findings quality first |
| T-11 | First real competitor price observed | **Convert `INFERRED RANGE` → `PRICE SIGNAL` and re-derive §4** |

## 12. Cash-flow risks

| Risk | Exposure | Mitigation |
|---|---|---|
| Deposit-to-delivery gap | Deposit spent before completion | Treat deposits as unearned; never fund next month's costs from this month's deposit |
| Client payment delay | 30–60 days on final tranche | Advance billing on L3; final tranche kept small; work pauses after 10 days |
| Concentration | One client = most of revenue | T-8 |
| Scope overrun | Unbilled hours | Change control; T-1/T-2 |
| Currency (`A-02`) | MXN/USD movement if costs and revenue diverge | Quote and cost in the same currency where possible |
| Tax and formalisation | Unplanned obligations from `U-01` | Reserve 25–30% of contribution until a local professional confirms actual obligations (`GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §8) |
| Founder illness / unavailability | Complete revenue stop | The strongest non-financial argument for the operated layer and a contractor bench |

## 13. What must be measured from engagement 1

Without these, every number above stays an assumption forever. Definitions in `AGENCY_SCORECARD.md`.

| Measure | Why | Calibrates |
|---|---|---|
| Actual delivery hours by phase | The entire model | All of §2.1 |
| Rework hours, separately logged | Largest controllable margin variable | `A-13` |
| Unbilled sales hours per opportunity | 28% yield swing | `A-14` |
| Proposal → close rate and cycle length | Pricing and capacity planning | `A-09`, `A-10` |
| Diagnostic → core conversion | Capacity planning | `A-08` |
| L3 attachment and retention | The structural bet | `A-11`, `A-12` |
| Actual tool and AI spend | Cost base | `A-15`, `A-16` |

**Discipline rule:** hours must be logged *as worked*, not reconstructed at month end. Reconstructed
hours systematically under-report rework, which is precisely the variable that matters most.
