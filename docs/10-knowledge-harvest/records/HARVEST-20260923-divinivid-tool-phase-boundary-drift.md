---
id: HARVEST-20260923-divinivid-tool-phase-boundary-drift
status: candidate
owner: meta
created: 2026-09-23
source_event_type: INCIDENT
confidentiality: INTERNAL
routes:
  - skill_candidate
  - sop_process
  - template_schema
  - eval_test
  - benchmark_lesson
provenance:
  artifact:
    - docs/03-brand/workbench/divinivid/generation/DIVINIVID_EXECUTION_ERROR_LEDGER_V1.md
    - docs/03-brand/workbench/divinivid/generation/TOOL_EXECUTION_CONTRACTS_V1.md
    - docs/03-brand/workbench/divinivid/evaluations/PLAN_DEVIATION_2026-09-23_PRELOCK_RECONCILIATION.md
---
# Harvest Record — Tool success is not phase success

## What happened
A mature brand workflow had multiple approved plans and connected premium tools. After several successful visual locks, execution advanced into a Figma-based Digital Behavior probe.

The Figma call technically succeeded, but the artifact used a low-resolution proxy, proxy typography, static structure and product/UI semantics before several identity prerequisites were formally closed.

The issue was not tool failure. It was **phase/tool mismatch**.

## Reusable finding

`TOOL_AVAILABLE != TOOL_AUTHORIZED_FOR_CURRENT_GATE`

and:

`EXECUTION_SUCCESS != PHASE_SUCCESS`.

A material tool call should have a purpose contract that states:
- active phase;
- question;
- why this tool;
- fixed variables;
- expected output;
- DoD;
- budget;
- failure route;
- promotion status.

## Why it mattered
Without call-level purpose, premium tools can increase confidence and complexity while answering the wrong question.

The resulting artifact may be polished, editable or technically valid and still be invalid evidence for the governing phase.

## Additional lessons
1. Identity/application/prototype phases need explicit prerequisite edges.
2. Proxy assets must carry typed status.
3. Post-call validation should test both technical correctness and phase relevance.
4. Tool cost includes review/rework complexity, not only subscription price.
5. A state/cursor integrity check is valuable even in well-governed repositories.
6. Figma, v0, Runway or any provider should remain capability implementations, not workflow authorities.

## Candidate Noema route
Evaluate generic protocol support for:
- phase -> capability authorization;
- tool-call work orders;
- typed proxy/evidence status;
- prerequisite/cursor integrity;
- cost/complexity-aware capability use.

Do not encode DIVINIVID-specific aesthetic rules.

## Candidate Skill Foundry route
Extend existing visual-production/orchestration candidates with evals for:
- one-variable experiment integrity;
- phase-boundary violations;
- proxy-resolution suitability;
- executor substitution;
- post-call efficacy;
- authority promotion.

Prefer EXTEND/MODE over a provider-specific Skill unless repeated cross-project evidence proves a distinct capability.

## Reuse boundary
High-value for:
- multi-agent projects;
- premium-tool stacks;
- visual/product workflows;
- workflows with phase gates and human approval;
- projects where a tool can mutate external state.

Low-value for trivial one-off calls where governance overhead would exceed risk.

## Human review
- reviewer: pending
- decision: pending
- notes: candidate for Noema protocol review and Skill Foundry G0-G5 overlap analysis.
