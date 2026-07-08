# Licensing Audit Baseline

This repository is the profile repo for `@askmy-stack`, so its licensing needs
are slightly different from the code repositories in the portfolio.

## Current position

- The profile content in this repository is licensed under **CC-BY-4.0**.
- Code repositories in the portfolio should each declare **one canonical SPDX
  identifier** in their `LICENSE`, package metadata, and README badges.

## Audit checklist for sibling repositories

For each repository in the portfolio:

1. Check the `LICENSE` file.
2. Check package metadata (`pyproject.toml`, `package.json`, `go.mod` docs, etc.).
3. Check the README badge or license statement.
4. Confirm that all three point to the same SPDX identifier.

## Recommended rollout

- Use **one license per repository**.
- If a repo contains both code and substantial docs/art, document that clearly.
- Prefer SPDX identifiers in badges and package metadata to avoid ambiguity.
- Track exceptions explicitly instead of letting mismatches persist.

## Portfolio note

Issue #8 is a **cross-repo audit**. This document establishes the policy and the
checklist in the profile repo so the actual remediation work in sibling repos
has a canonical reference point.
