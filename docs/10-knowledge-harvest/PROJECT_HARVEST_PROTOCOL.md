---
status: review
owner: meta
updated: 2026-09-16
authority: process
---
# Project Harvest Protocol

## 1. Objective

Capture high-signal knowledge created by real work and route it for reuse without adding meaningful friction, contaminating project canon, or auto-generating public content.

The protocol exists because completed work often contains more value than the primary deliverable:

- a reusable method;
- a better task contract;
- a failure pattern;
- a new eval;
- a Skill candidate;
- a case-study lesson;
- a strong story;
- an operational SOP;
- a reusable component or asset.

The protocol turns those side-effects into organizational capital.

---

# 2. Ten governing rules

## Rule 1 — Harvest events, not commits

The default unit is a meaningful event: PR, ADR, milestone, experiment, incident/postmortem, launch, project outcome, or reusable workflow discovery.

A commit is evidence, not automatically a harvest trigger.

## Rule 2 — Non-blocking by default

Harvesting is a sidecar process. Failure to create a harvest record must not block ordinary development, review, merge, or delivery unless a future project explicitly makes it part of its Definition of Done.

## Rule 3 — Capture before transformation

The originating worker captures what happened, why it mattered, evidence, and reusable lessons.

It does not need to write a polished article, video script, Skill, SOP, or case study.

Those are downstream transformations.

## Rule 4 — Evidence before narrative

A compelling story is never allowed to override what actually happened.

Every harvest record must preserve provenance to the relevant PR, ADR, issue, experiment, artifact, metric, or verified outcome where available.

## Rule 5 — Generated does not mean canonical

Harvest records are reusable knowledge candidates, not strategic canon.

A lesson that changes project policy or architecture still requires the normal ADR/review path.

## Rule 6 — Human gate before publication

Nothing captured by Project Harvest is automatically safe to publish.

Public media, marketing, case studies, client proof, and claims require explicit human approval.

## Rule 7 — Privacy and confidentiality beat content value

Do not copy secrets, credentials, personal data, confidential client data, private commercial terms, restricted source material, or unapproved client identifiers into a public-ready record.

If the lesson is valuable but sensitive, abstract/redact it and classify it appropriately.

## Rule 8 — Neutral handoff, not tool coupling

The project records reusable knowledge in a tool-agnostic format.

Noema, Skill Foundry, Gemini, another agent, or a future system may consume it later, but the originating repo must not require those tools to function.

## Rule 9 — One event, many routes

A single lesson may feed multiple destinations:

- story/media;
- Skill;
- SOP/process;
- template/schema;
- eval/test;
- reusable component/code;
- asset;
- case study/proof;
- benchmark/lesson.

Capture once; route many times.

## Rule 10 — Optimize signal-to-noise

Do not harvest routine activity.

The system is successful when it captures the small number of events that materially improve future execution, learning, proof, or communication.

---

# 3. Trigger test

At the end of a meaningful PR, milestone, ADR, experiment, incident, or delivery, ask:

1. Did this produce a reusable lesson, capability, decision pattern, failure pattern, proof point, or before/after?
2. Would preserving this save time, reduce risk, improve quality, support proof, or enable useful communication later?
3. Is there sufficient evidence to describe what happened without inventing a narrative?
4. Can it be captured safely under the confidentiality rules?

### Result

- If **no** to 1 or 2: no harvest record.
- If **yes** to 1/2 but evidence is weak: create only if clearly labeled as hypothesis/lesson-in-progress.
- If capture is unsafe: redact/abstract or defer.
- If high-signal and safe: create one harvest record.

One event should normally create **one** harvest record, even when it routes to multiple destinations.

---

# 4. Strong triggers

Typical strong triggers include:

- a major PR changes how the project is operated;
- a decision resolves a recurring ambiguity;
- a failed approach reveals a reusable anti-pattern;
- an experiment produces a concrete keep/reject result;
- a client/project outcome creates credible proof;
- a new workflow materially improves speed, quality, safety, or cost;
- a repeated task is now structured enough to become a Skill/SOP/template;
- an implementation creates a reusable component, test, schema, or asset;
- a postmortem exposes a failure mode worth preventing elsewhere;
- a before/after demonstrates a meaningful transformation.

---

# 5. Default non-triggers

Normally do not harvest:

- typo/formatting fixes;
- trivial refactors with no new lesson;
- dependency churn;
- routine generated outputs;
- administrative branch cleanup;
- duplicated lessons already captured;
- speculative ideas with no project evidence;
- content produced only to create more content.

---

# 6. Confidentiality classes

Every record must declare one of:

### PUBLIC_SAFE
No known confidential/client/privacy restriction after human review. This classification alone does not authorize publication.

### INTERNAL
Safe for internal organizational reuse, not cleared for external publication.

### CLIENT_CONFIDENTIAL
Contains or derives from client-specific information and must remain restricted unless explicitly cleared/redacted.

### RESTRICTED
Contains security, credentials-adjacent, legal, highly sensitive commercial, or other material that should not be propagated through ordinary harvest flows.

Default to the more restrictive class when uncertain.

---

# 7. Evidence and provenance

A harvest record should link to the strongest available sources, for example:

- issue;
- PR;
- commit;
- ADR;
- experiment/report;
- metric/dashboard snapshot;
- client-approved outcome;
- artifact/version;
- postmortem.

