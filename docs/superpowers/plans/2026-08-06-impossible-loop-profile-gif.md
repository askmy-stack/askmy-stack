# The Impossible Loop Profile GIF Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the existing profile hero with one deterministic, artistic, retro-futuristic GIF about reliable AI systems while preserving all other README content.

**Architecture:** A focused Pillow renderer draws a layered 900 by 340 scene from reusable primitives and renders eight timed story beats to an optimized animated GIF. Tests inspect renderer constants and output metadata, while the README consumes only the final GIF.

**Tech Stack:** Python 3, Pillow, unittest, GitHub-flavored Markdown.

## Global Constraints

- The GIF is the README's only animated element.
- Do not mention repositories, projects, accomplishments, or metrics in the animation.
- Preserve the README below the hero unchanged.
- Render 120 frames at 12 FPS on a 900 by 340 canvas.
- Keep the final GIF below 5 MB and make the loop visually seamless.
- Avoid rapid full-canvas flashing.

---

### Task 1: Deterministic animation renderer

**Files:**
- Create: `scripts/render_impossible_loop.py`
- Create: `tests/test_render_impossible_loop.py`

**Interfaces:**
- Produces: `render(output_gif: Path, output_poster: Path) -> None`
- Produces: constants `WIDTH`, `HEIGHT`, `FPS`, `FRAME_COUNT`, `DURATION_MS`, and `COPY`

- [x] **Step 1: Write structural renderer tests**

Create tests that import the renderer, assert the required dimensions/timing/copy, render into a temporary directory, and verify GIF animation metadata, frame count, poster size, and file-size budget.

- [x] **Step 2: Run tests and verify the missing renderer fails**

Run: `python3 -m unittest discover -s tests -v`

Expected: failure because `scripts.render_impossible_loop` does not exist.

- [x] **Step 3: Implement the layered renderer**

Implement deterministic star fields, CRT texture, an arcade frame, signal particles, memory orbits, a constellation maze, a verification prism, glitch fragments, a recovery pulse, infinity-loop geometry, pixel-inspired typography, and scene-specific copy. Export an adaptive-palette GIF and a poster PNG.

- [x] **Step 4: Run tests and inspect metadata**

Run: `python3 -m unittest discover -s tests -v`

Expected: all tests pass and the GIF remains below 5 MB.

### Task 2: Profile integration

**Files:**
- Create: `assets/the-impossible-loop.gif`
- Create: `assets/the-impossible-loop-poster.png`
- Modify: `README.md`

**Interfaces:**
- Consumes: renderer outputs from Task 1.
- Produces: one README hero image referencing `assets/the-impossible-loop.gif`.

- [x] **Step 1: Render final assets**

Run: `python3 scripts/render_impossible_loop.py`

Expected: both assets are created with the tested dimensions.

- [x] **Step 2: Replace only the hero source and alt text**

Change the first README image to `assets/the-impossible-loop.gif` and describe the observe, remember, reason, verify, and recover loop in its alt text. Leave the remaining README byte-for-byte unchanged.

- [x] **Step 3: Verify README references**

Run: `python3 -m unittest discover -s tests -v`

Expected: README integration and animation tests pass.

- [x] **Step 4: Visually inspect representative frames**

Create a contact sheet from eight evenly spaced frames and confirm legibility, contrast, story progression, and the absence of project references.

### Task 3: Publish the profile update

**Files:**
- Review all files listed in Tasks 1 and 2.

**Interfaces:**
- Consumes: verified repository diff.
- Produces: pushed feature branch and draft pull request targeting `main`.

- [x] **Step 1: Review the scoped diff**

Run: `git status --short && git diff -- README.md scripts/render_impossible_loop.py tests/test_render_impossible_loop.py docs/superpowers assets`

- [x] **Step 2: Run final verification**

Run: `python3 -m unittest discover -s tests -v`

- [ ] **Step 3: Commit and push**

Commit message: `Redesign profile hero as the Impossible Loop`

- [ ] **Step 4: Open a draft pull request**

Target `main` and summarize the new single-GIF concept, preserved README content, deterministic renderer, and validation results.
