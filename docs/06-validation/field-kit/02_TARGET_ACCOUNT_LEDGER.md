---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - ../FIELD_VALIDATION_PLAN.md
  - ../../02-strategy/icp/ICP_FRAMEWORK.md
  - ../../02-strategy/sales/SALES_SYSTEM.md
---
# 02 — Target Account Ledger

> **Instrument type:** operational ledger for 40–60 target accounts.
> **Machine-readable template:** `data/target_account_ledger.csv` (headers only — open it in a
> spreadsheet and work there; this file is the field dictionary and the rules).
> **Hypotheses:** H-03 (access), H-07 (competitive position), H-03b (signer reachability).
> **Gate:** D3.

## 1. Privacy rule — read before entering anything

> **Do not commit personal contact details to this repository.** No email addresses, no phone
> numbers, no personal names of individuals who have not consented.

The repository is the *evidence* system, not the *contact* system. Keep contact details in the CRM
or a local file that is git-ignored. In the ledger, identify people by **role + initials**
(`Ops Dir / M.R.`). Business names are fine — they are public. This follows `DR-2` (data
minimisation) and `DR-6` (recorded datasets) in `GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §4.1.

If you would be uncomfortable with the named person reading the row, do not write the row that way.

## 2. Field dictionary

| # | Field | Type | Rule |
|---:|---|---|---|
| 1 | `account_id` | `A-001`… | Stable. Never reused |
| 2 | `account` | text | Business name (public info) |
| 3 | `segment` | `S2` / `S7` / `S6` / `S4` / `other` | Per `ICP_FRAMEWORK.md` §3 |
| 4 | `tier` | `primary` / `hedge` | Must match the D2 allocation (~75/25) |
| 5 | `geography` | text | City / metro |
| 6 | `website` | URL | — |
| 7 | `source` | `warm` / `list` / `referral` / `partner` / `inbound` / `event` | How you found them |
| 8 | `warm_cold` | `warm` / `cold` | Warm = you can reach them without cold outreach |
| 9 | `contact_role` | text | **Role + initials only.** Never a full name + email |
| 10 | `committee_position` | `signer` / `champion` / `blocker` / `user` / `unknown` | Per `ICP_FRAMEWORK.md` §6.2 |
| 11 | `reason_selected` | text | Why this account, in one line. If you cannot say, do not add it |
| 12 | `observable_trigger` | text | A *dated, externally visible* event (`ICP_FRAMEWORK.md` §6.4). Not a guess |
| 13 | `observable_issue` | text | **What you actually observed.** Must be verifiable by a third party |
| 14 | `inference` | text | What you *think* it means. **Clearly separate from field 13** |
| 15 | `question_to_validate` | text | The question you would ask them. Never asserted as fact |
| 16 | `teardown_status` | `none` / `researched` / `produced` / `sent` | — |
| 17 | `touch_count` | 0–4 | Stops at 4 (`06_OUTREACH_SEQUENCE.md`) |
| 18 | `last_touch_date` | date | — |
| 19 | `reply` | `none` / `positive` / `neutral` / `negative` / `optout` | `optout` is terminal and permanent |
| 20 | `conversation_held` | `Y` / `N` | Any real-time conversation |
| 21 | `qualified_conversation` | `Y` / `N` | **Strict**: ≥20 min, with a DM or direct influencer, at an in-segment business, about their operations. This is the D3 counter |
| 22 | `interview_id` | `I-001`… | Links to `08_INTERVIEW_RECORD_TEMPLATE.md` output |
| 23 | `hypotheses_touched` | `H-01;H-10`… | Semicolon-separated |
| 24 | `qualification_status` | `QUALIFIED` / `QUALIFIED_WITH_RISK` / `NOT_YET` / `DISQUALIFIED` | From `09_QUALIFICATION_SCORECARD.md`. **Never set from impression** |
| 25 | `next_action` | text | One concrete action |
| 26 | `next_action_date` | date | Blank = stale. Flagged at weekly review |
| 27 | `outcome` | `open` / `nurture` / `lost` / `diagnostic_sold` / `disqualified` | — |
| 28 | `loss_code` | `L-01`…`L-13` | Mandatory when `outcome` is `lost` or `disqualified`. Taxonomy in `SALES_SYSTEM.md` §8 |
| 29 | `evidence_grade` | `NONE` / `SIGNAL` / `FACT` | **`FACT` only for money received.** Everything else is at most `SIGNAL` |
| 30 | `notes` | text | No interpretation dressed as observation |

## 3. The three-column discipline *(fields 13 / 14 / 15)*

The most common way a ledger corrupts the evidence base is by recording a guess as a finding.

| Column | Test it must pass | Example |
|---|---|---|
| `observable_issue` | Could a stranger verify this from outside, today? | "Web form submitted 14:02 Tue; first reply 11:40 Thu (45.6 h)" |
| `inference` | Marked as *my reading*, not theirs | "Suggests no owned intake queue outside business hours" |
| `question_to_validate` | Phrased as a question you will actually ask | "What happens to an enquiry that arrives after 6pm?" |

**Prohibited in `observable_issue`:** anything about revenue, conversion, lost patients, internal
performance, staff competence, or profitability. You cannot observe those from outside
(`04_TEARDOWN_SOP.md` §4).

## 4. Counting rules for the D3 gate

`qualified_conversation = Y` requires **all four**:

1. Duration ≥ 20 minutes of actual conversation.
2. The other party is a decision-maker or direct influencer (`signer`, `champion`, or an operations
   lead with genuine influence — **not** a receptionist, not a marketing contractor).
3. The business is in the primary or hedge segment as defined at D2.
4. The conversation was **about their operations**, not about you or your services.

**It does not count as qualified if:** it was a scheduling call · they only asked what you do ·
it was under 20 minutes · it was with someone who cannot influence a purchase · you spent most of
it pitching.

> A "qualified conversation" is an input measure for **access**, not a measure of interest.
> An unpleasant 25-minute conversation with a sceptical owner counts. A delightful 10-minute chat
> with an enthusiastic office manager does not.

`qualification_status` is a **different and stricter** thing — set only by
`09_QUALIFICATION_SCORECARD.md`, never from the same conversation's mood.

## 4b. Where the 40–60 accounts actually come from

Operator-simulation gap `OPSIM-01`: the plan says "build a target list" and never says how.

| Source | Method | Yield | Notes |
|---|---|---|---|
| **Warm network** (`U-04`) | From the founder-inputs answer, directly | 0–20 | Always first. Cheapest conversations available |
| Sector associations and member directories | Public membership lists for the specialty | 10–40 | Usually the densest single source |
| Maps / local business search | Search the specialty by metro; filter to multi-site by checking each site's own "our locations" page | 20–60 | Slow but reliable for the 3–15 site band |
| Specialty referral directories | Public patient-facing directories | 10–30 | Good for specialty filtering, weak for site count |
| Conference and event attendee lists | Public exhibitor/attendee pages | 5–15 | Also surfaces trigger events |
| Intermediary introductions (CH-3) | From X-06 partner conversations | 0–10 | Highest quality, slowest |

**Site-count verification is the filter that matters.** The ICP is 3–15 locations
(`ICP_FRAMEWORK.md` §6.1); single sites are a different business with different economics and are
explicitly deferred. Check the business's own locations page — directory data is frequently stale.

**Stop at 60.** A larger list is not a better list; it is a way of avoiding the first phone call.

### The selection-bias prohibition *(red-team finding `RT-K1`)*

> **Accounts are selected on ICP fit, never on observed dysfunction.**

If the list is built by searching for clinics with visibly broken booking paths, then the finding
that clinics have broken booking paths is manufactured, and every downstream gate inherits it. D4
would pass on a sample constructed to pass it.

| Permitted `reason_selected` | Prohibited |
|---|---|
| "5 sites, dermatology, in metro" | "Booking page is obviously broken" |
| "3 sites, opening a 4th — trigger event" | "Slowest reply of everyone I tested" |
| "Matches ICP size band; warm intro available" | "Looks like they need us" |
| "Specialty group, directory-listed, unverified" | "No tracking pixel — easy win" |

**Sequence is the control:** select the account on fit, *then* research it. Never the reverse.
A deep-tier research pass that finds nothing worth three observations is a normal and healthy
outcome (`04_TEARDOWN_SOP.md` §3) — roughly 1 in 5 should end that way. If none ever do, the list
was selected on dysfunction.

## 4c. Finding a contact route without scraping

Operator-simulation gap `OPSIM-02`. Binding rule from `GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §6:
**no scraped personal contact data, B2B channels only.**

