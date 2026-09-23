---
status: technical_validation_pass
owner: brand
created: 2026-09-23
updated: 2026-09-23
authority: evidence
human_approved: false
depends_on:
  - docs/03-brand/workbench/divinivid/generation/R1_SIGNATURE_SYSTEM_LOCK_SBE_V1.md
  - docs/08-plans/master/DIVINIVID_CURRENT_EXECUTION_PLAN_V2.md
  - docs/03-brand/workbench/divinivid/generation/DIVINIVID_R0_REQUIREMENT_MATRIX_V1.md
  - docs/03-brand/workbench/divinivid/generation/DIVINIVID_CORE_LOCK_V1.md
  - docs/03-brand/workbench/divinivid/generation/DIVINIVID_BASE_LOCK_B1.md
---
# R2-A Foundations — Technical Validation V1

## Scope

R2-A validates implementation viability before any aesthetic finalist comparison.

It does **not** reopen P1 Typography or R1 Signature Architecture.

Frozen inputs:
- P1: imposing dual-editorial direction;
- R1: S-BE Bilateral Body + Glyph-Class Logic;
- P2: Minimal / No-Icons;
- existing color semantics: Living Darkness, ivory/bone, Living Crimson, residual ultramar, aged-gold instrumentation.

## Decision model

Typography is split into:
- **brand/display serif** — carries ritual/editorial authority and the S-BE wordmark;
- **operational sans** — carries body, UI, data, navigation and clinical/B2B clarity.

Maximum default:
`2 families`.

R2-B must change only one major typographic variable at a time. Therefore the operational sans is fixed for the first finalist comparison and the display serif is the primary comparison variable.

---

# 1. Typography technical validation

## 1.1 Display serif candidate pool

### T1 — Newsreader

Technical status: `PASS`

- License: SIL OFL 1.1.
- Latin + Latin Extended; suitable for ES/EN.
- Variable font.
- Axes: `opsz 6–72`, `wght 200–800`.
- Roman + italic.
- Static weights/styles available.
- Designed for continuous on-screen reading in content-rich environments.
- Available in current Figma executor.
- Web/print: self-hostable; TTF/variable source available.
- Cost: `$0`.

Strength:
- strongest continuity with the R1 construction substrate;
- optical-size behavior is useful for macro/micro transition;
- less likely than a Didone to collapse into generic luxury.

Risk:
- may be insufficiently imposing at display scale unless S-BE construction supplies the signature force.

Sources:
- https://github.com/productiontype/Newsreader
- https://github.com/google/fonts/blob/main/ofl/newsreader/METADATA.pb

### T2 — Bodoni Moda

Technical status: `PASS_WITH_AESTHETIC_RISK`

- License: SIL OFL.
- Latin + Latin Extended; suitable for ES/EN.
- Variable font.
- Axes: `opsz 6–96`, `wght 400–900`.
- Roman + italic.
- Available in current Figma executor.
- Web/print: self-hostable through OFL distribution.
- Cost: `$0`.

Strength:
- highest natural monumentality/high-contrast authority of the open candidates;
- strong display range.

Risk:
- highest risk of fashion/editorial-luxury drift;
- must be judged only inside S-BE + DIVINIVID system, never as an isolated pretty wordmark.

Source:
- https://github.com/google/fonts/blob/main/ofl/bodonimoda/METADATA.pb

### T3 — Source Serif 4

Technical status: `PASS`

- License: SIL OFL 1.1.
- Open-source Adobe Originals family.
- ES/EN viable; extended multilingual support.
- Six core weights with italics; variable release available.
- Optical-size support.
- OTF / TTF / WOFF / WOFF2 / Variable releases.
- Available in current Figma executor.
- Web/print viability: excellent.
- Cost: `$0`.

Strength:
- strongest implementation robustness;
- excellent text/display flexibility;
- useful for agency, editorial, clinical/B2B and information-heavy surfaces.

Risk:
- may be too rational/generic unless S-BE supplies sufficient native character.

