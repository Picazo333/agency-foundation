---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - AGENCY_MASTER_PLAN.md
  - MASTER_PLAN_AUDITS.md
---
# Red Team Review — Pass 9

> **Mandate (Issue #2):** try to prove the whole model should not exist.
>
> This pass is adversarial by design. It argues against the plan without balancing caveats, then
> states what survived. Where an attack lands and cannot be answered, it is recorded as landed —
> because an audit that resolves every objection has not audited anything.

## Summary of attacks

| ID | Attack | Severity | Outcome |
|---|---|---|---|
| RT-01 | Planning is substituting for market contact | **Critical** | **Landed.** Structural rule imposed |
| RT-02 | No evidence the founder can sell | **Critical** | **Landed.** Unresolvable from the desk |
| RT-03 | Selling diagnosis into a segment that does not buy diagnosis | High | Partially answered |
| RT-04 | The "revenue leak" may be a supplier-invented problem | **Critical** | **Landed.** Routed to H-10 |
| RT-05 | The moat arrives years after it is needed | High | **Landed.** Accepted |
| RT-06 | The founder's edge is the fastest-depreciating asset in the plan | High | **Landed.** Argues for speed |
| RT-07 | The geography choice may be economically wrong | High | **Landed.** Routed to `U-01`/H-04 |
| RT-08 | The plan's own execution load may exceed founder capacity | Medium | Partially answered |
| RT-09 | The founder's skills may be worth more elsewhere | **Critical** | **Landed.** Named, not resolved |

---

## RT-01 — This program plans instead of selling `CRITICAL` — **attack lands**

**The attack.** This repository contains a governance system, an operating model, an ADR register,
four workstream contracts, a dependency map, a canon/workbench firewall, and now twenty-plus
strategy documents. It contains **zero conversations with a potential customer** (`E-09`).

The sophistication is real (`E-12`, `E-21`) and it is the problem. Planning of this quality is
enormously satisfying, produces visible artifacts, feels like progress, and carries no risk of
rejection. Cold outreach produces nothing to look at and a great deal of rejection. A capable person
with a strong preference for systems will, without a structural constraint, choose the first
indefinitely and describe it as preparation.

**Why it cannot be answered with a promise.** "We'll start outreach after this" is what every
version of this failure says. The failure mode is not laziness; it is a competence trap — being
genuinely excellent at the wrong stage of the work.

**What was done.** A binding stop rule (`AGENCY_THESIS.md` §11, proposed for approval with
`ADR-0005`): after this plan merges, **no further strategic planning artifact may be created until
10 qualified buyer conversations are logged.** Delivery templates, sales instruments and validation
tooling are permitted because they are consumed by market contact; more strategy is not.

**Residual.** The rule is self-imposed and can be self-repealed. The genuine safeguard is the D3
access gate at day 30, which produces a number that cannot be argued with.

**Verdict:** the attack lands. It is the single most likely cause of this program failing, ahead of
any market factor.

---

## RT-02 — Nothing establishes that the founder can sell `CRITICAL` — **attack lands**

**The attack.** The plan's critical path runs entirely through activities with no evidence base:
cold outreach, discovery conversations, price presentation, objection handling, closing. `U-05` is
unanswered. The founder's demonstrated competence is in systems design and AI orchestration, which
is a *different* skill and is frequently anti-correlated with comfort in sales conversations.

A plan that requires the operator to be good at the one thing there is no evidence they are good at
is not a plan; it is a hope with a Gantt chart.

**The honest response.** This cannot be resolved by analysis, and no amount of sales-process design
compensates for it. What the plan does:
- Chooses a low-pressure entry instrument (a free teardown, then a small paid diagnostic) rather
  than a high-ticket consultative close.
- Makes the opener an *observation about their business* rather than a pitch, which is a
  substantially easier conversation to have.
- Measures the outcome early and cheaply (D3 at day 30, D5 at day 60).
- Provides a designed exit: pivot P-C routes distribution through intermediaries, and P-D is
  employment or contract work, stated as a legitimate outcome rather than a defeat.

**Verdict:** the attack lands and is not answered. It is converted from an unknown risk into a
measured one, which is the most a plan can do.

---

## RT-03 — Diagnosis is being sold to a segment that does not buy diagnosis `HIGH` — partially answered

**The attack.** SMB owners buy *things*: a website, a campaign, a system. They do not buy analysis.
"Pay me to tell you what's wrong" is a professional-services frame that works for enterprises with
procurement functions and consultants with reputations. A clinic owner who wants more patients will
compare a USD 2,400 diagnostic with USD 2,400 of advertising and choose the advertising, because at
least advertising produces something.

**The answer.** The diagnostic is deliberately not sold as analysis. It is sold as *instrumentation
you keep* plus *a priced fix you may decline* — a bounded, concrete deliverable that leaves the
buyer with an asset either way. The framing is closer to a building survey than to a consulting
engagement.

**Why the answer is incomplete.** That framing is a hypothesis about how buyers will hear it, not an
observation of how they do. `H-01` exists precisely because this attack might be right, and D5
path B (fall back to a free wedge) exists because it might be right in a recoverable way.

**Verdict:** partially answered. Logged as contradiction `C-03`.

---

## RT-04 — The problem may be invented by the supplier `CRITICAL` — **attack lands**

**The attack.** The "revenue leak between demand arriving and demand being served" is an elegant
frame constructed by a planner, not reported by a buyer (`E-05`: the available VoC is synthetic).
Clinic owners may sincerely and *correctly* believe their binding constraint is demand, not
conversion. If so, the entire thesis is a solution looking for a problem, and every subsequent
document is downstream of a fiction.

Worse: the frame is persuasive enough that buyers may agree with it when pitched, producing false
positive signal. Agreement with a well-constructed frame is worth nothing.

**What was done.** The D4 resonance gate is designed specifically against this attack: the test is
not whether buyers agree, but whether they **volunteer the problem unprompted** in the first twelve
minutes, before hearing anything about the offer. Leading questions are explicitly prohibited.
Threshold: 5 of 10. Failure at ≤1 of 10 kills or reframes the thesis.

**Verdict:** the attack lands, and it is the correct attack. It is converted into the program's
third-priority test. Until D4 returns, every commercial document in this plan should be read as
conditional on an unverified premise.

---

## RT-05 — The moat arrives years after it is needed `HIGH` — **attack lands**

**The attack.** The plan's stated durable differentiator is accumulated benchmark data
(`AGENCY_THESIS.md` §4.2). Benchmark claims require n≥5 per cohort. At solo capacity of 3–5 core
engagements per year plus diagnostics, a meaningful dataset is 2–3 years away. The differentiator
that is supposed to make the business defensible does not exist during the period in which the
business is most vulnerable.

Meanwhile the copyable parts — the offer structure, the diagnostic format, the positioning — are
visible from the outside within weeks of the first published case study.

**Partial answer.** Diagnostics accumulate benchmark rows faster than cores do (7+ per year in the
base case), so n≥5 is reachable around month 9–12 rather than year 3. And in the interim the
relevant defence is not a moat but obscurity plus relationship: nobody imitates a supplier they have
not noticed.

**Why it is still a landed hit.** "Obscurity is our moat" is not a strategy, and the honest position
is that this business has **no defensibility in years 1–2** beyond execution quality and client
relationships. That is true of nearly every new services business, and the plan should not pretend
otherwise.

**Verdict:** lands. Accepted. Recorded as risk R-16.

---

## RT-06 — The founder's edge is depreciating fastest `HIGH` — **attack lands**

**The attack.** The economic case for a solo operator delivering team-scale work rests on AI
leverage (`E-21`, `AGENCY_THESIS.md` §9). That leverage is available to everyone, improving for
everyone, and becoming cheaper for everyone. Every month of planning spends a month of a closing
window. By the time this business has three case studies, the capability that made it possible may
be a commodity available to every competitor and to the clients themselves.

**Answer.** Correct, and the plan says so (`AGENCY_THESIS.md` §9, counter-argument). The strategic
response is that the durable asset is *knowing what to point the capability at* — diagnosis and
domain knowledge — not the capability itself. That is why M2 was killed as a category and retained
only as a mechanism.

**But the timing implication is the real content of this attack:** if the window is closing, speed
of market contact dominates completeness of planning. This is the same conclusion as RT-01, reached
from the opposite direction, which is why both are treated as critical.

**Verdict:** lands. Reinforces the stop rule rather than requiring a separate fix.

---

## RT-07 — The geography may be economically wrong `HIGH` — **attack lands**

**The attack.** The plan assumes a local-first Mexican metro market (`A-01`, low confidence) and
accepts a lower price anchor in exchange for in-person trust. But if local SMB price anchors are
substantially below the modelled ranges, the base case never reaches the founder's required draw —
while the *same work*, delivered remotely to US buyers at US anchors, might be viable at half the
volume.

In that case the local-first choice is not a reasonable trade-off; it is the wrong business.

**Why it cannot be settled here.** `U-01` is unanswered and no price observation exists (`E-22`).
The plan's own rule forbids inventing the answer.

**What was done.** The geography analysis states the trade explicitly rather than assuming it
(`AGENCY_THESIS.md` §7); `H-04` converts inferred ranges into real price signals; T-11 fires a
re-derivation of the entire pricing model on first observed competitor price; and the contracting
posture is required not to foreclose remote work.

**Verdict:** lands. This is the attack most likely to force a structural change after first contact,
and the plan is built to absorb it rather than to resist it.

---

## RT-08 — The plan is bigger than the operator `MEDIUM` — partially answered

**The attack.** Twenty-plus interlocking documents, thirty-plus metrics, a dozen hypotheses, eleven
repricing triggers, a nine-stage lifecycle. One person with 30 hours a week. The governance overhead
of the plan may consume the capacity the plan exists to allocate. A plan that cannot be executed by
its executor is a document, not a plan.

**Answer.** The plan is designed as **reference material with a thin execution surface**, not as a
sequential programme:
- The execution surface for days 0–90 is `30_60_90_180_365_ROADMAP.md` §11 — one paragraph.
- The validation-phase scorecard is seven metrics, not thirty-five
  (`AGENCY_SCORECARD.md` §5). The rest activate when there is data to put in them.
- The gates are six decisions over 180 days.

**Residual.** Real. The risk is that the plan's existence encourages consulting it rather than using
it. Mitigated by the stop rule and by the roadmap's explicit statement that everything else is
either support for the first sixteen conversations or a distraction from them.

**Verdict:** partially answered.

---

## RT-09 — Should this business exist at all? `CRITICAL` — **attack lands, unresolved by design**

The mandate requires arguing that the whole model should not exist. The strongest version:

**The attack.** The founder demonstrably possesses: multi-agent AI orchestration at a level most
organisations cannot hire for; systems and governance design discipline; unusual visual and
editorial taste; bilingual capability. These are, right now, among the most in-demand capabilities
in the labour market.

Building a solo agency converts those capabilities into: cold outreach to clinic administrators,
CRM configuration, invoice chasing, and a base-case outcome of roughly USD 6,350 per month in year
one — achieved only if six sequential gates pass on schedule, with no slack, at high personal risk,
in a business whose defensibility is zero for two years (RT-05) and whose core capability advantage
is depreciating (RT-06).

The same capabilities, applied to employment, contracting, or building a product, could plausibly
produce more income, more leverage and less risk. **The opportunity cost of this business may exceed
its expected value.**

**Counter-argument, stated fairly.** Agencies produce optionality that employment does not: direct
market contact, accumulating client relationships, a proof base, and the possibility of a product
discovered from delivered work. The founder may value autonomy, ownership and variety in ways that
a salary does not compensate. And the plan's *cost to test* is low — 90 days and near-zero cash —
against an outcome that is genuinely unknown.

**Why the attack still lands.** Because the counter-argument is about *preferences*, and the plan
cannot evaluate the founder's preferences. What the plan can do is refuse to hide the trade: `U-02`
and `U-03` (hours available, runway and required draw) are elevated to Day 0 blocking questions
precisely because a founder who needs USD 6,000 a month is being shown, in this plan's own numbers,
that the base case *is* the break-even case with no margin for error
(`PRICING_AND_ECONOMICS_MODEL.md` §10).

**Verdict:** lands, and is left open deliberately. It is a founder's decision, not a planner's, and
the correct service this document can provide is to state it plainly rather than to argue past it.
Pivot P-D in `DECISION_TREE.md` exists so that choosing employment is a recorded decision with
dignity, not a failure.

---

## What survived

After nine attacks, the following still stand:

1. **The elimination logic.** M1, M2, M4, M7 and M9 are disqualified for reasons that do not depend
   on any unvalidated number. Nothing in this review rehabilitates them.
2. **The evidence discipline.** No attack landed on the grading scheme, the `INFERRED RANGE`
   quarantine, or the refusal to import research precision. This is the plan's strongest section.
3. **The gate structure.** Every critical attack (RT-01, RT-02, RT-04, RT-07) is converted into a
   dated, thresholded test with a defined failure branch. The plan cannot fail silently.
4. **The refusal lists.** `RF-1`–`RF-9` and `DNS-1`–`DNS-13` each carry a stated cost. They are the
   parts of the plan most likely to be worth their weight.
5. **The proof architecture.** Baseline-at-kickoff as a structural gate is a genuine design
   advantage, and no attack reached it.

## What did not survive, and is now stated as exposure

| # | Exposure |
|---|---|
| 1 | **Planning has substituted for market contact for the entire life of this program.** Nothing is validated. Nothing has been sold. Nobody has been spoken to |
| 2 | **There is no evidence the founder can sell**, and the plan depends entirely on it |
| 3 | **The core problem may not exist in the buyer's mind.** The frame is the planner's, not a buyer's |
| 4 | **There is no defensibility for 18–24 months** |
| 5 | **The capability advantage is depreciating** while the plan is being written |
| 6 | **The geography and price assumptions may invalidate the economics** entirely |
| 7 | **The opportunity cost may exceed the expected value**, and only the founder can judge that |

## The Red Team's recommendation

> **Approve `ADR-0005`, activate the stop rule, and begin outreach within seven days.**
>
> Not because the plan is proven — it is not, and this review has shown how far from proven it is.
> But because every remaining question is answerable only in the field, and every additional week of
> planning makes the plan longer without making it truer.
>
> The plan's own best sentence is `30_60_90_180_365_ROADMAP.md` §11. Everything else in this
> repository should be treated as support for that paragraph, or deleted.
