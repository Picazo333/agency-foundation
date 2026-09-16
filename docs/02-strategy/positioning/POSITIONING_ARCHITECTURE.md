---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - AGENCY_THESIS.md
  - ICP_FRAMEWORK.md
---
# Positioning and Messaging Architecture

> **Module 6 of the Agency Master Plan** (Issue #2 Phase 4). Defines what is claimed, to whom, with
> what evidence, and what may not be said. This document produces **strategic messaging
> requirements** for the Brand workstream. It does not write brand voice and does not select a name
> (`OWNERSHIP_MATRIX.md`, `STOP_RULE.md`).

## 1. The positioning problem in one paragraph

The agency has no reputation (`A-06`), no case studies (`E-09`), a category that does not yet have
a name (`AGENCY_THESIS.md` §2), and a founder aesthetic that may not match its most reachable
buyers (`E-24`). Positioning must therefore do an unusual amount of work: it has to make an unknown
supplier credible, an unnamed category budgetable, and a distinctive style non-threatening — all in
the first thirty seconds of a cold contact.

The answer is not a better tagline. It is a **claim discipline**: say less, but say only things
that can be verified on the spot.

## 2. Positioning alternatives considered

| ID | Positioning | Statement | Strength | Fatal weakness |
|---|---|---|---|---|
| POS-1 | **Outcome / leak-repair** | "We find where you're losing customers you already paid for, then fix it" | Concrete, countable, ownable, escapes the marketing price war | Requires the loss to be real and measurable (`P-1`) |
| POS-2 | Technology-led | "AI and automation for clinics" | Fast comprehension among early adopters | `RF-1`, `E-17`; names our tools, not their problem |
| POS-3 | Vertical-generalist | "The digital partner for clinic groups" | Easy to say; broad | Indistinguishable from every marketing agency in the segment |
| POS-4 | Craft-led | "Distinctive digital work, made properly" | Best fit for `E-07`; strong differentiation | Buyers in S2/S7 do not buy craft as a primary criterion (`D-3`); M5's problem |
| POS-5 | Efficiency / cost | "Do more with fewer people" | Resonates in cost-pressured segments | Invites price comparison; anchors low; a solo operator loses that fight |

**Recommended: POS-1**, with POS-4 present as *texture* rather than as the claim — see §5.

**Rationale:** POS-1 is the only option whose truth can be demonstrated inside the entry offer. The
diagnostic *is* the proof of the positioning. Everything else requires the buyer to take the
supplier's word, which is exactly what a supplier with no reputation cannot ask for.

**Falsification:** POS-1 fails if buyers do not recognise the loss as theirs (`DECISION_TREE.md`
D4, H-10). If D4 fails, positioning is not the fix — the thesis is wrong.

## 3. Message source discipline

**Binding rule:** no research-derived voice-of-customer language may appear in any buyer-facing
asset. `E-05` establishes that the Spark VoC corpus is synthetic unless individually traceable, and
none of it is traceable because of `E-02`.

Until `DECISION_TREE.md` D4 produces real buyer language:

| Source | Status | Allowed use |
|---|---|---|
| Research VoC (Spark) | Synthetic | Hypothesis generation only. **Never** in copy |
| This plan's phrasing | Planning language | Internal only |
| Interview transcripts (D4 onward) | Real | **The only permitted source of buyer-facing language** |

**Mechanism:** `docs/06-validation/interviews/` accumulates a verbatim phrase log. At D4, the five
most frequently volunteered phrasings become the message corpus, and §4's placeholders are replaced
with them. All copy written before D4 is explicitly provisional and marked as such.

This single rule is the difference between messaging that sounds like an agency and messaging that
sounds like the buyer's own morning.

## 4. Message hierarchy

Provisional pending §3. Written for S2; the structure transfers, the wording does not.

### Level 1 — Opening claim (cold, ≤ 12 seconds)
> "Most clinic groups lose a quarter of their enquiries somewhere between the message arriving and
> the appointment being booked. Nobody's watching that gap. We measure it, and then we fix it."

Note: *"a quarter"* is a placeholder that **may not ship**. Until benchmark data exists, the cold
line must be quantifier-free: *"lose enquiries somewhere between…"*. Enforced in §8, prohibited
pattern PP-1.

### Level 2 — Method (the differentiator, ~30 seconds)
> "We don't quote a project before we know what's broken. We start with a two-week diagnostic:
> we instrument your enquiry-to-booking path, measure what's actually happening across your
> locations, and give you a numbered list of what each gap is costing. Then you decide whether to
> have us fix any of it. The measurement is yours either way."

Three things this does: makes a small ask, transfers a concrete asset regardless of outcome, and
positions the fee as the buyer's risk reduction rather than the supplier's revenue.

### Level 3 — Proof (`PROOF_STRATEGY.md`)
Ordered by current availability: method transparency and the governance artifact (`E-12`, available
today) → self-applied instrumentation → anonymised teardowns → pilot results → named case studies →
benchmark comparisons.

### Level 4 — Differentiation
> "We measure before we build, we hand over the measurement, and we keep measuring after launch.
> Most suppliers deliver a thing. We deliver a number that moved, and we show our work."

### Level 5 — Risk reversal
> "Fixed price, written scope, written exclusions. The diagnostic stands alone — if you never hire
> us to build anything, you keep the instrumentation and the findings."

## 5. The relationship between category and craft

The most-likely-to-be-misapplied section of this plan, so it is stated as a rule:

> **The category is bought. The craft is experienced.**

| Layer | Governed by | Visible when |
|---|---|---|
| **What we sell** (category, claim, first sentence) | This document; must be plain, buyer-language, budgetable | Cold contact, proposal, homepage above the fold |
| **How it feels** (typography, editorial rigor, annotation density, information design) | Brand workstream, informed by `E-07` | Diagnostic report, proposal, dashboard, deliverables — after interest exists |

`E-07`'s aesthetic register — illuminated/editorial/anatomical/annotation-dense — is an *unusually
good fit for a diagnostic report* and an *unusually bad fit for a cold email to a clinic owner*.
The architecture exploits exactly that: plain at the door, distinctive at the table.

This is also the honest resolution of `E-24`, and the primary input to Module 16.
`BRAND_BUSINESS_INTERFACE.md` §4 carries it as constraint `BC-01`.

## 6. Value propositions by audience

| Audience | Their actual concern | Message | Proof they will ask for |
|---|---|---|---|
| Owner / medical director | Growth without more of their time | "More of the demand you already pay for turns into booked revenue, without you managing it" | A number, and someone else's name |
| Operations director | Daily chaos; being blamed for it | "One queue, measured response times, and a report that shows what you fixed" | A walkthrough of the actual system |
| Marketing coordinator / incumbent agency | Being audited or replaced | "We measure what happens *after* your leads arrive. Your numbers get better, not questioned" | Explicit scope boundaries in writing |
| Front-desk staff | More work, new software | "Fewer places to check, not more" | A demo and training |
| E-commerce owner (S7) | Margin and operational drag | "Your funnel is instrumented; your operations aren't. We close that gap" | Before/after on a named metric |

## 7. AI in the message — the rule

Derived from the M2 kill (`STRATEGY_RECONCILIATION.md` §3) and `RF-1`.

| Context | AI's place |
|---|---|
| Category, tagline, first sentence, cold outreach | **Absent** |
| Website hero | **Absent** |
| Proposal "how we work" section | Present, factual, one paragraph |
| Delivery conversations | Present; how speed and price are achievable |
| Case studies | Present only where it changed the outcome |
| Pricing justification | **Never** — never explain a price by naming the tools |

Positive form when asked directly: *"Yes, heavily. It's how one team delivers in four weeks what
normally takes twelve. It's how we do it, not what you're buying."*

**Disclosure obligation:** if AI systems will process client or customer data, this must be
disclosed in the proposal and covered contractually — see
`GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §5. Non-negotiable, regardless of positioning convenience.

**The exception clause:** if validation shows that a specific segment pays a *premium* for
explicitly AI-labelled work, `RF-1` is revisited by ADR rather than quietly ignored. `U-07`, H-11.

## 8. Claim discipline

### 8.1 Claim tiers

| Tier | Requirement | Example |
|---|---|---|
| **T0 — Safe now** | Verifiable on the spot, no history required | "Fixed price with written exclusions." "You keep the instrumentation." "We publish our method." |
| **T1 — After first delivery** | One completed engagement with a captured baseline | "In our first clinic engagement, first-response time went from X to Y over Z weeks." |
| **T2 — After 3+ engagements** | Multiple captured outcomes | "Across three clinic groups, median enquiry-to-booking improved by…" |
| **T3 — After 10+ engagements** | A real dataset | "In 14 clinics like yours, the median is…" — the `AGENCY_THESIS.md` §4.2 differentiator |
| **Never** | — | Guarantees, projected ROI presented as expectation, industry averages the agency did not measure |

### 8.2 The outcome-claim rule
> No percentage without its **denominator**, its **time window**, and its **attribution caveat**.

"Bookings up 32%" is prohibited. "Enquiry-to-booking rose from 41% to 54% over eight weeks
(n=1,180 enquiries), alongside an unchanged ad budget; other factors were not controlled" is
permitted. This is slower, less impressive, and the only version that survives a sophisticated
buyer — and the only one compatible with `RF-5`.

### 8.3 Prohibited patterns

| ID | Pattern | Why |
|---|---|---|
| PP-1 | Unsourced statistics ("70% of clinics…") | `E-04`; the first credibility failure a knowledgeable buyer will catch |
| PP-2 | "AI-powered" as a value claim | `RF-1` |
| PP-3 | "Digital transformation", "growth engine", "end-to-end solutions", "we're not an agency, we're a partner" | Budget-free abstractions; procurement discounts them automatically |
| PP-4 | Implied client roster ("trusted by leading clinics") before named clients exist | Misrepresentation; unrecoverable if caught |
| PP-5 | Guaranteed outcomes | Uncontrollable variables; also `RF-9` |
| PP-6 | Competitor disparagement, including implicit audits of the incumbent agency | Creates the §6 blocker |
| PP-7 | Stock imagery of diverse people pointing at screens | Signals membership in the category being escaped |
| PP-8 | Fabricated urgency ("only 2 slots left") | Destroys the one asset the agency has: that its numbers are real |

## 9. Objections and rebuttals

| Objection | What is actually being said | Response | Do not |
|---|---|---|---|
| "We already have an agency" | *Is this a threat to a working relationship?* | "Good — they generate demand. We measure what happens to it after it arrives. Different scope, and it usually makes their numbers look better." | Criticise them |
| "Why pay for a diagnosis?" | *Everyone else audits for free.* | "Because a free audit is a sales pitch with a chart. We instrument your actual data and hand you the measurement whether or not you hire us. If you do hire us within 30 days, half the fee comes off the build." | Cave and offer it free |
| "You have no clients in our sector" | *Can I trust you?* | "Correct — you'd be the first clinic group. That's why the first step is small and produces something you keep. Here's the method in full, and here's what I've measured in my own systems." | Overclaim, imply experience |
| "Can you guarantee results?" | *Who carries the risk?* | "No. I can guarantee the measurement, the scope, the price and the timeline. If anyone guarantees the outcome, ask them what happens when it doesn't happen." | Guarantee anything (`PP-5`) |
| "Too expensive" | Usually: *value unclear*, sometimes: *budget absent* | Re-anchor on the quantified loss from the diagnostic; if genuinely absent, reduce scope, never price (`SALES_SYSTEM.md` §6) | Discount |
| "We'll do it internally" | *Feels like something we should own.* | "Often the right call. The diagnostic tells you what to build; some clients take it in-house. If you want it done in six weeks instead of six months, that's what we're for." | Argue |
| "Is this AI stuff?" | Curiosity or scepticism | "AI is how it gets built fast. What you're buying is a measured improvement to a specific number." | Lead with AI |
| "Send me a proposal" (early) | Usually a soft no | "I'll send something short, but I can't price a fix before measuring what's broken. Can we get 25 minutes with whoever signs?" | Send a speculative proposal (`SALES_SYSTEM.md` §5) |

## 10. Proof hierarchy in messaging

Order of persuasive power for *this* supplier, strongest first — note that #1 and #2 require no
history and are available today:

1. **A number from their own business**, produced by the diagnostic. Unbeatable, because it is theirs.
2. **Method transparency** — the published diagnostic method and the governance system (`E-12`).
   Rare enough in SMB services to function as proof of seriousness by itself.
3. **Self-applied evidence** — the agency's own instrumented operation.
4. **Anonymised teardowns** of comparable businesses.
5. **Named case studies** (T1+).
6. **Benchmark comparisons** (T3).
7. **Testimonials** — weakest, because everyone has them.

**Implication for the website:** the homepage's primary job is not to describe services. It is to
make #2 and #3 visible fast. Carried into `WEB_BUSINESS_REQUIREMENTS.md` §4.

## 11. Requirements handed to the Brand workstream

Not brand decisions — constraints the eventual brand must satisfy. Full set in
`BRAND_BUSINESS_INTERFACE.md`.

| ID | Requirement |
|---|---|
| MR-1 | Must carry a plain-language descriptor *and* a category label without breaking (§2 CAT-5 and CAT-1/2 both live) |
| MR-2 | Must read as *rigorous and measured* before it reads as *creative*, in buyer-facing surfaces |
| MR-3 | Must present dense information — tables, annotations, numbers — as a first-class citizen, not an afterthought. The diagnostic report is the flagship artifact |
| MR-4 | Must not signal "AI company" (`RF-1`, and the entire `E-07` anti-profile) |
| MR-5 | Must survive translation between ES and EN without losing meaning (`E-16`) |
| MR-6 | Must not require the buyer to appreciate the aesthetic in order to trust the claim (§5) |
| MR-7 | Must accommodate a 30-page evidence-heavy PDF and a 12-second cold pitch with equal credibility |

## 12. Open positioning questions

| ID | Question | Resolved by |
|---|---|---|
| PQ-1 | Which category label tests best, and does it differ ES vs EN? | H-11 |
| PQ-2 | Does the paid-diagnostic frame read as premium or as nickel-and-diming? | H-01 |
| PQ-3 | Does the incumbent-agency framing actually neutralise the blocker? | H-03 field notes |
| PQ-4 | Does distinctive visual work raise or lower trust in this segment? | H-08, Gate 1 |
| PQ-5 | Is there an existing local competitor already in this position? | H-07, `U-12` |
