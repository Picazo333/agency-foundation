---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - AGENCY_MASTER_PLAN.md
---
# Master Plan Audits — Passes 1–8

> Mandatory review passes required by Issue #2. Each pass reads the whole plan from one
> professional perspective and attacks it. Pass 9 (Red Team) is separate:
> `RED_TEAM_REVIEW.md`. Cross-document consistency is `INTEGRATION_PASS.md`.
>
> **Findings are only listed here if they were real.** Findings marked `APPLIED` have been fixed in
> the plan and the fix location is named. Findings marked `ACCEPTED` are real and not fixable at
> this scale — they are carried as known exposure rather than hidden. Findings marked `OPEN` are
> unresolved and routed to validation.

## Summary

| Pass | Perspective | Findings | Applied | Accepted | Open |
|---|---|---:|---:|---:|---:|
| 1 | Experienced agency founder | 5 | 3 | 1 | 1 |
| 2 | B2B go-to-market strategist | 4 | 3 | 0 | 1 |
| 3 | Operator / COO | 4 | 2 | 2 | 0 |
| 4 | CFO / unit economics | 5 | 3 | 2 | 0 |
| 5 | Sales leader | 4 | 3 | 0 | 1 |
| 6 | Delivery / quality lead | 4 | 3 | 1 | 0 |
| 7 | Security / privacy / risk | 5 | 4 | 1 | 0 |
| 8 | Sceptical buyer / procurement | 4 | 2 | 1 | 1 |
| **Total** | | **35** | **23** | **8** | **4** |

---

## Pass 1 — Experienced agency founder

*Reading for: will this actually work in practice, or only on paper?*

### AUD-01-01 — The paid diagnostic has a bootstrap problem `HIGH` `APPLIED`
**Finding.** A paid diagnostic requires credibility, and its purpose is to create credibility. No
clinic owner buys diagnosis from someone they have never heard of on the strength of a cold email.
The plan as originally drafted went straight from outreach to a paid entry offer.
**Fix.** Added **L0 Teardown** — free, asynchronous, capped at 3 hours — as the rung below the paid
diagnostic, so competence is demonstrated before it is charged for.
**Where:** `OFFER_ARCHITECTURE.md` §2; ladder in §1; stop-rule at 10 teardowns.
**Residual.** The circle is narrowed, not closed. Whether it is enough is `H-01`, and it is logged
as contradiction `C-03`.

### AUD-01-02 — Three weeks of silence in the first paid engagement `MEDIUM` `APPLIED`
**Finding.** The L1 measurement window runs days 6–15 with almost no client contact. The first paid
engagement with a new supplier is exactly when a client's doubt peaks, and silence reads as
inactivity.
**Fix.** Mandatory day-8 interim note.
**Where:** `DELIVERY_OS.md` §4, phase D4b.

### AUD-01-03 — "Skip the diagnostic, just build it" `MEDIUM` `APPLIED`
**Finding.** Some buyers arrive already knowing what they want. A rigid diagnostic-first rule loses
them or forces a dishonest workaround.
**Fix.** Written skip-upward exception requiring a recorded justification and an explicit
acknowledgement that no outcome claim may be made from that engagement.
**Where:** `OFFER_ARCHITECTURE.md` §8.

### AUD-01-04 — The founder will underprice the first deal `HIGH` `APPLIED`
**Finding.** Under pressure to get a first client, the first engagement is almost always discounted,
and the discount then anchors the relationship, the referrals and the market.
**Fix.** `DNS-13` prohibits portfolio discounts; the pilot exception is capped at two engagements,
no lower than 60% of base, and requires a written case-study agreement as consideration.
**Where:** `OFFER_ARCHITECTURE.md` §9; `PRICING_AND_ECONOMICS_MODEL.md` §7.1.

### AUD-01-05 — The plan assumes the founder enjoys outbound `MEDIUM` `OPEN`
**Finding.** The entire first 90 days rests on sustained cold outreach. Nothing in the evidence base
indicates whether the founder can do this consistently. A plan whose critical path runs through an
activity the operator avoids will fail quietly, and it will be attributed to the market.
**Status.** Unresolved. Routed to `U-04`/D0 and to the D3 access gate, which measures the outcome
rather than the intention. `DECISION_TREE.md` pivot P-C (partnership-led) is the designed response.

