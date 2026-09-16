---
status: draft
owner: asset-factory
updated: 2026-09-15
authority: workbench
depends_on:
  []
---
# Asset Factory Architecture Spec

This directory contains the complete, generator-agnostic architecture for the Agency Foundation Asset Factory.

The factory is designed to intake a frozen Brand V1 system and output production-ready, legally cleared, and strictly versioned assets for implementation.

## Architecture Documentation

1. [Brand Pack Contract](./01-brand-pack-contract.md): The input schema defining global aesthetic rules.
2. [Asset Taxonomy](./02-asset-taxonomy.md): Categorization, responsive variant rules, and supported formats.
3. [Prompt Contracts & Parameters](./03-prompt-contracts.md): Structured generation requests and invent-vs-ask rules.
4. [Metadata & Provenance Schema](./04-metadata-provenance-schema.md): Output metadata, strict licensing gates, and accessibility rules.
5. [Lifecycle & QA Gates](./05-lifecycle-qa.md): The state machine (`generated` -> `approved`) and QA review matrix.
6. [Batch Workflow & Handoff](./06-workflow-handoff.md): Naming conventions, batch execution, and the implementation handoff manifest.

## Examples

See the [`examples/`](./examples/) directory for illustrative JSON schemas and requests.

*Note: Future factory input must include Brand V1, design tokens, typography rules, palette, illustration rules, imagery rules, motion rules, SVG rules, licensing/provenance rules, composition rules and anti-patterns.*
