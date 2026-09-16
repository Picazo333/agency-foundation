# Metadata & Provenance Schema

## Overview

Every asset produced by the factory or injected into the repository must be accompanied by a strictly defined metadata sidecar file (e.g., `asset-name.meta.json`). This ensures traceability, accessibility, and legal safety.

## Core Metadata Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "asset_id": { "type": "string", "description": "Unique UUID for the asset family." },
    "version": { "type": "string", "description": "Semantic version of this specific asset." },
    "category": { "type": "string", "description": "Matches taxonomy (e.g., svg_ornament)." },
    "status": {
      "type": "string",
      "enum": ["generated", "staging", "reviewed", "approved", "rejected", "deprecated"]
    },
    "dimensions": { "type": "string" },
    "format": { "type": "string", "enum": ["svg", "png", "webp", "lottie"] },
    "accessibility": {
      "type": "object",
      "properties": {
        "alt_text": { "type": "string", "description": "Meaningful alt text for screen readers." },
        "role": { "type": "string", "enum": ["img", "presentation", "graphics-document"] }
      }
    },
    "responsive_variants": {
      "type": "array",
      "items": { "type": "string", "description": "References to other versioned files in this family." }
    },
    "provenance": { "$ref": "#/definitions/Provenance" }
  },
  "required": ["asset_id", "version", "category", "status", "format", "provenance"]
}
```

## Provenance & Rights Safety (Hard Gates)

The `provenance` block is the most critical metadata component. It tracks the legal and generative lineage of the asset.

### Provenance Schema Definition
```json
{
  "definitions": {
    "Provenance": {
      "type": "object",
      "properties": {
        "origin_type": {
          "type": "string",
          "enum": ["original_human", "generated_ai", "licensed_commercial", "open_source", "unknown"]
        },
        "generator_model": { "type": "string", "description": "e.g., gemini-1.5-pro, midjourney-v6" },
        "source_references": {
          "type": "array",
          "items": { "type": "string" },
          "description": "URLs or IDs of materials used to prompt/inform this asset."
        },
        "license_state": {
          "type": "string",
          "enum": ["CLEARED", "REFERENCE_ONLY", "UNKNOWN_RIGHTS", "UNVERIFIED_LICENSE"]
        }
      },
      "required": ["origin_type", "license_state"]
    }
  }
}
```

### Safety Rules (The Hard Gates)

The system enforces strict progression rules based on `license_state`:

1.  **`CLEARED`**: The asset is wholly original, generated safely without infringing prompts, or explicitly licensed for commercial use. **Can proceed to `approved`.**
2.  **`REFERENCE_ONLY`**: The asset was provided strictly as a mood board or stylistic reference. It cannot be used in production. **Blocked from `approved` state.**
3.  **`UNKNOWN_RIGHTS`**: The origin of the asset is untraceable, or a human uploaded an asset without providing license details. **Blocked from `approved` state.**
4.  **`UNVERIFIED_LICENSE`**: A license claim exists, but hasn't been validated by a designated human authority (e.g., verifying a stock photo purchase). **Blocked from `approved` state.**

*No asset with `REFERENCE_ONLY`, `UNKNOWN_RIGHTS`, or `UNVERIFIED_LICENSE` may silently enter the `approved` state. The CI/CD pipeline and deployment scripts will explicitly fail if such an asset is detected outside the `/assets/generated` or `/assets/staging` directories.*
