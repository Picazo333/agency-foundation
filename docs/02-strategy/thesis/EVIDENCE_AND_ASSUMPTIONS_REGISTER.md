---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - ADR-0004
---
# Evidence and Assumptions Register

> **Module 1 of the Agency Master Plan.** Every other master-plan document is required to cite
> identifiers from this register rather than restating numbers inline. If a claim elsewhere in
> the plan has no `E-##` or `A-##` behind it, treat it as unsourced and reject it in review.

## 1. Why this document exists first

The governing risk in this program is not that the plan is wrong. It is that the plan is
**precise**. The repository already contains three ingested research corpora whose own
summaries warn that their numeric outputs are unreliable
(`docs/01-research/synthesis/RESEARCH_STATUS.md`,
`docs/01-research/curated/spark-final/SPARK_CLOSURE_SUMMARY.md`). A master plan built on top of
that material will inherit false precision unless precision is quarantined at the base layer.

This register is that quarantine.

## 2. Evidence grading scheme

| Label | Meaning | Allowed use |
|---|---|---|
| `FACT` | Directly verifiable from a primary artifact available to this program right now | May be asserted without qualification |
| `SIGNAL` | Observed pattern from secondary/AI-mediated research, or an artifact that implies but does not prove the claim | May shape priorities; may not be stated to a buyer as fact |
| `INFERENCE` | A conclusion this plan draws from `FACT`/`SIGNAL` by explicit reasoning | Must carry the reasoning; reversible |
| `HYPOTHESIS` | A testable proposition with no supporting evidence yet | Must have a validation test and a kill criterion |
| `UNKNOWN` | A material question with no current answer | Must be routed to `FIELD_VALIDATION_PLAN.md` or to a named expert |

Financial/pricing sub-scheme:

| Label | Meaning |
|---|---|
| `PUBLIC PRICE` | A published price observable by anyone |
| `PRICE SIGNAL` | A price implied by a proposal, job post, marketplace listing or interview report |
| `INFERRED RANGE` | A range this plan constructs from cost/capacity logic, not from observation |
| `UNKNOWN` | No defensible basis |

**Rule:** this plan currently holds **zero** `PUBLIC PRICE` records and **zero** `PRICE SIGNAL`
records, because no primary pricing artifact has been imported into the repository. Every number
in `PRICING_AND_ECONOMICS_MODEL.md` is therefore an `INFERRED RANGE` derived from capacity and
cost logic. This is stated once here and enforced everywhere.

## 3. What this program actually knows — evidence register

### 3.1 Facts (verifiable from repository artifacts)

