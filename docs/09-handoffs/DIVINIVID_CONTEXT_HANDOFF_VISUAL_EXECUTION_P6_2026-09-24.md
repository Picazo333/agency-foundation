---
status: superseded
owner: brand
created: 2026-09-24
updated: 2026-09-25
authority: historical_recovery_cursor
scope: visual_execution
prompt_version: 2
supersedes_chat_state: true
superseded_by: docs/09-handoffs/DIVINIVID_CONTEXT_HANDOFF_BRAND_IDENTITY_VERTICAL_SLICE_2026-09-25.md
checkpoint: docs/09-handoffs/DIVINIVID_CHECKPOINT_PRE_NOEMA_VNEXT_2026-09-24.md
supersedes:
  - docs/09-handoffs/DIVINIVID_CONTEXT_HANDOFF_P6_DIGITAL_BRAND_SPECIMEN_2026-09-23.md
---
# DIVINIVID Context Handoff — Visual Execution / P6 — 2026-09-24

## Scope

This handoff is for a **visual-execution conversation**.

Own:
- Figma P6 review;
- bounded visual mutation if the human names a concrete P6 failure;
- P6 visual evidence and QA;
- recording the final human P6 PASS/MUTATE decision.

Do not use this conversation to redesign the global program or plan P7/P8 in depth.
That belongs to:
`DIVINIVID_CONTEXT_HANDOFF_GENERAL_PROGRAM_2026-09-24.md`.

## Exact visual cursor

`P6_HUMAN_REVIEW_GATE`

## Review artifact

Figma:
`https://www.figma.com/design/bqcKhEQHs4EEQgnn6lNU8O/?node-id=34-2`

File:
`bqcKhEQHs4EEQgnn6lNU8O`

Page:
`8:2 — P6 / DIGITAL BEHAVIOR`

Specimen root:
`34:2 — P6 — DIGITAL BRAND SPECIMEN V1`

## Required surfaces

- Homepage `34:18`;
- Case Study `34:50`;
- Research/Editorial `34:72`;
- Service/System `34:86`;
- Mobile `34:117`;
- Temporal/Accessibility `34:138`.

## Final verified image lineage

- Homepage `34:48` -> B1 -> 1672×941 -> hash `6bd7451eb0900c36f22e56f3b6d2ea9c9b53e198`;
- Case `34:69` -> M1-B -> 1145×1374 -> hash `a695b8f827fa3bc867495ce2b72aa6e12b0becbb`;
- Research `34:75` -> Core -> 1672×941 -> hash `5d6063850b9799112a725bc7f009c59dcd1f0602`;
- Mobile `34:129` -> B1 -> same B1 hash as Homepage.

## Final internal QA

- canonical asset binding PASS;
- Newsreader + IBM Plex Sans only;
- text-bound/overflow issues: 0;
- Case auto-layout restored;
- no stray raster nodes in the specimen;
- full specimen visual QA: PASS_INTERNAL.

Evidence:
`docs/03-brand/workbench/divinivid/generation/P6_DIGITAL_BRAND_SPECIMEN_EVIDENCE_V1.md`.

Human gate:
`docs/03-brand/workbench/divinivid/evaluations/DIVINIVID_P6_HUMAN_REVIEW_GATE_V1.md`.

## Frozen visual authority

Do not reopen:
- Core/B1/B0/M1-B;
- P1–P5;
- R1 S-BE;
- R2 Foundations;
- R3 Composition;
- R4 Image Language;
- R5 Temporal Identity.

A P6 mutation must name a translation defect in the specimen itself.

## Next visual action

Human reviews `34:2`.

Allowed response:
- `PASS`;
- or `MUTATE: <one concrete P6 translation failure>`.

On PASS:
1. record P6 `COMPLETE_PASS / HUMAN_APPROVED`;
2. promote specimen as positive pre-lock digital evidence;
3. hand control back to General Program scope for P7 planning;
4. stop broad visual mutation.

On MUTATE:
1. identify the exact failing surface/rule;
2. apply minimum necessary reversible correction;
3. rerun relevant QA only;
4. return to this gate.

## Noema vNext boundary

This handoff is the pre-migration visual cursor.
Noema vNext may change context/eval orchestration but must not reinterpret the visual locks, Figma evidence or human gate.

## Start prompt for the new Visual Execution conversation

