---
status: approved
owner: brand
created: 2026-09-23
authority: module_lock
human_approved: true
depends_on:
  - docs/08-plans/master/DIVINIVID_PRE_LOCK_EXPLORATION_V1.md
  - docs/03-brand/workbench/divinivid/generation/P4_DENSITY_LOCK_D2_EXPRESSIVE_MOSAIC_V1.md
---
# P5 Motion Grammar Lock — Registration + Negative Revelation

## Decision
The human owner selected a **hybrid motion grammar combining M-B Registration and M-C Negative Revelation**.

This closes P5.

## Selected artifact
Library:
- selected hybrid storyboard: `/DIVINIVID/visual-generation/prelock-v1/P5_MB_MC_HYBRID_SELECTED.png`
- library_file_id: `libfile_b5a4604dffb08191963577d5ec630259`

Comparison evidence:
- path: `/DIVINIVID/visual-generation/prelock-v1/P5_MOTION_COMPARISON_MA_MB_MC_MD.png`
- library_file_id: `libfile_9793d897cc688191ac84522a02247f76`

## Motion hierarchy

### Primary reveal — M-C Negative Revelation
Use for:
- hero introduction;
- section reveals;
- opening content modules;
- high-value heading/image appearance.

Principle:
Meaning appears because another layer withdraws, erodes, masks away or exposes active negative space.

The motion should feel discovered rather than inserted.

### Structural transition — M-B Registration
Use for:
- transitions between major sections;
- shifts between visual plates;
- state changes involving layered content;
- assembly/reassembly of mosaic fragments.

Principle:
Layers temporarily misregister, separate or slide out of alignment, then resolve into a coherent registered state.

The motion should create tension through controlled displacement, not glitch.

## Combined sequence
Preferred choreography:

`OBSCURE -> MISREGISTER -> REVEAL -> RESOLVE`

1. **Obscure** — much of the composition remains hidden under dark/negative plates.
2. **Misregister** — selected layers shift or separate slightly.
3. **Reveal** — negative space pulls back and exposes more of the underlying composition.
4. **Resolve** — fragments return to a stable, legible registered state.

The sequence is directional logic, not a mandatory literal four-step animation in every use.

## Secondary motion roles

### M-A Breathing Matter
Status: SECONDARY / OPTIONAL.

Allowed only as extremely subtle ambient life when needed.

Do not use as the principal motion language.

### M-D Instrument Response
Status: SECONDARY / FUNCTIONAL.

Allowed for:
- hover states;
- navigation response;
- state feedback;
- small content-specific controls.

It must obey P2 Minimal / No-Icons and must not introduce fake instrumentation.

## Timing character
The motion system should feel:
- deliberate;
- restrained;
- tactile;
- editorial;
- slightly uncanny;
- materially grounded.

Avoid frantic, elastic or entertainment-first timing.

Production timing values are not locked here; they belong to implementation testing.

## Motion invariants
Motion must preserve:
- P1 typographic authority;
- P2 Minimal / No-Icons;
- P3 H-B Editorial / Systemic hero logic;
- P4 D2 expressive mosaic;
- M1-B macro/micro ambiguity;
- B1 printed-evidence and negative-space behavior.

Motion may alter temporal relationships but must not redesign the static identity.

## Hard fails
Reject:
- RGB/glitch aesthetics;
- chromatic aberration as a default effect;
- liquid/blob morphing;
- excessive parallax;
- generic wipes/slides/fades as signature behavior;
- decorative particles;
- fake scanner/medical UI effects;
- kinetic lines with no semantic target;
- motion that obscures legibility longer than the narrative requires;
- spectacle that overwhelms the editorial hierarchy.

## Implementation boundary
P5 defines grammar, not final production parameters.

Actual:
- durations;
- easings;
- breakpoints;
- performance strategy;
- reduced-motion behavior;
- CSS/Web Animations/GSAP/motion library choice;

must be validated later in P6 / responsive and technical implementation work.

## Accessibility requirement
Any production implementation must include a reduced-motion equivalent that preserves:
- hierarchy;
- reveal order;
- content availability;
- semantic state.

Motion can enhance comprehension but cannot be required to understand the interface.

## Next handoff
P6 — Digital Behavior Lab.

P6 must test the approved visual and motion grammar on:
1. one editorial surface;
2. one functional surface.

P6 is where Figma becomes materially useful for deterministic layout, responsive behavior, component/state testing and, where warranted, motion implementation.
