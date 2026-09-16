---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - AGENCY_MASTER_PLAN.md
  - MASTER_PLAN_AUDITS.md
  - RED_TEAM_REVIEW.md
---
# Final Integration Pass

> Cross-document consistency review performed after the nine audit passes. Checks that the modules
> agree with each other and with existing repository canon, validates references, and logs the
> contradictions that could **not** be resolved.
>
> Issue #2: *"Resolve contradictions where evidence permits; otherwise log them explicitly."*

## 1. Scope of the pass

| Check | Method | Result |
|---|---|---|
| All required deliverables exist | File existence against Issue #2 §"Required Master Outputs" | ✅ 23/23 — `DELIVERABLE_MAP.md` |
| Relative markdown links resolve | Automated link resolution across all new modules | ✅ 0 broken (§5) |
| Backtick file references resolve | Automated basename resolution against the repository | ✅ 0 unresolved (§5) |
| Front-matter present and well-formed | Automated | ✅ 35/35 new files |
| No secrets committed | Automated pattern scan | ✅ 0 (matches were security *policy* statements) |
| Numeric consistency across modules | Manual trace (§3) | ✅ after 2 corrections |
| Ownership boundaries respected | Manual (§6) | ✅ |
| Canon untouched | `git status` on `docs/00-meta/`, `docs/01-research/`, `docs/03-brand/` | ✅ |
| Contradictions | Manual (§4) | 6 logged, 3 resolved |

## 2. Dependency graph

```text
EVIDENCE_AND_ASSUMPTIONS_REGISTER  ← cited by every module
        ↓
STRATEGY_RECONCILIATION → AGENCY_THESIS → DECISION_TREE
        ↓                       ↓              ↓
   ICP_FRAMEWORK ───────→ POSITIONING_ARCHITECTURE
        ↓                       ↓
   OFFER_ARCHITECTURE ──→ PRICING_AND_ECONOMICS_MODEL
        ↓                       ↓
   PROOF_STRATEGY          AGENCY_SCORECARD
        ↓                       ↑
   ACQUISITION_MARKETING → SALES_SYSTEM → CLIENT_LIFECYCLE → DELIVERY_OS
                                              ↓                 ↓
                                        OPERATING_MODEL   TOOLING_AUTOMATION
                                              ↓                 ↓
                                   GOVERNANCE_RISK_SECURITY_CHECKLIST
                                              ↓
        FIELD_VALIDATION_PLAN ← tests every unvalidated assumption above
                ↓
   BRAND_BUSINESS_INTERFACE · WEB_BUSINESS_REQUIREMENTS · ROADMAP
```

**Cycle check:** one intentional feedback loop — `AGENCY_SCORECARD` measures inputs that calibrate
`PRICING_AND_ECONOMICS_MODEL`, which sets the thresholds the scorecard enforces. This is a
measurement loop, not a reasoning circularity.

**Orphan check:** none. Every module is referenced by at least one other and reachable from
`AGENCY_MASTER_PLAN.md` §3.

## 3. Numeric consistency trace

Key figures traced across every module that uses them.

| Figure | Source of truth | Consumers | Consistent? |
|---|---|---|---|
| `A-03` 30 h/week | Evidence register §4.1 | Pricing §2, Operating §1, Validation §9 | ✅ |
| 780 delivery hours/year | Pricing §2.2 | Pricing §9, Operating §9, Red Team RT-05 | ✅ |
| L1 = 44 total founder hours | Pricing §2.1 | Offer §3, Delivery §4, Pricing §4 | ✅ — Delivery §4 shows 30 delivery hours; 44 includes rework + unbilled sales |
| C-1 = 152 total founder hours | Pricing §2.1 | Pricing §4, §8.1, Delivery §5 | ✅ — Delivery §5 shows 110 base |
| `A-13` rework 20% | Evidence register | Pricing §2.1/§8.1, Delivery §11, Scorecard M-26 | ✅ |
| `A-08` conversion 30% | Evidence register | Pricing §8.4, Offer §3, Scorecard M-07 | ✅ |
| `A-11` attachment 40% | Evidence register | Thesis §5, Offer §6.1, Scorecard M-11, Decision D9 | ✅ |
| Diagnostic credit 50% | Offer §3.1 | Positioning §9, Sales §7, ADR-0007 | ✅ **corrected** — was 100% pre-audit |
| WIP: 1 core | Operating §5 | Pricing §2, Decision D8 | ✅ **corrected** — was 2 pre-audit |
| L3 WIP 4 → 2 during a build | Operating §5 | Pricing §2.2 | ✅ **corrected** (`AUD-03-02`) |
| Break-even incl. tax | Pricing §10 | Red Team RT-09 | ✅ **corrected** (`AUD-04-03`): 1.35–1.45× multiplier |
| Outreach 8–10 h/week | Acquisition CH-1 | Validation §9, Operating §6 | ✅ **corrected** (`AUD-02-02`): research tiering added |
| D3 threshold 8 conversations | Decision D3 | Validation H-03, Scorecard §5, Roadmap §3 | ✅ |
| D5 threshold 2 diagnostics | Decision D5 | Validation H-01, Scorecard §5, Roadmap §4 | ✅ |
| Gate 1 timing (after D5) | Decision §3 | Brand interface §7, Roadmap §5 | ✅ |