| ID | Claim | Grade | Source | Decision impact |
|---|---|---|---|---|
| E-01 | Three research corpora were ingested: BOLD, Web/Aesthetic Applications, Spark Final Closure Pack | `FACT` | `docs/01-research/raw/SOURCE_ARCHIVES.md` | Establishes the evidence ceiling |
| E-02 | The raw source archives are **not** present in the repository; only synthesis summaries are | `FACT` | `docs/01-research/raw/SOURCE_ARCHIVES.md`; repository file listing | **Critical.** No claim in this plan can be traced to a primary source. Every downstream number degrades to `INFERRED RANGE` |
| E-03 | The research phase is declared "closed enough for decision work" and explicitly non-canonical | `FACT` | `docs/01-research/synthesis/RESEARCH_STATUS.md` | Authorises decision work; forbids treating research as truth |
| E-04 | Spark's numeric scores and ranges are declared non-factual unless individually sourced | `FACT` | `SPARK_CLOSURE_SUMMARY.md` | Forbids importing any Spark number |
| E-05 | Spark's VoC language is declared synthetic unless traceable | `FACT` | `SPARK_CLOSURE_SUMMARY.md` | Forbids using research VoC as buyer language in copy |
| E-06 | BOLD's anti-generic-AI-agency conclusion is designated contrarian input, not a decision | `FACT` | `BOLD_CONTRARIAN_SUMMARY.md`; `CLAUDE_MASTER_PLAN_WORKSTREAM.md` | Sets the falsification posture of Module 2 |
| E-07 | The founder's visual taste profile is human-calibrated and documented in detail, including an explicit anti-profile | `FACT` | `docs/03-brand/workbench/visual-territories/CURRENT_VISUAL_DIRECTION.md` | Real constraint on the brand interface; **not** evidence of market attractiveness (`E-08`) |
| E-08 | Repository canon forbids using visual taste as a business-attractiveness score | `FACT` | `SPARK_CLOSURE_SUMMARY.md`; `KEY_RESEARCH_INPUTS.md` | Hard constraint on Module 2 and Module 16 |
| E-09 | Zero primary buyer contact has occurred: no interviews, experiments or findings exist | `FACT` | `docs/06-validation/*` contain only stub READMEs | **The single most important fact in this register.** Sets the entire posture of the 90-day plan |
| E-10 | No agency name, ICP, positioning, offer, price or business model has been decided | `FACT` | `PROJECT_STATE.md` "Open decisions" | Confirms this plan proposes, never freezes |
| E-11 | Brand V0 is provisional and gated behind a Brand/Business Fit Review | `FACT` | `PROJECT_STATE.md`; `ADR-0002`; `CONVERGENCE_GATES.md` | Module 16 writes requirements, not identity |
| E-12 | The program operates a functioning multi-agent, repo-first governance system with ADRs, status metadata, ownership matrix and canon/workbench firewall | `FACT` | Repository structure; `docs/00-meta/*`; `docs/07-decisions/*` | Founder-capability evidence, and a usable proof artifact (see `PROOF_STRATEGY.md` L0) |
| E-13 | Research source archives are named in Spanish (`INVESTIGACION_*`) | `FACT` | `SOURCE_ARCHIVES.md` | Supports, but does not prove, a Spanish-language operating context (`E-16`) |
| E-14 | The governing issue names "Mexico/LATAM/international implications" as the geographic frame to analyse | `FACT` | GitHub Issue #2, Phase 2 | Authorises MX/LATAM as the modelling frame; does not confirm it |
| E-15 | Implementation methodology is fixed: Aesthetic/Functional/System spines, `S0→S4` maturity, licensing and provenance gates | `FACT` | `IMPLEMENTATION_SUMMARY.md`; `PROJECT_STATE.md` | Binding on Module 17 |

### 3.2 Signals (secondary, AI-mediated or implied)

| ID | Claim | Grade | Source | Decision impact |
|---|---|---|---|---|
| E-16 | The founder operates bilingually (ES/EN) and the likely primary market is Mexico | `SIGNAL` | `E-13`, `E-14`, naming criteria requiring "pronunciation ES/EN" in `NAMING_WORKBENCH.md` | Modelling frame for ICP access and pricing. **Must be confirmed in the first week** (`U-01`) |
| E-17 | A generic horizontal AI/automation agency is commercially weak and commoditising | `SIGNAL` | `BOLD_CONTRARIAN_SUMMARY.md` | Falsification input to Module 2; strong enough to demand a defence, not strong enough to decide |
| E-18 | Diagnostic-led, productized and RevOps-oriented models are comparatively stronger | `SIGNAL` | `BOLD_CONTRARIAN_SUMMARY.md` | Origin of the working thesis; must still be tested against buyer evidence |
| E-19 | Healthcare, dental, clinics, labs, professional services and B2B services appear in research as candidate segments | `SIGNAL` | `docs/02-strategy/icp/README.md`; `CLAUDE_KICKSTART.md` §3 | Seeds the ICP longlist. Repository canon explicitly states none is a predetermined winner |
| E-20 | Competitor, offer, pricing, funnel, proof and operations patterns exist in the Spark corpus | `SIGNAL` | `SPARK_CLOSURE_SUMMARY.md` | Usable as hypothesis generators only; unavailable in detail because of `E-02` |
| E-21 | The founder can specify, decompose and govern complex multi-agent work to a standard well above SMB-service-provider norm | `SIGNAL` | `E-12`; the structure and internal consistency of `docs/00-meta/` and `docs/08-plans/` | Genuine differentiation candidate; also a genuine over-planning risk (`R-14`) |

