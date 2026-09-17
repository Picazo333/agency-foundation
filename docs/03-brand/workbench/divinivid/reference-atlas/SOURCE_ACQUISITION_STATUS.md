---
status: active
owner: brand
updated: 2026-09-16
authority: workbench
phase: 3
---
# DIVINIVID — Reference Atlas Source Acquisition Status

## Purpose
Track the exact visual surrogate selected for each Atlas source and make the transfer state explicit before Figma assembly.

A named artwork is not considered acquired until the exact surrogate URL, source page and rights/reuse state are recorded.

## Current verified Tier-A surrogates

### Martin Schongauer — *Saint Anthony Tormented by Demons* (1470–74)
- source: The Metropolitan Museum of Art
- source page: https://www.metmuseum.org/art/collection/search/336142
- exact image surrogate: https://collectionapi.metmuseum.org/api/collection/v1/iiif/336142/770484/main-image
- rights state: Public Domain / Met Open Access
- atlas role: `ORDER CONTAINS ANOMALY`
- acquisition state: `VERIFIED`

### Albrecht Dürer — *The Four Horsemen* (1498)
- source: National Gallery of Art
- source page: https://www.nga.gov/artworks/142352-four-horsemen
- exact image surrogate: https://api.nga.gov/iiif/232a7f4d-b3ca-42d4-ae93-39ec84701957/full/!800,800/0/default.jpg
- rights state: media explicitly marked free/public domain
- atlas role: `CONTROLLED DENSITY`
- acquisition state: `VERIFIED`

### Francesco Colonna / Aldus Manutius — *Hypnerotomachia Poliphili* (1499)
- source: The Metropolitan Museum of Art
- source page: https://www.metmuseum.org/art/collection/search/365313
- exact image surrogate: https://collectionapi.metmuseum.org/api/collection/v1/iiif/365313/726889/main-image
- rights state: Public Domain / Met Open Access
- atlas role: `TEXT / IMAGE HARMONY`
- acquisition state: `VERIFIED`

### Matthias Grünewald — *Isenheim Altarpiece: Resurrection* (1512–16)
- provenance root: Musée Unterlinden
- verified reusable surrogate: Wikimedia Commons file with Public Domain Mark
- source page: https://commons.wikimedia.org/wiki/File:Grunewald_Resurrection_Isenheim.jpg
- exact image surrogate: https://upload.wikimedia.org/wikipedia/commons/6/68/Grunewald_Resurrection_Isenheim.jpg
- rights state: Public Domain Mark; record Commons file page with any internal use
- atlas role: `DARKNESS STORES REVELATION`
- acquisition state: `VERIFIED`

### Andreas Cellarius — *Planisphaerium Arateum* from *Harmonia Macrocosmica* (1708 ed.)
- source: Library of Congress, Geography and Map Division
- source page: https://www.loc.gov/resource/g3190m.gct00305/?sp=10
- exact displayed raster root: https://tile.loc.gov/storage-services/service/gmd/gmd3m/g3190m/g3190m/gct00305/ca000010.gif
- rights state: LOC Geography and Map Division content free to use/reuse unless item-specific advisory says otherwise
- atlas role: `POLYCHROME KNOWLEDGE`
- acquisition state: `VERIFIED`; higher-resolution derivative preferred before final assembly

### Andreas Vesalius — *Fabrica Epitome* (1543)
- source: Wellcome Collection
- source page: https://wellcomecollection.org/works/g6b6smge
- representative IIIF surrogate root: https://iiif.wellcomecollection.org/thumbs/b33544189_0001.jp2/full/!200,200/0/default.jpg
- rights state: Public Domain Mark
- atlas role: `BODY AS KNOWLEDGE`
- acquisition state: `VERIFIED ROOT`; exact plate/canvas still needs selection before final board

### Master of Catherine of Cleves — *Hours of Catherine of Cleves*, ff. 80v–81r (ca. 1440)
- source: Morgan Library & Museum
- source page: https://www.themorgan.org/collection/hours-of-catherine-of-cleves/98
- exact image surrogate: https://www.themorgan.org/sites/default/files/styles/largest_800_x_800_/public/facsimile/76941/098-M945_080v-081r.jpg?itok=MvrTL0Td
- rights state: manuscript historical; Morgan digital surrogate remains `REFERENCE_ONLY` until terms are explicitly cleared for reuse
- atlas role: `SACRED POLYCHROMY / CENTER↔MARGIN`
- acquisition state: `VERIFIED / REFERENCE_ONLY`

## Figma transfer test
A controlled six-source proof sheet was attempted in the prepared `DIVINIVID — Reference Atlas` Figma file.

Result: all six remote fetches failed inside the current Figma write environment. The connector can create and edit frames, but remote HTTP image fetch is not currently a reliable acquisition path.

Implication:
- do **not** spend additional Figma calls trying arbitrary remote-image imports;
- continue acquisition/provenance outside Figma;
- Figma remains justified for final spatial assembly once image bytes can be transferred through a supported asset-upload route;
- until then, board curation and source verification continue in the repo and visual review can use source pages directly.

## Gate rule
`FIGMA_READY` requires:
1. every survivor has an exact surrogate or explicit `TEXT_ONLY / SOURCE_PENDING` exception;
2. rights state is known;
3. the image bytes can be transferred through a supported path;
4. board composition is the remaining unresolved problem.

Current Figma readiness: **NOT YET — transfer mechanism blocked, curation/provenance proceeding.**