Sources:
- https://github.com/adobe-fonts/source-serif
- https://fonts.adobe.com/fonts/source-serif-4-variable

### T4 — Cormorant Garamond

Technical status: `PASS_NOT_SHORTLISTED`

- License: open source / OFL.
- Latin Extended.
- Five weights plus italics.
- Variable configuration supports `wght 300–700`.
- Available in current Figma executor.
- Cost: `$0`.

Reason not shortlisted:
- materially higher risk of historical revival / medieval-pastiche reading;
- the project already has strong historical material elsewhere and does not need typography to duplicate that signal.

Sources:
- https://github.com/CatharsisFonts/Cormorant
- https://github.com/google/fonts/blob/main/ofl/cormorantgaramond/upstream_info.md

### T5 — Canela

Technical status: `HOLD_PREMIUM`

- Commercial Type.
- Spanish included in supported Latin languages.
- broad weight range from Thin to Black;
- separate Canela / Deck / Text families;
- strong monumental/classical-modern character.
- trial available for evaluation.
- current displayed family pricing begins around USD 325 per family; licensing varies by use.
- desktop and web rights are separate license classes.
- **not available in current Figma executor**.
- current Commercial Type EULA includes AI-use restrictions that create operational friction for an AI-native production workflow and should be clarified before adoption.

Reason not in R2-B:
- no technical need to pay before open candidates fail;
- current executor cannot render it;
- licensing/AI workflow friction is disproportionate at this stage.

Sources:
- https://commercialtype.com/catalog/canela
- https://commercialtype.com/eula
- https://commercialtype.com/faqs

## 1.2 Operational sans candidates

### S1 — IBM Plex Sans

Technical status: `PASS / SELECTED_CONSTANT_FOR_R2-B`

- SIL OFL 1.1.
- extensive Latin and broad multilingual coverage;
- Roman + true italics;
- static families in many weights;
- variable Sans build exists with weight/width axes;
- multiple web/package delivery formats;
- available in current Figma executor;
- strong UI / technical / information-density behavior.
- Cost: `$0`.

Why selected as constant:
- more severe/technical personality than generic UI sans;
- enough identity to support DIVINIVID without competing with the serif;
- suitable for data, navigation, clinical/B2B and operational copy.

Caveat:
- production should prefer maintained static files if variable-font versioning creates deployment ambiguity.

Sources:
- https://github.com/IBM/plex
- https://github.com/IBM/plex/blob/master/LICENSE.txt

### S2 — Source Sans 3

Technical status: `PASS / FALLBACK_FINALIST`

- open-source Adobe Originals;
- broad language support;
- many weights/styles;
- variable files and WOFF/WOFF2 delivery;
- designed specifically for UI environments;
- available in current Figma executor;
- Cost: `$0`.

Why not primary:
- technically excellent but intentionally neutral;
- IBM Plex Sans better matches the approved severe operational secondary logic.

Sources:
- https://github.com/adobe-fonts/source-sans
- https://fonts.adobe.com/fonts/source-sans-3

## 1.3 R2-B typography shortlist

Keep one secondary constant and compare only the display serif:

1. **Newsreader + IBM Plex Sans**
2. **Bodoni Moda + IBM Plex Sans**
3. **Source Serif 4 + IBM Plex Sans**

This isolates the actual unresolved question:
`which serif best preserves P1 + S-BE across brand/display and macro/micro use?`

Canela remains a premium HOLD, not a required purchase.

## 1.4 Fallback strategy

Provisional technical fallback stacks:

Display:
`<selected-serif>, Georgia, "Times New Roman", serif`

Operational:
`"IBM Plex Sans", system-ui, -apple-system, "Segoe UI", Arial, sans-serif`

Exact metric overrides / `size-adjust` are deferred until implementation because they depend on the selected production serif and actual web stack.

---

# 2. Color technical validation

## 2.1 Method

Approved artifacts were sampled only to create **candidate production anchors**, not to infer new visual semantics.

