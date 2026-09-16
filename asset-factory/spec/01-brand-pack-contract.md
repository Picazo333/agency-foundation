# Brand Pack Contract

## Overview

The Brand Pack is the foundational input layer for the Asset Factory. It strictly governs the aesthetic and compositional parameters for all asset generation. The factory cannot generate production assets without a complete, validated Brand Pack.

## Required Sections

A valid Brand Pack must define the following areas:

### 1. Global Identity
*   **Brand Name:** Placeholder until Brand V1 freezes.
*   **Archetype/Voice:** Tone parameters that influence illustration or graphic style.
*   **Core Concepts:** Foundational visual metaphors.

### 2. Design Tokens & Palette
*   **Primary Palette:** Core brand colors (e.g., `#hex`, RGB).
*   **Secondary/Accent Palette:** Acceptable accents and their specific usage constraints.
*   **Neutral Palette:** Backgrounds, borders, text colors.
*   **Token Mapping:** Semantic mapping (e.g., `color.primary.base`, `color.surface.subdued`).

### 3. Typography Rules
*   **Primary Typeface:** Name, weight, style, licensed usage.
*   **Secondary Typeface:** Name, weight, style, licensed usage.
*   **Typographic Hierarchy:** Scale, line height, letter spacing for embedding text inside graphic assets if required.

### 4. Graphic & Illustration Rules
*   **Illustration Style:** e.g., Line-art, flat vector, 3D, isometric, photorealistic.
*   **Line Weight & Stroke:** Base thickness, scaling rules.
*   **Corner Radii:** Sharp vs. rounded, specific pixel/rem values.
*   **Shading & Texture:** Acceptable gradients, stippling, flat fill, or noise.

### 5. Motion Rules
*   **Easing Curves:** Standard brand easing functions (e.g., `cubic-bezier`).
*   **Duration/Timing:** Standard pacing for micro-interactions vs. macro-animations.

### 6. Composition & Anti-patterns
*   **Grid System:** Base grid (e.g., 8pt, 4pt).
*   **White Space / Margin:** Density rules.
*   **Anti-patterns:** Explicit "do not do this" examples (e.g., "no drop shadows", "no gradients", "avoid human faces").

## JSON Schema Example (Placeholder)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "BrandPack",
  "type": "object",
  "properties": {
    "version": { "type": "string" },
    "palette": {
      "type": "object",
      "properties": {
        "primary": { "type": "array", "items": { "type": "string" } },
        "secondary": { "type": "array", "items": { "type": "string" } }
      }
    },
    "illustrationRules": {
      "type": "object",
      "properties": {
        "style": { "type": "string" },
        "lineWeight": { "type": "string" },
        "antiPatterns": { "type": "array", "items": { "type": "string" } }
      }
    }
  },
  "required": ["version", "palette", "illustrationRules"]
}
```
