---
id: HARVEST-20260922-divinivid-active-reference-binding
status: candidate
owner: meta
created: 2026-09-22
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
    - docs/03-brand/workbench/divinivid/generation/POSTMORTEM_2026-09-22_ACTIVE_VISUAL_CONDITIONING_FAILURE.md
    - docs/03-brand/workbench/divinivid/generation/CURRENT_GENERATION_STATE.yaml
---
# Harvest Record — Active multimodal reference binding is distinct from reference availability

## What happened
A mature visual-generation project recovered its exact repository state, approved image anchors and generator-facing contracts, yet repeated recovery outputs drifted into stable generic visual priors.

The approved anchor files were available and inspectable, but the runtime could not prove that those images were effectively attached to and consumed by the image-generation request.

The incident therefore exposed a missing authority state between storage/retrieval and execution.

## Reusable finding
For multimodal generative systems:

`REFERENCE_AVAILABLE != REFERENCE_BOUND != REFERENCE_EFFECTIVE`

A robust executor should be able to attest:
- which references were selected;
- their authority role;
- whether their bytes/pixels were attached to the request;
- whether the executor supports the intended conditioning mode;
- whether unapproved descendants were excluded.

## Additional findings
1. Reconstructing logical state does not automatically reconstruct perceptual/multimodal state.
2. Root-approved visual anchors should form a star topology; generated siblings should not become implicit style ancestry.
3. Large negative prompts are not equivalent to Anti-Canon enforcement.
4. Technical-content prompts can trigger genre takeover even when semantic Canon is correct.
5. Executor substitution requires a capability/conditioning compatibility gate.
6. A high-precision information-design artifact may need deterministic composition with bounded generative assets.
7. Structured assembly should be a fallback/mode, not an automatic replacement for a previously proven monolithic workflow.

## Reuse boundary
Portable:
- reference-binding attestation;
- authority-role typing;
- root-anchor topology;
- executor compatibility checks;
- structured-assembly fallback trigger;
- evals for available-vs-bound references.

Project-local:
- DIVINIVID palette;
- its specific anchors;
- Figma component names;
- dark-field percentages;
- contract IDs.

## Candidate evals
- reference exists in context but is not attached to the executor request -> hard fail before generation;
- wrong authority class attached -> fail;
- current-round rejected output used as positive style reference -> fail;
- executor cannot accept image conditioning but adapter claims equivalent support -> fail;
- two correctly bound attempts still miss style -> route to structured assembly, not indefinite prompting.

## Downstream
### Noema
Evaluate an execution-context attestation pattern that can distinguish retrievable context from actively bound execution context without owning domain aesthetics.

### Skill Foundry
Feed this evidence into the approved visual-production candidate and add eval coverage for multimodal binding, executor compatibility and structured-assembly fallback.

## Canon impact
Candidate only. No automatic policy change outside the source project.
