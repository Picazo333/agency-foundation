---
status: draft
owner: asset-factory
updated: 2026-09-16
authority: workbench
depends_on:
  []
---
# Asset Factory Architecture Spec

This directory defines the generator-agnostic architecture for the Agency Foundation Asset Factory.

The factory is intended to consume an approved Brand V1 system and produce **reviewable, versioned asset candidates** that can become implementation-ready only after the required Brand, technical, accessibility, provenance and human-approval gates pass.

This specification is architecture/workbench material. It does not itself prove legal clearance, implement CI enforcement, authorize a generation provider, or promote any asset to production.

## Architecture Documentation

1. [Brand Pack Contract](./01-brand-pack-contract.md) — input contract for approved visual rules and unresolved-data behavior.
2. [Asset Taxonomy](./02-asset-taxonomy.md) — asset categories, responsive families and context-specific outputs.
3. [Prompt Contracts & Parameters](./03-prompt-contracts.md) — structured generation requests and invent-vs-ask authority.
4. [Metadata & Provenance Schema](./04-metadata-provenance-schema.md) — identity, lifecycle, accessibility, source lineage and rights-review states.
5. [Lifecycle & QA Gates](./05-lifecycle-qa.md) — generation/review/approval state machine and bounded QA responsibilities.
6. [Batch Workflow & Handoff](./06-workflow-handoff.md) — naming/versioning, batch flow and implementation manifest contract.

## Examples

See [`examples/`](./examples/) for illustrative requests/manifests. Example values are not Brand decisions and do not imply that the referenced assets/providers actually exist.

## Non-negotiable boundaries

- Brand V1 remains the authority for visual rules; the factory may not invent missing Brand canon.
- `REFERENCE_ONLY`, `UNKNOWN_RIGHTS`, and `UNVERIFIED_LICENSE` material cannot enter production approval.
- `CLEARED` is a reviewed project workflow state, not a universal legal warranty.
- Final production approval defaults to an authorized human review.
- Generated/staging outputs are never production assets merely because they look correct.
- Provider-specific capabilities must adapt to this contract rather than redefining it.
- Future automated validators/CI must be implemented and tested before the repo may claim those gates are automatically enforced.

## Expected Brand V1 input

Future activation should provide, where applicable:
- Brand name/status;
- design tokens and palette semantics;
- typography rules/licensing;
- illustration and imagery grammar;
- motion rules;
- SVG/security rules;
- licensing/provenance rules;
- composition/grid rules;
- accessibility requirements;
- explicit anti-patterns and invent-vs-ask boundaries.
