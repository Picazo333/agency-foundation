---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - 02_TARGET_ACCOUNT_LEDGER.md
  - 04_TEARDOWN_SOP.md
  - ../../02-strategy/icp/ICP_FRAMEWORK.md
---
# 03 — Account Research Template

> **Instrument type:** per-account research record. **Time: 10 min (light tier) or 35 min (deep tier).**
> **Feeds:** `02_TARGET_ACCOUNT_LEDGER.md` fields 11–15, and `05_TEARDOWN_TEMPLATE.md`.
> **Hypotheses:** H-03, H-07.

## 1. Research tiering *(this is a capacity rule, not a preference)*

Uniform deep research at 20 targets/week costs 12+ hours against an 8–10 hour budget
(`ACQUISITION_MARKETING_SYSTEM.md` CH-1, finding `AUD-02-02`). So:

| Tier | Volume/week | Time each | Gets |
|---|---|---|---|
| **Deep** | 6–8 highest-fit accounts | ~35 min | Full template + test enquiry + teardown |
| **Light** | 8–12 remaining | ~10 min | §3 only, no test enquiry, no teardown |

Deep tier is earned by ICP fit, not by how interesting the business looks.

## 2. The classification rule *(the core discipline of this kit)*

Every line you write is exactly one of three things. Label it. No exceptions.

| Label | Definition | Test |
|---|---|---|
| **OBSERVABLE** | Something you directly saw or measured from outside | Could a stranger reproduce it today and get the same result? |
| **INFERENCE** | Your reading of what an observable might mean | Is it clearly marked as *yours*, and would you accept being wrong? |
| **QUESTION TO VALIDATE** | What you will ask them to find out | Is it phrased as a genuine open question? |

> **You cannot observe a business's performance from its website.** You can observe its *surfaces*.
> A slow reply to one test enquiry is an observable about one enquiry, not a conversion rate,
> not lost revenue, and not evidence of poor management.

## 3. Light-tier research *(10 min)*

| # | Item | Record as |
|---|---|---|
| 1 | Business name, locations, specialties | OBSERVABLE |
| 2 | Approximate size band (site count, staff visible on site) | OBSERVABLE (state the source) |
| 3 | Enquiry channels present (form / WhatsApp / phone / IG / booking widget) | OBSERVABLE |
| 4 | Booking path: does one exist online? How many steps to reach it? | OBSERVABLE (count them) |
| 5 | Cross-location consistency: same channels on every location page? | OBSERVABLE |
| 6 | Visible tracking (analytics/pixel present in page source) | OBSERVABLE |
| 7 | Any dated trigger event (`ICP_FRAMEWORK.md` §6.4) | OBSERVABLE, **with a date** |
| 8 | ICP fit: meets `ICP_FRAMEWORK.md` §6.1 size band? Any §6.7 disqualifier visible? | Decision |
| 9 | Competitor signal: do they mention a named agency/supplier? | OBSERVABLE — feeds **H-07** |

**Light-tier exit:** promote to deep, keep on the list, or drop. If you drop, record the reason in
the ledger — dropped-account reasons are data about the segment definition.

## 4. Deep-tier research *(adds ~25 min)*

### 4.1 Test enquiry — rules are binding

Per `DELIVERY_OS.md` §3 and audit finding `AUD-07-04`:

| Rule | |
|---|---|
| Enquiry **only** | Never make a booking |
| Never occupy an appointment slot | Someone else needs it |
| **Never present a medical complaint or impersonate a patient** | Non-negotiable for healthcare targets |
| Use a neutral but real address you monitor | No fake identities |
| Ask a plain, answerable general question | e.g. availability and price range for an initial consultation |
| **Disclose it in the teardown itself** | "I sent a general enquiry on [date] to time the response" |
| One enquiry per account. Ever. | Repeating it is harassment |
| Log the exact timestamps | The measurement is the point |

If disclosing the test would embarrass you, the test was designed wrong.

### 4.2 Measurement record

| Measure | Value | Label |
|---|---|---|
| Enquiry sent (channel, exact timestamp) | | OBSERVABLE |
| First human reply (exact timestamp) | | OBSERVABLE |
| **Elapsed first-response time** | | OBSERVABLE |
| Was it automated or human? | | OBSERVABLE |
| Did the reply answer the question asked? | | OBSERVABLE |
| Any follow-up if I did not respond? (check at +72 h) | | OBSERVABLE |

**n = 1.** One enquiry on one day. It is an existence proof about a single interaction and nothing
more. Phrase it that way in the teardown, always.

### 4.3 Booking-path walk

Steps to book · required fields · mobile behaviour · dead ends · whether it works outside business
hours. All OBSERVABLE, all counted, none interpreted.

## 5. Per-account record

```markdown
## Account research — [ACCOUNT NAME]
account_id: A-___   tier: deep|light   date: ____   researcher: ____
segment: ____   sites: ____   ICP fit: pass|fail|unclear

### OBSERVABLE
- (each line reproducible by a stranger today)

### INFERENCE  (my reading — may be wrong)
- 

### QUESTIONS TO VALIDATE  (what I will actually ask)
1. 
2. 
3. 

### Trigger event (dated, or "none found")
- 

### Competitor signal  (H-07)
- 

### Disqualifiers visible?  (ICP_FRAMEWORK §6.7)
- 

### Decision
[ ] Deep tier + teardown   [ ] Light tier, keep   [ ] Drop — reason: ______
```

## 6. Prohibited — with the permitted alternative

| Prohibited | Why | Permitted instead |
|---|---|---|
| "They're losing ~30% of enquiries" | Invented; you have no denominator | "One test enquiry took 45.6 h for a first reply" |
| "Their conversion is poor" | Unobservable from outside | "The booking path takes 6 steps and asks for 9 fields" |
| "They're wasting ad spend" | You cannot see spend or return | "I can see a paid campaign running; I can't see what it returns — that's a question for them" |
| "Their team doesn't follow up" | An accusation about people | "I received no follow-up within 72 h of my enquiry" |
| "This is costing them USD X/month" | Fabricated economics | "If this pattern holds beyond my one test, it's worth measuring — that's what the diagnostic does" |
| "Based on industry benchmarks…" | `PP-1`; no sourced benchmark exists | Say nothing. You have no benchmark until n≥5 (`PROOF_STRATEGY.md` §8) |
| Naming or criticising their current agency | `PP-6`; creates the blocker | "I don't know who handles this for you — that's worth understanding" |

## 7. Stop rule

**35 minutes, hard cap, deep tier.** Going over means you are treating a target as a prospect
before they have shown any interest. Stop, log what you have, move to the next account.
