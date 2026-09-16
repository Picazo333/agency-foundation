---
status: review
owner: meta
updated: 2026-09-16
authority: workbench
depends_on:
  []
---
# Open Questions

## Brand
- What is the agency name?
- Which visual territory becomes Brand Direction V0?
- How far should medieval/angelic/grotesque/anatomical imagery enter the system versus remain campaign/illustration language?

## Business

Strategy reconciliation is complete (`docs/02-strategy/thesis/STRATEGY_RECONCILIATION.md`). The
questions below are updated accordingly; answered questions are retained with their answers so the
reasoning stays traceable.

- ~~Which agency archetype survives strategy reconciliation?~~ **Proposed:** a diagnostic-led,
  vertical, productized studio (M8). Four archetypes killed, one demoted. Pending `ADR-0005`.
- ~~What is the primary economic unit?~~ **Proposed:** a measured revenue gap — diagnostic, then a
  bounded build, then an operated layer. Not a website and not automation per se.
- Which ICP survives the access gate? Multi-site specialty clinic groups are the recommended
  primary candidate; the selection is made by evidence at D2/D3, not by analysis.
- **Will any buyer pay for diagnosis before implementation?** (H-01 — the program's highest-risk
  open question.)
- Do buyers recognise the revenue-leak problem unprompted, or is it supplier-invented? (H-10)
- What are real willingness-to-pay levels? No price observation exists (`E-22`). (H-04)
- Does a recurring operated layer attach at all? (H-09)
- Is the local market's price anchor high enough for the economics to work, or does the geography
  choice need to change? (`RED_TEAM_REVIEW.md` RT-07)

## Founder context — blocking, answerable in one sitting

- Geography, jurisdiction, operating language, entity status (`U-01`)
- Hours per week available (`U-02`)
- Runway in months and minimum monthly draw (`U-03`)
- Who can be contacted this month without cold outreach, by name and count (`U-04`)
- Verifiable prior delivery work and references (`U-05`)

## Validation
- ~~What must be validated in the first 90 days?~~ **Answered:** 12 ranked hypotheses with gates,
  thresholds and kill criteria — `docs/06-validation/FIELD_VALIDATION_PLAN.md`.
- Does the founder's visual direction raise or lower trust with the target buyer? (H-08 — feeds
  the Brand/Business Fit Review.)
- Is there an existing local competitor in the proposed position? (H-07)

## Technical
- Monorepo versus later website split?
- Final frontend/backend/automation stack after business and brand convergence?
- Which two CRM platforms and two booking/PMS integration patterns will be supported for clients?
  Supporting more destroys repeatability (`TOOLING_AUTOMATION_REQUIREMENTS.md` TQ-4, TQ-5).

## Legal / professional ⚖️

Requires qualified local professionals, not research. Full list:
`docs/04-operations/GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §12.

- Entity, tax and compliant-invoicing requirements — **before the first invoice**.
- Contract templates (MSA, SOW, change order, IP, liability cap) — **before the first signed SOW**.
- Data-protection obligations for patient-adjacent lead data — **determines whether the healthcare
  ICP is viable at all** (`U-10`).
- Whether target clients require suppliers to carry insurance — may gate the ICP.
