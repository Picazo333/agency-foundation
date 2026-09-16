---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - 03_ACCOUNT_RESEARCH_TEMPLATE.md
  - 05_TEARDOWN_TEMPLATE.md
  - ../../04-operations/delivery/DELIVERY_OS.md
  - ../../02-strategy/proof/PROOF_STRATEGY.md
---
# 04 — Teardown SOP

> **Instrument type:** production procedure for the L0 teardown.
> **Hard cap: 3 hours per account** (`DELIVERY_OS.md` §3). **Target: 2h20m.**
> **Hypotheses:** H-03 (does observation-first outreach earn conversations), X-01.
> **Offer reference:** L0 in `OFFER_ARCHITECTURE.md` §2 — free, asynchronous, bounded.

## 1. What a teardown is and is not

| Is | Is not |
|---|---|
| A short, specific, verifiable set of observations about surfaces a stranger can see | An audit |
| Evidence that you look carefully and say only what you can support | A performance assessment |
| A reason for someone to take a 25-minute call | A pitch |
| A gift that costs them nothing and obliges them to nothing | A lead magnet with a hook |

> The teardown's persuasive power comes entirely from **restraint**. Anyone can assert that a
> clinic is losing patients. Almost nobody sends three verifiable observations and openly says
> what they *cannot* tell from outside. That contrast is the whole mechanism.

## 2. Procedure (2h20m)

| # | Step | Time | Output |
|---:|---|---|---|
| 1 | Deep-tier research (`03_ACCOUNT_RESEARCH_TEMPLATE.md` §4) | 35 min | Classified observations |
| 2 | Send test enquiry, note timestamp | 5 min | Start of measurement |
| 3 | **Wait 24–48 h** (elapsed, not worked) | — | Response measurement |
| 4 | Record response behaviour; check +72 h follow-up | 10 min | Timing data |
| 5 | Select the **3 highest-value observations** | 15 min | Teardown spine |
| 6 | Record 5–8 min screen walkthrough, single take | 30 min | Video |
| 7 | Write the one-page summary from `05_TEARDOWN_TEMPLATE.md` | 25 min | Document |
| 8 | Self-check against §4 prohibitions | 10 min | Pass/fix |
| 9 | Send via `06_OUTREACH_SEQUENCE.md` touch 2; log in ledger | 10 min | Sent |

**Recording rules:** single take, no script-reading, no editing beyond trimming. A polished video
undermines the "I spent twenty minutes looking at this" framing that makes it credible. Show your
screen and your actual clicks.

## 3. Choosing the three observations

Pick for **verifiability and specificity**, not for severity.

| Prefer | Over |
|---|---|
| Something with a timestamp or a count | Something qualitative |
| Something they can reproduce in 30 seconds | Something requiring your tooling |
| Something inside their control | Something structural about their market |
| Something cross-location or inconsistent | A single cosmetic flaw |

**If you find nothing worth three observations, send nothing.** A weak teardown is worse than no
teardown: it spends your credibility and their attention at the same time. Record `teardown_status
= researched` and move on. Roughly 1 in 5 accounts should fail this test — if none ever do, your
standard is too low.

## 4. Prohibited content *(checked at step 8 — all must be absent)*

| # | Prohibited | Why |
|---|---|---|
| T-1 | Any claim of lost revenue, lost patients or lost conversions | Fabricated; you have no denominator. `EC-1`, `EC-2` |
| T-2 | Any conversion, close or no-show rate | Unobservable from outside |
| T-3 | Any statement about internal operational performance | Unobservable, and an accusation about people |
| T-4 | Any statement about customer behaviour you did not observe | Fabricated |
| T-5 | Implying you have analytics, CRM or booking-system access | False. You have a website and one enquiry |
| T-6 | Industry benchmarks or "typically clinics…" statistics | `PP-1`; no sourced benchmark exists until n≥5 |
| T-7 | Naming or criticising their current supplier | `PP-6`; creates the blocker directly |
| T-8 | Estimated financial impact of any kind | `EC-1` |
| T-9 | Undisclosed test enquiry | `AUD-07-04` |
| T-10 | Manufactured urgency | `PP-8` |
| T-11 | A pitch, a price, or a description of the diagnostic offer | Contaminates **H-10**. §6 |
| T-12 | Generalising n=1 into a pattern | "One enquiry" is one enquiry |

**Step-8 self-check — answer out loud:**
1. Could a stranger reproduce every factual line today?
2. Is every inference labelled as mine?
3. Have I stated at least one thing I **cannot** tell from outside?
4. Would I be comfortable if they forwarded this to their current agency?
5. Is the test enquiry disclosed?
6. Have I avoided all mention of what I sell?

Any "no" → fix before sending.

## 5. The mandatory limits paragraph

Every teardown contains this, near the top, in the operator's own words:

> "This is what's visible from outside: your public pages and one enquiry I sent on [date] to time
> the response. I can't see your booking data, your enquiry volume, or what any of this actually
> costs you — so I haven't guessed. Where I've drawn a conclusion, I've marked it as mine and it
> may be wrong."

This paragraph is not a disclaimer. It is the single most persuasive element in the document,
because it is the part no competitor includes.

## 6. Why the teardown must not pitch *(H-10 protection)*

H-10 tests whether buyers **volunteer** the revenue-leak problem before it is described to them.
A teardown that names the problem has described it. Every subsequent conversation with that account
is contaminated for the resonance gate.

| Rule | |
|---|---|
| The teardown describes **what happens**, never **what it costs** or **what fixes it** | — |
| It never uses the plan's framing language ("revenue leak", "gap between demand arriving and being served") | That is the thing being tested |
| It ends with a question, not an offer | See §7 |
| If the teardown named the problem anyway, the interview record must be marked `resonance_contaminated = Y` and **excluded from the H-10 denominator** | `10_PROBLEM_RESONANCE_LOG.md` §4 |

## 7. The close

The teardown ends with a genuine question, not a call to action:

> "Two things I couldn't tell from outside: [question 1] and [question 2]. If you've got 25 minutes
> I'd like to ask you about them — I'm mapping how groups your size handle this. Happy to send the
> video either way."

**Not:** "Let's discuss how I can help." **Not:** "Book a free consultation."

The ask is for a *research conversation*. It converts better and — more importantly here — it is
what keeps H-10 testable.

## 8. Publication and consent

Per `PROOF_STRATEGY.md` §6, binding:

| Rule | |
|---|---|
| A **named** teardown may be published only with written consent | No exceptions |
| An **anonymised** teardown must be genuinely unidentifiable | Test: could a competitor in that segment name them? |
| **Never publish a teardown of a business that declined to engage** | Reads as retaliation and will be recognised as such |
| Never frame a teardown as criticism of an incumbent supplier | `PP-6` |

## 9. Stop rule and the L0 economics check

L0 is unpaid labour that scales linearly with outreach.

| Trigger | Action |
|---|---|
| Any single teardown exceeds 3 hours | Stop it. Send what you have or nothing |
| **After 10 teardowns: conversation rate < 15%** | L0 is consuming capacity that should produce revenue. Reassess before producing an eleventh (`OFFER_ARCHITECTURE.md` §2, M-04) |
| Teardowns are displacing interview time | Interviews outrank teardowns. Teardowns exist to *produce* interviews |
