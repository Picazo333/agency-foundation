---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - OFFER_ARCHITECTURE.md
  - ACQUISITION_MARKETING_SYSTEM.md
  - PRICING_AND_ECONOMICS_MODEL.md
---
# Sales Operating System

> **Module 11 of the Agency Master Plan** (Issue #2 Phase 9). The sales process as an execution
> contract: stages, gates, fields, boundaries and metrics. Specifies what must exist; does not
> write final client-facing copy (`POSITIONING_ARCHITECTURE.md` §3 — buyer language comes from
> real buyers, not from this document).

## 1. Design constraints

Three facts shape everything below:

1. **Unbilled sales hours are worth 28% of effective yield** (`PRICING_AND_ECONOMICS_MODEL.md`
   §8.3). Qualification discipline is not politeness; it is the third-largest economic lever in the
   business after price and rework.
2. **The founder is the entire sales function**, and sales capacity collapses from 39 to 16 hours a
   month during delivery (§2 of the same document). The process must therefore be *low-touch by
   design*, not by exception.
3. **The diagnostic converts selling into a paid activity.** After L1 is sold, discovery, scoping
   and proposal work are funded by the client. This is the structural advantage of the model and it
   should be exploited deliberately: **do as little unpaid selling as the market permits.**

## 2. Pipeline stages

| # | Stage | Entry condition | Exit condition | Target duration |
|---|---|---|---|---|
| 0 | **Target** | On the named list | First contact sent | — |
| 1 | **Contacted** | Touch 1 sent | Reply received, or sequence exhausted | 14 days |
| 2 | **Conversation** | Reply received | 20+ min conversation held | 7 days |
| 3 | **Qualified** | Passes Q1–Q4 (§3) | Diagnostic proposed | 7 days |
| 4 | **Diagnostic proposed** | Written proposal sent | Signed or lost | 10 days |
| 5 | **Diagnostic active** | Payment received | Findings delivered | 15–21 days |
| 6 | **Core proposed** | Findings delivered, options priced | Signed or lost | 14 days |
| 7 | **Core won** | Deposit received | → Delivery | — |
| — | **Lost** | Any stage | Reason recorded (§8) | — |
| — | **Nurture** | Lost for timing only | Re-entry date set | — |

**Stage-2 rule:** the first conversation is **research, not a pitch**. Its purpose is the D4
resonance test (`DECISION_TREE.md`) — does the buyer volunteer the problem in their own words? A
conversation spent pitching produces a worse outcome *and* destroys the only evidence the program
currently needs.

## 3. Qualification gates

All four required to reach stage 3. Any failure sends the opportunity to Lost or Nurture with a
recorded reason. **No exceptions without a written note.**

| Gate | Test | Why it is non-negotiable |
|---|---|---|
| **Q1 — Fit** | Meets `ICP_FRAMEWORK.md` §6.7 qualify-in criteria; hits no disqualifier | Prevents the slow accumulation of unservable clients |
| **Q2 — Problem** | The buyer has described a commercial problem *in their own words*, unprompted | Without this there is nothing to diagnose, and the engagement will be judged against an unstated expectation |
| **Q3 — Authority** | The person who signs is **named**, and has been in at least one conversation | The most commonly skipped gate and the most expensive. A proposal to a non-signer is unpaid labour with a courteous ending |
| **Q4 — Access** | The buyer has confirmed willingness to grant read access to booking/enquiry data within 5 business days | `RF-8`. Without measurement there is no proof, no defensible renewal and no case study |

**Q3 in the S2 buying committee** (`ICP_FRAMEWORK.md` §6.2): the operations director is usually the
champion and rarely the signer. The correct move is not to bypass them but to arm them — and to
require one direct conversation with the owner before any proposal. Script: *"Before I put numbers
on paper, I need 20 minutes with whoever signs. I'd rather they hear the trade-offs from me than
read them in a document."*

**Multi-owner groups (`AUD-05-02`):** clinic groups are frequently owned by a partnership of
practising clinicians, where spend above a threshold needs more than one signature. Q3 is not
satisfied by "the managing partner is keen." The required answer is: *who else has to agree, what
is the threshold, and when do they meet?* If the answer is a monthly partners' meeting, the cycle
is set by that calendar and the proposal must be written to be read without the author present.

**The marketing-coordinator blocker:** where an incumbent agency or internal marketing owner exists,
include them early and frame the scope boundary explicitly — *"we measure what happens after the
leads arrive; your numbers get better, not questioned"* (`POSITIONING_ARCHITECTURE.md` §9). A
blocker discovered at proposal stage has already cost the deal.

## 4. Discovery

**Structure, 40 minutes:**

| Segment | Time | Purpose |
|---|---|---|
| Their situation, unguided | 12 min | The D4 resonance evidence. **Ask, then stop talking.** The single most valuable 12 minutes in the process |
| Mechanics — channels, tools, who handles what, what happens after an enquiry arrives | 12 min | Scoping input |
| Measurement — what they currently track, who looks at it | 6 min | Q4 and the no-baseline path (`OFFER_ARCHITECTURE.md` §3.2) |
| Consequence — what it costs them, what they have already tried | 6 min | Price anchoring |
| Process — who decides, what happens next, by when | 4 min | Q3 |

**Discovery rules:**
- Do not present capabilities in discovery. If the buyer asks, answer in two sentences and return.
- Record verbatim phrasing for the messaging corpus (`POSITIONING_ARCHITECTURE.md` §3).
- Never quote a core price in discovery. The honest and strategically correct answer is:
  *"I can't price a fix before I've measured what's broken. That's what the diagnostic is for."*
- Log actual minutes spent (`A-14` calibration).

## 5. Proposals

### 5.1 The speculative-proposal prohibition

> **No written proposal is produced before Q1–Q4 pass.** A proposal is a deliverable with a real
> cost (2–4 hours), and speculative proposals are the primary mechanism by which `A-14` inflates
> from 20 to 80 hours per close — a 28% yield loss (`PRICING_AND_ECONOMICS_MODEL.md` §8.3).

A buyer who requests a proposal before qualification is asking for free consulting or a document to
price-shop with. The correct response is a 25-minute call, not a document.

### 5.2 Diagnostic proposal *(≤ 2 pages, ≤ 45 minutes to produce)*

Deliberately short. A long proposal for a small engagement signals that the supplier is not used to
selling it.

1. What you told me (their words, verbatim where possible).
2. What I will measure, and how.
3. What you receive — including the instrumentation, which you keep either way.
4. What is excluded.
5. What I need from you, and by when.
6. Price, payment, dates.
7. What happens after: 2–3 build options will be priced in the findings; 50% of this fee credits
   against a build contracted within 30 days.

### 5.3 Core proposal *(produced from diagnostic findings — the key structural advantage)*

Because the diagnostic already established the problem, the quantified loss, the scope and the
client's own data, the core proposal is **evidence restated with a price on it**, not persuasion.

Structure: findings recap with the quantified loss → 2–3 bounded options (not one, not five) →
scope and exclusions per option → milestones and dates → client inputs with dates and a stated
consequence for delay → acceptance criteria → price and payment → what is explicitly not included.

**Always three options, priced as a ladder:** narrow/fast, recommended, comprehensive. This moves
the conversation from *whether* to *which*, and it produces information about the buyer's real
budget that a single-option proposal never yields.

**Never:** send a proposal without a scheduled walkthrough. An unaccompanied proposal is read by
whoever is most sceptical, in the least favourable order, and answered by silence.

### 5.4 SOW requirements

Every engagement, without exception: scope by deliverable · **explicit exclusions** · client inputs
with dates and delay consequences · milestones and acceptance criteria · revision allowance and the
change-order path · payment schedule · IP and licensing · data access and handling · confidentiality
· case-study and benchmark consent (`PROOF_STRATEGY.md` §7.1) · termination and kill-fee terms.

Template and jurisdiction-specific clauses require qualified review —
`GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §2.

## 6. Negotiation boundaries

| Dimension | Boundary |
|---|---|
| Price | **No discounts** (`PRICING_AND_ECONOMICS_MODEL.md` §7). Scope reduction only |
| Scope | Reducible by removing named deliverables; never by "we'll also throw in…" |
| Payment | Schedule is negotiable within reason; deposit is not. Never net-60 |
| Timeline | Compressible only by narrowing scope, never by absorbing the difference |
| Exclusivity | Never offered |
| Results-based pricing | Refused (`DNS-11`) |
| Free pilot | Refused (`DNS-13`); the pilot exception is §7.1 of the pricing model and is written, capped and paid |
| Free diagnostic | Refused, except where D5 path B has already falsified the paid model program-wide |
| IP | Client owns deliverables on full payment; the agency retains its methods, templates and tooling |
| Unlimited revisions | Refused. The allowance and the change-order path are in the SOW |

**The walk-away line, in one sentence:** if a buyer requires a prohibited term, the deal costs more
than it pays, and taking it teaches the next three buyers that the terms are negotiable.

## 7. Follow-up cadence

| Situation | Cadence | Stop |
|---|---|---|
| Post-conversation, no proposal yet | Day 2, day 7, day 14 | After 3 |
| Proposal sent | Day 2 (walkthrough), day 5, day 10, day 14 close-out | After close-out |
| Diagnostic delivered, core not decided | Day 3, day 10, day 21, day 30 (credit expiry) | After credit expiry |
| Lost — timing | Re-entry at the stated date | — |
| Lost — other | One value touch per quarter | Opt-out |

**The close-out message** ("I'll assume the timing isn't right and stop following up — tell me if
that's wrong") produces the highest response rate of any follow-up and, more importantly, produces
*reasons*. Reasons are the output the validation plan needs (`FIELD_VALIDATION_PLAN.md` H-04).

## 8. Loss-reason taxonomy

Mandatory on every lost opportunity. Free text is not acceptable — the taxonomy is what makes loss
data aggregatable, and aggregated loss data is the cheapest market research available.

| Code | Reason | What it implies |
|---|---|---|
| L-01 | No budget | Qualification or ICP failure |
| L-02 | Price too high, value understood | Pricing signal → `A-07`/`U-07` calibration |
| L-03 | Price too high, value not understood | Positioning failure, not pricing |
| L-04 | Chose a competitor | Record who and why — the only competitive intelligence available (`U-12`) |
| L-05 | Chose to do it internally | Common; often a deferred win |
| L-06 | Timing | → Nurture with a date |
| L-07 | No perceived problem | **D4 resonance failure — the most strategically important code** |
| L-08 | Could not reach the signer | Q3 failure |
| L-09 | Would not grant data access | `RF-8`; correct disqualification |
| L-10 | Trust — no sector references | Proof-ladder gap (`A-06`) |
| L-11 | Internal politics / blocker | Buying-committee failure |
| L-12 | Went silent | Record the last stage reached |
| L-13 | We disqualified them | Record which rule |

**Review cadence:** weekly during validation, monthly after. Three consecutive L-07s are a thesis
signal, not a sales problem, and must be escalated to `DECISION_TREE.md` D4.

## 9. CRM requirements

Requirements, not a vendor (`TOOLING_AUTOMATION_REQUIREMENTS.md`). The agency's own CRM is also a
P2 proof artifact (`PROOF_STRATEGY.md` §5) and its first internal dogfood of C-2.

**Objects:** Organisation · Contact (with committee role) · Opportunity · Activity · Proposal ·
Engagement.

**Required opportunity fields:** stage · segment · source (verbatim buyer answer) · signer named
(Y/N) · Q1–Q4 status · problem statement in buyer's words · offer type · value · probability band
(High/Medium/Low — **not a percentage**, which would be false precision) · next action + date ·
founder hours logged to date · loss code.

**Required automations:** stage-change timestamping; follow-up task generation; stale-opportunity
alert at 14 days without activity; weekly pipeline digest; unbilled-hours rollup per opportunity.

## 10. Sales metrics

Definitions in `AGENCY_SCORECARD.md` §3.

| Metric | Why | Threshold |
|---|---|---|
| Qualified conversations/week | The D3 gate input | ≥ 2 during validation |
| Conversation → qualified rate | Targeting quality | Diagnose below 40% |
| Qualified → diagnostic sold | H-01 / `A-09` | Base 20% |
| Diagnostic → core | `A-08` | Base 30%; T-10 at 3 consecutive failures |
| Core proposal win rate | Pricing signal | **>70% → raise price (T-3)**; <20% → diagnose (T-4) |
| Cycle length by stage | Cash planning | `A-10` |
| Unbilled sales hours per close | 28% yield swing | ≤ 20; T-7 above 40 |
| Loss-reason distribution | Strategy signal | L-07 cluster → D4 |

## 11. Handoff to delivery

An opportunity may not become an engagement without: signed SOW · deposit cleared · client inputs
scheduled with named owners · access request sent · kickoff booked · **baseline capture scheduled
for day 1** (`PROOF_STRATEGY.md` §10) · the discovery record transferred in full.

**The handoff exists even though it is founder-to-founder.** Writing it down is what makes it
delegable later, and what prevents the commitments made in the sales conversation from being lost
between the two roles the same person is playing.

## 12. Templates to build *(specifications, not final copy)*

| Template | Priority | Notes |
|---|---|---|
| Outreach sequence (4 touches) | P0 | Observation-first |
| Discovery guide | P0 | §4 structure, timed |
| Diagnostic proposal | P0 | ≤ 2 pages |
| Diagnostic SOW | P0 | Legal review required |
| Core proposal | P1 | Three options |
| Core SOW + MSA | P1 | Legal review required |
| Change order | P1 | — |
| Follow-up sequences | P1 | Including the close-out |
| Objection reference card | P2 | From `POSITIONING_ARCHITECTURE.md` §9 |
| Reference-call brief | P2 | For P6 |

**Copy rule:** all client-facing wording written before `DECISION_TREE.md` D4 is provisional and
must be marked as such. Real buyer language replaces it at D4.
