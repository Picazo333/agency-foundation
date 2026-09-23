---
status: approved
owner: meta
created: 2026-09-23
authority: execution_policy
human_approved: true
depends_on:
  - docs/00-meta/capability-governance.md
  - docs/08-plans/workstreams/DIVINIVID_VISUAL_IDENTITY_MASTER_PLAN.md
---
# DIVINIVID Tool Execution Contracts V1

## Purpose

Tool availability is not authorization.

Every material call to an external tool, plugin, paid service or generative executor must have a concrete role in the active phase and a call-level Definition of Done.

The objective is not to minimize tool use at all costs. It is to ensure every call buys information, quality, reproducibility or implementation value.

## Global TOOL_CALL_CONTRACT

Before a material call, the executor must be able to state:

- `CALL_ID`
- `ACTIVE_PHASE`
- `QUESTION` — the uncertainty the call resolves
- `WHY_THIS_TOOL` — why this capability is materially better than a lighter available option
- `SOURCE_OF_TRUTH`
- `VARIABLE_UNDER_TEST`
- `FIXED_VARIABLES`
- `EXPECTED_OUTPUT`
- `CALL_DOD`
- `BUDGET`
- `FAILURE_ROUTE`
- `PROMOTION_RULE`

If these cannot be answered concretely, do not make the call.

## Universal per-call Definition of Done

A material call is complete only when:

1. it answers the declared question;
2. it used the authorized source inputs;
3. it did not silently change frozen variables;
4. the resulting artifact/data is technically usable at its intended resolution/format;
5. output status is explicit: `EVIDENCE_PENDING / APPROVED / QUARANTINED / IMPLEMENTATION_CANDIDATE`;
6. a relevant validation check is performed when the tool can fail silently;
7. the result changes a decision, reduces uncertainty, or creates an approved downstream dependency;
8. failure does not trigger blind rerolls.

## PAID_TOOL_GATE

For paid tools, credit-metered tools, premium MCP quotas and high-context execution:

`EXPECTED_VALUE > COST + CONTEXT_COMPLEXITY + REWORK_RISK`

Default operating budget:
- one purposeful initial call;
- at most one targeted repair when a concrete defect is identified;
- no cosmetic reroll loops;
- no premium call when an already-available lighter capability answers the same question adequately;
- no paid downstream execution before upstream prerequisites are approved.

## Tool-specific contracts

### GitHub

**Legitimate use**
- source of truth;
- contracts;
- decisions;
- lineage;
- state;
- review;
- PRs;
- CI evidence.

**Not for**
- deciding visual taste by repository state alone;
- silently promoting generated evidence to canon.

**Call DoD**
- scope-limited change;
- auditable diff;
- authority/status preserved;
- rollback path exists;
- current state remains internally coherent.

### Image generation

**Legitimate use**
- visual divergence;
- morphology;
- specimens;
- controlled mutations;
- bounded aesthetic hypotheses.

**Not for**
- exact final typography;
- exact diagrams/data;
- deterministic UI;
- deciding canon;
- changing multiple frozen identity layers at once.

**Call DoD**
- exact positive authority identified;
- maximum one primary development variable;
- frozen variables enumerated;
- no obvious drift or generic fallback;
- artifact is visually reviewable;
- status begins as `EVIDENCE_PENDING`;
- one targeted repair maximum by default.

### Figma / Figma MCP

**Legitimate use before Final Expression Lock**
- deterministic composition when exact geometry is the question;
- signature/wordmark comparison;
- typography/foundation comparison with real candidate fonts;
- responsive validation;
- component/state behavior when the identity layer exists;
- motion implementation when timing/interaction, not motion concept, is the question;
- editable assembly of already-approved visual ingredients.

**Legitimate use after Final Expression Lock**
- production design system;
- variables/tokens;
- components/variants;
- responsive layouts;
- website/product prototypes;
- handoff;
- Code Connect where justified.

