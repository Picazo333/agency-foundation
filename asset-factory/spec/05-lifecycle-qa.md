# Lifecycle & QA Gates

## Overview

Generated or imported assets do not become production assets automatically. They move through an auditable lifecycle that separates generation, structural checks, design review, rights review, approval, rejection, and later deprecation.

## State Machine

1. **`generated`** — raw output from a generator or newly introduced asset. Metadata is initialized; production use is forbidden.
2. **`staging`** — candidate asset proposed for review after basic structural checks relevant to its format/category.
3. **`reviewed`** — design/technical/provenance review has occurred and findings are recorded. An automated system or QA agent may assist at this stage.
4. **`approved`** — an authorized human has approved the asset for project implementation after required gates pass. The asset may move to `assets/approved/` and appear in an approved handoff manifest.
5. **`rejected`** — the asset failed one or more gates and must not be used in production.
6. **`deprecated`** — a previously approved asset has been superseded or retired and must not be selected for new implementation work unless explicitly restored.

`reviewed` and `approved` are intentionally separate. Automated or agentic review can accelerate QA, but it does not silently grant rights clearance or final production authority.

## QA Review Matrix

Before promotion to `approved`, evaluate the gates applicable to the asset.

### 1. Brand Consistency
- **Palette / tokens:** Uses only approved values and mappings required by Brand V1, where applicable.
- **Style:** Matches the approved category/illustration rules rather than only being visually attractive.
- **Anti-patterns:** Explicitly forbidden treatments are absent.
- **Composition/context:** Works in the intended surface and responsive variants rather than only in isolation.

### 2. Technical Quality
- **Format validity:** Markup/file can be parsed by the intended production toolchain.
- **SVG security:** Generated/third-party SVG must pass the separately approved production SVG security pipeline; lab regex experiments do not satisfy this gate.
- **Responsiveness:** Required family variants preserve concept, legibility and intended hierarchy.
- **Performance:** File dimensions/weight are appropriate to the intended surface and production budgets.
- **Determinism/versioning:** Asset ID, version, filename and metadata agree.

### 3. Accessibility & Context
- **Meaningful vs decorative:** Determine whether the asset conveys information or is decorative.
- **Alternative text:** Meaningful images receive concise context-appropriate alternative text; decorative assets use the appropriate empty/presentational treatment.
- **Functional contrast/state:** Functional graphics/icons satisfy the applicable accessibility requirements in their actual UI context.
- **Motion:** Motion assets provide appropriate reduced-motion/fallback behavior where required.

### 4. Provenance & Rights
- `license_state` must be `CLEARED` for production approval.
- `CLEARED` requires an authorized human rights review under `04-metadata-provenance-schema.md`.
- `REFERENCE_ONLY`, `UNKNOWN_RIGHTS`, and `UNVERIFIED_LICENSE` are hard blockers.
- Rights clearance is specific to the intended project use and does not imply a universal legal guarantee.

## Approval Record

Promotion to `approved` should record at minimum:
- approving human/reviewer;
- approval timestamp;
- asset version/hash or immutable identifier;
- applicable QA findings/exceptions;
- rights-review state;
- Brand Pack version used for review.

## Failure, Rejection & Regeneration

When an asset fails, record a specific reason. Suggested reason codes include:
- `REASON_OFF_BRAND`
- `REASON_TECHNICAL_FAIL`
- `REASON_ACCESSIBILITY_FAIL`
- `REASON_PROVENANCE_FAIL`
- `REASON_DUPLICATE`
- `REASON_CONTEXT_FAIL`

### Regeneration workflow
1. Record the failing gate and evidence.
2. Update the request/prompt constraints rather than merely hiding the failure.
3. Generate or author a new candidate.
4. Assign a new asset version, or a new `asset_id` when the concept materially changes.
5. Re-enter the normal lifecycle; prior approval never transfers automatically.

## Duplicate / Sprawl Controls

Before minting a new asset family:
- search approved and staging metadata for the semantic need;
- prefer a valid existing family/variant when it genuinely fits;
- do not create cosmetic duplicates merely because another generator/model is available;
- retain rejected candidates only when they have diagnostic or prompt-tuning value;
- archive or remove low-value rejected/stale candidates according to the future retention policy.

## Automation Boundary

Automated checks may move a candidate through machine-verifiable sub-gates, but **no automation should self-promote an asset to production approval unless project governance explicitly delegates that authority in the future**. The default for Brand V1 assets is human final approval.
