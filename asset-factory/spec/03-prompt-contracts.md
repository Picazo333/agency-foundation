# Prompt Contracts & Parameter Schemas

## Overview

Prompting the Asset Factory generator is not an ad-hoc exercise. Generation requests are structured contracts that merge immutable Brand Pack context with specific request parameters.

## Generation Request Schema

A valid generation request must conform to a JSON schema encompassing these fields:

```json
{
  "type": "object",
  "properties": {
    "request_id": { "type": "string", "description": "Unique UUID for tracing this request." },
    "category": { "type": "string", "enum": ["svg_ornament", "illustration", "icon", "..."] },
    "description": { "type": "string", "description": "Semantic description of the asset needed." },
    "dimensions": {
      "type": "object",
      "properties": {
        "width": { "type": "integer" },
        "height": { "type": "integer" },
        "aspect_ratio": { "type": "string" }
      }
    },
    "variants_requested": {
      "type": "array",
      "items": { "enum": ["mobile", "desktop", "dark_mode", "light_mode"] }
    },
    "reference_materials": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "url": { "type": "string" },
          "handling": { "enum": ["stylistic_reference_only", "strict_trace_authorized"] }
        }
      }
    }
  },
  "required": ["request_id", "category", "description"]
}
```

## Reusable Prompt Templates

The system dynamically constructs the final prompt sent to the LLM/Generator:

`[GLOBAL_BRAND_CONTEXT] + [CATEGORY_RULES] + [SPECIFIC_REQUEST_PARAMETERS] + [NEGATIVE_CONSTRAINTS]`

*   **Global Brand Context:** Injected automatically from the frozen `BrandPack`. (e.g., "Use only colors from the primary palette. Maintain a flat geometric style.")
*   **Category Rules:** Injected based on the `category` field. (e.g., if category is `icon`, inject "Must align to a 24x24 grid, 2px stroke, no fills.")
*   **Specific Request:** The user's `description`. (e.g., "A stylized magnifying glass representing 'search'.")
*   **Negative Constraints:** Injected from the Brand Pack anti-patterns. (e.g., "Do NOT use drop shadows. Do NOT use gradients.")

## Invent-vs-Ask Authority Rules

The generator must distinguish between creative decisions it is authorized to make autonomously and decisions requiring human/Brand intervention.

### Allowed to Invent (Autonomy)
*   **Compositional Layout:** Arranging elements within requested dimensions as long as grid rules are obeyed.
*   **Palette Selection:** Choosing which specific colors from the approved palette to use for which elements (unless strictly mapped in tokens).
*   **Shape Generation:** Creating new geometric or organic forms that match the established Brand Pack style.
*   **Safe Fallbacks:** If a requested variant is impossible due to space constraints, simplifying the asset (e.g., removing a background element in the mobile variant).

### Must Ask (Requires Authority / Rejection)
*   **Palette Deviation:** If the generator determines an asset needs a color outside the Brand Pack, it must reject the prompt, not invent a color.
*   **Missing Brand Data:** If the Brand Pack lacks a definition for a required property (e.g., requested an illustration, but `illustrationRules` are missing), the generator must halt and request human definition.
*   **Rights Uncertainty:** If a reference image is provided without explicit handling rules, the generator must assume `REFERENCE_ONLY` and cannot emit an output that directly copies the reference.
*   **Format/Dimension Conflict:** If requested dimensions conflict with category rules (e.g., requesting a 1920x1080 `icon`), it must reject the request.
