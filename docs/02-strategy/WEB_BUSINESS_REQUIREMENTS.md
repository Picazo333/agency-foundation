---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - POSITIONING_ARCHITECTURE.md
  - PROOF_STRATEGY.md
  - SALES_SYSTEM.md
  - BRAND_BUSINESS_INTERFACE.md
---
# Web and Digital Presence — Business Requirements

> **Module 20 of the Agency Master Plan** (Issue #2 Phase 17). Specifies the website as a
> **business system**: what it must accomplish, for whom, with what conversion paths and what
> launch gates.
>
> **Scope boundary:** this document does not design or build anything. Visual design belongs to the
> Brand workstream; implementation belongs to the technical workstream (`OWNERSHIP_MATRIX.md`). It
> is placed under `docs/02-strategy/` rather than `docs/05-product-web/` because
> `docs/05-product-web/*/README.md` states that those directories are populated *after* strategy and
> brand convergence — which has not happened.
>
> **Do not build the production site.** `META_PLAN.md` Wave 5; §9 defines the gates.

## 1. The site's actual job

For a supplier with no reputation, the website's primary function is not lead generation. It is
**credibility verification**: a buyer who received a cold message or a referral will look the
supplier up, and will decide in roughly eight seconds whether this is a real, serious operation.

| Priority | Job | Audience | Evidence |
|---|---|---|---|
| 1 | **Pass the credibility check** | Someone who just received outreach or a referral | `PROOF_STRATEGY.md` §11 |
| 2 | **Make the method visible** | A buyer evaluating whether this person knows what they are doing | P0 — the highest-value proof available pre-reputation |
| 3 | **Convert interest into a conversation** | A buyer ready to talk | `SALES_SYSTEM.md` §2 |
| 4 | **Host proof** | A buyer in evaluation | P3, P5, P7 |
| 5 | Capture organic demand | Later | Month 6+ |

**Implication that overrides conventional practice:** the homepage's most important element is not
a value proposition or a hero image. It is **visible evidence of method** — the thing a sceptical
stranger can read and judge for themselves (`POSITIONING_ARCHITECTURE.md` §10, rung 2).

## 2. Two distinct builds

| | **MVS — Minimum Viable Site** | **Production Site** |
|---|---|---|
| Purpose | Pass the credibility check during validation | Full business system |
| When | **Week 3, before any outreach** | After Brand V1 + D5 + Gate 1 |
| Blocked by | Nothing | Brand V1, validated message, proof |
| Pages | 5 | 15–25 |
| Design | Plain, typographically competent, fast | Full brand system |
| Cost | ~8 founder hours | Separate engagement |

> **The MVS must not wait for Brand V1.** A plain, fast, well-written site published in week 3
> outperforms a beautiful site published in month 5, because in month 5 the validation window has
> closed. Delaying outreach for brand readiness is the over-planning failure mode
> (`RT-01`, `BRAND_BUSINESS_INTERFACE.md` §6).

### 2.1 MVS requirements

| Page | Contents | Purpose |
|---|---|---|
| Home | What we do, in plain buyer language · who it is for · the method in three steps · a link to the full method · booking link | Credibility in 8 seconds |
| Method | The full diagnostic method, honestly and in detail, including limitations · a redacted sample report | **P0 — the most important page on the MVS** |
| Who this is for | Segment, qualification and disqualification criteria, stated plainly | Self-selection; also signals confidence |
| About | Who the founder is, what they have actually done, what they are building. **`A-06` stated honestly** | Trust; the honest version outperforms the vague one |
| Contact | Booking link, email, response-time commitment | Conversion |

**MVS must have:** working booking link · a real response-time commitment that is honoured (a
supplier selling response-time improvement is judged on their own) · mobile-first · fast load ·
basic analytics · no broken links · no placeholder text · no stock photos of people pointing at
screens (`PP-7`).

**MVS must not have:** fake testimonials or implied client rosters (`EC-3`, `PP-4`) · "trusted by"
logos not earned · unsourced statistics (`PP-1`) · a blog with one post · a chatbot · a newsletter
signup with nothing to send.

## 3. Production-site information architecture

| Section | Pages | Job | Blocked by |
|---|---|---|---|
| Home | 1 | Credibility, orientation, primary conversion | Validated message (D4) |
| Method | 2–3 | P0 proof; the diagnostic explained; sample report | — |
| Services | 3–5 | One page per offer with scope, exclusions, duration, price posture | Validated offers (D8) |
| Who it's for | 1–2 | Segment pages; qualification criteria | Validated ICP (D3) |
| Proof | 3–8 | Case studies, teardown library, benchmark data | First case study (month 4–6) |
| About | 1–2 | Founder, principles, the `DO NOT SELL` list (a genuine differentiator when published) | — |
| Insights | ongoing | Teardowns, method notes, benchmark findings | Content flow |
| Contact | 1 | Qualification-aware conversion | CRM |
| Legal | 3 | Privacy, terms, cookies | Counsel ⚖️ |

**Publishing the `DO NOT SELL` list is recommended.** Naming what you refuse to do increases trust
more reliably than any capability claim (`PROOF_STRATEGY.md` §11), and it pre-qualifies traffic.

## 4. Conversion paths

| Entry | Path | Conversion | Notes |
|---|---|---|---|
| Cold outreach recipient verifying | Home → Method → About → Contact | Booking | **The dominant path during validation.** Optimise this first |
| Referral | Home → Proof → Contact | Booking | Wants social proof fast |
| Teardown recipient | Insights → Method → Contact | Booking | Already saw competence |
| Organic search (month 6+) | Insight → Method → Contact | Booking or subscribe | Long path |
| Partner referral | Home → Method → Contact | Booking | May need a partner-specific page |

**Primary CTA everywhere: book a 25-minute conversation.** Single, consistent, low-commitment.

**Secondary CTA: request a free teardown** (L0). Better than a gated PDF because it is specific to
the requester and it feeds the outreach engine.

**No contact forms that only collect an email.** The form must capture enough to run Q1 (segment,
size, what prompted the enquiry) so the first conversation starts qualified — this directly reduces
`A-14` unbilled sales hours.

## 5. Proof presentation requirements

| Asset | Requirement |
|---|---|
| Case studies | Fixed structure (`PROOF_STRATEGY.md` §7.2) · every metric with denominator, window and caveat · the "what we would do differently" section included |
| Teardown library | Anonymised to a standard where a segment competitor could not identify the business (`EC-8`) |
| Benchmark data | Only at n≥5 per cohort; n and period always shown |
| Method document | Downloadable, complete, honest about limitations |
| Sample report | Redacted, clearly labelled as illustrative if constructed |

**Structural requirement:** the site must present dense tabular and annotated content legibly. This
is `BC-05`/`BR-6` and is the single most likely place for a beautiful brand to produce an unusable
deliverable.

## 6. Content architecture

| Type | Cadence | Source |
|---|---|---|
| Teardowns | 1–2/week | Byproduct of CH-1 — zero marginal cost |
| Method notes | 1/month | Delivery learning |
| Benchmark findings | Quarterly from month 9 | P7 dataset |
| Case studies | As produced | Delivery |

**Rule:** content is a byproduct of commercial work, never a separate production line
(`ACQUISITION_MARKETING_SYSTEM.md` CH-5). A content calendar that requires work not otherwise
being done will be abandoned within six weeks.

## 7. Technical requirements

| Category | Requirement |
|---|---|
| Performance | Sub-2.5s LCP on a representative mobile connection; the site sells operational competence and is judged on its own |
| Accessibility | WCAG 2.2 AA as the working target (`DELIVERY_OS.md` §9.1; legal position per `GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §9 ⚖️) |
| SEO | Semantic structure, metadata, sitemap, schema. **No SEO investment before month 6** |
| Analytics | Privacy-respecting; event tracking on conversion paths; source attribution reconciling with CRM |
| Forms → CRM | Direct handoff creating an opportunity record with source; no manual re-entry |
| Booking | Calendar integration; confirmation and reminder automation; **the agency's own C-1 product, dogfooded** (P2) |
| Language | ES/EN capability from the start if `A-01` holds; do not retrofit |
| Privacy/cookies | Per jurisdiction ⚖️ |
| Hosting | Portable; no proprietary lock-in |
| Content editing | Founder-editable without a developer |

## 8. Spine separation and maturity

Per `IMPLEMENTATION_SUMMARY.md` and `docs/05-product-web/README.md`:

| Spine | Owns | Depends on |
|---|---|---|
| **Aesthetic** | Visual design, typography, imagery, motion | Brand V1 |
| **Functional** | IA, routes, content, forms, SEO, analytics, accessibility | Validated message and offers |
| **System** | CRM integration, automation, booking, dashboards, any AI feature | Working internal systems |

| Stage | State | Gate |
|---|---|---|
| **S0 Visual** | Design complete, no interaction | Brand V1 approved |
| **S1 Interactive** | Navigation, forms, responsive | Functional spine specified |
| **S2 Mock Data** | Proof and case-study structures with placeholder content | Content architecture |
| **S3 Backend Wired** | Forms → CRM, booking, analytics live | Internal systems working |
| **S4 AI/MCP** | Any AI-assisted feature | **Justified by a concrete need, not by capability** |

> **Binding rule** (`IMPLEMENTATION_SUMMARY.md` principle 3): a visually complete site is never
> represented — internally or to a client — as functionally or systemically complete. The agency
> sells honest measurement; misrepresenting its own maturity is a direct contradiction.

**On S4:** the agency should be slow to add AI features to its own site. An AI chat widget on the
homepage of a business that refuses to lead with AI (`RF-1`) would contradict the positioning in
the most visible possible place.

## 9. Launch gates

| Gate | Requirement | Why |
|---|---|---|
| **G-W0 — MVS live** | 5 pages, booking link, method page, honest about `A-06` | **Week 3, before outreach begins.** Not gated on anything |
| **G-W1 — Production design start** | Brand V1 approved (Gate 1 passed) + D4 message validated | Designing before the message is validated designs the wrong site |
| **G-W2 — Content freeze** | Real buyer language from D4; ≥1 case study; method document final | Writing copy from planning language wastes the build (`POSITIONING_ARCHITECTURE.md` §3) |
| **G-W3 — Functional complete** | S1+S2; accessibility pass; performance pass | — |
| **G-W4 — System wired** | S3; CRM handoff tested end to end; analytics reconciling | — |
| **G-W5 — Launch** | Legal pages reviewed ⚖️; licensing verified for every asset; QA passed; rollback available | `DELIVERY_OS.md` §9.1 |

**Earliest realistic production launch: month 6–9.** This is a feature of the plan, not a delay:
the site built after validation will be a different and better site than one built before, and the
MVS carries the load in the meantime.

## 10. What the site must never do

| # | Prohibited | Why |
|---|---|---|
| W-1 | Imply clients that do not exist | `EC-3`, `PP-4` |
| W-2 | Publish unsourced statistics | `PP-1` |
| W-3 | Lead with AI | `RF-1` |
| W-4 | Publish an outcome without a baseline, denominator and window | `EC-1`, `EC-2` |
| W-5 | Use client data or screenshots without consent | `DR-8` |
| W-6 | Use unlicensed fonts, images or icons | Licensing gates |
| W-7 | Promise response times the agency does not honour | The most visible possible self-contradiction |
| W-8 | Be slower or less accessible than what it sells | Same |
| W-9 | Collect personal data without a lawful basis and a privacy notice | ⚖️ §4 of the governance checklist |
| W-10 | Present S0/S1 maturity as a finished system | `IMPLEMENTATION_SUMMARY.md` principle 3 |
