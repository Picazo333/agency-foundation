# JULES START PROMPT — ASSET FACTORY ARCHITECTURE

Repository: `Picazo333/agency-foundation`

Preferred execution branch: `asset/jules-asset-factory-architecture`

Governing task: GitHub Issue #3 — Asset Factory architecture — Jules execution.

## Preflight

Before making changes:

1. Confirm the repository is exactly `Picazo333/agency-foundation`.
2. Confirm you are NOT on `main`.
3. Prefer the prepared branch `asset/jules-asset-factory-architecture`. If Jules provisions an isolated task branch, it must start from this branch or an equivalent up-to-date base.
4. Confirm the governance change from PR #10 (`meta: simplify executors and consolidate foundation work on Jules`) is present in the base you are using. If PR #10 has not been merged to `main`, do not start substantive work; report that dependency instead.
5. Sync from the latest `main` using a normal non-destructive merge/update path before substantive edits. If synchronization causes conflicts, stop and report them rather than force-resolving or rewriting history.
6. Confirm the working tree is clean before substantive edits.
7. Read `AGENTS.md`, `PROJECT_STATE.md`, `docs/00-meta/source-of-truth.md`, `docs/08-plans/master/META_PLAN.md`, `docs/08-plans/workstreams/GEMINI_ASSET_FACTORY_WORKSTREAM.md`, `asset-factory/spec/README.md`, relevant Brand workbench material as provisional context only, and Issue #3 in full.
8. Treat the branch name/file names that still mention Gemini as historical. The capability contract is generator-agnostic and the current executor is Jules.

## Safety and scope

- Never write directly to `main`.
- Never force-push or rewrite history.
- Never merge your own PR.
- Do not modify Brand canon, Strategy, Technical Foundation labs or repo-hardening work except for a narrowly required interface/documentation link.
- Do not generate the final Brand asset library yet.
- Do not promote reference-only, unknown-rights or unverified-license materials to approved assets.
- Do not commit secrets, credentials or private environment values.
- If Brand V1 has not decided a value, create a schema/interface/placeholder rather than inventing the value.
- Optimize for a reusable production system, not for attractive example imagery.

## Mission

Design a complete, tool-agnostic Asset Factory architecture that can later use Gemini or another generator after Brand System V1 is frozen.

The specification must define at minimum:

- Brand Pack input contract;
- asset taxonomy;
- generation-request / prompt contracts;
- parameter schemas;
- output metadata schema;
- provenance/licensing schema;
- naming/versioning rules;
- responsive variants;
- accessibility metadata;
- generated -> staging -> reviewed -> approved/rejected lifecycle;
- QA gates;
- invent-vs-ask authority rules;
- failure/rejection/regeneration rules;
- duplicate/sprawl controls;
- batch workflow;
- handoff manifest to implementation agents.

The taxonomy must cover at least:

- SVG ornaments;
- frames, borders and dividers;
- patterns and textures;
- illustrations;
- anatomical/figurative/celestial systems when Brand V1 permits them;
- icons;
- backgrounds;
- web-section assets;
- UI decoration;
- case-study assets;
- social assets;
- deck assets;
- motion frames;
- responsive variants.

## Required implementation quality

Do not deliver prose-only architecture where a structured artifact is more useful. Create schemas, examples, lifecycle/state definitions, QA matrices, naming conventions, manifests and checklists where appropriate.

Rights/provenance must be a hard gate. Explicitly define how the system handles:

- `REFERENCE_ONLY`
- `UNKNOWN_RIGHTS`
- `UNVERIFIED_LICENSE`

None of those states may silently become `APPROVED`.

## Audit before delivery

Review the work from these perspectives:

1. Creative Director / Brand Systems
2. Design Systems Engineer
3. Production / Batch Operations
4. Web Performance
5. Accessibility
6. Licensing / Provenance
7. Maintainability / Tool Portability
8. Red Team against asset sprawl, hidden assumptions and premature Brand decisions

Correct material findings before delivery.

## Delivery

1. Review the full changed-file list.
2. Confirm every change belongs to Issue #3.
3. Confirm no secrets or unapproved Brand values were introduced.
4. Run any deterministic validation added by the workstream.
5. Commit only on the isolated Jules task branch for this workstream.
6. Open a Pull Request to `main` referencing Issue #3.
7. In the PR summarize: architecture created, schemas/contracts added, assumptions, Brand V1 dependencies, provenance controls, validation performed and unresolved risks.
8. Do NOT merge the PR.
