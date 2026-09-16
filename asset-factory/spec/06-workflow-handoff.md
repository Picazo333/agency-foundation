# Batch Workflow & Implementation Handoff

## Overview

The Asset Factory should support individual requests and governed batches without coupling the architecture to one generation provider. Batch generation is useful when implementation needs a coherent family of assets, but scale must not bypass review or provenance gates.

## Naming & Versioning Rules

**File naming convention:**

`[category]--[semantic-name]--[variant]--v[version].[ext]`

- `category` — taxonomy category such as `icon`, `illustration`, `bg`.
- `semantic-name` — kebab-case functional/concept name.
- `variant` — `base`, `mobile`, `desktop`, `dark`, etc.
- `version` — integer version for the file artifact.

Example:
`icon--search-magnifier--base--v1.svg`

Metadata sidecar:
`icon--search-magnifier--base--v1.meta.json`

The filename is not the source of truth for approval; the metadata/manifest must agree with the actual reviewed file/version.

## Batch Workflow

1. **Request manifest** — a human or implementation agent authors a structured batch request containing individual asset requests.
2. **Input validation** — validate category, dimensions/variants, Brand Pack availability, reference handling, and required provenance fields before generation.
3. **Execution** — an approved provider/tool generates candidates into the governed generated/staging area; no candidate is production-ready at this step.
4. **Machine/agent pre-review** — run applicable structural, duplication, accessibility, technical and Brand-rule checks. Findings are recorded; automated review cannot grant final rights clearance.
5. **Human approval** — an authorized reviewer resolves remaining visual/context/provenance questions and explicitly promotes eligible versions to `approved`.
6. **Handoff manifest** — compile only approved immutable asset versions into the implementation handoff.

A rejected or changed asset re-enters the lifecycle and cannot inherit approval merely because it belongs to an already approved batch/family.

## Implementation Handoff

Implementation agents should consume a structured **Handoff Manifest** instead of discovering arbitrary files in generated/staging folders.

### Handoff Contract

A valid manifest identifies approved files, exact versions, accessibility intent and implementation notes.

```json
{
  "batch_id": "batch-12345",
  "status": "COMPLETED",
  "brand_pack_version": "v1.0.0",
  "approved_assets": [
    {
      "asset_id": "uuid-001",
      "version": "1",
      "semantic_name": "hero-abstract",
      "filepath": "assets/approved/illustration--hero-abstract--base--v1.svg",
      "implementation_notes": "Uses currentColor where documented by the reviewed SVG contract.",
      "accessibility": {
        "alt_text": "Abstract network representing connectivity.",
        "role": "img"
      },
      "provenance": {
        "license_state": "CLEARED",
        "rights_reviewed_by": "reviewer-id"
      }
    }
  ]
}
```

## Consumer Rules

Implementation agents:
- may use only the exact asset versions listed in a valid approved handoff manifest;
- must not promote or consume `generated`, `staging`, `rejected`, or `REFERENCE_ONLY` material as production assets;
- must not silently swap a listed file for a newer version;
- should treat missing/contradictory metadata as a blocking asset-contract issue rather than inventing approval;
- must preserve accessibility/implementation requirements recorded in the manifest.

## Provider Independence

The handoff contract does not assume Gemini, Runway, an image model, a human illustrator, or any other particular producer. Provider-specific metadata may be recorded inside provenance, while the consumer contract remains stable.

## Future Automation

A future implementation may generate manifests and enforce folder/license rules automatically. Until that validator exists and is tested, the manifest plus human approval record is the governing gate. This specification must not be interpreted as evidence that CI enforcement already exists.
