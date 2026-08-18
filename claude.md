# CLAUDE.md — Python Game Dev Curriculum (6th Grade)

Context for continuing this project in a local Claude session. This captures everything established so far so work can resume without re-deriving decisions already made.

## Project

A 16-week Python game development curriculum for a total-beginner 6th grader, built around Pygame (`pygame-ce`). Each week should have a self-contained folder that references shared modules from a top-level `./shared` folder in the repository. Each folder should have an `ASSIGNMENT.md`, `RUBRIC.md` and any supporting code/assets needed to complete the assignment.

Baseline pace: **~3 hours/week**, self-paced, with explicit **stretch goals** in every lesson and project for a student who wants to go further.

## Repo & tooling

- **`arobson/programming-with-pygame`** is the single course repo: prerequisites, shared library code, and all weekly starter material live here. Layout:
  ```
  arobson/programming-with-pygame/
    shared/
      sprite_loader.py
      input_handler.py
    weeks/
      week-01/
        reference/
        exercises/
        project/
      week-02/
        ...
  ```
- **`proji`** (`arobson/proji`) is the student-facing CLI. It wraps git so the student never runs git directly — used to pull each week's reference material and to "check in" (stage/commit/push) finished exercises and projects.

## Scaffold-fading design (the core pedagogical idea)

The student is given working modules up front so they can build real games immediately without first learning file I/O or low-level input handling:

- `input_handler.py` — reads keyboard state (assumed interface: `get_movement_vector() -> (dx, dy)`
- `physics.py` - a set of physics utilities for handling collisions, gravity, and physics-based movement
- `sound.py` - a set of functions to load and play sound effects and background music
- `sprite_loader.py` — loads/slices sprite sheets (assumed interface: `load_sheet(path, frame_width, frame_height) -> list[Surface]`

These are used as-is until the student rebuilds simplified versions of functionality for themselves once they've used the "black box" versions enough times to understand what the code needs to do. This replaces-the-scaffold arc is the payoff of the whole course design and should be preserved in any future edits.

## The 16-week arc

**Phase 1 — Guided Building (1–4):** first window/game loop, sprites & coordinates, keyboard movement, game loop internals (bouncing ball)
**Phase 2 — Core Mechanics (5–8):** functions, collision detection, lists/multiple objects, classes & OOP (midpoint checkpoint)
**Phase 3 — I/O (9–12):** sprite sheets & animation, keyboard input, sound & score
**Phase 4 — Capstone (13–16):** design & planning, build sprint 1, build sprint 2 (polish), presentation/playtest/reflection

Full detail should be kept in `00_Curriculum_Overview.md`.

## Lesson doc format (established in Week 1, use as the template)

Each `ASSIGNMENT.md` has, in this order:
1. Learning objectives (bullet list, observable/testable)
2. Setup (proji commands to ensure they have the latest version of their fork's upstream)
3. Resources — **real, verified links only** (video + reading). Never fabricate URLs; web-search and confirm before citing. Note runtime/section to watch if a video covers more than the week needs.
4. Functional example — written as a **skeleton to build together**, not a fully solved script, with discussion/talking points embedded (this course explicitly wants co-built examples, not handed-over solutions)
5. Exercises — 2–3 small, done in `week-XX/exercises/`, each with a one-line stretch variant where relevant
6. Weekly project — core requirements + optional stretch goals, done in `week-XX/project/`
7. Submitting work — proji commands

## Rubric doc format (established in Week 1, use as the template)

Each `RUBRIC.md` has:
1. Scoring categories (typically 4), each with Emerging/Developing/Proficient/Advanced descriptions tied to *observable* behavior in the code or the student's process — not vibes
2. **Signs of struggle** — specific, diagnosable patterns (e.g. "window is a single frozen color" → drawing calls placed before `screen.fill()`), written to help the instructor figure out *what to re-teach*, not just what to mark down
3. Suggested next step by score pattern

## Conventions to keep consistent

- pygame-ce is the specified install (`pip install pygame-ce`); code still reads `import pygame`
- Weekly folders are `week-01`, `week-02`, ... `week-16` (zero-padded, two digits)
- All resource links must be real and verified via search before inclusion — no placeholder or invented URLs
- Keep stretch goals genuinely optional; core requirements should be achievable in the 3-hour baseline
