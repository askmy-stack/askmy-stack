# Futuristic Profile Copy Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the content below the merged profile GIF with a concise, futuristic, GitHub-safe systems manifesto and publish it through a new PR.

**Architecture:** Keep the hero asset unchanged, version its URL to invalidate caches, and express the remaining profile with supported Markdown/HTML primitives. Add focused README tests so the structure, links, and removed copy cannot regress.

**Tech Stack:** GitHub-flavored Markdown, semantic HTML, Python unittest.

## Global Constraints

- The existing GIF remains the only animated element.
- The removed `I work at the layer...` paragraph must not appear.
- Use `<samp>` and code labels for futuristic typography; do not use unsupported CSS or external font loading.
- Preserve portfolio, LinkedIn, GitHub, Medium, and Hugging Face links.
- Keep the profile readable on desktop and mobile.

---

### Task 1: Define the README contract

**Files:**
- Create: `tests/test_profile_readme.py`

**Interfaces:**
- Consumes: `README.md` as UTF-8 text.
- Produces: structural assertions for the hero, identity, perspective, operating layers, system stack, and links.

- [x] **Step 1: Write failing tests**

Assert one GIF, a cache-busting `?v=prism-rays-2` query, the `<samp>` identity line, numbered sections `01` through `04`, five operating-layer labels, all five links, and absence of the removed paragraph.

- [x] **Step 2: Confirm the current README fails the new contract**

Run: `python3 -m unittest discover -s tests -v`

Expected: failures for the missing futuristic content and cache-busting query.

### Task 2: Rewrite the profile content

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: the approved copy structure.
- Produces: one GitHub-renderable profile README with no custom CSS dependency.

- [x] **Step 1: Replace the content below the GIF**

Use the identity block, one-line perspective quote, operating-layers table, compact stack block, and transmission links defined in the design spec.

- [x] **Step 2: Version the hero URL**

Append `?v=prism-rays-2` to the raw GIF URL so GitHub and browser caches request the merged asset again.

- [x] **Step 3: Run the full test suite**

Run: `python3 -m unittest discover -s tests -v && git diff --check`

Expected: all README and GIF tests pass and the diff is whitespace-clean.

### Task 3: Review and publish

**Files:**
- Review: `README.md`
- Review: `tests/test_profile_readme.py`

**Interfaces:**
- Produces: pushed branch and draft PR targeting `main`.

- [x] **Step 1: Review the rendered hierarchy and scoped diff**

Confirm that the hero, identity, numbered sections, table, stack, and links appear in that order and that no unrelated file changed.

- [x] **Step 2: Commit and push**

Commit message: `Polish profile copy with futuristic systems layout`.

- [x] **Step 3: Open a draft PR**

Title: `Polish profile copy with futuristic systems layout`.