**Two figures deliberately differ by context and are annotated in place:** delivery-hour tables show
*base* hours in `DELIVERY_OS.md` and *total founder* hours (base + rework + unbilled sales) in
`PRICING_AND_ECONOMICS_MODEL.md`. Conflating them was the source of an earlier inconsistency and is
now labelled at both ends.

## 4. Contradictions log

### Resolved

**C-03 — The diagnostic bootstrap circle.** A paid diagnostic requires credibility whose creation is
its own purpose. *Partially resolved* by the free L0 teardown rung, which demonstrates competence
before charging for it, and by framing the diagnostic as instrumentation the buyer keeps rather than
as analysis. **Residual:** whether that is sufficient is H-01. Recorded as partially resolved, not
closed.

**C-04 — BOLD says avoid AI positioning; AI is the founder's fastest lever.** Resolved by
`ADR-0009`: AI is killed as a category and kept as a mechanism. The founder's own visual anti-profile
(`E-07`) independently rejects AI-coded aesthetics, so the commercial and aesthetic arguments agree.
**Residual:** whether some segment pays an AI premium is H-11; the ADR names the reopen path rather
than foreclosing it.

**C-05 — Two deliverable-name contracts.** `CLAUDE_MASTER_PLAN_WORKSTREAM.md` (canon) and Issue #2
(governing task) name different files. Resolved by treating Issue #2 as the later, more specific
contract and recording the mapping in `DELIVERABLE_MAP.md` rather than editing a canonical document
to match a task. **Flagged to the human owner** in `CLAUDE_HANDOFF.md` — the canonical workstream
spec may want updating, but that is a canon change and not this workstream's call.

### Unresolved — logged explicitly

**C-01 — Founder aesthetic vs conservative buyer trust.** `E-07` (documented, distinctive, partly
grotesque visual direction) against `ICP_FRAMEWORK.md` §6 (conservative clinical buyers evaluating an
unknown supplier). The register-separation proposal (`BRAND_BUSINESS_INTERFACE.md` §2) is a
*hypothesis about buyer reaction*, not a resolution. **Routed to:** H-08, then Gate 1.
**Why it cannot be resolved here:** `E-08` forbids deciding it on taste, and no buyer evidence
exists.

**C-02 — Vertical focus vs option value.** Vertical specialisation produces proof and access fastest
(M6) but forecloses the breadth the founder's capability could serve. The plan chooses focus with a
dated review at D8, which manages the tension without dissolving it. **Unresolved by design.**

**C-06 — `CLAUDE_KICKSTART.md` cites research files that do not exist.** Items 10–12 of its
"Read first" list (`BOLD_STRATEGIC_INPUT.md`, `SPARK_RESEARCH_GUARDRAILS.md`,
`WEB_IMPLEMENTATION_RESEARCH_SYNTHESIS.md`) are not in the repository; the curated summaries under
`docs/01-research/curated/` were used instead. Additionally, the task brief for this workstream
referenced `docs/09-handoffs/claude/START_PROMPT.md`, which does not exist —
`CLAUDE_KICKSTART.md` was used as the equivalent contract. **Not resolved here:** `docs/01-research/`
and the kickstart are outside this workstream's write scope. **Flagged in `CLAUDE_HANDOFF.md`.**

## 5. Automated validation results

Run against all 40 new and modified markdown files on 2026-09-16 (35 created, 5 modified):