---

## Pass 2 — B2B go-to-market strategist

*Reading for: does this reach a market, and does it learn fast enough?*

### AUD-02-01 — Three segments would halve the learning rate `HIGH` `APPLIED`
**Finding.** An earlier draft carried three candidate segments into outreach. At the available
outreach volume, three segments means none reaches conversational saturation inside 30 days, and
the access gate produces ambiguous data.
**Fix.** Exactly one primary (75%) and one hedge (25%), with a defined swap rule at D3.
**Where:** `ICP_FRAMEWORK.md` §5; `DECISION_TREE.md` D2, D3.

### AUD-02-02 — The outreach research budget did not fit the hour budget `HIGH` `APPLIED`
**Finding.** Observation-first outreach requires ~35 minutes of research per target. At 20 targets
per week that is 12+ hours against a stated 8–10 hour budget. The plan was internally inconsistent.
**Fix.** Tiered research: deep observation for 6–8 high-fit targets/week, light observation for the
remainder.
**Where:** `ACQUISITION_MARKETING_SYSTEM.md` CH-1.

### AUD-02-03 — Content was positioned as a channel `MEDIUM` `APPLIED`
**Finding.** Founder-led content cannot produce evidence inside a 90-day validation window, and
treating it as a channel invites the substitution of publishing for selling.
**Fix.** Content reclassified as a *byproduct* of teardown production, with an explicit stop rule if
it displaces outreach hours, and a reassessment date of month 6.
**Where:** `ACQUISITION_MARKETING_SYSTEM.md` CH-5, §1.

### AUD-02-04 — No competitive map before entering the market `MEDIUM` `OPEN`
**Finding.** The white-space claim (`AGENCY_THESIS.md` §4.1) is structural reasoning, not
observation. Entering a market whose competitive density is unknown (`U-12`) risks discovering the
position is occupied after the message is built.
**Status.** Partially addressed by H-07, which asks every buyer who else they have considered —
the cheapest available competitive research. Not resolvable from the desk.

---

## Pass 3 — Operator / COO

*Reading for: can one person actually run this?*

### AUD-03-01 — WIP of 2 concurrent core builds was impossible `HIGH` `APPLIED`
**Finding.** Two concurrent cores consume ~140% of available delivery hours and assume sales stops
entirely.
**Fix.** Hard WIP of 1 core + 2 diagnostics; raising it requires a contractor, not optimism.
**Where:** `OPERATING_MODEL.md` §5, §5.1.

### AUD-03-02 — The L3 limit conflicted with the core-build limit `MEDIUM` `APPLIED`
**Finding.** Four operated accounts at 9 hours each is 36 hours/month. During a core build, delivery
allocation is already 91 hours/month, so 4 L3 accounts and an active build cannot coexist.
**Fix.** L3 WIP reduced to 2 while a core build is active; 4 is permitted only between builds, and
a permanent increase requires the operations coordinator.
**Where:** `OPERATING_MODEL.md` §5.

### AUD-03-03 — Founder unavailability has no real mitigation `HIGH` `ACCEPTED`
**Finding.** Illness or absence stops all revenue and damages live client systems with no
substitute.
**Status.** Accepted as an unresolvable residual at solo scale, and stated as such rather than
papered over. Blast radius is reduced by documentation-first practice, client-operable runbooks,
and the refusal of any 24/7 SLA (`DNS-8`). Insurance is routed to `I-04` ⚖️.
**Where:** `OPERATING_MODEL.md` §8.

### AUD-03-04 — The protected sales block will be broken `HIGH` `ACCEPTED`
**Finding.** Every solo operator intends to protect prospecting time; a delivery deadline always
feels more urgent. Intention is not a control.
**Status.** Accepted as a behavioural risk with the strongest available structural counter: a named
calendar block, a metric that detects the failure (M-41, sales <10% of hours for 3 weeks), and an
offer (L0, 3 hours) small enough to fit inside a delivery week.
**Where:** `OPERATING_MODEL.md` §6.1; `AGENCY_SCORECARD.md` M-41.

---

