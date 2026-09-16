---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - ICP_FRAMEWORK.md
  - POSITIONING_ARCHITECTURE.md
  - PROOF_STRATEGY.md
---
# Acquisition and Demand-Generation System

> **Module 10 of the Agency Master Plan** (Issue #2 Phase 8). Channel portfolio, sequencing,
> prerequisites and stop/continue criteria. Governed by one constraint the conventional channel
> plan ignores: **the program has 90 days to produce evidence, and most marketing channels cannot
> produce evidence in 90 days.**

## 1. The selection rule

| Channel class | Time to first evidence | Verdict for days 0–90 |
|---|---|---|
| Outbound (direct, targeted) | Days | **Primary** |
| Warm network / referral | Days | **Primary, if `U-04` permits** |
| Partnerships / intermediaries | Weeks | **Secondary — highest long-term leverage** |
| Communities and events | Weeks | Secondary |
| Founder-led content | 3–9 months | **Build, do not depend on** |
| SEO | 6–18 months | Deferred |
| Paid acquisition | Days to spend, months to learn | **Prohibited until D5** |

> **Rule:** in the first 90 days, a channel is chosen for **speed of learning**, not for cost per
> acquisition. Outbound is expensive per conversation and unbeatable per unit of information.
> Content is cheap per impression and produces no information at all inside the window.

This inverts the usual advice to "build an audience." Building an audience is correct for a
business that knows what it sells. This one does not yet (`DECISION_TREE.md` D4, D5).

## 2. Channel portfolio

### CH-1 — Targeted outbound *(primary, days 0–90)*

| Field | Specification |
|---|---|
| Role | Produce the 8 qualified conversations that pass the D3 access gate |
| Assumption | S2 owners/administrators will respond to a specific, non-generic observation about their own business (`HYPOTHESIS`, H-03) |
| Prerequisites | Named target list (40–60 businesses); teardown template (P3); a specific observation per target; a booking link |
| Mechanism | **Observation-first, not offer-first.** Every contact leads with something measured about *their* business — response latency from an actual test enquiry, a broken booking path, an inconsistency between two locations. No capability pitch, no company introduction |
| Sequence | Touch 1: the observation, one paragraph, one question. Touch 2 (+4 days): short teardown video. Touch 3 (+7 days): a relevant pattern from another teardown. Touch 4 (+14 days): explicit close-out — "should I stop?" |
| Volume | 15–20 new targets/week, 4 touches each |
| **Research tiering** | Deep observation (test enquiry + booking-path walk, ~35 min) for **6–8 targets/week**; light observation (visible surfaces only, ~10 min) for the remaining 8–12. `AUD-02-02`: uniform deep research at 20 targets/week would cost 12+ hours and does not fit the budget below. Deep research is reserved for the highest-fit targets |
| Effort | 8–10 h/week |
| Measurement | Reply rate, conversation rate, qualified-conversation rate (`AGENCY_SCORECARD.md` M-01…M-03) |
| **Stop/continue** | Reply rate < 8% after 60 contacts → the message is wrong, not the channel: rewrite the observation format before adding volume. Qualified conversations < 4 by day 30 → `DECISION_TREE.md` D3b |
| Compliance | Business-to-business contact only; honour opt-outs immediately; no scraped personal contact data; identify yourself and your purpose in the first message. See `GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §6 |

**Why touch 4 exists:** an explicit "should I stop?" produces a higher response rate than any
follow-up, and — more valuable at this stage — it produces *reasons*, which are exactly the
information the validation plan needs.

### CH-2 — Warm network and referrals *(primary if available)*

| Field | Specification |
|---|---|
| Role | Fastest possible path to qualified conversations; highest conversion |
| Assumption | `U-04` — completely unknown until D0 |
| Prerequisites | An honest inventory of every professional contact, mapped to segments |
| Mechanism | Ask for **a conversation for research**, not for a sale or an introduction to a buyer. "I'm mapping how clinic groups handle enquiries — can I ask you 20 minutes of questions?" is answered far more often than a pitch, and it produces better data |
| Referral engineering | After every delivered engagement, and at every quarterly review, one specific ask: *"Who else has this problem?"* — named, not general |
| Effort | 3–4 h/week |
| Measurement | Conversations sourced; referral rate per delivered client (M-15) |
| Stop/continue | Never stops. If `U-04` reveals 15+ reachable businesses in one segment, this becomes the dominant channel and the ICP ranking is overridden (`ICP_FRAMEWORK.md` §5) |

### CH-3 — Partnerships and intermediaries *(secondary, highest long-term leverage)*

| Field | Specification |
|---|---|
| Role | Borrowed trust and borrowed distribution — the standard answer to a pure access problem |
| Partner types | PMS/EMR and clinic-software vendors (their implementation gap is our offer, and their churn driver); accountants and fractional CFOs serving clinic groups; practice-management consultants; equipment suppliers; sector associations; non-competing agencies (brand/creative shops with no ops capability) |
| Assumption | Intermediaries have the relationships and lack the capability (`HYPOTHESIS`) |
| Prerequisites | P0 method document; one delivered engagement is strongly preferred before approaching software vendors |
| Mechanism | Lead with what they lack: "your customers churn when implementation stalls; I fix implementation." Offer a co-delivered pilot before discussing referral economics |
| Economics | Referral fee or margin share — **define in writing before the first referral**, never after |
| Effort | 2–3 h/week from week 4 |
| Measurement | Partners engaged, referrals received, conversion |
| Stop/continue | Zero referrals from an active partner after 90 days → the partnership is nominal; stop investing and say so |
| Escalation | If CH-1 and CH-2 both fail at D3b twice, CH-3 becomes the primary strategy (`DECISION_TREE.md` pivot P-C) |

### CH-4 — Communities and events *(secondary)*

Sector associations, practice-management groups, local business networks, online communities where
clinic administrators actually talk. Contribute answers, not promotion. Effort 2 h/week.
Stop/continue: zero conversations after 8 weeks of genuine participation → wrong community.

### CH-5 — Founder-led content *(build, do not depend on)*

| Field | Specification |
|---|---|
| Role | Compounding credibility. **Will not produce revenue inside 90 days** — stated so it is not mistaken for a plan |
| Prerequisites | P0, P3 teardowns |
| Mechanism | Publish the teardown output that already exists. Zero marginal cost: the teardowns are produced for CH-1 regardless |
| Cadence | 1–2 posts/week, one long-form piece/month |
| Format | Anonymised teardowns, the method document, "what I measured this month", the benchmark data once n≥5 |
| Effort | 2–3 h/week, mostly repackaging |
| Measurement | Inbound conversations attributed (M-16) — not followers, not impressions |
| Stop/continue | Reassess at month 6, not before. Judging content at month 2 and stopping is the most common and most expensive content mistake |

**The discipline:** content is a *byproduct* of outbound work here, never a substitute for it.
The moment content production starts displacing outreach hours, it has become procrastination with
a publishing schedule.

### CH-6 — Website and SEO *(deferred)*

The site is needed as a **credibility surface** (does this person exist and look serious?), not as
an acquisition channel, until after D5. Minimum viable version in week 3: what we do, for whom, the
method, the founder, a booking link. Full build is gated in `WEB_BUSINESS_REQUIREMENTS.md` §9.
SEO investment deferred to month 6+; it cannot pay back inside the validation window.

### CH-7 — Paid acquisition *(prohibited until D5)*

**Prohibited** until the monetisation gate passes. Paying to amplify an unvalidated message buys
expensive silence, and the resulting data confounds message failure with targeting failure.

After D5, permitted only as a **retargeting and search-intent** layer — capturing existing demand,
not creating it — with a defined test budget, a single hypothesis, and a stop criterion set before
spending. Cold prospecting spend is not justified at this scale (`AUD-02` finding).

### CH-8 — Lead magnets and tools

The teardown (L0) *is* the lead magnet, and it is better than a downloadable PDF because it is
specific to the recipient. A second-order option after D5: a self-serve benchmark tool
("how does your response time compare?"), which doubles as a P7 data-collection instrument.
Not before D5.

## 3. Sequencing

| Phase | Weeks | Active | Hours/week | Goal |
|---|---|---|---|---|
| Foundation | 1–2 | Target list, P0 method, teardown template, minimum site, CH-2 inventory | 15 | Instruments ready |
| Access | 3–6 | CH-1 heavy, CH-2, CH-4 light | 14 | 8 qualified conversations (D3) |
| Resonance | 7–8 | CH-1, CH-2, CH-3 opens | 12 | Problem confirmed (D4) |
| Monetisation | 9–12 | CH-1, CH-2, CH-3, CH-5 begins | 10 | 2 paid diagnostics (D5) |
| Delivery | 13–20 | CH-1 reduced, CH-5, CH-3 | 6 | Pipeline survives delivery |
| Compounding | 21+ | All; CH-7 permitted; CH-6 invested | 8–10 | Repeatable flow |

**The week 13–20 row is the one that fails in practice.** Sales hours drop to 6/week during
delivery (`PRICING_AND_ECONOMICS_MODEL.md` §2). The mitigation is structural: L0 teardowns are
3 hours and can be produced during a build; a core proposal cannot. Protect the teardown cadence
above everything else during delivery periods.

## 4. Channel economics

No CAC figures are given, because none can be defended (`E-22`). What can be stated is the
**cost structure** of each channel in the only currency that is actually scarce:

| Channel | Founder hours per qualified conversation (`INFERRED RANGE`) | Cash cost | Scalability |
|---|---:|---|---|
| CH-1 Outbound | 2–4 h | Near zero | Linear with hours — does not scale past the founder |
| CH-2 Warm/referral | 0.5–1 h | Zero | Limited by network size, then by delivered clients |
| CH-3 Partnerships | 4–8 h initially, then <1 h | Margin share | **Superlinear** — one partner produces repeated flow |
| CH-4 Communities | 3–6 h | Zero | Sublinear |
| CH-5 Content | Unknown early; falls sharply later | Zero | **Superlinear** — the only channel that compounds without the founder present |
| CH-7 Paid | <1 h | Real cash | Scales with budget; no compounding |

**Strategic reading:** CH-1 buys evidence now and never scales. CH-3 and CH-5 scale but pay back
late. The correct posture is to run CH-1 hard for evidence while seeding CH-3 and CH-5 at low cost
— and to plan explicitly for CH-1's ceiling rather than being surprised by it at month 6.

## 5. Content and asset requirements

| Asset | Channel | Priority | Owner | Blocked by |
|---|---|---|---|---|
| Target list (40–60, S2) | CH-1 | P0 | Founder | `U-01` geography |
| Observation research template | CH-1 | P0 | Founder | — |
| Teardown template + recording setup | CH-1, CH-5 | P0 | Founder | — |
| Method document (P0) | All | P0 | Founder | — |
| Minimum viable site | All | P0 | Founder | Nothing — must not wait for Brand V1 |
| Booking link + calendar | All | P0 | Founder | — |
| Outreach sequence templates | CH-1 | P0 | Founder | — |
| Redacted sample diagnostic report | CH-1, CH-3 | P1 | Founder | First L1 delivery, or a constructed sample clearly labelled as illustrative |
| Partner one-pager | CH-3 | P1 | Founder | — |
| Case study template | CH-5 | P2 | Founder | — |
| Benchmark tool | CH-8 | P3 | Founder | D5 + n≥5 |

**Explicit non-blocker:** none of these requires Brand V1. Waiting for final identity before making
market contact would be the most expensive possible instance of the over-planning failure mode
(`R-14`, `RT-01`). A plain, well-typeset, fast site with real content outperforms a beautiful site
that ships three months later.

## 6. Measurement

Per channel, weekly: contacts, replies, conversations, qualified conversations, opportunities,
diagnostics sold, cores sold, founder hours invested. Definitions in `AGENCY_SCORECARD.md` §3.

**Attribution rule:** ask every buyer how they came to be talking to you, and record their answer
verbatim. Multi-touch attribution at this volume is noise; a one-line human answer is signal.

## 7. Stop/continue summary

| Channel | Continue if | Stop / change if |
|---|---|---|
| CH-1 Outbound | ≥ 8 qualified conversations by day 30 | < 4 by day 30 → rewrite message, then rotate segment |
| CH-2 Warm | Any conversations produced | Network exhausted (not a failure — a fact) |
| CH-3 Partnerships | ≥ 1 referral per active partner per quarter | Zero after 90 days → deprioritise that partner |
| CH-4 Communities | Conversations emerging | Zero after 8 weeks of real participation |
| CH-5 Content | Reassess at month 6 | Only if it displaces outreach hours |
| CH-6 SEO | After D5 | — |
| CH-7 Paid | Only after D5, with a pre-set stop criterion | Any spend before D5 |
