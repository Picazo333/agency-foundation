# Lifecycle & QA Gates

## Overview

Assets do not spring into production immediately upon generation. They follow a strict, auditable lifecycle. This ensures quality, consistency, and legal safety before an asset reaches the Implementation agents.

## State Machine

The lifecycle of an asset is defined by the following sequential states:

1.  **`generated`**: The raw output from the Asset Factory (or human upload). Resides only in temporary or sandbox directories. Metadata is initialized.
2.  **`staging`**: The asset is proposed for inclusion in the broader project. Initial automated structural checks (e.g., SVG validity) have passed.
3.  **`reviewed`**: A human or designated QA agent has inspected the asset against the Brand Pack and specific QA gates.
4.  **`approved`**: The asset is cleared for use by Implementation agents. It is moved to the canonical `assets/approved/` directory.
5.  **`rejected`**: The asset failed review. It is retained for analysis/prompt-tuning but must not be used.
6.  **`deprecated`**: An previously `approved` asset is superseded by a new version or removed from the active brand system.

## QA Gates (The Review Matrix)

Before moving from `staging` to `approved`, an asset must pass the following checks:

### 1. Brand Consistency
*   **Palette:** Does it strictly use only allowed Brand Pack colors? (Automated hex check).
*   **Style:** Does the visual approach match the `illustrationRules` (e.g., line-art vs. flat)?
*   **Anti-patterns:** Are forbidden elements (e.g., drop shadows, unauthorized gradients) absent?

### 2. Technical Quality
*   **SVG Validity:** Is the markup valid XML? Are there inline styles that should be CSS? Is it bloated with unnecessary metadata (e.g., Illustrator cruft)?
*   **Responsiveness:** If a variant family (mobile/desktop), do the assets align visually while respecting their specific constraints?
*   **Performance:** Is the file size optimized?

### 3. Accessibility & Context
*   **Contrast:** Do adjacent colors meet WCAG contrast requirements (especially for functional icons)?
*   **Metadata:** Is meaningful `alt_text` and the correct ARIA `role` present in the metadata sidecar?

### 4. Provenance & Licensing
*   **Rights:** Is `license_state` strictly `CLEARED`? (See `04-metadata-provenance-schema.md`).

## Failure, Rejection & Regeneration

### Rejection Handling
When an asset is rejected, the reviewer must append a specific rejection reason to the metadata:

*   `REASON_OFF_BRAND`: Visually attractive, but violates Brand Pack.
*   `REASON_TECHNICAL_FAIL`: Bloated SVG, broken markup.
*   `REASON_PROVENANCE_FAIL`: Unknown rights, or too close to a reference image.

### Regeneration Workflow
Instead of manually tweaking a rejected `generated` asset, the standard flow is to:
1. Update the Prompt Request constraints based on the rejection reason.
2. Issue a new generation request.
3. The new asset receives a new `version` tag or a completely new `asset_id` depending on the severity of the change.

### Duplicate / Sprawl Controls
To prevent an explosion of near-identical generated assets:
*   Generators must first search existing `approved` and `staging` assets for the requested semantic concept before generating a new one.
*   If a visually similar asset exists, the generator proposes re-using it rather than minting a duplicate.
*   Batch cleanups periodically archive `rejected` and long-stagnant `staging` assets.