## Pass 4 — CFO / unit-economics reviewer

*Reading for: do the numbers survive contact with arithmetic?*

### AUD-04-01 — A 100% diagnostic credit destroyed margin on success `HIGH` `APPLIED`
**Finding.** Crediting the full diagnostic fee against the build makes the diagnostic free whenever
conversion is good — i.e. it penalises exactly the outcome the model wants — and it contradicts the
claim that the diagnostic has standalone value.
**Fix.** Credit capped at 50%, time-boxed to 30 days.
**Where:** `OFFER_ARCHITECTURE.md` §3.1.

### AUD-04-02 — Contribution margin was presented misleadingly `MEDIUM` `APPLIED`
**Finding.** 94% contribution margin is arithmetically correct and strategically meaningless,
because it excludes the founder's labour — the only real cost in the business. Quoted unqualified,
it would justify bad decisions.
**Fix.** Effective yield per founder hour named as the master metric, with an explicit warning
against quoting contribution margin.
**Where:** `PRICING_AND_ECONOMICS_MODEL.md` §6.3; `AGENCY_SCORECARD.md` §2.

### AUD-04-03 — Break-even ignored the tax reserve `HIGH` `APPLIED`
**Finding.** The break-even table was stated in pre-tax contribution while F-02 requires reserving
25–30%. Every break-even figure was therefore understated by roughly 35–45%.
**Fix.** Multiplier correction added directly above the table.
**Where:** `PRICING_AND_ECONOMICS_MODEL.md` §10.

### AUD-04-04 — The base case has no slack `HIGH` `ACCEPTED`
**Finding.** The base case consumes ~790 of ~780 available delivery hours. There is no allowance for
a failed engagement, an illness, or a slow quarter.
**Status.** Accepted and stated explicitly rather than smoothed. It is the quantitative argument for
the contractor trigger and for treating `U-03` as a go/no-go input.
**Where:** `PRICING_AND_ECONOMICS_MODEL.md` §9, §10.

### AUD-04-05 — High diagnostic conversion is a capacity crisis, not a win `MEDIUM` `ACCEPTED`
**Finding.** At 50% diagnostic→core conversion, ten diagnostics generate 1,200 hours of work against
a 780-hour ceiling. The plan's "good" scenario is an over-commitment scenario.
**Status.** Made explicit in the sensitivity table so that good conversion triggers a contractor
decision rather than a celebration.
**Where:** `PRICING_AND_ECONOMICS_MODEL.md` §8.4.

---

## Pass 5 — Sales leader

*Reading for: will deals actually close?*

### AUD-05-01 — No buying-committee model `HIGH` `APPLIED`
**Finding.** The plan treated "the buyer" as one person. In a multi-site clinic group there are at
least four roles, one of which (the marketing coordinator or incumbent agency) is structurally
threatened by a diagnostic that quantifies leakage.
**Fix.** Full committee map with each role's interest, authority and risk; a mandatory Q3 gate
requiring the signer to be named and in a conversation; and explicit framing to neutralise the
blocker.
**Where:** `ICP_FRAMEWORK.md` §6.2; `SALES_SYSTEM.md` §3; `POSITIONING_ARCHITECTURE.md` §9.

### AUD-05-02 — Partner-owned groups need more than one signature `MEDIUM` `APPLIED`
**Finding.** Clinician partnerships commonly require multi-partner approval above a spend threshold,
often on a monthly meeting cycle. "The managing partner is keen" does not satisfy Q3.
**Fix.** Q3 extended: who else must agree, what the threshold is, when they meet; and a requirement
that the proposal be readable without the author present.
**Where:** `SALES_SYSTEM.md` §3.

### AUD-05-03 — Speculative proposals were not prohibited `HIGH` `APPLIED`
**Finding.** At 80 unbilled sales hours per close, effective yield drops 28%. Speculative proposals
are the main mechanism by which that happens, and they feel productive.
**Fix.** Explicit prohibition on producing a written proposal before Q1–Q4 pass, with the economics
stated so the rule has a reason attached.
**Where:** `SALES_SYSTEM.md` §5.1; `PRICING_AND_ECONOMICS_MODEL.md` §8.3.