### 3.3 Inferences drawn by this plan

| ID | Inference | Derived from | Reversal condition |
|---|---|---|---|
| E-22 | Because no primary pricing artifact exists (`E-02`), every price in this plan must be built bottom-up from capacity and cost, never benchmarked | `E-02`, `E-04` | A primary pricing corpus is imported and graded |
| E-23 | Because zero buyer contact has occurred (`E-09`), the scarcest resource in the next 90 days is **qualified buyer conversations**, not plan quality | `E-09`, `E-12` | 10+ qualified conversations logged |
| E-24 | Because the founder's aesthetic is distinctive and polarising (`E-07`) and the candidate segments are conservative (`E-19`), brand and buyer are in latent conflict | `E-07`, `E-19` | Buyer evidence shows distinctiveness raises trust in the chosen segment |
| E-25 | Because the founder is currently the only delivery resource, capacity — not demand — will be the first binding constraint after the first two sales | `E-09`, `E-12`, absence of any team artifact | A contractor bench exists |
| E-26 | Because governance sophistication (`E-12`, `E-21`) is unusual among SMB service providers, it is a credible trust artifact in its own right | `E-12`, `E-21` | Buyers show indifference to process rigor in discovery |

### 3.4 Unknowns that block commitment

| ID | Unknown | Blocks | Routed to |
|---|---|---|---|
| U-01 | Founder's actual geography, jurisdiction, operating language and legal entity status | Pricing currency, legal checklist, ICP access | Founder answer, Week 1 |
| U-02 | Founder's available hours per week for this business | Entire economic model | Founder answer, Week 1 |
| U-03 | Founder's cash runway and revenue floor (months of survival, minimum monthly draw) | Pricing floor, whether a slow diagnostic-led ramp is survivable | Founder answer, Week 1 |
| U-04 | Founder's existing network: who can be contacted this month without cold outreach | ICP selection — this may dominate all other criteria | Founder answer, Week 1 |
| U-05 | Founder's verifiable delivery track record (shipped client work, references) | Proof ladder starting rung, price anchoring | Founder answer, Week 1 |
| U-06 | Whether any candidate ICP will pay for a paid diagnostic cold | Entire offer architecture | `FIELD_VALIDATION_PLAN.md` H-01 |
| U-07 | Real willingness-to-pay ranges in the selected segment and geography | Pricing model | `FIELD_VALIDATION_PLAN.md` H-04 |
| U-08 | Whether target buyers have any measurement baseline at all | Proof strategy, outcome claims, delivery scope | `FIELD_VALIDATION_PLAN.md` H-06 |
| U-09 | Buying-committee structure in multi-site clinical groups (owner vs administrator vs coordinator) | Sales system, qualification gates | `FIELD_VALIDATION_PLAN.md` H-03 |
| U-10 | Local data-protection obligations when handling patient-adjacent lead data | Whether healthcare ICP is legally viable at all | Qualified local counsel — see `GOVERNANCE_RISK_SECURITY_CHECKLIST.md` |
| U-11 | Whether the founder's aesthetic helps or harms trust with the selected buyer | Brand/Business Fit Review outcome | `FIELD_VALIDATION_PLAN.md` H-08 |
| U-12 | Competitive density and price anchoring in the selected local market | Positioning, pricing | `FIELD_VALIDATION_PLAN.md` H-07 |

> `U-01` through `U-05` are **founder-answerable in one sitting** and gate a disproportionate share
> of the model. They are the first action in the 30-day roadmap, ahead of all market work.

## 4. Planning assumptions

Each assumption carries: a value, a confidence band, what breaks if it is wrong, and how it gets
calibrated. **No assumption in this table is evidence.**

### 4.1 Context assumptions

