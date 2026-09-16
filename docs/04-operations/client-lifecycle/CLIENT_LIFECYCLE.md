---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - SALES_SYSTEM.md
  - DELIVERY_OS.md
  - PROOF_STRATEGY.md
---
# Client Lifecycle

> **Module 12 of the Agency Master Plan** (Issue #2 Phase 10). The full arc from lead to
> offboarding, with the artifacts, gates and owners at each stage. `DELIVERY_OS.md` specifies *how
> the work is produced*; this document specifies *how the relationship is run*.

```text
lead → qualify → discover → propose → close → onboard → deliver → QA →
launch/handoff → support → optimize → expand → offboard/referral
```

## 1. Stage map

| Stage | Owner | Duration | Exit gate | Key artifact |
|---|---|---|---|---|
| Lead | Founder | — | Reply received | CRM record |
| Qualify | Founder | 7 d | Q1–Q4 pass | Qualification record |
| Discover | Founder | 7 d | Problem stated in buyer's words | Discovery record |
| Propose | Founder | 10 d | Signed or lost | Proposal + SOW |
| Close | Founder | 5 d | Deposit cleared | Countersigned SOW |
| Onboard | Founder | 5 d | Access verified, baseline captured | Onboarding pack |
| Deliver | Founder | 2–8 wk | Milestones accepted | Working system |
| QA | Founder | 3–5 d | Internal QA passed | QA record |
| Launch/handoff | Founder | 3–5 d | Training complete, runbook delivered | Runbook |
| Support | Founder | 30 d | Stabilised | Monitoring record |
| Optimize (L3) | Founder | Ongoing | Monthly report delivered | Monthly report |
| Expand | Founder | Quarterly | Expansion offered | QBR record |
| Offboard | Founder | 5 d | Data returned/deleted, referral asked | Offboarding record |

## 2. Onboarding *(the highest-leverage five days in the relationship)*

Most engagement failures are visible in week one and are almost always the same failure: access did
not arrive, or the client's side had no owner.

### 2.1 Required within 5 business days

| Item | Why | If not received |
|---|---|---|
| Named client project owner with ≥ 2 h/week | Without one, every decision waits on the signer | **Do not start.** Escalate to the signer |
| Read access: booking system, CRM, analytics, ad accounts, enquiry channels | The engagement is measurement-first | Clock pauses (SOW clause) |
| Credential handover via the agreed secure method | Security baseline (§3) | Do not proceed with insecure alternatives |
| Brand assets, content, legal/clinical copy constraints | Delivery input | Scope note |
| Named approvers per gate | Prevents approval drift | Escalate |
| Kickoff meeting held | Alignment | — |
| **Baseline snapshot captured and stored** | `PROOF_STRATEGY.md` §10 — non-negotiable | Engagement cannot proceed to delivery |

> **The clock-pause clause.** The SOW states that if client inputs are not received within 5
> business days, the schedule pauses and the end date moves. This is written, explained at kickoff,
> and applied. Absorbing client delay silently is the most common cause of margin loss in service
> businesses, and it also teaches the client that deadlines are soft.

### 2.2 Kickoff agenda (60 minutes)

Restate the problem in the client's own words (2 min — this single move does more for the
relationship than anything else on the agenda) · confirm scope *and exclusions*, read aloud
(10 min) · milestones, dates, approval gates (10 min) · what we need and by when, with named owners
(10 min) · communication protocol and response times (5 min) · change-order process, explained
before it is needed (5 min) · **baseline review — "this is what we're measuring against"** (10 min)
· questions (8 min).

**Reading the exclusions aloud** is uncomfortable and prevents most scope disputes. A client who
hears "this does not include X" in week one does not experience it as a refusal in week five.

## 3. Access and credential handling

| Rule | Detail |
|---|---|
| Never by email or chat | Password manager share, or client-created accounts |
| Named accounts only | Never a shared client login where the platform allows named users |
| Least privilege | Read-only until write access is demonstrably required |
| Documented | Every credential recorded in the engagement access register: system, access level, granted date, purpose |
| Time-bound | Access reviewed at handoff; revoked at offboarding within 5 business days |
| MFA | Enabled wherever the platform supports it |
| No production changes without a rollback path | Applies to every live system touched |
| Client data minimisation | Only what the scope requires. **No clinical/patient records** (`RF-7`) |

