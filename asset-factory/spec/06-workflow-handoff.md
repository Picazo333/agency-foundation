# Batch Workflow & Handoff Manifest

## Overview

The Asset Factory is designed for scale. Individual generations are possible, but the primary operational mode is Batch Generation, driven by the needs of Implementation agents (e.g., "Generate all icons needed for the Dashboard view").

## Naming & Versioning Rules

Strict naming prevents chaos.

**File Naming Convention:**
`[category]--[semantic-name]--[variant]--v[version].[ext]`

*   `category`: e.g., `icon`, `illustration`, `bg`
*   `semantic-name`: Kebab-case description (e.g., `user-profile`, `hero-abstract`)
*   `variant`: `base`, `mobile`, `desktop`, `dark`, etc.
*   `version`: Integer (e.g., `v1`, `v2`)

*Example:* `icon--search-magnifier--base--v1.svg`
*Accompanying Metadata:* `icon--search-magnifier--base--v1.meta.json`

## Batch Generation Workflow

1.  **Request Manifest:** An Implementation agent (or human) authors a JSON Batch Request containing multiple individual Asset Requests.
2.  **Validation:** The Factory validates the Batch Request against the Brand Pack and taxonomy.
3.  **Execution (Async):** The Factory processes the batch, generating assets and metadata sidecars into `assets/staging/`.
4.  **Batch Review:** A QA agent reviews the staging batch. Approvals move to `assets/approved/`; rejections trigger the Regeneration workflow.
5.  **Handoff:** The Factory compiles a Handoff Manifest.

## Implementation Handoff

Implementation agents (like Codex or UI/UX agents) do not rummage through the asset folders. They consume a structured **Handoff Manifest**.

### The Handoff Contract
The Handoff Manifest provides a finalized registry of approved assets, their locations, and how to implement them.

```json
{
  "batch_id": "batch-12345",
  "status": "COMPLETED",
  "approved_assets": [
    {
      "asset_id": "uuid-001",
      "semantic_name": "hero-abstract",
      "filepath": "assets/approved/illustration--hero-abstract--base--v1.svg",
      "implementation_notes": "Requires CSS 'fill: currentColor' to support dark mode.",
      "accessibility": {
        "alt_text": "Abstract geometric network representing connectivity."
      }
    }
  ]
}
```

Implementation agents are strictly bound to only use assets listed in a valid Handoff Manifest pointing to the `assets/approved/` directory. They are explicitly forbidden from using `assets/staging/` or `assets/generated/`.
