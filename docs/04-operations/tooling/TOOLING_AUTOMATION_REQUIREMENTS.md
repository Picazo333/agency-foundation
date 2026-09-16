---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - OPERATING_MODEL.md
  - DELIVERY_OS.md
---
# Tooling and Automation Requirements

> **Module 15 of the Agency Master Plan** (Issue #2 Phase 12). Specifies **requirements and
> selection criteria**, deliberately not vendors. Premature vendor commitment is the mechanism by
> which a small business acquires switching costs it cannot afford, and `docs/04-operations/tooling/README.md`
> already states the governing principle: *tools are replaceable; project state must remain portable.*

## 1. Selection principles

| # | Principle | Test |
|---|---|---|
| 1 | **Data portability is mandatory** | Can all data be exported in an open format, without the vendor's cooperation, today? If not, reject |
| 2 | **Start at the cheapest tier that meets the requirement** | Tool cost is fixed and compounds; capability is usually available later at the same price |
| 3 | **Fewer tools beats better tools** | Every tool adds an integration surface, a credential, a subscription and a failure mode |
| 4 | **Dogfood what is sold** | The agency's own CRM and automation stack is a P2 proof artifact (`PROOF_STRATEGY.md` §5) |
| 5 | **Client tooling follows the client's constraints, not the agency's preference** | Standardising the *pattern*, not the *platform*, is what makes delivery repeatable |
| 6 | **Support at most two platforms per client-facing category** | `DELIVERY_OS.md` §10; more destroys repeatability |
| 7 | **Security posture is a selection criterion, not an afterthought** | MFA, SSO where relevant, audit logs, granular permissions, a published data-processing position |

## 2. Internal stack requirements

### 2.1 CRM / pipeline
**Must:** custom objects or equivalent for the `SALES_SYSTEM.md` §9 model · custom fields including
loss codes and Q1–Q4 status · stage automation and timestamping · task and reminder generation ·
email integration with logging · **full data export** · API access.
**Should:** proposal-status tracking, basic reporting, mobile access.
**Must not:** per-contact pricing that penalises outbound volume; mandatory annual commitment.
**Budget:** USD 0–60/mo. **Note:** this is also the first internal implementation of the C-2
product, so its configuration doubles as a template.

### 2.2 Project management
**Must:** per-engagement workspace · task and milestone tracking · **time tracking against tasks,
with a rework category** (non-negotiable — it is the input to `A-13`, the largest margin variable)
· document attachment · client-visible view or exportable status.
**Budget:** USD 0–25/mo.

### 2.3 Proposal and e-signature
**Must:** templated documents with variable substitution · legally valid e-signature in the relevant
jurisdiction (**verify with counsel — `U-01`, `U-10`**) · view tracking · version history ·
PDF export and archive.
**Budget:** USD 20–50/mo.

### 2.4 Invoicing and accounting
**Must:** compliant invoicing for the jurisdiction (`U-01` — in Mexico this means CFDI/SAT
requirements; **confirm with a local accountant, do not assume**) · multi-currency if serving
outside the home market · payment-status tracking · export for the bookkeeper.
**Budget:** USD 0–40/mo + bookkeeper USD 100–250/mo.

### 2.5 File and document management
**Must:** per-client folder structure with access control · version history · external sharing with
expiry · **separation of client data from internal data** · backup.
**Budget:** USD 0–20/mo.

### 2.6 Password and secrets management *(non-negotiable)*
**Must:** encrypted vault · secure sharing with contractors · per-item access control · access
logging · MFA on the vault itself · secure credential handover to clients at offboarding.
**Must not:** credentials in email, chat, spreadsheets, documents, or any AI prompt (`AI-7`).
**Budget:** USD 10–40/mo. **This is the one category where the cheapest option is the wrong choice.**

### 2.7 Automation and orchestration
**Must:** connect the tools in this list · webhook support · error handling and failure alerting ·
execution logging · version or change history.
**Should:** self-hostable or exportable workflow definitions, so client-facing automations are not
hostage to one vendor's pricing.
**Budget:** USD 30–150/mo, scaling with volume.

### 2.8 Analytics and reporting
**Must:** connect to client data sources · scheduled report generation · client-shareable
dashboards · export.
**Note:** the monthly L3 report is the retention mechanism (`CLIENT_LIFECYCLE.md` §8), so the
binding requirement here is **presentation quality**, not analytical depth.
**Budget:** USD 0–100/mo.

### 2.9 Communication
Email with a professional domain · one shared client channel platform · video calls with recording
(training recordings are a delivery requirement) · scheduling/booking link.
**Budget:** USD 10–30/mo.

### 2.10 AI tooling
**Must:** capable general model access · code assistance · **a documented data-handling position
that can be shown to a client** (`AI-1`) · the ability to disable training on submitted data.
**Budget:** USD 60–200/mo.

### 2.11 Code and configuration repository
Already in place (`E-12`). Client-specific configuration stored per engagement, **secrets never
committed** (`AGENTS.md`, `.gitignore`, `.env.example` — already enforced in this repository).
**Budget:** USD 0.

### 2.12 Knowledge base
The repository serves this today. Revisit only when a non-technical team member needs it.
**Budget:** USD 0.

### 2.13 Support and ticketing
**Not required at current scale.** Email plus a tracked task list suffices below ~6 L3 accounts.
Revisit at the coordinator hiring trigger. Adding it now would be tooling for an imagined
organisation.

### 2.14 Client portal
**Not justified now.** A shared folder plus a dashboard link covers the need. Revisit only if
clients ask twice.

## 3. Total internal cost

| Tier | Monthly | When |
|---|---:|---|
| Minimum viable | USD 170 | Months 1–3 |
| Working | USD 385 | Months 4–12 |
| Scaling | USD 800 | Month 12+, with a team |

Consistent with `A-15`. **Review quarterly and cancel what is unused** — tool sprawl is the exact
problem the agency sells the fix for, and running a bloated stack while selling operational
discipline is both expensive and embarrassing.

## 4. Client-side tooling policy

| Situation | Policy |
|---|---|
| Client has a working platform | Use it. Do not migrate without a diagnostic-supported reason |
| Client has nothing | Recommend from the two supported platforms per category |
| Client wants an unsupported platform | Quote as custom with explicit added scope, or decline. Do not silently absorb the learning cost |
| Client wants to migrate | Separate, priced engagement. Never bundled into a build |

**Licence ownership:** the client buys and owns their own tool licences, in their own accounts,
always. The agency never resells, never holds the client's subscriptions, and never becomes a
billing intermediary — this avoids margin-on-licences temptation, cash-flow exposure, and the
lock-in position that contradicts the anti-lock-in stance in `CLIENT_LIFECYCLE.md` §7.

## 5. Human / AI-assisted / automated work map

| Workflow | Disposition | Rationale |
|---|---|---|
| Prospect research and list building | **Automated + AI-assisted** | High volume, low judgement |
| Teardown observation capture | AI-assisted | Founder judgement on what matters |
| Teardown recording | **Human** | The voice is the product |
| Outreach personalisation | AI-assisted, **human-sent** | Never fully automated — a detectably automated message destroys the observation-first premise |
| Follow-up scheduling | **Automated** | — |
| Discovery calls | **Human only** | — |
| Discovery notes and summary | AI-assisted | Verified by founder |
| Proposal drafting | AI-assisted from structured inputs | Founder owns price and scope |
| Contract generation | Automated from templates | Templates lawyer-reviewed |
| Onboarding sequence | **Automated** | Checklists, requests, reminders |
| Baseline data collection | Automated where possible | — |
| Diagnostic analysis | AI-assisted, **human-verified** (`AI-4`) | Every figure traced to source |
| Findings and quantification | **Human-owned** | This is the product |
| Build execution | AI-assisted | Reviewed and tested (`AI-5`) |
| QA | **Human** with automated checks | Automated where deterministic |
| Client status updates | AI-drafted, **human-sent** | Nothing unread is sent |
| Monthly L3 reports | Automated data + AI draft + **human insight** | The insight paragraph is why it is read |
| Invoicing and reminders | **Automated** | — |
| Bookkeeping | **Outsourced** | — |
| Pricing and scope decisions | **Human only** | Never delegated to any system |

**The line:** automate the mechanical, AI-assist the voluminous, keep the judgement. Any automation
that touches a client's perception of being personally attended to must have a human in the loop,
because the moment it is detected as automated it becomes evidence against the agency's own claim
of attentiveness.

## 6. Automation governance

| # | Rule |
|---|---|
| AG-1 | Every automation has a named owner and a documented purpose |
| AG-2 | Every automation has failure alerting. A silent automation failure in a client system is worse than no automation — the client stops checking manually |
| AG-3 | Automations touching client data are documented in the engagement record |
| AG-4 | No automation sends external communication on the client's behalf without their explicit configured approval |
| AG-5 | Automation logic is exportable or reproducible; no un-recoverable vendor-locked logic in client systems |
| AG-6 | Automations are reviewed quarterly; unused ones are removed |
| AG-7 | Test in a sandbox before production; production changes require a rollback path (`DELIVERY_OS.md` §5) |

## 7. Tool-evaluation checklist

Before adopting anything: Does a current tool already do this? · Can all data be exported today? ·
What is the annual cost at projected scale? · What breaks if the vendor doubles the price or shuts
down? · Does it support MFA and granular permissions? · Where is client data stored, and under what
terms? · Can a contractor be given scoped access? · How long to migrate away? · Is this solving a
problem we have now, or one we imagine having?

**The last question kills most candidates.**

## 8. Open questions

| ID | Question | Blocked by |
|---|---|---|
| TQ-1 | Which e-signature providers are legally valid in the operating jurisdiction? | `U-01`, counsel |
| TQ-2 | Invoicing/tax-compliance requirements (e.g. CFDI/SAT if Mexico) | `U-01`, accountant |
| TQ-3 | Which AI providers' data-handling terms are acceptable for client work? | Counsel review |
| TQ-4 | Which two CRM platforms to support for clients? | First 3 engagements — let clients decide by revealed preference |
| TQ-5 | Which two booking/PMS integration patterns to support? | S2 engagements |
| TQ-6 | Is data residency required for the selected ICP? | `U-10`, counsel |
