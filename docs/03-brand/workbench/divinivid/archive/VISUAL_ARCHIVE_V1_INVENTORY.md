---
status: approved
owner: brand
updated: 2026-09-20
authority: evidence
depends_on:
  - ../VISUAL_UNIVERSE_CHECKPOINT_2026-09-20.md
  - ../../../../08-plans/master/DIVINIVID_VISUAL_UNIVERSE_META_PLAN_V2.md
---
# DIVINIVID — Visual Archive V1 Inventory

## Purpose
Freeze and inventory the visual evidence currently available before canon/lineage promotion and the 100-board expansion program.

This phase is intentionally **evidence-oriented**. It preserves all material visual files, including known failures, condensed five-in-one composites, experiments, duplicates and screenshots/source evidence.

The archive does **not** promote polished-looking work to canon merely because it exists.

## Inventory result

- image files: **277**
- legacy HTML visual-review/canon artifacts: **4**
- raw image payload: **616,723,114 bytes** (~588.15 MiB)
- exact duplicate records: **1**
- near-duplicate annotations: **12**

### Phase-1 status counts

| Status | Count | Meaning |
|---|---:|---|
| `UNASSESSED` | 213 | thematically organized; canon/approval promotion intentionally deferred |
| `EXPERIMENT` | 40 | auto-named/unverified experimental outputs |
| `AESTHETIC_DRIFT` | 3 | potential anti-canon drift candidates preserved for review |
| `COMPOSITE_FAILURE` | 10 | strong evidence of the known “five requested boards condensed into one” failure mode |
| `FAILED` | 5 | explicitly rejected initial Motion 21–25 attempt |
| `DUPLICATE_NEAR_DUPLICATE` | 6 | preserved copies/variants for traceability |

## Thematic working corpus

| Family | Count |
|---|---:|
| Core Identity / Visual Universe | 45 |
| Anatomy / Specimens / Transformations | 33 |
| Bestiary / Entities | 39 |
| Environments / Impossible Geometry | 18 |
| Digital / Web / Mobile UI | 16 |
| Motion Master Language | 20 |
| Editorial / Typography / Information | 33 |
| Communication / Physical | 2 |
| Asset Factory Bridge | 5 |

These counts are archive organization only. They do not prove that the family has sufficient coverage or that every file is approved.

## Explicit high-confidence negative evidence

### Initial Motion 21–25 rejection
The following files are preserved under `99_FAILURES/KNOWN_REJECTED_MOTION_21_25`:
- `divinivid_motion_21_typographic_grammar.png`
- `divinivid_motion_22_symbols_seals.png`
- `divinivid_motion_23_annotation_indexing.png`
- `divinivid_motion_24_editorial_composition.png`
- `divinivid_motion_25_data_visualization.png`

These correspond to the low-quality attempt that was explicitly rejected and later regenerated.

### Five-in-one composite failure
Ten files with strong filename signatures matching the explicitly observed failure mode are quarantined under:
`99_FAILURES/COMBINED_5_IN_1`.

Phase 2 may refine individual classification if approval/lineage evidence proves a different role.

## Duplicates / provenance notes
The archive records:
- SHA-256 for each image;
- perceptual hash;
- image dimensions;
- byte size;
- exact/near-duplicate relationship where detected;
- classification confidence;
- original filename;
- stable archive ID `DVV-VIS-####`.

One byte-identical duplicate was found. Several low-resolution/numeric copies perceptually match descriptive generated files and are retained rather than deleted.

## Delivery packaging

The single byte-preserving archive is ~589 MiB, above the reliable attachment size of the current environment. To avoid recompression, downsampling or format conversion, V1 is delivered as **eight independent ZIP volumes** plus a small index ZIP.

All volumes share the root:
`DIVINIVID_VISUAL_UNIVERSE_ARCHIVE_V1/`

Extract all volumes into the same parent directory to reconstruct the archive tree.

| Volume | Payload | Size bytes | SHA-256 |
|---|---|---:|---|
| VOL00 | Index, manifests, volume map | 56,003 | `a968b123aba78437d9a20e04623b626bc6b4ddd621ba436a143ff678d42f25f5` |
| VOL01 | Core Identity / Visual Universe | 104,994,474 | `0f11d27925d463cf8c29500c908accafb0c115d70c0f05d218945194a3cf35f0` |
| VOL02 | Anatomy / Specimens | 79,313,485 | `689696dc748d220c4bfdd4ebbbeceefc29985f55899523349d73387804cb35bc` |
| VOL03 | Bestiary / Entities | 100,156,114 | `483843e761d3b68667d7241eed15eaef7eb7dd759aaca371f6e13f9235e2e219` |
| VOL04 | Environments / Digital | 79,124,716 | `bc1f10e1910d4a0d6a1dbb816bbfcffff87d3555e7fb06b0823e6818ae9c7c78` |
| VOL05 | Motion | 38,144,941 | `ad75cc7e28e1a9f639ec3394d6b6add270b5f4a9b342ac8065aafda453cf6811` |
| VOL06 | Editorial / Communication | 77,571,181 | `13a4f2a46d074c96e7a86c740e72fb033a785c806fb3d0aa26674d6ac428c4a4` |
| VOL07 | Asset Factory + failures + evidence + legacy HTML | 41,139,230 | `0b9da1607febe5ad788a437110eeebdc2a1c6739050b5e353999c44ccd1f4fc8` |
| VOL08 | Experiments / unverified / drift candidates | 99,545,065 | `8348bdaa804f6773349cbe701c8a544f4bd047fc45762af9f90ff3d87a23e6bf` |

## Authority rule for Phase 2
Phase 2 must reconcile:
1. explicit human approvals;
2. approval evidence/screenshots where available;
3. generated-file lineage;
4. Anti-Canon;
5. supersession/replacement relationships.

Only then may a record be promoted to:
- `CANON`;
- `APPROVED_SUPPORT`;
- or a more specific negative/superseded state.

Absence of evidence remains `UNASSESSED`; it is never converted into an approval by inference.

## Phase 1 gate
**PASS.**

The currently available visual corpus has been inventoried and delivered with preserved originals, stable IDs, failure buckets and duplicate metadata.

## Next gate
**Phase 2 — Canon Promotion + Lineage Registry.**
