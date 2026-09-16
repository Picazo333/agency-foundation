---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - AGENCY_THESIS.md
  - EVIDENCE_AND_ASSUMPTIONS_REGISTER.md
---
# ICP Framework

> **Module 5 of the Agency Master Plan** (Issue #2 Phase 3). Produces a *selection procedure* and a
> ranked candidate set — not a chosen customer. The choice is made by `DECISION_TREE.md` D2/D3 on
> evidence, not by this document.

## 1. The selection principle that overrides the others

Conventional ICP scoring ranks segments by attractiveness: budget, pain, ROI, expansion. That
ordering assumes the supplier can reach whichever segment it selects. This program cannot make
that assumption: `E-09` (zero buyer contact), `A-06` (no references), `U-04` (network unknown).

> **Principle: reachability dominates attractiveness until the first three engagements are
> delivered.** An attractive segment you cannot get a meeting with produces zero learning.
> An average segment where you can hold eight real conversations in thirty days produces the
> evidence that makes every later decision cheaper.

This is why `DECISION_TREE.md` places the **access gate at Day 30, before the resonance and
monetisation gates**. It is the most consequential structural choice in this framework, and it
will look wrong to anyone scoring segments on a spreadsheet.

**Attractiveness reasserts itself at Day 120** (D8), when the program has proof and can choose
where to aim it.

## 2. Evaluation criteria

All fourteen criteria from Issue #2 Phase 3, grouped by what they actually govern. Bands:
`STRONG` / `MODERATE` / `WEAK` / `UNKNOWN`. No composite score is computed — see §4.

### Group A — Can we reach them? *(gates Day 30)*
| # | Criterion | Question |
|---|---|---|
| A1 | Access / distribution difficulty | Can a named list be built, and will those people answer? |
| A2 | Decision-maker clarity | Is there one person who can say yes, reachable directly? |
| A3 | Channel availability | Do associations, events, referral paths or intermediaries exist? |

### Group B — Do they have the problem, urgently? *(gates Day 45)*
| # | Criterion | Question |
|---|---|---|
| B1 | Pain urgency | Is it bleeding now, or is it a someday problem? |
| B2 | Trigger events | What observable event makes them start looking? |
| B3 | Current alternatives / DIY | What are they doing instead, and why is it failing? |

### Group C — Will they pay, and can they? *(gates Day 60)*
| # | Criterion | Question |
|---|---|---|
| C1 | Budget existence and size | Is there money, in which line item? |
| C2 | Sales-cycle length | Weeks or quarters? |
| C3 | ROI measurability | Can value be counted in a way *they* accept? |

### Group D — Can we serve them repeatably and profitably? *(gates Day 90–120)*
| # | Criterion | Question |
|---|---|---|
| D1 | Repeatability | Does the next client look like the last one? |
| D2 | Recurring potential | Is there an ongoing job to be done? |
| D3 | Expansion potential | More locations, lines, processes? |
| D4 | Churn / maintenance risk | What breaks the relationship? |
| D5 | Compliance / privacy burden | What data will we touch, and what does that trigger? |
| D6 | Proofability | Can the outcome be published? |

> **Deliberately absent:** "brand fit" and "founder interest." Per `E-08`, aesthetic affinity may
> not score a market. Founder interest is real and matters for persistence, but it is applied as a
> **tiebreaker between segments already equal on A–D**, and is recorded as such in §6.

## 3. Candidate longlist

Seeded from `E-19` (research-named segments), extended by reasoning about the thesis' structural
requirements (a countable demand-to-service pipeline with multiple handoffs).

| ID | Segment |
|---|---|
| S1 | Single-site dental / general clinics |
| S2 | **Multi-site specialty clinic groups (3–15 locations)** — dermatology, aesthetics, fertility, ophthalmology, dental groups |
| S3 | Diagnostic labs and imaging centres |
| S4 | Mid-market professional services firms (legal, accounting, architecture, engineering), 20–150 staff |
| S5 | B2B industrial / manufacturing SMBs with inside-sales or quoting functions |
| S6 | Boutique real-estate developers and brokerages |
| S7 | Established D2C / e-commerce brands with operational drag |
| S8 | Funded LATAM startups and scaleups |
| S9 | Other agencies (white-label) |
| S10 | Private education (schools, academies, training providers) |

## 4. Segment assessment

Bands are `INFERENCE` from structural reasoning unless marked otherwise. **None is `FACT`.**
`U-12` (competitive density) and `U-07` (WTP) are unresolved for every row.

| | A1 Access | A2 DM clarity | B1 Urgency | B3 Alternatives | C1 Budget | C2 Cycle | C3 ROI measurable | D1 Repeat | D2 Recurring | D3 Expansion | D5 Compliance | D6 Proofable |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **S1** Single-site clinics | `MODERATE` | `STRONG` | `MODERATE` | Marketing agencies | `WEAK` | `STRONG` (short) | `STRONG` | `STRONG` | `MODERATE` | `WEAK` | `MODERATE` | `MODERATE` |
| **S2** Multi-site clinic groups | `MODERATE` | `MODERATE` | `STRONG` | Internal staff, spreadsheets | `MODERATE` | `MODERATE` | `STRONG` | `STRONG` | `STRONG` | `STRONG` | `MODERATE`→`STRONG` | `MODERATE` |
| **S3** Labs / imaging | `WEAK` | `WEAK` | `MODERATE` | Vendor software | `MODERATE` | `WEAK` (long) | `MODERATE` | `MODERATE` | `MODERATE` | `MODERATE` | `STRONG` (bad) | `WEAK` |
| **S4** Professional services | `MODERATE` | `STRONG` | `MODERATE` | Referrals, do nothing | `MODERATE` | `MODERATE` | `WEAK` | `MODERATE` | `MODERATE` | `MODERATE` | `MODERATE` | `WEAK` |
| **S5** B2B industrial | `WEAK` | `MODERATE` | `MODERATE` | Email + spreadsheets | `STRONG` | `WEAK` (long) | `MODERATE` | `WEAK` | `MODERATE` | `MODERATE` | `WEAK` (low) | `WEAK` |
| **S6** Real estate | `MODERATE` | `STRONG` | `STRONG` | Portals, brokers | `MODERATE` | `STRONG` | `STRONG` | `MODERATE` | `MODERATE` | `MODERATE` | `WEAK` | `MODERATE` |
| **S7** D2C / e-commerce | `STRONG` | `STRONG` | `MODERATE` | Apps, agencies, in-house | `MODERATE` | `STRONG` | `STRONG` | `STRONG` | `STRONG` | `MODERATE` | `MODERATE` | `STRONG` |
| **S8** Funded startups | `MODERATE` | `STRONG` | `MODERATE` | In-house | `MODERATE` | `STRONG` | `MODERATE` | `WEAK` | `WEAK` | `WEAK` | `WEAK` | `STRONG` |
| **S9** Agencies (white-label) | `STRONG` | `STRONG` | `STRONG` | Other subcontractors | `WEAK` | `STRONG` | n/a | `STRONG` | `MODERATE` | `WEAK` | `WEAK` | **None** |
| **S10** Private education | `MODERATE` | `MODERATE` | `MODERATE` | Internal staff | `WEAK` | `WEAK` | `MODERATE` | `MODERATE` | `MODERATE` | `MODERATE` | `MODERATE` | `WEAK` |

### 4.1 Eliminations and why

| Segment | Outcome | Reason |
|---|---|---|
| **S9** Agencies | **Eliminated** | `D6` proofability is structurally zero — white-label work can never be shown or claimed. This is M7, already killed (`STRATEGY_RECONCILIATION.md` §3). Permitted only under the bounded runway exception |
| **S3** Labs / imaging | **Eliminated for entry** | Heaviest compliance burden (`D5`) combined with weakest access and longest cycles — the worst possible first customer for a supplier with no references. Revisit at year 2 |
| **S5** B2B industrial | **Deferred** | Highest budget in the set, but long cycles and low repeatability make it a poor *learning* segment. A 4-month sales cycle produces one data point per quarter. Correct segment for year 2, wrong for day 30 |
| **S8** Funded startups | **Deferred** | Excellent proofability, but they build in-house, churn fast, and have no expansion surface. Also: their budget is someone else's runway, which makes them fragile clients |
| **S10** Private education | **Deferred** | Budget weakness plus long, seasonal cycles |
| **S1** Single-site clinics | **Deferred in favour of S2** | Same domain, strictly worse economics: lower budget, no expansion surface, and the most agency-saturated inbox in SMB services. S2 is the same knowledge investment with a materially better return |

### 4.2 The three that advance

**S2 — Multi-site specialty clinic groups (3–15 locations)** — *recommended primary candidate*

The argument, stated as a chain rather than a score:

1. **The problem is operational, not promotional.** At 3+ locations, lead routing, intake
   response time, no-show handling and cross-location scheduling break in ways a single site never
   experiences. This is precisely the gap the thesis names (`AGENCY_THESIS.md` §1). `INFERENCE`.
2. **That framing escapes the saturated channel.** Every marketing agency in the market contacts
   clinics offering more patients. Almost nobody contacts them offering to fix what happens to the
   patients they already attract. A different message into a saturated inbox is a real access
   advantage. `INFERENCE`, tested by H-03.
3. **The outcome is countable in the buyer's own terms.** Bookings, show rate, response latency,
   cost per booked patient. `C3` is the strongest of any candidate and directly enables the proof
   engine (`P-1`).
4. **Expansion is structural.** Each additional location is a unit of the same sale, with zero
   acquisition cost. `D3 STRONG` is rare in SMB services.
5. **Benchmark data compounds fastest here.** Homogeneous operations across many businesses is
   exactly the condition under which "in 14 clinics like yours…" becomes the differentiator
   described in `AGENCY_THESIS.md` §4.2.

Risks, stated honestly:
- **`A2 MODERATE`, not strong.** The buying committee is real: clinical owner (authority, no time),
  administrator (operational pain, limited authority), marketing coordinator (often the contact,
  usually a blocker who feels threatened). `U-09`. Mitigated by a mandatory "who signs" gate
  (`SALES_SYSTEM.md` §3).
- **`D5` compliance escalates on contact with patient data.** `U-10`, `RF-7`. The scope boundary is
  hard: lead and appointment *metadata* only, never clinical records, until counsel reviews.
- **Saturation cuts both ways.** A different message helps; owner fatigue with agency outreach is
  still real.

**S7 — Established D2C / e-commerce brands with operational drag** — *recommended hedge candidate*

- Best access in the set (`A1 STRONG`): reachable online, publicly identifiable, active in
  communities, short path to the owner.
- Best proofability (`D6 STRONG`): everything is instrumented already, which directly de-risks
  `U-08`/`P-1` — for these buyers a baseline almost certainly exists.
- Weaker differentiation: this segment is served by a mature app and agency ecosystem, and buyers
  are sophisticated about pricing.
- **Strategic role:** S7 is the *fast-feedback* segment. It will teach the program whether the
  diagnostic instrument works at all, faster than S2 will, even if S2 is the better long-term home.

**S6 — Boutique real-estate developers / brokerages** — *reserve, rotation-1 candidate*

High urgency, high transaction value, countable outcomes, low compliance. Weaker repeatability and
a cyclical market. Held as the first rotation target at `DECISION_TREE.md` D3b.

## 5. Ranked candidate set

| Rank | Segment | Role | Effort at Day 0 |
|---|---|---|---|
| 1 | S2 Multi-site specialty clinic groups | Primary | 75% |
| 2 | S7 D2C / e-commerce with ops drag | Hedge (M9 tactic, 90 days only) | 25% |
| 3 | S6 Boutique real estate | Rotation 1 | 0% |
| 4 | S4 Professional services | Rotation 2 | 0% |
| — | S5, S8, S10 | Year-2 candidates | 0% |
| — | S1, S3, S9 | Excluded from entry | 0% |

> **Override clause (from `DECISION_TREE.md` D0):** if the founder's warm network contains ≥ 15
> reachable businesses in any single segment, that segment becomes primary regardless of this
> ranking. Fifteen warm doors beat a better-scoring segment behind a cold one. This ranking is
> desk reasoning; a real network is evidence.

## 6. Primary candidate profile — S2 in full

*All fields are `HYPOTHESIS` pending H-03/H-04/H-09 unless marked otherwise.*

### 6.1 Firmographics
| Field | Working definition |
|---|---|
| Type | Private specialty clinic group: dermatology, aesthetic medicine, fertility, ophthalmology, orthodontics/dental groups |
| Size | 3–15 locations; 15–120 staff |
| Revenue | Unknown; proxy is location count and appointment volume |
| Geography | Metro area consistent with `A-01`, pending `U-01` |
| Maturity | Has a PMS/EMR and some form of CRM or spreadsheet; has run paid acquisition at some point |
| Disqualifying size | 1–2 locations (insufficient operational complexity); >25 locations (has internal ops leadership and a procurement process) |

### 6.2 Buying committee
| Role | Interest | Authority | Risk to the deal |
|---|---|---|---|
| Owner / medical director | Growth, reputation, time | **Signs** | Has no time; delegates and then never reads |
| Operations / administrative director | Daily operational pain | Recommends strongly | The true champion — closest to the pain, most credible internally |
| Marketing coordinator or incumbent agency | Owns current lead generation | Can block | **Structural blocker.** A diagnostic that quantifies leakage implicitly audits their work. Must be framed as "we measure what happens after your leads arrive — we make your marketing look better," never as an audit of them |
| Front-desk / patient-coordination staff | Will use whatever is built | None | Adoption risk; ignoring them is the top cause of a technically successful, practically dead implementation |

**Qualification rule:** no proposal is issued until the signer is identified by name and has been
in at least one conversation. `SALES_SYSTEM.md` §3, gate Q3.

### 6.3 Jobs to be done and urgent pains
| JTBD | Observable symptom | Countable metric |
|---|---|---|
| Stop losing enquiries between arrival and booking | Messages across WhatsApp/IG/phone/web form with no single queue | Enquiry-to-booking rate; first-response latency |
| Reduce no-shows | Empty chairs on a full calendar | No-show %, revenue per available slot |
| Know which acquisition spend actually produced patients | "We spend on ads, we think it works" | Cost per booked patient, by source |
| Make locations behave consistently | One site performs, another does not, nobody knows why | Per-location conversion spread |
| Reactivate dormant patients | A large inactive list nobody contacts | Reactivation rate |
| Stop the owner being the bottleneck | Owner personally chasing operational issues | Owner hours on ops |

### 6.4 Trigger events *(these are the outbound timing signals)*
- Opening or acquiring a new location
- Hiring, or losing, an operations/administrative director
- Switching PMS/EMR or CRM
- A visible increase in ad spend with flat bookings
- A bad review cluster about responsiveness or scheduling
- A specialist hire whose calendar must be filled quickly
- New year / new budget cycle

### 6.5 Current alternatives
| Alternative | Why it underperforms |
|---|---|
| Marketing agency | Optimises lead volume; indifferent to what happens after |
| PMS/EMR vendor | Sells software; implementation and adoption are the customer's problem |
| Internal staff + spreadsheets | No measurement, no continuity, breaks with staff turnover |
| Freelance automation contractor | Builds the specific thing asked for; no diagnosis, no accountability for outcome |
| Do nothing | The most common and most underestimated competitor |

### 6.6 Commercial parameters
| Field | Value | Grade |
|---|---|---|
| Budget line | Marketing/growth, or owner discretionary | `INFERENCE` |
| Budget size | **UNKNOWN** | `U-07` — H-04 |
| Diagnostic price tolerance | **UNKNOWN** | H-01 |
| Sales cycle | 3–8 weeks, owner-availability-limited | `HYPOTHESIS` |
| Compliance | Personal data handling; clinical data explicitly out of scope (`RF-7`) | `U-10` |
| Recurring potential | `STRONG` — ongoing measurement and optimisation is a real job | `INFERENCE` |
| Expansion | Per-location rollout | `INFERENCE` |
| Churn risk | Staff turnover destroying adoption; owner attention loss; "we'll handle it internally now" | `INFERENCE` |

### 6.7 Qualification and disqualification

**Qualify in (all required):**
1. 3+ locations, or 2 locations with a third planned within 12 months.
2. An identified, reachable signer.
3. Willingness to grant read access to booking/enquiry data within 5 business days.
4. A named commercial problem the buyer stated before being pitched (`DECISION_TREE.md` D4 logic).
5. Budget authority confirmed, even if the amount is not.

**Disqualify out (any one):**
1. No measurement access and no willingness to instrument → violates `RF-8`. Without a baseline
   there is no proof, no defensible renewal and no case study.
2. Wants clinical-record integration in the first engagement → `RF-7` until counsel clears it.
3. Wants ad management as the primary deliverable → `RF-2`.
4. Under contract with an incumbent agency whose scope this would duplicate, with no intention to
   change → political cost exceeds deal value.
5. Price-shopping against a named cheaper competitor at first contact → `RF-3`/`D-4` dynamics.
6. Signer will not join any call.
7. Expects payment on results / revenue share → uncontrollable variables, uncapped exposure.

## 7. How the ICP decision actually gets made

1. **Day 0–3 (D0):** founder answers `U-04`. If a warm cluster exists, the override clause applies.
2. **Day 7 (D2):** confirm primary (75%) + hedge (25%).
3. **Day 30 (D3):** access gate. Swap, rotate or proceed on conversation counts, not on opinion.
4. **Day 45 (D4):** resonance gate. Record the buyers' *own words*; they replace all research VoC (`E-05`).
5. **Day 60 (D5):** monetisation gate. Money is the only evidence that counts here.
6. **Day 120 (D8):** with three delivered engagements, re-run §4 with real data and **re-rank**.
   The ICP is expected to change at this point. A framework that survives contact unchanged was
   probably not testing anything.

## 8. What this framework refuses to do

- **No composite numeric score.** Weighting fourteen ungraded criteria would produce a decisive
  number from undecidable inputs — exactly the false precision `E-04` prohibits.
- **No single ICP commitment at Day 0.** Committing before the access gate converts an untested
  assumption into a sunk cost.
- **No ICP chosen for aesthetic compatibility.** `E-08`. If S2 wins and its buyers respond badly to
  the founder's visual direction, that is Module 16's problem to solve, not a reason to pick a
  prettier customer.