**Not for**
- unresolved aesthetic invention by default;
- replacing approved imagery with surrogate reconstructions;
- silent proxy-font substitution;
- static mockups that do not answer a deterministic question;
- product/IA invention before Website Strategy/IA;
- making a design system before its identity decisions exist.

**Figma write-call DoD**
1. deterministic question declared;
2. canonical/high-resolution assets used;
3. no thumbnail/proxy asset unless explicitly testing a proxy;
4. exact candidate fonts or clearly labelled proxy/test state;
5. frozen design decisions unchanged;
6. editable structure preserved where appropriate;
7. resolution adequate for final display size;
8. post-write visual or structural validation performed;
9. no clipping, overflow or accidental rasterization of native text/diagram elements;
10. result affects a real identity/implementation decision.

Rule: **"Figma can do it" is not a reason to call Figma.**

### Runway

**Legitimate use**
- targeted image/video transformation;
- continuous motion prototype after motion grammar exists;
- temporal behavior that static storyboards can no longer answer.

**Not for**
- substitute image executor without compatibility evidence;
- discovering a new identity direction;
- generic "make it move" experimentation.

**Call DoD**
- approved static DNA preserved;
- one P5 motion behavior tested;
- duration/effect is evaluable;
- output is not promoted automatically;
- executor substitution compatibility is documented.

### Firecrawl / Web Research

**Legitimate use**
- primary-source research;
- licensing;
- font availability/licensing;
- technical documentation;
- external verification.

**Not for**
- replacing private repo truth;
- aesthetic authority by search popularity.

**Call DoD**
- question resolved with appropriate source authority;
- provenance retained;
- inference distinguished from sourced fact.

### Mobbin

**Legitimate use**
- UX/reference patterns during Digital Brand Specimen and later product/web phases.

**Not for**
- Brand aesthetic authority;
- copying another product's visual language.

**Call DoD**
- functional pattern identified;
- principle abstracted;
- no copied aesthetic promoted into canon.

### Canva

**Legitimate use**
- downstream template adaptation after identity rules are stable.

**Not for**
- identity discovery.

**Call DoD**
- approved system preserved;
- editable template fits the intended operational use.

### v0

**Authorization prerequisite**
v0 remains blocked until these inputs exist:
- Final Expression Lock;
- Website Strategy/IA;
- approved Golden Slice;
- design tokens/component contracts sufficient for implementation.

**Legitimate use**
- responsive code prototype;
- implementation acceleration;
- component implementation candidate;
- production-oriented React/Next drafts.

**Not for**
- discovering identity;
- deciding IA;
- inventing a design system;
- publishing directly.

**Call DoD**
- implements an approved frame/contract;
- responsive;
- accessible enough for the stated stage;
- no material visual drift;
- code is reviewable;
- status is `IMPLEMENTATION_CANDIDATE`, not authority.

### GitHub Actions

**Legitimate use**
- repeatable validation;
- previews;
- CI;
- accessibility/performance checks;
- visual regression after a stable reference exists.

**Not for**
- expensive design loops without a gate;
- automating an unresolved aesthetic decision.

**Call DoD**
- workflow maps to a concrete failure condition;
- output is actionable;
- cost/frequency is proportionate;
- failure is interpretable.

### New Skills / Plugins / MCPs

Follow `docs/00-meta/capability-governance.md`.

**Do not install "because it may help."**

A new capability needs:
- demonstrated gap;
- expected uplift;
- authority boundary;
- permissions/risk review;
- phase/use-case restriction;
- rollback/removal path.

## Executor substitution contract

Changing provider/tool midstream requires a compatibility check covering:
- input modalities;
- reference conditioning;
- supported controls;
- output resolution;
- determinism expectations;
- rights/data implications;
- known failure modes.

Provider substitution is not equivalent capability by default.

## Call ledger expectation

Meaningful paid/high-risk calls should be reconstructable from:
- active phase;
- purpose;
- inputs;
- output;
- result/status;
- whether a repair was consumed.

The project does not require bureaucratic logging for trivial reads. Governance depth must remain proportional to risk and cost.
