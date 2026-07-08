# Contributing

Thanks for your interest in contributing. This repository is the profile
README for [@askmy-stack](https://github.com/askmy-stack), and it also serves
as the **baseline contribution guide** referenced by the other repositories in
the portfolio. If a project in the org does not ship its own `CONTRIBUTING.md`,
these rules apply.

## Ways to contribute

- **Report a problem** — open an issue describing what you expected and what happened.
- **Suggest an improvement** — open an issue with the `category:feature` or `category:documentation` label.
- **Send a fix** — small, focused pull requests are the easiest to review and merge.

For anything larger than a typo or a one-line change, please open an issue
first so we can agree on the approach before you invest time.

## Workflow

1. **Fork** the repository and clone your fork.
2. **Create a branch** off `main`. Use the pattern `issue-<number>/<short-slug>`
   (for example, `issue-42/fix-broken-link`).
3. **Make your change.** Keep the diff scoped to a single concern.
4. **Commit** with a clear, imperative message
   (for example, `Add reduced-motion fallback for header banner`).
5. **Push** to your fork and **open a pull request** against `main`.
6. **Link the issue** in the PR body with `Closes #<number>`.
7. Wait for review. Address feedback with additional commits rather than
   force-pushes while review is in progress.

## Pull request checklist

- [ ] The PR is scoped to one issue or one logical change.
- [ ] The PR body links the issue it resolves (`Closes #<number>`).
- [ ] Any new links in the README or docs resolve (no 404s).
- [ ] Markdown renders correctly in the GitHub preview.
- [ ] CI checks (link-check, spellcheck) pass where configured.

## Code style

- **Markdown:** one sentence idea per line where practical; wrap long prose.
  Use `##` for top-level sections. Prefer relative links for in-repo files.
- **YAML (workflows, config):** two-space indentation, pin third-party actions
  to a major version tag (for example, `actions/checkout@v4`).
- **Commit messages:** imperative mood, capitalized subject, no trailing period.

## Code of conduct

Be respectful and constructive. Assume good intent, give actionable feedback,
and keep discussions focused on the work.

## Questions

Not sure where to start? Look for issues labeled
[`good first issue`](https://github.com/askmy-stack/askmy-stack/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
or open a discussion. Contact details are in [`CONTACT.md`](./CONTACT.md) once
available.
