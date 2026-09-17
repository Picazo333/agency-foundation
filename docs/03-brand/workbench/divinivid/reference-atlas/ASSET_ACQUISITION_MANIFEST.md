---
status: review
owner: brand
updated: 2026-09-16
authority: workbench
depends_on:
  - PHASE_3_CURATION_PASS_2.md
  - ../reference-research/SOURCE_REGISTRY.md
---
# DIVINIVID Reference Atlas — Asset Acquisition Manifest

## Purpose
Acquire the **minimum exact visual surrogate set** required to assemble the five approved-for-review boards plus Anti-Atlas without wasting Figma operations or introducing untracked rights risk.

This manifest is about internal research-board images only. It does not authorize production use.

## Acquisition policy
For every asset record:
1. use the collecting institution / archive / artist foundation when possible;
2. prefer Public Domain / Open Access / CC surrogates for historical work;
3. record the exact item page and image-rights state;
4. for film/contemporary art/architecture, retain `REFERENCE_ONLY` unless a reuse license is explicit;
5. do not download from Pinterest, repost blogs, AI recreation sites or anonymous scan aggregators;
6. if the authoritative source does not expose a practical visual surrogate, use a reputable secondary source **only for the internal Atlas** and preserve the primary provenance root beside it.

---

# Tier A — acquire first: low-friction historical/open-access anchors

These assets carry the largest mechanism yield and the lowest rights friction. They should be acquired before copyrighted film/contemporary references.

| ID | Exact source object | Preferred provenance | Rights target | Boards |
|---|---|---|---|---|
| A01 | Martin Schongauer — *Saint Anthony Tormented by Demons* | Metropolitan Museum of Art | Open Access / Public Domain | 02, 05 |
| A02 | Andreas Vesalius — *Fabrica/Epitome* anatomical plate | Wellcome Collection | Public Domain Mark | 02, 04 |
| A03 | Andreas Cellarius — *Planisphaerium Arateum* / *Harmonia Macrocosmica* | Library of Congress | free use/reuse unless advisory says otherwise | 04, 05 |
| A04 | Albrecht Dürer — *The Four Horsemen* | National Gallery of Art | public-domain media | 04 |
| A05 | *Hypnerotomachia Poliphili* — selected text/woodcut spread | Metropolitan Museum of Art | Open Access / Public Domain | 04 |
| A06 | Robert Fludd — selected macrocosm/microcosm diagram | Wellcome Collection | Public Domain Mark | 04 |
| A07 | Matthias Grünewald — Isenheim *Resurrection* surrogate | Musée Unterlinden provenance + verified PD/CC surrogate if available | historical artwork; verify digital surrogate | 01, 05 |
| A08 | Matthias Grünewald — Isenheim *Crucifixion* surrogate | Musée Unterlinden provenance + verified PD/CC surrogate if available | historical artwork; verify digital surrogate | 02, 05 |
| A09 | William Blake — *Book of Job* selected plate | British Museum | historical work; verify image terms | 01, 04, 05 |
| A10 | William Blake — *Behemoth and Leviathan* | British Museum | historical work; verify image terms | 02 |
| A11 | Hours of Catherine of Cleves — *Resurrection*, ff. 73v–74r | Morgan Library | historical work; verify digital surrogate | 01, 05 |
| A12 | Hours of Catherine of Cleves — page architecture / border example | Morgan Library | historical work; verify digital surrogate | 04 |
| A13 | Luttrell Psalter — selected grotesque marginalia page | British Library | verify digital surrogate terms | 02 |
| A14 | Aberdeen Bestiary — selected creature/classification page | manuscript host / scholarly project | verify digital surrogate terms | 02, 04 |
| A15 | Beatus of Liébana — selected saturated Apocalypse page | British Library | verify digital surrogate terms | 01 |
| A16 | Hieronymus Bosch — selected Saint Anthony/grotesque detail | Museo del Prado | historical work; verify image terms | 02 |
| A17 | Odilon Redon — selected noir / Eye work | MoMA | historical object; verify image terms | 02 |
| A18 | Caravaggio — *The Calling of Saint Matthew* or equivalent tenebrist anchor | authoritative church/museum/open surrogate | historical artwork; verify photography | 01, 03 |