Do not copy large source bodies unnecessarily. Prefer references plus a concise abstraction.

For external/public claims, evidence quality must be reviewed separately before publication.

---

# 8. Routing taxonomy

A record may set one or more routes.

## `story_media`
Potential narrative for video, carousel, article, thread, podcast, deck, or educational material.

## `skill_candidate`
Repeated capability that may belong in Skill Foundry after sufficient abstraction/evaluation.

## `sop_process`
Operational procedure worth standardizing.

## `template_schema`
Reusable structured document, schema, checklist, prompt contract, or form.

## `eval_test`
Scenario, regression case, adversarial case, fixture, or dataset item worth preserving.

## `component_code`
Reusable implementation or technical pattern.

## `asset`
Reusable visual/design/media asset or production rule.

## `case_study_proof`
Evidence suitable for future proof/case-study development, subject to client/privacy/claims review.

## `benchmark_lesson`
Comparative result, performance lesson, failure mode, or operating insight.

---

# 9. Lifecycle and authority

Project Harvest lifecycle:

`CANDIDATE -> REVIEWED -> APPROVED_FOR_REUSE -> ROUTED`

Optional terminal states:

`REJECTED / DUPLICATE / DEPRECATED`

Media/publication uses a separate downstream state machine, for example:

`STORY_SEED -> EDITORIAL_REVIEW -> APPROVED_FOR_PRODUCTION -> PUBLISHED`

A harvest record never becomes strategic/project canon automatically.

If a harvested lesson implies a canonical process change, open an ADR or normal governance change.

---

# 10. Story/media separation

The source worker should usually capture:

- what happened;
- the previous problem/state;
- what changed;
- why the decision mattered;
- evidence;
- failure/constraint;
- transferable lesson;
- possible narrative angles;
- available visuals/artifacts.

It should **not** optimize clickbait, invent drama, exaggerate results, or write final public claims.

A downstream editorial system may transform an approved story seed into:

- short-form script;
- long-form script;
- carousel;
- article;
- presentation;
- educational module.

---

# 11. Skill Foundry separation

A useful project lesson is not automatically a Skill.

A `skill_candidate` route means only that the capability may deserve later abstraction.

Before becoming a Skill it should be evaluated for:

- recurrence;
- generalizability;
- stable inputs/outputs;
- contracts;
- evalability;
- tooling requirements;
- safety;
- maintenance cost.

---

# 12. Case-study/proof separation

A project event is not automatically credible marketing proof.

Before external case-study use, verify:

- client permission where required;
- baseline;
- outcome attribution;
- metric accuracy;
- timeframe;
- confounders;
- privacy/compliance;
- claim wording.

Do not transform an internal impression into a quantified public result.

---

# 13. Agent behavior

When an agent completes a meaningful unit of work, it should perform a quick harvest assessment.

### If there is no meaningful reusable knowledge
Do nothing.

### If there is meaningful knowledge
Create a `HARVEST_RECORD` using the template, unless the task explicitly delegates capture to another owner.

### Agent limits
Agents must not:

- auto-publish;
- auto-create marketing claims;
- expose confidential data;
- create dozens of low-signal records;
- change canon through harvest records;
- create recursive harvest records about the act of harvesting itself unless new material learning occurred.

---

# 14. Minimal overhead standard

A harvest record should normally take less effort than reconstructing the lesson later.

Prefer concise, high-signal records.

Do not add mandatory meetings, heavy CI, or per-commit generation merely to satisfy this protocol.

Automation may be added later only after real usage shows that capture itself is a bottleneck.

---

# 15. Future automation boundary

Possible future flow:

`meaningful event -> draft harvest candidate -> human review -> route`

Potential triggers may include merged PRs, milestone completion, or approved postmortems.

This automation is intentionally **not** required now.

Before automating, measure:

- number of meaningful records;
- false-positive rate;
- review burden;
- downstream reuse rate;
- confidentiality incidents/near misses;
- whether records actually save time or improve outcomes.

---

# 16. Quality gate

A good harvest record is:

- specific;
- evidence-linked;
- reusable;
- concise;
- safe;
- honest about uncertainty;
- useful outside the originating conversation;
- routed without depending on a specific downstream tool.

Reject or merge records that are generic, duplicative, purely speculative, or content-for-content's-sake.

---

# 17. Example: current agency foundation work

A valid harvest event could be the transition from chat-first coordination to repo-first multi-agent work.

Possible reusable lesson:

> As project complexity and agent count increase, the bottleneck moves from generation to coordination; versioned source-of-truth, ownership, branch isolation, PR review, and explicit convergence gates reduce coordination entropy.

Possible routes:

- `story_media` — educational content on repo-first AI work;
- `skill_candidate` — multi-agent repo orchestration capability;
- `sop_process` — project initialization protocol;
- `template_schema` — branch/PR/agent contracts;
- `case_study_proof` — internal proof of project operating maturity.

The harvest record would capture this lesson once. Each downstream system would transform it independently.

---

# 18. Success criteria

Project Harvest is working when:

- meaningful lessons survive beyond a conversation;
- future projects start with better assets/processes than previous ones;
- media content originates from real evidence rather than generic idea generation;
- Skill candidates emerge from repeated real work;
- case-study/proof capture is easier;
- the harvest system itself remains low-friction and low-noise.