### AUD-05-04 — No answer to "send me your rates" `MEDIUM` `OPEN`
**Finding.** A common opener that the diagnostic-first model cannot answer. The plan's response
("I can't price a fix before measuring") is correct and will lose some buyers who simply want a
number.
**Status.** Open. It is a real cost of the positioning, accepted deliberately. Whether it is a
frequent objection is an empirical question for H-04 field notes.

---

## Pass 6 — Delivery / quality lead

*Reading for: can this be delivered to a standard that survives review?*

### AUD-06-01 — No path when the client has no baseline `HIGH` `APPLIED`
**Finding.** The entire proof engine assumes a measurable baseline. Many SMBs record nothing usable.
The plan had no route for them except disqualification, which would exclude a large share of the
addressable market.
**Fix.** O-0 Instrumentation Sprint added as a priced pre-phase; time-to-findings extends to 5–6
weeks and must be disclosed at the point of sale. `RF-8` still disqualifies clients who refuse to
instrument at all.
**Where:** `OFFER_ARCHITECTURE.md` §3.2; `DECISION_TREE.md` D6; H-06.

### AUD-06-02 — Platform proliferation would destroy repeatability `HIGH` `APPLIED`
**Finding.** C-2 is CRM-dependent and clients arrive with arbitrary platforms. Supporting all of
them multiplies the template library and guarantees failure at the D8 repeatability gate.
**Fix.** Hard limit of two supported CRM platforms and two booking/PMS integration patterns;
anything else is quoted as custom or declined.
**Where:** `DELIVERY_OS.md` §10; `TOOLING_AUTOMATION_REQUIREMENTS.md` §4.

### AUD-06-03 — The founder QAs their own work `HIGH` `APPLIED` *(partially)*
**Finding.** Self-review is the weakest QA arrangement and is structurally unavoidable solo.
**Fix.** Three partial mitigations made mandatory: a minimum 12-hour gap between build completion
and QA, literal item-by-item checklist execution rather than from memory, and automation of every
deterministic check.
**Where:** `DELIVERY_OS.md` §9.0.
**Residual.** Real. Resolved properly only when a second person exists.

### AUD-06-04 — AI speed creates a verification temptation `HIGH` `ACCEPTED`
**Finding.** The delivery economics depend on AI leverage, and the same leverage makes it tempting
to skip verification. A confidently wrong number in a diagnostic report is worse than no report,
because the product *is* the accuracy.
**Status.** Structurally mitigated by `AI-4` (every AI-produced figure traced to source) being a
named QA checklist item rather than an intention, and by the Measured/Reconstructed/Estimated
labelling requirement. Behavioural residual accepted and named.
**Where:** `DELIVERY_OS.md` §7.1, §9.1, §4.1.

---

## Pass 7 — Security / privacy / risk reviewer

*Reading for: what could end the business rather than merely hurt it?*

### AUD-07-01 — The primary ICP is a data-protection exposure `CRITICAL` `APPLIED`
**Finding.** Multi-site clinic groups mean patient-adjacent personal data. The plan proposed
building automated communication systems handling it, with `U-10` unresolved, in a jurisdiction that
is itself unconfirmed (`U-01`).
**Fix.** `RF-7` and `DNS-9` prohibit clinical/patient-record access entirely until counsel clears
it; `DR-1`–`DR-8` impose minimisation, pseudonymisation and deletion rules that bind now;
`D-04` is escalated as the specific question that determines whether the ICP is viable at all; the
data-protection lawyer is item 3 on the professional-advice list with "before first healthcare
engagement" as the deadline.
**Where:** `GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §4, §10, §12.

### AUD-07-02 — Benchmark data is a re-identification risk `HIGH` `APPLIED`
**Finding.** "In 14 clinics like yours" is the plan's key differentiator and is built on client data.
Small-n medians in a narrow specialty and city are re-identifiable.
**Fix.** Never published below n=5 per cohort; anonymised storage separated from the join key;
contractual consent required; `D-10` routed to counsel.
**Where:** `PROOF_STRATEGY.md` §8; `GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §4.