## Tier-A acceptance rule
If an authoritative source image is too low-resolution for board reading, a second surrogate may be used **only** when:
- its attribution is stable;
- rights state is visible;
- the authoritative provenance root remains recorded.

---

# Tier B — reference-only copyrighted anchors

These are necessary for mechanism diversity but must never silently migrate into Brand production assets.

| ID | Exact source object | Preferred source | Rights state | Boards |
|---|---|---|---|---|
| B01 | *The Color of Pomegranates* — tableau still | Criterion Collection | REFERENCE_ONLY | 01, 05 |
| B02 | *Kwaidan* — luminous supernatural color still | Criterion Collection | REFERENCE_ONLY | 01 |
| B03 | Bruder Klaus Field Chapel — interior / oculus | Pritzker / ArchDaily / credited photographer | REFERENCE_ONLY unless licensed | 01, 03, 05 |
| B04 | *Macario* — darkness / metaphysical still | authoritative archive/distributor | REFERENCE_ONLY | 03, 05 |
| B05 | *The Seventh Seal* — figure/void still | authoritative archive/publisher | REFERENCE_ONLY | 03 |
| B06 | *The Night of the Hunter* — silhouette/void still | Criterion Collection | REFERENCE_ONLY | 03 |
| B07 | *Vampyr* — spectral half-light still | BFI / authoritative archive | REFERENCE_ONLY | 03 |
| B08 | Pierre Soulages — *Outrenoir* example | Musée Soulages | REFERENCE_ONLY unless explicit image license | 03, 05 |
| B09 | *Andrei Rublev* — matter/weather/ritual still | Criterion Collection | REFERENCE_ONLY | 03 |
| B10 | Bill Viola — *The Crossing* | museum/institutional exhibition record | REFERENCE_ONLY | 05 |

## Tier-B visual rule
Use only the minimum crop needed to understand the mechanism. The internal Atlas is not a substitute for a licensed production library.

---

# Unique asset count

Current target before Anti-Atlas:
- Tier A: **18** source assets;
- Tier B: **10** source assets;
- total unique positive-board assets: **28**.

Because references intentionally recur across boards for different mechanisms, 28 unique source images are enough to populate 42 board placements without sourcing 42 unrelated images.

This is deliberate: **mechanism clarity > reference quantity**.

---

# Board assembly mapping

## 01 — DIVINE / ILLUMINATION
`A11, A07, B01, A18, A09, B03, B02, A15`

## 02 — GROTESQUE / CORPOREAL
`A01, A14, A13, A16, A02, A08, A17, A10`

## 03 — DARKNESS / REVELATION
`B04, B05, B06, B07, A18, B08, B03, B09`

## 04 — ORDER / KNOWLEDGE
`A02, A03, A09, A05, A04, A12, A14, A06`

## 05 — RECONCILIATION
`A07/A08 relationship, A11, A01, B01, B04, B08, B03, A03, A09, B10`

---

# Figma assembly trigger

Figma assembly begins only when:
- all 28 positive-board source assets have either an exact surrogate or an explicit `TEXT_ONLY / SOURCE_PENDING` exception;
- every image has source + rights metadata;
- no unresolved question remains about whether the source belongs on the board.

At that point Figma is the correct tool because the unresolved questions become:
- relative visual weight;
- crop and scale;
- color balance;
- rhythm and negative space;
- board-to-board overlap;
- whether the thesis reads visually without explanatory prose.

## Figma call budget principle
Prefer **few high-density write calls**:
1. create/clean six pages or sections and board skeletons;
2. upload/position source assets in batches;
3. run one composition-refinement pass;
4. capture only the screenshots needed for human gate review.

Do not spend individual calls per reference when a batch operation is possible.

---

# Anti-Atlas acquisition

Anti-Atlas is intentionally deferred until the positive boards are visually assembled.
Reason: the Anti-Atlas should demonstrate **the actual failure modes adjacent to the chosen visual universe**, not generic styles in the abstract.

Its ten categories remain locked, but example selection follows the first positive-board composition review.

---

# Current gate

Asset manifest: **PASS**.

Next operational step:
**Acquire and verify Tier A first, then Tier B; only then spend Figma calls on visual assembly.**
