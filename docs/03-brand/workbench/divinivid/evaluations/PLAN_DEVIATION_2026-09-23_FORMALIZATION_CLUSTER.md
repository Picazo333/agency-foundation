---
status: approved
owner: brand
created: 2026-09-23
authority: plan_deviation
human_approved: true
depends_on:
  - docs/08-plans/master/DIVINIVID_CURRENT_EXECUTION_PLAN_V2.md
  - docs/08-plans/workstreams/DIVINIVID_VISUAL_IDENTITY_MASTER_PLAN.md
  - docs/07-decisions/ADR-0014-targeted-visual-synthesis-and-expression-bases.md
  - docs/07-decisions/ADR-0015-pre-lock-exploration-before-final-expression-lock.md
  - docs/03-brand/workbench/divinivid/evaluations/PLAN_DEVIATION_2026-09-23_PRELOCK_RECONCILIATION.md
  - docs/03-brand/workbench/divinivid/generation/DIVINIVID_R0_REQUIREMENT_MATRIX_V1.md
---
# PLAN_DEVIATION — Formalization Cluster / Audit Adoption

## phase
DIVINIVID identity formalization after R0 and during R1 Signature System.

## requested_change
Keep R1 and R2 as explicit gates, but replace the strictly serial execution topology:

`R3 Composition -> R4 Image / Illustration -> R5 Temporal Mapping -> P6`

with:

```text
             R3 Composition
            /
R2 PASS ---+--- R4 Image / Illustration
            \
             R5 Temporal Mapping
                    |
          CROSS-CONSISTENCY AUDIT
                    |
        SYSTEM FORMALIZATION GATE
                    |
                   P6
```

R3, R4 and R5 remain separate specifications and retain their individual objectives and Definitions of Done. Their drafting/formalization work may interleave from the same approved evidence set because R0 already found substantial/high evidence in all three areas.

## reason
The independent process audit identified that strict serial handoffs between R3, R4 and R5 create avoidable context churn and can hide contradictions between composition, image behavior and motion.

R0 already established:
- R3 Composition Grammar: `PARTIAL / HIGH EVIDENCE`;
- R4 Image / Illustration Language: `PARTIAL / HIGH EVIDENCE`;
- R5 Temporal Identity: `PARTIAL / CLOSE`.

The remaining work is predominantly formalization and validation, not broad aesthetic discovery.

The three domains contain legitimate cross-dependencies:
- composition <-> image;
- composition <-> motion;
- image <-> motion.

A joint consistency gate is therefore more informative than pretending the three domains can be frozen independently without reconciliation.

## evidence_or_new_constraint
The change is based on:
- approved R0 Requirement Matrix;
- Current Execution Plan V2;
- Visual Identity Master Plan;
- ADR-0014 and ADR-0015;
- Pre-Lock Reconciliation PLAN_DEVIATION;
- Execution Error Ledger;
- Tool Execution Contracts;
- independent DIVINIVID process audit dated 2026-09-23.

No new visual evidence contradicts the current locks.

## impact_on_downstream_phases
- R1 remains the current creative gate.
- R2 remains required before the Formalization Cluster.
- R3/R4/R5 may be drafted/interleaved after R2 PASS.
- none of R3/R4/R5 independently authorizes P6;
- P6 remains blocked until the Cross-Consistency Audit and System Formalization Gate pass;
- P6 remains a Digital Brand Specimen, not the actual agency website;
- P7/P8/Red Team/Human Final Gate remain unchanged;
- Final Expression Lock remains required before the Figma Production System, Website Strategy/IA, Golden Slice, full prototype and v0/code.

## what_remains_frozen
This deviation does not reopen:
- DIVINIVID Core;
- BASE_LOCK_B1;
- BESTIARY_BASE_B0;
- M1-B Topografia Organica;
- P1 Typography;
- P2 Minimal / No-Icons;
- P3 H-B Editorial / Systemic;
- P4 D2 Controlled / Expressive Mosaic;
- P5 Registration + Negative Revelation;
- R0 Reconciliation result.

## execution simplifications adopted
### R1
Five comparable architecture proofs remain the basis of comparison. Baseline-comparability repair is distinct from survivor completion. Only surviving architectures receive deeper reduced/micro-size completion.

### R2
Separate:
1. technical validation;
2. shortlist;
3. aesthetic/functional finalist comparison.

R2 must not become the production design system.

### P6
Execute the five required surfaces as one Digital Brand Specimen workstream with one integrated review cycle.

### P7
Use minimum diagnostic fidelity:
`constraint -> representative artifact -> failure threshold -> PASS/MUTATE/KILL`.

### Tool governance
Use risk-proportional execution contracts:
- T0 READ;
- T1 deterministic/reversible;
- T2 paid/generative/nondeterministic;
- T3 high-impact agentic.

### Iteration policy
Use:
`CONSTRUCT -> ADVERSARIAL -> CORRECT -> VERIFY -> STOP`.

A new iteration requires a new named failure mode or material delta.

### Tool substitution
`FAILED EXECUTION != NEED ANOTHER TOOL`.

Classify failure before substitution:
- specification;
- input/context;
- authority;
- conditioning;
- deterministic-vs-generative mismatch;
- executor capability mismatch;
- runtime/integration.

Only executor capability mismatch justifies provider/tool substitution by default.

### State authority
Maintain one authoritative cursor per scope rather than one universal state file.

### Chat -> Agent crossover
Do not delegate unresolved visual human gates.
After R1 is closed, deterministic R2 technical validation becomes the first preferred agent/executor crossover.
After R2 PASS, R3/R4/R5 formalization may be agent-heavy under the approved evidence and gate contracts.

## rollback_path
Return R3/R4/R5 to strict serial execution if interleaving causes:
- unclear ownership of a decision;
- contamination between domains;
- conflicting specifications that cannot be resolved by the Cross-Consistency Audit;
- inability to attribute a failure to Composition, Image/Illustration or Temporal Identity.

## human_approval
Approved in-chat by the human creative owner on 2026-09-23.

## consequence
`DIVINIVID_CURRENT_EXECUTION_PLAN_V2.md` remains the governing plan and is updated in place to incorporate this deviation.

The current cursor does not advance. It remains the R1 Signature System targeted-repair human review.
