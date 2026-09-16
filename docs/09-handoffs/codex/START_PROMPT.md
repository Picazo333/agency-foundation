# START PROMPT — Technical Foundation Lead

Preferred lead: Codex. Antigravity and Jules may later receive narrower sub-tasks derived from this workstream.

Work in repository `Picazo333/agency-foundation` on branch `tech/agent-foundation` and execute GitHub Issue #4 end-to-end.

Read first:
1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `docs/00-meta/source-of-truth.md`
4. `docs/08-plans/master/META_PLAN.md`
5. `docs/08-plans/workstreams/TECH_FOUNDATION_WORKSTREAM.md`
6. relevant web/aesthetic implementation research summaries.

Mission:
Prepare neutral technical foundations that can later receive Brand V1, Functional specifications and System integrations without major architectural rework. Do NOT build the production agency website now.

Required work:
- define neutral design-token schema with values TBD;
- establish `labs/visual`, `labs/motion`, `labs/svg`, `labs/interaction` scaffolding where appropriate;
- define/test SVG validation and optimization pipeline;
- establish component/asset naming and provenance conventions;
- create isolated proof-of-concept patterns for CSS masks, SVG, GSAP/scroll behavior and any other justified implementation technique;
- establish accessibility and reduced-motion conventions;
- establish performance budgets/baselines appropriate to future rich visual work;
- establish visual-regression/testing approach;
- establish secrets/security baseline and `.env.example` conventions where relevant;
- document Aesthetic / Functional / System spine boundaries;
- encode S0 Visual -> S1 Interactive -> S2 Mock Data -> S3 Backend Wired -> S4 AI/MCP maturity model into technical documentation/checklists;
- identify work that should later be delegated to Jules or Antigravity as narrowly scoped follow-on issues.

Constraints:
- no final production site;
- no permanent encoding of provisional Brand V0;
- no business-strategy decisions;
- avoid unnecessary framework lock-in before requirements justify it;
- experiments live in labs and do not become production canon automatically;
- if code/dependencies are added, include validation/tests and document why they exist.

Autonomy:
Continue without routine checkpoints unless a fatal blocker exists. Prefer neutral interfaces/placeholders over guessing future brand or business decisions.

Before finishing run:
1. Senior Frontend/Platform audit: will Brand V1 plug in cleanly?
2. Performance/Accessibility audit: can rich visual implementation remain usable?
3. Red Team audit: identify overengineering, premature lock-in, security gaps, dependency risk, and places agents could collide.

Finish by committing to `tech/agent-foundation` and opening a PR to `main` that references/closes Issue #4. Include tests/validation performed, files changed, architectural decisions proposed, experiments created, risks, and recommended follow-on issues for Antigravity/Jules.