Full baseline in `GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §5–6.

## 4. Communication protocol

| Channel | Use | Response commitment |
|---|---|---|
| Email | Decisions, approvals, anything contractual | 1 business day |
| Shared channel (Slack/WhatsApp) | Day-to-day questions | 4 business hours |
| Weekly written update | Progress, blockers, what is needed | Every Friday, without fail |
| Scheduled call | Gates, reviews, escalations | Booked in advance |
| Emergency | Defined narrowly in the SOW | Best effort; **no 24/7 SLA** (`DNS-8`) |

**The weekly written update is mandatory even in a quiet week**, and especially in a bad week. Its
format: done this week · next week · blocked on you (with names and dates) · risks · budget/schedule
status. Clients do not churn because of problems; they churn because of silence about problems.

**Scope-request handling:** every request arriving through an informal channel is acknowledged
warmly and immediately routed: *"Good idea — that's outside the current scope, let me price it as a
change order."* Never "sure, I'll add that." The informal-channel yes is where `A-13` rework is
born.

## 5. Delivery-stage relationship management

| Gate | Client action | Timebox | If missed |
|---|---|---|---|
| G1 Discovery sign-off | Approve findings and approach | 3 business days | Schedule pauses |
| G2 Design/structure sign-off | Approve before build | 3 business days | Schedule pauses |
| G3 Internal QA | None (agency-side) | — | — |
| G4 Client review | Consolidated feedback, one round | 5 business days | Deemed approved after written notice |
| G5 Launch approval | Go/no-go | 2 business days | — |

**"Deemed approved after written notice"** is essential for a solo operator: an engagement held
open indefinitely by an absent approver consumes WIP capacity that cannot be sold. It must be in
the SOW, and it must be exercised politely and in writing when needed.

**Consolidated feedback, one round:** feedback arriving in a drip destroys estimation. The SOW
specifies a single consolidated round per gate, and the mechanism is a shared feedback document
with a deadline, not a thread.

## 6. Change control

Any request outside the SOW follows: log → assess (hours, schedule, dependencies) → **written
change order with price and revised dates** → client approval → execute.

**The rule that protects the margin:** no work begins on a change before written approval. The
"I'll just do it, it's small" instinct is the single largest contributor to `A-13`, and it is
generous in a way the client never notices and never values.

Threshold: changes under 1 hour may be absorbed at the founder's discretion, logged, and **reported
in the weekly update as absorbed**. Making generosity visible converts an invisible cost into
relationship credit.

## 7. Launch and handoff

| Item | Requirement |
|---|---|
| Runbook | How the system works, how to change common settings, what to do when something breaks, who to call |
| Training | 2 sessions: operators (how to use it) and manager (how to read the numbers). **Recorded** — staff turnover is the top cause of implementation decay |
| Access transfer | Client owns all accounts and credentials. Agency access documented and time-bound |
| Measurement handover | Dashboard access + walkthrough of how each number is produced |
| Baseline comparison | Current state vs the day-1 baseline (`PROOF_STRATEGY.md` §10) |
| Known limitations | Written. What was deliberately not done, and why |
| 30-day support window | Defined scope, start and end dates |

**Anti-lock-in stance:** the client owns everything and can operate it without the agency. This
costs some retention leverage and buys something worth more — it is the single most credible
differentiator against suppliers who retain clients through dependency, and it is the truthful
version of the L3 pitch (the system needs *maintenance*, not *hostage-taking*).

## 8. Support and the optimize loop (L3)

| Cadence | Activity |
|---|---|
| Continuous | Monitoring and alerting on data integrity and system health |
| Monthly | Measured report against baseline; change requests within allowance; one optimisation experiment |
| Quarterly (top tier) | Business review: results, benchmark comparison, next-quarter priorities, expansion conversation |

**The monthly report is the product.** If the client does not read it, L3 will churn regardless of
system quality (`DECISION_TREE.md` D9). Requirements: one page of substance, the three numbers that
matter with direction of travel, one thing that changed and why, one recommendation. Editorial
clarity here is a retention mechanism, not decoration — `BRAND_BUSINESS_INTERFACE.md` `BC-03`.

**Health monitoring** — leading indicators of churn, reviewed monthly:

| Signal | Reading |
|---|---|
| Report unopened 2 months running | **Strongest churn predictor.** Act immediately |
| Champion left the business | High risk; re-onboard the successor within 30 days |
| Zero change requests for 3 months | Either perfect or disengaged — assume disengaged, verify |
| Metrics declining and unacknowledged | Value is eroding; escalate |
| Payment delays | Cash stress or dissatisfaction |
| Expansion refused twice | Relationship plateau |

## 9. Expansion

Scheduled, not opportunistic: one expansion conversation per operated account per quarter, at the
QBR (`OFFER_ARCHITECTURE.md` §5). Prepared with: what the numbers show, the largest remaining gap
from the original diagnostic, and a specific priced option.

**Ad-hoc upselling is prohibited.** It erodes the advisory posture the whole model depends on. A
scheduled quarterly review does not.

## 10. Offboarding

Every ending, including bad ones, follows the same procedure. Handled well, offboarding produces
referrals; handled badly, it produces the one review that matters.

| Step | Requirement | Timebox |
|---|---|---|
| Written confirmation | Scope of ending, effective date | Immediate |
| Access audit | Every agency access identified | 2 days |
| Data return | All client data exported in portable formats | 5 days |
| **Data deletion** | Agency copies deleted; written confirmation issued | 5 days, per `GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §7 |
| Access revocation | All agency access removed; client confirms | 5 days |
| Documentation | Final runbook, known issues, recommendations | 5 days |
| Final invoice | Reconciled | 5 days |
| Exit conversation | What worked, what did not, would you recommend us | 10 days |
| Referral ask | Specific, named | At the exit conversation |
| Case study | If consent exists and results permit | 30 days |

