# Portfolio Milestone Strategy

This document defines the shared milestone language used across the
`askmy-stack` portfolio. The goal is to make issue triage and release planning
consistent even when the repositories serve different products.

## v1.0-oss-ready

**Meaning:** the repository is safe and clear for open-source contributors.

Typical work in this milestone:

- `CONTRIBUTING.md`, `SECURITY.md`, `LICENSE`, `CONTACT.md`
- issue templates and label standards
- dependency update automation
- repo metadata, project board setup, baseline governance docs

Use `v1.0-oss-ready` when the work primarily improves:

- contributor onboarding
- legal clarity
- security posture
- governance and triage

## v2.0-features

**Meaning:** the repository has the supporting product and documentation work
needed to feel complete and polished.

Typical work in this milestone:

- architecture docs and portfolio navigation hubs
- integration tests and CI quality checks
- README improvements that explain usage or project relationships
- documentation that deepens the feature story

Use `v2.0-features` when the work primarily improves:

- product understanding
- developer experience
- test coverage and confidence
- cross-repo discoverability

## v3.0-platform

**Meaning:** the work expands the portfolio into broader platform capabilities
or reusable systems.

Typical work in this milestone:

- org-wide automation and reporting
- advanced dashboards and metrics
- monetization/adopters/funding maturity
- shared infrastructure that spans many repositories

Use `v3.0-platform` when the work primarily improves:

- portfolio-wide operations
- reusable platform primitives
- ecosystem visibility
- long-term scaling

## How to choose between milestones

When triaging a new issue, ask:

1. Does this make the repo safer or easier to contribute to? → `v1.0-oss-ready`
2. Does this explain, test, or polish the product story? → `v2.0-features`
3. Does this create a broader reusable platform capability? → `v3.0-platform`

If an issue spans multiple categories, assign the **earliest milestone that must
land first**.
