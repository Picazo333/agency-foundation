---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - DELIVERY_OS.md
  - PRICING_AND_ECONOMICS_MODEL.md
---
# Agency Operating Model and Organisation Design

> **Module 14 of the Agency Master Plan** (Issue #2 Phase 11).
>
> **Disambiguation:** this document is the *agency's* internal organisation design — roles,
> capacity, delegation, cadence. It is **not** `docs/00-meta/operating-model.md`, which governs the
> multi-agent program that produced this plan. Different subjects, unfortunately similar names;
> the filename here is fixed by the Issue #2 deliverable contract.

## 1. Starting position

One person, ~30 productive hours/week (`A-03`), no team, no contractors engaged (`A-04`, `A-05`),
performing every function: sales, delivery, QA, finance, admin and strategy.

The design question is not "what is the org chart?" It is: **which functions must the founder keep,
which must be systematised, and in what order do they leave?**

## 2. Functions and their disposition

| Function | Hours/week at steady state | Founder keeps? | First to delegate |
|---|---:|---|---|
| Sales — discovery, proposals, closing | 6–9 | **Permanently, until revenue supports a specialist** | Last |
| Outbound prospecting and teardowns | 4–6 | No | **2nd** |
| Diagnostic analysis and findings | 3–5 | **Yes** — this is the product | Never (until a trained analyst exists) |
| Build execution | 8–14 | No | **1st** |
| QA | 2–3 | Partially — final sign-off stays | 4th |
| Client communication | 2–3 | Yes during engagement | 5th |
| L3 operated cycles | 1–4 | No | **3rd** |
| Finance and admin | 2 | No | Early, cheap, high relief |
| Strategy and planning | 1–2 | Yes | Never |

**Delegation order is by ratio of hours consumed to judgement required**, not by unpleasantness.
Build execution is first because it is the largest block with the most specifiable output.
Diagnostic analysis is last because it *is* the differentiated product.

## 3. Roles now

| Role | Who | Notes |
|---|---|---|
| Principal / diagnostician | Founder | Sales, diagnosis, findings, pricing, client relationship, final QA |
| Delivery lead | Founder | Build execution |
| Operations | Founder | Admin, finance, tooling |
| **Bookkeeper** | External, from month 2–3 | USD 100–250/mo. Cheapest possible relief of the least-valuable founder hours, and it removes a real compliance risk |
| **Legal counsel** | External, as needed | Contract templates, entity, data obligations — one-time cost, mandatory before the first signed SOW (`GOVERNANCE_RISK_SECURITY_CHECKLIST.md`) |

## 4. Roles later, with triggers

| Role | Trigger | Engagement | First responsibility |
|---|---|---|---|
| **Implementation contractor** | 2 concurrent core engagements for 2 consecutive months **or** delivery hours >70% of capacity for 6 weeks | Project-based, hourly (`A-17`) | B2/B3 build execution against a written spec |
| **Operations coordinator** (PT) | 4+ active L3 accounts **or** admin >4 h/week | PT contract | L3 cycles, reporting, scheduling, client admin |
| **Analyst** | 10+ diagnostics delivered, templates stable | PT then FT | L1 measurement and first-pass analysis; findings stay with the founder |
| **Sales support / SDR** | Founder sales hours <6/week for 2 months while demand exists | PT | Outbound, teardown production, qualification to Q2 |
| **Delivery lead** (FT) | 6+ concurrent engagements, revenue supports the salary for 6 months from cash on hand | FT | Owns delivery; founder moves to sales and diagnosis |

**Every trigger is a measured condition, not a feeling.** The two failure modes are symmetric:
hiring from stress before the revenue exists, and refusing to hire past the point where the founder
is the bottleneck. Measured triggers prevent both.

## 5. Capacity and WIP limits

**Hard WIP limits, solo:**

| Work type | Limit | Rationale |
|---|---|---|
| Active core builds | **1** | A core consumes 70% of delivery capacity (`PRICING_AND_ECONOMICS_MODEL.md` §2) |
| Active diagnostics | **2** | Small, schedulable, mostly elapsed-time-bound |
| Active L3 accounts | **4**, reduced to **2** while a core build is active | 9 h/month each at Operated tier = 36 h/month. During a core build, delivery allocation is already 91 h/month, and 36 of those cannot also be L3 (`AUD-03-02`). Raising this permanently requires the operations coordinator, not willpower |
| L0 teardowns | 2/week | Outreach cadence |
| Total active client engagements | **5** | — |

### 5.1 The audit correction

An earlier version of this plan allowed 2 concurrent core builds. The operator audit
(`AUD-03-01`) rejected it: 2 cores = 140% of available delivery hours, and it assumes sales work
stops entirely. The limit is **1**, and raising it requires a contractor, not optimism.

**What happens when demand exceeds WIP** — in priority order: schedule the client for a start date
(a waiting list is a positioning asset, not an apology) · sell a diagnostic now and the build later
· engage a contractor · **raise prices** (T-3). **Never:** accept the work and hope. Every
over-committed engagement damages an existing client, and existing clients are the referral engine.

## 6. Cadence architecture

| Cadence | When | Duration | Content |
|---|---|---|---|
| Daily start | Morning | 10 min | Today's one delivery priority, one sales action; check alerts |
| Weekly planning | Monday | 45 min | Pipeline; WIP; capacity for the week; blocked items; **hours logged last week vs planned** |
| Weekly client updates | Friday | 60 min total | `CLIENT_LIFECYCLE.md` §4 |
| Weekly sales block | Fixed, protected | 4 h | Outbound and follow-up. **Protected means protected** — see §6.1 |
| Monthly review | 1st week | 2 h | Scorecard; assumption calibration; trigger check; pipeline health |
| Monthly client reports | By 5th business day | Variable | L3 deliverable |
| Quarterly review | Quarter start | Half day | Strategy, pricing, offer performance, hiring triggers, assumption register update, ADR review |
| Quarterly client QBR | Per account | 1 h | Expansion conversation |

### 6.1 The protected sales block

The single most important operational rule in this document, and the one most likely to be broken:

> **Four hours per week of sales activity are scheduled, protected, and never given to delivery.**
> Not "when there is time." A named block in the calendar.

The oscillation analysis (`PRICING_AND_ECONOMICS_MODEL.md` §2) shows sales capacity dropping 59%
during builds. The protected block is the mechanism that keeps it from dropping to zero, which is
what actually happens without one. A delivery deadline will always feel more urgent than a
prospecting hour; that asymmetry is exactly why the block must be a rule rather than an intention.

## 7. Delegation model

**Precondition: nothing is delegated that is not documented.** The documentation-first practice in
`DELIVERY_OS.md` §10 exists primarily to make delegation possible, and it is the reason templates
are treated as engagement deliverables.

| Step | Requirement |
|---|---|
| 1. Document | A written spec with inputs, steps, acceptance criteria and failure conditions — the same standard `DEFINITION_OF_READY.md` applies to AI agents, applied to humans |
| 2. Demonstrate | Do it once while recording |
| 3. Co-execute | They do it, founder observes |
| 4. Delegate with review | They do it, founder reviews output |
| 5. Delegate with sampling | Founder samples periodically |

**Never delegated:** pricing, scope decisions, diagnostic findings and their quantification, final
client sign-off, and any decision that would breach a `DO NOT SELL` or ethical claim rule.

**Contractor management:** written scope per engagement · fixed price or capped hours · NDA and IP
assignment signed before access · **least-privilege access, revoked at engagement end** · work
reviewed against the QA checklist before it reaches the client · a contractor's output is the
agency's output and the agency's liability.

## 8. Single points of failure

| SPOF | Exposure | Mitigation | Residual |
|---|---|---|---|
| **Founder unavailability** | Total revenue stop; client damage | Documentation-first; runbooks so clients can self-operate; a contractor who has seen the systems; client contracts with realistic timelines | **High.** Genuinely unresolvable at solo scale. State it honestly rather than pretending otherwise |
| Founder as sole sales channel | Pipeline stops during delivery | Protected sales block; L0 cadence; CH-3 partnerships | Medium |
| Single CRM/automation platform | Client systems depend on a vendor | Data portability requirement (`TOOLING_AUTOMATION_REQUIREMENTS.md` §3); export tested at handoff | Medium |
| Client concentration | One client = most of revenue | T-8 monitoring | Medium |
| Undocumented knowledge | Cannot delegate; cannot recover | Documentation as a deliverable | Low if practised |
| Credential/access loss | Cannot serve clients | Password manager with recovery; documented access register | Low |
| Single AI provider dependency | Delivery economics change if pricing or access changes | Provider-agnostic workflows where practical; no proprietary lock-in in client deliverables | Medium |

**On founder unavailability:** the honest position is that a solo agency cannot fully mitigate it.
What it can do is reduce blast radius — clients who can operate their own systems, documentation a
substitute could follow, and no promises (like a 24/7 SLA, `DNS-8`) that require the founder to be
permanently available. Business-interruption insurance is a question for the professional-advice
checklist (`GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §10).

## 9. Bottleneck analysis

| Stage | Bottleneck at month 3 | At month 12 | At month 24 |
|---|---|---|---|
| Demand | **Access to buyers** | Founder sales hours | Channel scalability |
| Qualification | — | — | Judgement (delegable with training) |
| Diagnosis | Founder analysis time | **Founder — this is the product** | Analyst training |
| Build | Founder hours | **Founder hours** | Contractor quality and availability |
| QA | — | Founder review time | Process |
| Operate | — | Coordinator capacity | Systems |

**Reading:** the bottleneck moves from *demand* (month 3) to *delivery capacity* (month 12) to
*management capacity* (month 24). Each transition requires a different response — outreach, then
contractors, then systems and a delivery lead — and mistaking which phase you are in is the classic
scaling error. A founder who responds to a month-12 capacity bottleneck with more marketing makes
things worse.

## 10. Knowledge and SOP system

| Layer | Contents | Where |
|---|---|---|
| Method | Diagnostic method, quantification rules, analysis patterns | Repo, versioned |
| Delivery SOPs | Per-offer runbooks, QA checklists, templates | Repo, versioned |
| Client records | Engagement folders, baselines, access registers, outcomes | Client system, access-controlled |
| Benchmark data | Anonymised P7 dataset | Separate store, join key held separately |
| Commercial | Pricing models, proposal templates, loss analysis | Repo, versioned |
| Decisions | ADRs | Repo (`docs/07-decisions/`) |

**Rule inherited from the program's own governance (`E-12`):** a decision that changes how the
business operates is recorded as an ADR. This is already the practice that produced this plan;
extending it to the operating business costs almost nothing and is the reason the business will be
explicable to a first employee, a partner or an acquirer.

## 11. Organisational milestones

| Milestone | Trigger | Change |
|---|---|---|
| **Solo** | Now | All functions founder-held |
| **Solo + external admin** | Month 2–3 | Bookkeeper; legal templates in place |
| **Solo + contractor bench** | 2 concurrent cores | Build execution delegated against written specs |
| **Small team** | 4+ L3 accounts, 6+ engagements | PT coordinator; founder exits L3 cycles |
| **Structured** | Revenue supports 6 months of a salary from cash | Delivery lead; founder moves to sales + diagnosis |
| **Scaled specialist** | Second vertical opened (post-D8) | Duplicated delivery pod; founder moves to strategy + key accounts |

Each milestone raises fixed cost and lowers flexibility. None is entered on optimism — each has a
measured trigger, and each should be entered **one month later than it feels necessary and not
two**.
