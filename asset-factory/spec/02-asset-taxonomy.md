# Asset Taxonomy

## Overview

This taxonomy defines the categorical structure for all output from the Asset Factory. Every generated asset must belong to one of these explicit categories, determining its metadata requirements, QA gates, and responsive behavior.

## Categories

### 1. Primitives & Foundations
*   **SVG Ornaments:** Small, non-semantic decorative flourishes (asterisks, arrows, abstract shapes).
*   **Borders / Frames / Dividers:** Line rules, framing devices for content, edge treatments.
*   **Patterns & Textures:** Repeating background tiles, grain overlays, brand-specific noise.

### 2. Illustration & Imagery
*   **Illustration Families:** Hero illustrations, empty-state graphics, conceptual spot illustrations.
*   **Anatomical / Figurative Plates:** (Pending Brand V1 authorization). Diagrammatic breakdowns of organic or mechanical subjects.
*   **Celestial / Diagrammatic Systems:** Abstract representations of data, networks, or process flows.
*   **Backgrounds:** Abstract fields, gradients, or scenes used primarily behind content.

### 3. Interface Assets
*   **Icons:** Scalable vector symbols representing actions, objects, or concepts. Usually constrained to strict grids (e.g., 24x24, 16x16).
*   **UI Decoration:** Embellishments tightly coupled to interface components (e.g., custom radio button states, tooltip tails).

### 4. Layout & Context-Specific
*   **Web-Section Art:** Large, composite visual assets designed for specific page regions (e.g., Hero, Footer, Feature block).
*   **Case-Study Assets:** Standardized mockups, device frames, and presentation layouts for portfolio work.

### 5. Marketing & Output Formats
*   **Social Formats:** Assets pre-cropped and composed for specific social platforms (e.g., 1080x1080 IG, 1200x630 OG Image).
*   **Deck / Presentation Assets:** Slide templates, chart graphics, standard slide layouts.

### 6. Dynamic Assets
*   **Motion Frames / Sequences:** Keyframes, Lottie JSON, sprite sheets, or storyboards for animation.

## Responsive Variants Handling

For categories where size and context dictate form (e.g., Web-Section Art, Illustration Families), the asset must include responsive variants:

*   **Small / Mobile:** Simplified form, larger stroke relative to canvas, minimal detail.
*   **Medium / Tablet:** Standard form, balanced detail.
*   **Large / Desktop:** Extended canvas, maximum detail, horizontal orientation often preferred.

All variants of a single concept must share a core `asset_id` and be tracked as a cohesive family in metadata.