Sources sampled:
- `P1_TYPOGRAPHY_WINNER_IMPOSING_DUAL_EDITORIAL.png`;
- `DIVINIVID_R02_A08_MATERIAL_BEHAVIOR.png`.

Observed artifact medians were approximately:
- darkness: RGB `6,6,4`;
- ivory material: RGB `199–206, 179–183, 154–158`;
- crimson matter: RGB `92–96, 22–28, 16–22`;
- aged-gold matter: RGB `128–133, 104–106, 71–78`;
- ultramar matter: RGB `16,33,57`.

These are evidence-derived anchors, not automatically final tokens.

## 2.2 Candidate production roles

### Living Darkness
- `darkness/950 = #060604`
- role: dominant field / deepest surface.

### Ivory
- `ivory/100 = #E8DDC9`
- role: primary readable text / high-contrast light field.
- `ivory/200 = #CEB39A`
- role: material/counterform / secondary light.

### Living Crimson
- `crimson/matter = #601C16`
- role: matter, rupture, marrow, transformation; **not body text**.
- `crimson/ui = #C15B4D`
- role: functional signal on Living Darkness when text-level contrast is required.

### Aged Gold
- `gold/instrument = #856A47`
- role: measurement, rule, instrumentation, hierarchy; not default body text.
- `gold/text = #BDA16F`
- role: rare text-capable gold on Living Darkness.

### Residual Ultramar
- `ultramar/matter = #102139`
- role: rare material/celestial depth.
- `ultramar/ui = #6984B4`
- role: rare functional ultramar on Living Darkness.

## 2.3 WCAG contrast checks against #060604

WCAG 2.2 AA:
- normal text: at least `4.5:1`;
- large text: at least `3:1`;
- meaningful non-text UI/graphics: at least `3:1`.

Measured candidate ratios:

| Token | Contrast vs #060604 | Operational result |
|---|---:|---|
| `ivory/100 #E8DDC9` | 15.08:1 | PASS normal text |
| `ivory/200 #CEB39A` | 10.18:1 | PASS normal text |
| `crimson/matter #601C16` | 1.62:1 | MATTER ONLY |
| `crimson/ui #C15B4D` | 4.70:1 | PASS normal text |
| `gold/instrument #856A47` | 4.01:1 | PASS large/non-text; FAIL normal text |
| `gold/text #BDA16F` | 8.20:1 | PASS normal text |
| `ultramar/matter #102139` | 1.25:1 | MATTER ONLY |
| `ultramar/ui #6984B4` | 5.37:1 | PASS normal text |

Important:
- pigment/matter values are allowed to fail text contrast because they are not text tokens;
- functional text/state variants are separate tokens;
- color is never the sole carrier of meaning.

Accessibility source:
- https://www.w3.org/TR/wcag/
- https://www.w3.org/WAI/WCAG22/understanding/non-text-contrast.html

## 2.4 Color conclusion

Technical status:
`PASS_TO_R2-B_CONTEXT_VALIDATION`

No second aesthetic palette is justified yet.

R2-B should validate this single candidate production set in-context against the three typographic finalists. If a color failure appears, mutate the named role rather than reopen color direction.

---

# 3. R2-A gate result

## Result
`PASS`

R2-A has produced:
- technically viable open-source typography;
- a bounded 3-pair shortlist;
- one fixed operational sans for controlled comparison;
- a premium HOLD candidate without forcing purchase;
- ES/EN viability;
- web/print delivery paths;
- licensing status;
- variable-font status;
- fallbacks;
- candidate production color values;
- measured accessibility pairings.

## Next authorized step

`R2-B — AESTHETIC / FUNCTIONAL FINALIST COMPARISON`

Figma comparison must test the same:
- S-BE wordmark architecture;
- hero statement;
- body copy;
- navigation;
- annotation/data;
- CTA;
- 32px / 16px behavior;
- candidate color production set.

Only display serif changes across finalists.
IBM Plex Sans remains fixed.

Human gate:
`PASS / MUTATE / KILL`.
