---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - OPERATING_MODEL.md
  - DELIVERY_OS.md
  - TOOLING_AUTOMATION_REQUIREMENTS.md
---
# Governance, Legal, Risk and Security Checklist

> **Module 16 of the Agency Master Plan** (Issue #2 Phase 13).
>
> ## Scope limitation — read first
>
> **This document contains no legal advice and no jurisdiction-specific legal conclusions.** It is
> a structured checklist of questions that require qualified professionals — a lawyer and an
> accountant licensed in the operating jurisdiction — and a set of operational security practices
> that are within the agency's own control.
>
> `U-01` (jurisdiction) and `U-10` (data-protection obligations) are unresolved. Any statement below
> that appears to describe a legal requirement is describing a **question to ask**, not an answer.
> Items marked **⚖️ PROFESSIONAL ADVICE REQUIRED** must not be resolved by reasoning, by research,
> or by an AI system.

## 1. Business and entity ⚖️

| # | Question | Why it matters | Timing |
|---|---|---|---|
| G-01 | What entity structure is appropriate for a solo services business in this jurisdiction? | Liability, tax, client credibility | Before first contract |
| G-02 | Can the business operate and invoice legally before formalising? | Determines whether revenue can precede registration | **Before first invoice** |
| G-03 | What registrations, licences or permits are required? | Compliance | Before formalising |
| G-04 | What are the tax obligations, rates and filing cadence? | Cash reserve (`PRICING_AND_ECONOMICS_MODEL.md` §12) | Before first invoice |
| G-05 | Business banking requirements and separation of personal/business funds | Accounting integrity, audit exposure | Before first payment |
| G-06 | Invoicing-format requirements (e.g. electronic invoicing regimes such as CFDI in Mexico) | Client payment may be blocked without a compliant invoice | **Before first invoice** |
| G-07 | Obligations when invoicing clients outside the home jurisdiction | Cross-border implications | Before first foreign client |
| G-08 | Thresholds at which obligations change (revenue, headcount) | Planning | Annual review |

## 2. Contracts ⚖️

| # | Item | Requirement |
|---|---|---|
| C-01 | **MSA / framework agreement** | Governing terms: liability cap, IP, confidentiality, data, termination, dispute resolution, governing law |
| C-02 | **SOW template** | Per-engagement scope, exclusions, client inputs, milestones, acceptance, revisions, change orders, payment |
| C-03 | **Change-order template** | Scope delta, price, revised dates, approval |
| C-04 | **Liability limitation** | Is a cap at contract value enforceable here? What is customary? |
| C-05 | **IP and licensing** | Client owns deliverables on full payment; **agency retains methods, templates, tooling and pre-existing IP.** This clause protects the productization strategy and must be explicit |
| C-06 | **Third-party licence pass-through** | Fonts, images, libraries, plugins — the client must know what they are licensed for (`DELIVERY_OS.md` §9.1) |
| C-07 | **Case-study and benchmark consent** | Publication rights, anonymised aggregate use (`PROOF_STRATEGY.md` §7.1, §8) |
| C-08 | **Termination and kill fee** | Work performed is payable; deposit treatment on early termination |
| C-09 | **Payment terms and late-payment remedies** | Work suspension rights; interest if permitted |
| C-10 | **Subcontractor clause** | Right to use contractors; agency remains liable |
| C-11 | **Acceptance and deemed approval** | The `CLIENT_LIFECYCLE.md` §5 clause must be enforceable |
| C-12 | **AI-use disclosure** | Whether and how AI processing must be disclosed and consented to |

**Contractor-side contracts ⚖️:** NDA · IP assignment (signed before any access) · scope and payment
terms · confidentiality extending to client data · security obligations · post-engagement access
revocation.

## 3. Insurance ⚖️

| # | Question |
|---|---|
| I-01 | Is professional liability / E&O insurance available and customary here for a solo services business? |
| I-02 | Is cyber liability insurance warranted given client-data access? |
| I-03 | Do any target clients (especially healthcare) **require** suppliers to carry insurance? This may gate the ICP entirely and should be asked during validation |
| I-04 | Business-interruption cover, given the founder-unavailability SPOF (`OPERATING_MODEL.md` §8) |
| I-05 | Cost, and how it affects the pricing model |

## 4. Data protection and privacy ⚖️ *(the highest-exposure area)*

`U-10` is open and **gates whether the S2 healthcare ICP is viable at all**. Answer before the
first healthcare engagement, not after.

| # | Question |
|---|---|
| D-01 | What data-protection law applies (in Mexico, LFPDPPP and its regulations — **confirm scope and current status with counsel**)? |
| D-02 | Is the agency a data controller or processor for client lead data, and what obligations follow? |
| D-03 | Is a data-processing agreement required with each client? |
| D-04 | What is the legal status of **patient-adjacent data** — appointment records, contact details of patients — as distinct from clinical records? This is the specific question that determines the achievable scope of the S2 offer |
| D-05 | Consent requirements for the automated communications built for clients (appointment reminders, reactivation campaigns) |
| D-06 | Data-residency or cross-border transfer restrictions, including data sent to AI providers |
| D-07 | Breach-notification obligations and timelines |
| D-08 | Retention and deletion requirements |
| D-09 | Data-subject rights (access, deletion) and the agency's role in servicing them |
| D-10 | What is required to use **anonymised client data in a benchmark dataset** (P7)? Is contractual consent sufficient, or is a stronger anonymisation standard required? |

### 4.1 Operational rules pending legal answers *(binding now)*

| # | Rule |
|---|---|
| DR-1 | **No clinical or patient medical records** are accessed, processed or stored, under any circumstances, before counsel clears it (`RF-7`, `DNS-9`) |
| DR-2 | **Data minimisation:** only the fields the engagement requires. Never take a full database export because it is convenient |
| DR-3 | Pseudonymise wherever analysis permits — most diagnostic analysis needs counts and timestamps, not names |
| DR-4 | **No client personal data in any AI prompt** without a documented contractual basis and client disclosure (`AI-1`) |
| DR-5 | Client data stays in client-controlled systems wherever possible; the agency holds the minimum |
| DR-6 | Every dataset held is recorded in the engagement data register: what, why, where, how long, who has access |
| DR-7 | Deletion on offboarding within 5 business days, **with written confirmation** (`CLIENT_LIFECYCLE.md` §10) |
| DR-8 | No client data in screenshots, case studies or teardowns without explicit consent and verification that it is genuinely unidentifiable |

## 5. Security baseline *(agency-controlled — implement now, no advice required)*

| # | Control | Status target |
|---|---|---|
| S-01 | MFA on every business account without exception | Before first client |
| S-02 | Password manager for all credentials; nothing in email, chat, docs or AI prompts | Before first client |
| S-03 | Full-disk encryption on all work devices | Before first client |
| S-04 | Automatic OS and software updates | Before first client |
| S-05 | Encrypted, tested backups of business-critical data | Month 1 |
| S-06 | Separate business and personal accounts and devices where practical | Month 1 |
| S-07 | Least-privilege client access; read-only by default | Every engagement |
| S-08 | Engagement access register maintained and reviewed | Every engagement |
| S-09 | Access revoked within 5 business days of offboarding | Every offboarding |
| S-10 | No secrets in the repository (already enforced — `.gitignore`, `.env.example`, `AGENTS.md`) | Continuous |
| S-11 | Contractor access scoped, time-bound and logged | When contractors engaged |
| S-12 | Client credential handover via secure share only | Every engagement |
| S-13 | Device lock timeout ≤ 5 minutes | Now |
| S-14 | Incident-response plan written, even if one page | Month 2 |
| S-15 | Annual review of all third-party access to agency systems | Annual |

### 5.1 Incident-response outline

Contain (revoke access, isolate) → assess (what data, whose, how) → **notify the affected client
within 24 hours** → remediate → document → review. Notification timing to authorities is
jurisdiction-specific (`D-07`) ⚖️.

## 6. Outbound and marketing compliance ⚖️

| # | Question / rule |
|---|---|
| M-01 | What rules govern unsolicited B2B commercial contact in this jurisdiction? |
| M-02 | Are there specific rules for email, WhatsApp or phone outreach? |
| M-03 | Are there advertising restrictions on **marketing for healthcare providers**? This affects what the agency may build for clinic clients and is easy to miss |
| M-04 | Requirements for testimonials and results claims in advertising |
| M-05 | Cookie/consent requirements for the agency's own site and for client sites built |
| **Binding now** | Identify yourself and your purpose in the first message · honour opt-outs immediately and permanently · no scraped personal contact data · B2B contacts only · no misleading subject lines |

## 7. Records, retention and continuity

| Record | Retention | Note |
|---|---|---|
| Contracts and SOWs | Per statutory requirement ⚖️ | Minimum 5–7 years is typical; **confirm** |
| Invoices and financials | Per tax law ⚖️ | — |
| Client data | Engagement + agreed period, then deleted | DR-7 |
| Baselines and outcome records | Permanent (agency-owned analysis) | `PROOF_STRATEGY.md` |
| Benchmark data | Permanent, anonymised, stored separately from the join key | P7 |
| Access registers | Engagement + 12 months | Audit evidence |
| Decision records (ADRs) | Permanent | `E-12` |

**Business continuity:** encrypted backups tested quarterly (an untested backup is a hypothesis) ·
credential recovery documented and stored securely offline · client runbooks enable self-operation
· a trusted person knows how to reach clients if the founder cannot.

## 8. Financial governance

| # | Practice |
|---|---|
| F-01 | Business and personal funds fully separated |
| F-02 | **Reserve 25–30% of contribution for tax** until the actual obligation is confirmed ⚖️ |
| F-03 | Client deposits treated as unearned revenue, not as available cash |
| F-04 | Monthly reconciliation with the bookkeeper |
| F-05 | Quarterly review of the tool and subscription base |
| F-06 | Client-concentration monitoring (T-8) |
| F-07 | Minimum operating reserve target: 3 months of fixed costs plus founder draw |
| F-08 | No personal guarantees on business obligations without advice ⚖️ |

## 9. Accessibility and consumer-facing obligations ⚖️

| # | Question |
|---|---|
| A-01 | Are there accessibility requirements for public-facing websites in this jurisdiction? |
| A-02 | Do healthcare providers face additional accessibility or disclosure requirements? |
| A-03 | What accessibility standard should client deliverables meet by default? |

**Binding now, regardless of the answers:** the `DELIVERY_OS.md` §9.1 accessibility checks are
mandatory. They are cheap at build time, expensive to retrofit, and a defensible professional
standard independently of what any regulator requires.

## 10. Sector-specific compliance triggers

Encountering any of these **stops work** pending advice:

| Trigger | Action |
|---|---|
| Client asks for clinical/EMR record integration | **Stop.** `DR-1`, `DNS-9`. Counsel before any scoping |
| Client asks for automated clinical communication (results, treatment info) | **Stop.** Medical-communication rules ⚖️ |
| Client asks for payment-card handling | **Stop.** PCI scope. Use a compliant processor; never touch card data |
| Client is regulated beyond general business law (finance, insurance, legal) | Sector-specific supplier obligations ⚖️ |
| Client requires a supplier security questionnaire or audit | Assess capacity honestly; do not overstate |
| Client requires specific insurance | `I-03` |
| Cross-border data transfer required | `D-06` ⚖️ |
| Client asks for automated decisions affecting individuals | Automated-decision-making rules ⚖️ |

## 11. Risk register additions

Proposed for `RISK_REGISTER.md` (business-operation risks, distinct from the existing
program-governance risks):

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Operating without required legal/tax formalisation | Medium | High | G-01…G-08 before first invoice |
| Data-protection breach involving client customer data | Low | **Critical** | §5 baseline; DR-1…DR-8; cyber insurance |
| Contract dispute with no enforceable written terms | Medium | High | C-01…C-12 lawyer-reviewed before first SOW |
| Client demands scope beyond a `DO NOT SELL` boundary | High | Medium | Written refusals; §10 triggers |
| Founder unavailability halts all delivery | Medium | **Critical** | `OPERATING_MODEL.md` §8; accepted residual |
| Unlicensed asset used in a client deliverable | Medium | Medium | Licence check in QA (`DELIVERY_OS.md` §9.1) |
| AI provider terms change, affecting delivery economics or data handling | Medium | Medium | Provider-agnostic workflows; no client lock-in |
| Client credential compromise traced to the agency | Low | **Critical** | §5 baseline; least privilege; revocation discipline |
| Outcome claim challenged as misleading | Low | High | `PROOF_STRATEGY.md` §9 ethical claim rules |
| Tax reserve insufficient at year end | Medium | High | F-02 |

## 12. Professional-advice action list *(priority order)*

| # | Professional | Question set | Before |
|---|---|---|---|
| 1 | **Accountant (local)** | §1 entirely; F-02; TQ-2 | **First invoice** |
| 2 | **Lawyer (local, commercial)** | §2 contract templates; C-04; C-05 | **First signed SOW** |
| 3 | **Lawyer (data protection)** | §4, especially D-04 and D-10 | **First healthcare engagement** |
| 4 | Insurance broker | §3 | Month 3, or earlier if a client requires it |
| 5 | Lawyer (advertising/healthcare marketing) | M-03, M-04 | Before building client marketing automation |

**Cost expectation:** `A-18` (USD 300–800/month post-formalisation) plus one-time legal setup.
This is a real cost that must survive `U-03`. Operating without contract templates or tax
compliance is not a saving; it is an unpriced liability held on the founder's personal balance
sheet.