| ID | Assumption | Working value | Confidence | Breaks if wrong | Calibration |
|---|---|---|---|---|---|
| A-01 | Primary market is a major Mexican metropolitan area; secondary is LATAM/US-remote | MX metro | Low | Pricing currency, legal checklist, channel plan | `U-01`, Week 1 |
| A-02 | Modelling currency is USD; client-facing pricing may be quoted in MXN | USD | Medium | Nothing structural; conversion only | `U-01` |
| A-03 | Founder availability for this business | 30 productive hrs/week | Low | Every capacity and break-even figure | `U-02`, Week 1 |
| A-04 | Founder is the sole delivery resource for at least the first 90 days | Solo | Medium | Capacity, WIP limits, hiring triggers | Observed |
| A-05 | A contractor bench can be assembled within ~30 days when needed (design, front-end, integrations) | Available | Low | Scaling path, hiring triggers | Test in Month 2 |
| A-06 | Founder has no significant existing client roster or referenceable case studies | None | Medium | Proof ladder start rung; price ceiling | `U-05`, Week 1 |

### 4.2 Commercial assumptions

| ID | Assumption | Working value | Confidence | Breaks if wrong | Calibration |
|---|---|---|---|---|---|
| A-07 | A paid diagnostic is sellable cold to the selected ICP | Sellable | Low | The whole entry offer; falls back to free teardown → paid core | H-01 |
| A-08 | Diagnostic → core conversion rate | 30% | Very low (`INFERRED RANGE`) | Revenue model, channel volume requirements | H-02, after 6 diagnostics |
| A-09 | Qualified-conversation → diagnostic-sold rate | 20% | Very low (`INFERRED RANGE`) | Outbound volume requirements | H-02 |
| A-10 | Core engagement cycle from first contact to signature | 30–60 days | Very low | Cash-flow timing, 90-day revenue expectation | H-05 |
| A-11 | Recurring "operated" tier attaches to 40% of delivered cores within 60 days of launch | 40% | Very low | The entire valuation and stability argument | H-09, Month 4+ |
| A-12 | Monthly logo churn on the recurring tier | 5% | Very low | Long-run recurring economics | Month 6+ |
| A-13 | Revision/rework overhead as % of budgeted delivery hours | 20% | Low (planning norm, not observed) | Gross margin — the most sensitive single input | Measured from engagement 1 |
| A-14 | Unbilled sales + admin hours per closed core engagement | 20 hrs | Low | Effective hourly yield | Measured from engagement 1 |

### 4.3 Cost assumptions

| ID | Assumption | Working value | Confidence | Notes |
|---|---|---|---|---|
| A-15 | Fixed monthly software/tooling stack | USD 250–450/mo | Medium | Bottom-up from `TOOLING_AUTOMATION_REQUIREMENTS.md` categories at entry tiers |
| A-16 | Variable AI/compute cost per active engagement | USD 40–120/mo | Low | Scales with agent usage, not headcount |
| A-17 | Contractor blended cost when used | USD 25–60/hr | Low | Wide band; MX/LATAM contractor market, unconfirmed |
| A-18 | Non-billable overhead (accounting, legal, banking, insurance) | USD 300–800/mo once formalised | Very low | Depends entirely on `U-01`/`U-10` |

## 5. Register maintenance rules

1. Any document in the master plan that introduces a new number must first add an `A-##` row here.
2. When a hypothesis in `FIELD_VALIDATION_PLAN.md` resolves, the corresponding `A-##` row is
   updated **and its confidence band is raised only by the grade of the evidence obtained** —
   twelve interviews produce `SIGNAL`, not `FACT`.
3. `INFERRED RANGE` never becomes `PRICE SIGNAL` through repetition. It becomes `PRICE SIGNAL`
   only when an actual buyer responds to an actual quote.
4. An assumption whose calibration date has passed without calibration is escalated in the next
   scorecard review, not silently carried forward.

## 6. Honest statement of evidence quality

This master plan is a **reasoning artifact, not a research artifact**. Its defensible content is:
the comparative logic, the decision architecture, the execution contracts, the risk exposure and
the validation design. Its non-defensible content is: every quantity. The plan is built so that
quantities can be replaced without rebuilding the structure.

A reader who wants to know "is this business good?" will not find the answer here. They will find
the shortest path to an answer, and the criteria that decide it.
