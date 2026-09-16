# Metadata & Provenance Schema

## Overview

Every asset produced by the factory or introduced into the governed asset pipeline must carry metadata sufficient to trace its identity, lifecycle, accessibility intent, source lineage, and rights-review state. The metadata sidecar is a control surface for review; it is not by itself a legal opinion or proof of ownership.

## Core Metadata Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "asset_id": { "type": "string", "description": "Stable identifier for the asset family." },
    "version": { "type": "string", "description": "Version of this specific asset." },
    "category": { "type": "string", "description": "Matches the governed asset taxonomy." },
    "status": {
      "type": "string",
      "enum": ["generated", "staging", "reviewed", "approved", "rejected", "deprecated"]
    },
    "dimensions": { "type": "string" },
    "format": { "type": "string", "enum": ["svg", "png", "webp", "lottie"] },
    "accessibility": {
      "type": "object",
      "properties": {
        "alt_text": { "type": "string", "description": "Meaningful alternative text when the asset conveys information; decorative assets may intentionally use an empty value." },
        "role": { "type": "string", "enum": ["img", "presentation", "graphics-document"] }
      }
    },
    "responsive_variants": {
      "type": "array",
      "items": { "type": "string", "description": "References to related versioned files in this asset family." }
    },
    "provenance": { "$ref": "#/definitions/Provenance" }
  },
  "required": ["asset_id", "version", "category", "status", "format", "provenance"]
}
```

## Provenance & Rights Review

The `provenance` block records what is known about an asset's origin and whether an authorized reviewer has cleared it for the intended project use.

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
        "generator_model": {
          "type": ["string", "null"],
          "description": "Provider/model identifier when AI generation materially contributed to the asset."
        },
        "source_references": {
          "type": "array",
          "items": { "type": "string" },
          "description": "URLs or internal IDs for source/reference material that materially informed the asset."
        },
        "license_state": {
          "type": "string",
          "enum": ["CLEARED", "REFERENCE_ONLY", "UNKNOWN_RIGHTS", "UNVERIFIED_LICENSE"]
        },
        "rights_reviewed_by": {
          "type": ["string", "null"],
          "description": "Authorized human reviewer when license_state is CLEARED."
        },
        "rights_reviewed_at": {
          "type": ["string", "null"],
          "format": "date-time"
        },
        "rights_notes": {
          "type": ["string", "null"],
          "description": "Scope, license record, restrictions, or rationale relevant to the clearance decision."
        }
      },
      "required": ["origin_type", "license_state"]
    }
  }
}
```

## License-State Gates

1. **`CLEARED`** — an authorized human reviewer has determined that available provenance/license evidence is sufficient for the asset's intended project use. This is a project workflow state, **not a universal legal guarantee**. A production-approved asset should record `rights_reviewed_by` and `rights_reviewed_at`.
2. **`REFERENCE_ONLY`** — material may inform mood, direction, or analysis but is not cleared for production use. Block from `approved`.
3. **`UNKNOWN_RIGHTS`** — origin or rights are not sufficiently known. Block from `approved`.
4. **`UNVERIFIED_LICENSE`** — a license claim exists but has not been verified by an authorized reviewer. Block from `approved`.

No asset in `REFERENCE_ONLY`, `UNKNOWN_RIGHTS`, or `UNVERIFIED_LICENSE` may be promoted to `approved` or included in an approved handoff manifest.

## Enforcement Boundary

The architecture requires future validators/CI/deployment tooling to enforce these states before production consumption. **That enforcement is not assumed to exist merely because this specification exists.** Until automated enforcement is implemented and tested, the human approval gate and manifest review are mandatory.

The implementation-facing provenance contract under `packages/assets/` should remain a compatible subset of these field names and license-state semantics rather than creating a competing vocabulary.
