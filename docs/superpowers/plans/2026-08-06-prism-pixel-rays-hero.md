# Prism-Core Pixel Rays Hero Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the profile GIF's character-like glitch moment with an artistic holographic prism that refracts light into pixel rays, while making the philosophy readable and slower for general visitors.

**Architecture:** Keep the existing deterministic Pillow renderer and bundled font. Replace the scene copy and anomaly drawing, render 168 frames with a 14-second timing schedule, and extend structural tests to verify every new phrase, timing contract, and asset reproducibility.

**Tech Stack:** Python 3, Pillow 12.2.0, unittest, GitHub-flavored Markdown.

## Global Constraints

- The GIF remains the only animated README element.
- No faces, emojis, characters, repositories, or project names appear in the GIF.
- The GIF uses exactly 168 frames at 12 FPS and exactly 14,000 ms of playback.
- Each text beat holds long enough to read; no copy changes during a transition.
- The final GIF remains below 5 MB and loops back to a compatible opening frame.
- Existing README content and links below the hero remain unchanged.

---

### Task 1: Update copy and renderer contract

**Files:**
- Modify: `scripts/render_impossible_loop.py`
- Modify: `tests/test_render_impossible_loop.py`

**Interfaces:**
- Produces: `COPY`, `FRAME_COUNT`, `FRAME_DURATIONS`, and `render_frame(frame)` for the new 14-second story.

- [x] **Step 1: Add failing assertions for the new copy and timing**

Assert the phrases `MODELS PREDICT.`, `AGENTS DELIVER.`, `SYSTEMS ANCHOR CONTEXT.`, `EXECUTION REVEALS THE TRUTH.`, `WHEN ABSTRACTIONS LEAK,`, `EXAMINE THE PRIMITIVES.`, `WHEN COMPLEXITY BLINDS,`, `ISOLATE THE ARCHITECTURE.`, `ORCHESTRATION IS THE PULSE.`, and `AUTONOMY IS THE ENDGAME.`. Assert 168 frames and a 14,000 ms duration schedule.

- [x] **Step 2: Run the tests and verify they fail against the current renderer**

Run: `python3 -m unittest discover -s tests -v`

Expected: failures for the old copy, frame count, and timing.

- [x] **Step 3: Implement the new copy and timing**

Use 168 frames and a deterministic duration tuple totaling 14,000 ms. Each scene should introduce its text, hold it, then transition; the final message should hold for two seconds before the opening frame returns.

- [x] **Step 4: Run tests and verify the contract passes**

Run: `python3 -m unittest discover -s tests -v`

Expected: all contract tests pass after rendering is updated.

### Task 2: Replace the anomaly artwork with Prism-Core

**Files:**
- Modify: `scripts/render_impossible_loop.py`
- Modify: `tests/test_render_impossible_loop.py`
- Replace: `assets/the-impossible-loop.gif`
- Replace: `assets/the-impossible-loop-poster.png`

**Interfaces:**
- Consumes: the new copy/timing contract from Task 1.
- Produces: an artistic prism scene with square pixel particles, colored light rays, a wireframe primitive grid, and a recombined infinity beam.

- [x] **Step 1: Add scene-level assertions**

Assert that the renderer source contains the prism, pixel, ray, and primitive-grid drawing calls and contains no face/emoji terminology. Keep the existing byte-reproducibility assertions for the committed GIF and poster.

- [x] **Step 2: Implement the Prism-Core sequence**

Draw one cyan beam entering a transparent geometric prism. Refract it into square pixel rays using cyan, violet, amber, and coral. During the anomaly beat, scatter the pixels into a wireframe grid; during recovery, recombine the rays into one green beam and an infinity loop. Remove the old glitch-face geometry entirely.

- [x] **Step 3: Render and visually inspect representative frames**

Run the renderer, create a contact sheet at evenly spaced timestamps, and create a 375px-wide poster preview. Confirm that the prism remains legible, rays read as light, pixels are square, and no frame contains a face or emoji.

- [x] **Step 4: Run the full test suite**

Run: `python3 -m unittest discover -s tests -v && git diff --check`

Expected: all tests pass, the asset is below 5 MB, and the diff is whitespace-clean.

### Task 3: Publish the follow-up PR

**Files:**
- Modify: `docs/superpowers/plans/2026-08-06-prism-pixel-rays-hero.md`

**Interfaces:**
- Consumes: verified renderer, assets, and tests from Tasks 1–2.
- Produces: pushed branch and draft PR targeting `main`.

- [x] **Step 1: Review the scoped diff and mark the plan complete**

Run: `git status --short --branch && git diff --check && git diff --stat origin/main...HEAD`.

- [x] **Step 2: Commit and run the final tests**

Commit message: `Refine profile GIF with prism pixel rays`.

Run: `python3 -m unittest discover -s tests -v`.

- [x] **Step 3: Push and open a draft PR**

Push `agent/prism-pixel-rays-hero` and open a draft PR titled `Refine profile GIF with prism pixel rays`, describing the copy, pacing, Prism-Core artwork, and validation results.