**The exit conversation happens even when the client is leaving unhappy** — especially then. It is
the only reliable source of honest feedback the business will get, and a well-handled bad ending is
recoverable. Retention data is captured in `AGENCY_SCORECARD.md` M-12.

## 11. Lifecycle artifacts

| Artifact | Created | Retained | Used by |
|---|---|---|---|
| Discovery record | Discover | Engagement | Proposal, delivery, messaging corpus |
| Qualification record | Qualify | CRM | Loss analysis |
| SOW + MSA | Propose | Permanent | Contractual |
| Onboarding pack | Onboard | Engagement | Delivery |
| **Baseline record** | Onboard day 1 | Permanent | Proof, benchmark |
| Access register | Onboard | Until offboard + audit | Security |
| Weekly updates | Delivery | Engagement | Dispute record |
| Change orders | As needed | Permanent | Margin analysis |
| QA record | QA | Engagement | Quality system |
| Runbook | Handoff | Permanent | Client + support |
| Outcome record | Acceptance, +30d, +90d | Permanent | Proof, case study |
| Benchmark row | Onboard + acceptance | Permanent, anonymised | P7 dataset |
| Monthly reports | L3 | Permanent | Retention, proof |
| Offboarding record | Offboard | Permanent | Compliance evidence |

## 12. Lifecycle failure modes

| Failure | Where it shows | Prevention |
|---|---|---|
| Access never arrives | Onboarding | Clock-pause clause; do not start without it |
| No client-side owner | Onboarding | Named owner is a start condition, not a preference |
| Scope drift via informal channels | Delivery | Route every request to change control (§4) |
| Approval limbo | Gates | Deemed-approval clause (§5) |
| Baseline missed | Onboarding | Structural gate — engagement cannot proceed (`PROOF_STRATEGY.md` §10) |
| Training skipped when late | Handoff | Acceptance criterion, not a nicety |
| Support becomes unpriced retainer | Support | 30-day window with a written end date; then L3 or lapse |
| Champion departs | Optimize | Health monitoring; re-onboard successor in 30 days |
| Offboarding data left in place | Offboard | Deletion confirmation is a required artifact |
