# Security Policy

This document is the **baseline security policy** for
[@askmy-stack](https://github.com/askmy-stack) repositories. Individual
projects may add stricter rules, but they inherit this policy by default.

## Reporting a vulnerability

**Please do not open a public issue for security problems.**

Report privately through GitHub's
[private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability):

1. Go to the affected repository's **Security** tab.
2. Choose **Report a vulnerability**.
3. Describe the issue, affected versions, and reproduction steps.

If private reporting is not enabled on a repo, contact the maintainer through
the channels listed in `CONTACT.md`.

### What to expect

| Stage | Target |
| --- | --- |
| Acknowledgement | within 48 hours |
| Initial assessment | within 5 business days |
| Fix or mitigation plan | communicated after assessment |
| Public disclosure | coordinated with the reporter after a fix ships |

## Handling API keys and secrets

These projects integrate with LLM providers, databases, and message brokers,
so secret hygiene matters:

- **Never commit secrets.** Use environment variables or a secrets manager.
- Keep real values out of source control with `.gitignore` (for example,
  `.env`, `*.pem`, credential JSON files).
- Provide a committed `.env.example` with placeholder values only.
- Rotate any credential that is exposed, even briefly, in git history or logs.
- Scope tokens to the minimum permissions required.

## Handling personally identifiable information (PII)

Several projects process signals that may contain PII:

- Do not log raw PII. Redact or hash identifiers before they reach logs or
  telemetry.
- Do not persist PII to knowledge graphs, vector stores, or caches unless it is
  strictly required and documented.
- Prefer aggregated or anonymized data for examples, tests, and fixtures.
- Delete PII on request and honor data-retention limits.

## Supported versions

Unless a repository states otherwise, only the latest release on the default
branch receives security fixes.