| Permitted | Not permitted |
|---|---|
| The business's own published contact channel (web form, published office address, main line) | Scraping personal inboxes from any source |
| A role-based address the business publishes (`info@`, `admin@`) | Buying a contact list of named individuals |
| A named individual's business contact **that they published themselves** for business purposes | Guessing an address pattern and mailing it |
| Asking reception for the right person **by role**, not by name | Inferring personal mobile numbers |
| An introduction from a mutual contact | Contacting anyone who has opted out, ever, by any route |

**The realistic route into a clinic group is the published channel, addressed to a role.** That is
also exactly what the teardown measures, which makes the first message honest: you used the same
channel a patient would.

If reception gives you a name, record **role + initials** in the ledger (§1), never the full name
with contact details.

## 5. Hygiene rules

| Rule | Reason |
|---|---|
| Log within 24 hours of the touch | Recall quality collapses after that |
| One row per account, not per contact | Multiple contacts go in `committee_position` notes |
| `optout` is permanent and repository-wide | `GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §6, binding now |
| Never delete a row | Losses are the cheapest market research you will get |
| Never upgrade `evidence_grade` without new evidence | `EVIDENCE_AND_ASSUMPTIONS_REGISTER.md` §5 rule 2 |
| A row with no `next_action_date` is stale after 14 days | Flagged at the weekly review |
| 40–60 rows is the target, not a minimum to pad | A padded list produces a false sense of pipeline |

## 6. Weekly rollups this ledger must produce

Feed `14_WEEKLY_VALIDATION_REVIEW.md` and `AGENCY_SCORECARD.md`:

| Metric | Formula | Scorecard ID |
|---|---|---|
| Contacts initiated | count(`touch_count` ≥ 1) | M-01 |
| Reply rate | count(`reply` ≠ none) ÷ count(`touch_count` ≥ 1) | M-02 |
| **Qualified conversations** | count(`qualified_conversation` = Y) | **M-03 — the D3 counter** |
| Teardown → conversation | count(conversation ∧ teardown sent) ÷ count(teardown sent) | M-04 |
| Conversation → qualified | count(`qualification_status` ∈ {QUALIFIED, QUALIFIED_WITH_RISK}) ÷ count(conversation) | M-05 |
| Loss distribution | count by `loss_code` | M-17 |
| Warm vs cold yield | qualified ÷ contacts, split by `warm_cold` | — |

**Watch the warm/cold split.** If every qualified conversation is warm, H-03 has **not** been
tested — you have tested your network, not the segment's reachability. Record that explicitly at
D3 rather than passing the gate on a misread.

## 7. Row format

```csv
account_id,account,segment,tier,geography,website,source,warm_cold,contact_role,committee_position,reason_selected,observable_trigger,observable_issue,inference,question_to_validate,teardown_status,touch_count,last_touch_date,reply,conversation_held,qualified_conversation,interview_id,hypotheses_touched,qualification_status,next_action,next_action_date,outcome,loss_code,evidence_grade,notes
```

### SYNTHETIC EXAMPLE — NOT EVIDENCE

*The row below is a format illustration only. It describes no real business, contains no real
observation, and must never be counted, aggregated, or cited as evidence. Delete it before use.*

```csv
A-001,[SYNTHETIC] Example Clinic Group,S2,primary,[metro],example.invalid,list,cold,Ops Dir / X.Y.,champion,"3 sites, booking widget on 1 of 3","[SYNTHETIC] new site announced on their site 2026-08-11","[SYNTHETIC] test enquiry sent Tue 14:02, reply Thu 11:40 (45.6h)","[SYNTHETIC] suggests no out-of-hours intake owner","What happens to an enquiry that arrives after 6pm?",produced,2,2026-09-16,none,N,N,,H-03,NOT_YET,Send touch 3,2026-09-23,open,,NONE,SYNTHETIC ROW — DELETE BEFORE USE
```