### AUD-07-03 — AI processing of client personal data was unaddressed `HIGH` `APPLIED`
**Finding.** Diagnostic analysis uses AI and touches client data. Sending it to a third-party
provider without a contractual basis is a real exposure, and the plan originally assumed AI use
freely.
**Fix.** `AI-1`–`AI-8` governance rules; `DR-3` pseudonymisation; disclosure obligation in the
proposal; `TQ-3` routed to counsel. Noted that most diagnostic analysis needs counts and timestamps
rather than names, so minimisation is usually achievable without losing analytical value.
**Where:** `DELIVERY_OS.md` §7.1; `GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §4.1, §5.

### AUD-07-04 — Test enquiries to prospects are an ethical question `MEDIUM` `APPLIED`
**Finding.** The teardown method involves submitting an enquiry to a business as a prospect in order
to measure response latency. This consumes a real person's time under a false pretext, and doing it
to a healthcare provider is worse than doing it to a retailer.
**Fix.** Enquiry only, never a booking; never occupy an appointment slot; never present a medical
complaint; and the teardown itself discloses that the enquiry was a timing test.
**Where:** `DELIVERY_OS.md` §3.

### AUD-07-05 — Contractor access has no lifecycle `MEDIUM` `ACCEPTED`
**Finding.** Contractors will need client system access, and revocation discipline degrades when a
project ends untidily.
**Status.** Rules exist (`S-11`, `OPERATING_MODEL.md` §7, access register with time-bounding). The
residual is enforcement by a busy solo operator, which is accepted and monitored via the
offboarding checklist artifact requirement.

---

## Pass 8 — Sceptical buyer / procurement reviewer

*Reading as the person trying to find a reason to say no.*

### AUD-08-01 — An unnamed category cannot be budgeted `HIGH` `APPLIED`
**Finding.** "Revenue operations studio" maps to no budget line the buyer owns. Procurement rejects
line items with no owner, and a busy clinic owner will not invent a category to accommodate a
supplier.
**Fix.** Dual-frame messaging — anchor in an existing budget ("the revenue you already pay to
generate and then lose"), differentiate on method. Plain description (CAT-5) leads in all cold
contexts; category labels are tested (H-11), and the budget-line question is asked directly.
**Where:** `AGENCY_THESIS.md` §2.1; `POSITIONING_ARCHITECTURE.md` §2, §4.

### AUD-08-02 — "You have no clients in our sector" has no good answer `HIGH` `APPLIED`
**Finding.** True, unavoidable, and the buyer will raise it.
**Fix.** The answer is structural rather than rhetorical: admit it plainly, then point at the small
first step that produces something the buyer keeps regardless. `A-06` is volunteered rather than
concealed, which converts a weakness into a credibility signal. The diagnostic *is* the risk
reduction.
**Where:** `POSITIONING_ARCHITECTURE.md` §9; `PROOF_STRATEGY.md` §11.

### AUD-08-03 — Procurement will ask for insurance and liability caps `MEDIUM` `ACCEPTED`
**Finding.** A supplier with system access and no professional-liability cover may be disqualified
before price is discussed — and some healthcare buyers mandate it.
**Status.** Routed to `I-01`–`I-05` ⚖️, with `I-03` flagged as potentially gating the ICP entirely
and explicitly added to the validation questions. Liability cap is `C-04`.

### AUD-08-04 — The three-option proposal may read as upselling `LOW` `OPEN`
**Finding.** A sophisticated buyer may read a good/better/best ladder as a sales device rather than
as genuine choice.
**Status.** Open. Mitigated by deriving every option from the diagnostic's own findings, so each
option maps to a specific quantified gap rather than to a price tier. Whether it reads as intended
is observable in field notes.

---

## Findings routed to validation

| Finding | Hypothesis |
|---|---|
| AUD-01-01 bootstrap | H-01 |
| AUD-01-05 outbound sustainability | H-03 (measures outcome, not intention) |
| AUD-02-04 competitive density | H-07 |
| AUD-05-04 "send me your rates" | H-04 field notes |
| AUD-06-01 baseline availability | H-06 |
| AUD-07-01 data-protection viability | ⚖️ counsel, before first healthcare engagement |
| AUD-08-01 budget line | H-11 |
| AUD-08-03 insurance requirement | Asked directly in interviews |
| AUD-08-04 option framing | Field notes |