```text
MISSING FILES:                none
BROKEN RELATIVE LINKS:        none
UNRESOLVED .md REFERENCES:    none
MISSING FRONTMATTER:          none
SECRET PATTERNS:              none
PROTECTED-AREA MODIFICATIONS: none  (docs/00-meta, docs/01-research, docs/03-brand,
                                     docs/05-product-web, docs/08-plans/workstreams,
                                     apps, packages, labs, infra, scripts,
                                     asset-factory, assets, .github — all untouched)
```

An earlier pass flagged three "secret-like" lines; all three were reviewed and are security
*policy* statements (e.g. "no secrets in the repository", "no credentials, secrets or access tokens
in any AI prompt"), not credentials.

Historical-name references in `DELIVERABLE_MAP.md` §3 (`PRICING_MODEL.md`, `ECONOMIC_MODEL.md`,
`90_DAY_ROADMAP.md`) intentionally name files that do not exist — that is the purpose of the
superseded-name column.

## 6. Repository-canon compliance

| Rule | Source | Compliance |
|---|---|---|
| Research is not canon | `source-of-truth.md`, `ADR-0004` | ✅ All research cited as `SIGNAL`/`research-only`; no research number imported |
| Workbench is not canon | `CANON_PROMOTION_RULE.md` | ✅ Every new file `status: review`, `authority: workbench` |
| No FROZEN decision changed | `AGENTS.md` | ✅ None touched |
| Work only in assigned scope | `OWNERSHIP_MATRIX.md` | ✅ `DELIVERABLE_MAP.md` §5 |
| No direct work on `main` | `DO_NOT_CONTINUE_ON_MAIN.md` | ✅ Isolated branch; PR to `main` |
| State what was not changed | `AGENTS.md` | ✅ `CLAUDE_HANDOFF.md` |
| No secrets | `AGENTS.md` | ✅ Scanned |
| Brand canon untouched | Task brief, `OWNERSHIP_MATRIX.md` | ✅ `docs/03-brand/` unmodified |
| Evidence labels preserved | `RESEARCH_CANON_FIREWALL.md` | ✅ Module 1 and per-claim citation |
| ADRs only where a human decision is needed | `CLAUDE_KICKSTART.md` rule 5 | ✅ 5 proposed, each naming a decision the founder must make |
| No silent downgrade | `NO_SILENT_DOWNGRADE.md` | ✅ §8 below |
| Stop at other workstreams' decisions | `STOP_RULE.md` | ✅ Name, identity, legal, jurisdiction all deferred |

## 7. Definition-of-Done check

Against `docs/00-meta/definitions-of-done.md`, "Strategic plan":

| Criterion | Evidence |
|---|---|
| Assumptions explicit | `EVIDENCE_AND_ASSUMPTIONS_REGISTER.md` §4, 18 assumptions with confidence and calibration |
| Evidence dependencies explicit | §3 of the same, 26 evidence items graded; 12 unknowns routed |
| Kill criteria and validation plan included | `FIELD_VALIDATION_PLAN.md` §6; `DECISION_TREE.md` D7; `AGENCY_THESIS.md` §1.3 |
| Does not silently freeze unvalidated claims | All files `status: review`; five ADRs `PROPOSED`; `ADR-0008` prohibits publishing prices |

## 8. Known limitations of this plan *(per `NO_SILENT_DOWNGRADE.md`)*

Stated plainly rather than concealed:

1. **No primary research was performed or available.** `E-02`: the raw archives are not in the
   repository. Every conclusion rests on synthesis summaries plus structural reasoning.
2. **No market data of any kind.** No competitor prices, no market sizing, no buyer evidence. This
   is a reasoning artifact.
3. **Every currency figure is an `INFERRED RANGE`.** None is observed.
4. **Segment analysis is desk reasoning**, not field research. Bands are `INFERENCE`.
5. **Founder context is unknown.** `U-01`–`U-05` gate a disproportionate share of the model and are
   answerable in one sitting.
6. **No legal or tax conclusions.** Only questions, routed to qualified professionals.
7. **The buying-committee model for S2 is inferred**, not observed (`U-09`).
8. **Delivery hour estimates are constructed**, not measured. They will be wrong; the plan is built
   so they can be replaced.

## 9. Integration verdict

The plan is internally consistent after five numeric corrections and seven audit-driven structural
changes. Its reasoning chain is traceable from evidence grade to decision gate. Its known weaknesses
are stated rather than smoothed over, and the three contradictions that could not be resolved are
each routed to a dated test rather than argued away.

**It is ready for human review as a proposal.** It is not ready to be treated as truth, and
`ADR-0005` is written so that approving it authorises validation rather than belief.