> Continue DIVINIVID from repo `Picazo333/agency-foundation` in **VISUAL EXECUTION scope only**.
>
> **Do not reconstruct operational state from chat memory.**
>
> ## Authority rule
>
> Use:
>
> `CURRENT AUTHORITATIVE REPO STATE > explicit current user statement > current Figma evidence > pre-Noema checkpoint > handoff text > historical chat`.
>
> The pre-Noema checkpoint is a migration anchor, not a reason to revert newer state.
>
> ## Required read order
>
> Read before any Figma mutation:
>
> 1. `docs/03-brand/workbench/divinivid/generation/CURRENT_GENERATION_STATE.yaml`
> 2. `docs/03-brand/workbench/divinivid/BRAND_STATE.md`
> 3. `docs/03-brand/workbench/divinivid/generation/P6_DIGITAL_BRAND_SPECIMEN_EVIDENCE_V1.md`
> 4. `docs/03-brand/workbench/divinivid/evaluations/DIVINIVID_P6_HUMAN_REVIEW_GATE_V1.md`
> 5. `docs/09-handoffs/DIVINIVID_CHECKPOINT_PRE_NOEMA_VNEXT_2026-09-24.md`
> 6. `docs/09-handoffs/DIVINIVID_CONTEXT_HANDOFF_VISUAL_EXECUTION_P6_2026-09-24.md`
>
> If Noema vNext has already introduced a newer project-state representation, inspect it only after the canonical sources above and reconcile it rather than allowing it to reinterpret visual authority.
>
> ## Mandatory startup reconciliation
>
> Before touching Figma, verify:
>
> - current visual cursor;
> - current P6 gate outcome: `PENDING / PASS / MUTATE`;
> - whether specimen root `34:2` is still the current P6 authority;
> - whether canonical asset lineage and deterministic QA remain valid;
> - whether any change since the pre-Noema checkpoint materially affects P6;
> - whether Noema migration created an authority/state discrepancy.
>
> If the repo already records `P6 COMPLETE_PASS / HUMAN_APPROVED`, **do not reopen P6**. Report that the visual scope is complete and hand control to General Program.
>
> ## Figma authority if P6 is still pending
>
> File:
> `bqcKhEQHs4EEQgnn6lNU8O`
>
> Page:
> `8:2 — P6 / DIGITAL BEHAVIOR`
>
> Current specimen root:
> `34:2 — P6 — DIGITAL BRAND SPECIMEN V1`
>
> Review URL:
> `https://www.figma.com/design/bqcKhEQHs4EEQgnn6lNU8O/?node-id=34-2`
>
> The old probe `11:2` is quarantined negative evidence and must never replace `34:2` as positive authority.
>
> ## Verified baseline
>
> At the pre-Noema checkpoint:
>
> - Homepage `34:48` -> canonical B1;
> - Case `34:69` -> canonical M1-B;
> - Research `34:75` -> canonical Core;
> - Mobile `34:129` -> same canonical B1 as Homepage;
> - Newsreader + IBM Plex Sans only;
> - text overflow/bounds failures = 0;
> - Case auto-layout repaired;
> - no stray raster nodes;
> - structural QA = PASS;
> - internal visual QA = PASS.
>
> Re-check only what could materially have changed. Do not rerun completed audits by default.
>
> ## Scope owned by this conversation
>
> Own:
>
> - P6 Figma human-review support;
> - bounded visual correction if the human names a concrete P6 translation failure;
> - relevant post-mutation QA;
> - P6 evidence/gate state updates;
> - recording the explicit human P6 PASS/MUTATE outcome.
>
> Do **not**:
>
> - plan P7/P8 in depth;
> - redesign the global program;
> - build the final website;
> - start Website Strategy/IA;
> - build the production Figma design system;
> - start v0/code;
> - invent a new palette, type family, signature or image family;
> - reopen R1–R5 because of taste disagreement.
>
> ## Frozen visual authority
>
> Do not reopen:
>
> - Core/B1/B0/M1-B;
> - P1–P5;
> - R1 S-BE;
> - R2 Foundations;
> - R3 Composition;
> - R4 Image Language;
> - R5 Temporal Identity;
> - System Formalization Gate PASS.
>
> A mutation is allowed only for a **named P6 translation defect**.
>
> ## Human decision logic
>
> If the human says `PASS`:
>
> 1. verify the current specimen has not materially changed since the latest QA;
> 2. record `P6 COMPLETE_PASS / HUMAN_APPROVED` in the human gate;
> 3. update `CURRENT_GENERATION_STATE.yaml`, Execution Plan, `PROJECT_STATE.md`, `BRAND_STATE.md` and P6 evidence so they agree;
> 4. promote `34:2` as positive **pre-lock digital evidence**, not as final website design;
> 5. mark the Visual Execution handoff complete/superseded;
> 6. activate/hand off `P7_APPLICATION_STRESS` to General Program scope;
> 7. stop broad visual mutation.
>
> If the human says `MUTATE: <specific failure>`:
>
> 1. restate the exact failing surface/rule;
> 2. classify the failure before changing tools or strategy;
> 3. apply the minimum deterministic/reversible Figma correction;
> 4. do not change unrelated surfaces;
> 5. rerun only the relevant structural + visual QA;
> 6. update P6 evidence;
> 7. return to `P6_HUMAN_REVIEW_GATE`.
>
> If the user gives an ambiguous reaction rather than PASS/MUTATE, inspect and explain the relevant surface but **do not promote the gate**.
>
> ## Tool discipline
>
> Figma is authorized for deterministic P6 correction/review only.
>
> New image generation is prohibited unless:
>
> - a concrete missing visual asset is proven;
> - existing canonical assets cannot satisfy the requirement;
> - the user explicitly authorizes reopening that bounded need.
>
> Do not substitute low-resolution proxies, generated lookalikes or the quarantined probe.
>
> ## Noema vNext boundary
>
> Noema may change context/eval orchestration but may not reinterpret:
>
> - the visual locks;
> - Figma node authority;
> - asset lineage;
> - prior human approvals;
> - current gate outcome.
>
> If Noema state conflicts with the current repo/Figma evidence, stop mutation and resolve the authority-state discrepancy first.
>
> ## Expected first response
>
> Return a compact **VISUAL STATE RECONCILIATION**:
>
> 1. current P6 gate outcome;
> 2. authoritative Figma root;
> 3. whether baseline QA remains valid;
> 4. material delta since checkpoint, if any;
> 5. next allowed visual action.
>
> If P6 is still pending, present the human review question and wait for `PASS` or a specific `MUTATE`. Do not self-approve the gate.
