# Curriculum Overview

A 16-week Python game development course for a total-beginner 6th
grader, built around [pygame-ce](https://pyga.me/docs/). Baseline pace
is **~3 hours/week**, self-paced, with explicit stretch goals in every
lesson and project for a student who wants to go further.

## Tools & setup

- **Python 3** + `pip install pygame-ce` (code still `import pygame`).
- **[`proji`](https://github.com/arobson/proji)** — the student-facing
  CLI. It wraps git so the student never runs git directly.

  | Command | When a student uses it |
  |---|---|
  | `proji copy arobson/programming-with-pygame` | Once, at the very start of the course: forks this repo and clones the fork locally. |
  | `proji check upstream` | At the start of each week: pulls new assignment material from the instructor's repo into the student's fork. |
  | `proji checkin` | Whenever work is ready to turn in: commits and pushes. |
  | `proji checkout` | Optional: syncs a student's own fork across two machines (e.g. school + home). |

  Full command reference: the [proji README](https://github.com/arobson/proji#commands).

## Scaffold-fading design (the core pedagogical idea)

The student is given working modules up front so they can build real
games immediately, without first learning file I/O, trigonometry-heavy
physics, or low-level input handling:

- `shared/input_handler.py` — `get_movement_vector(normalize=False) -> (dx, dy)`,
  reads arrow keys / WASD and returns a direction.
- `shared/sprite_loader.py` — `load_sheet(path, frame_width, frame_height) -> list[Surface]`,
  slices a sprite sheet image into individual animation frames.
- `shared/physics.py` — gravity, bouncing, and collision-detection
  helpers (`apply_gravity`, `bounce`, `check_collision`,
  `check_collision_group`, `keep_in_bounds`).
- `shared/sound.py` — loads and plays sound effects and background
  music (`load_sound`, `play_sound`, `play_music`, `stop_music`).

These are used as black boxes for most of the course. Once the student
has called them enough times to understand *what the code needs to
do* — not just what to type — Phase 3 has them rebuild simplified
versions of the input handler and sprite loader themselves. That
replace-the-scaffold arc is the payoff of the whole course design and
should be preserved in any future edits to the schedule below.

Every project folder in `weeks/week-XX/project/` imports from
`shared/` the same way:

```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "shared"))

from input_handler import get_movement_vector
```

That's boilerplate the student doesn't need to understand yet — it's
included at the top of every starter file with a one-line comment
saying so.

## The 16-week arc

**Phase 1 — Guided Building (1–4)**
first window & game loop · sprites & coordinates · keyboard movement · game loop internals (bouncing ball)

**Phase 2 — Core Mechanics (5–8)**
functions · collision detection · lists & multiple objects · classes & OOP (midpoint checkpoint)

**Phase 3 — I/O (9–12)**
sprite sheets & animation · keyboard input (deep dive) · sound & score · rebuild the input handler and sprite loader

**Phase 4 — Capstone (13–16)**
design & planning · build sprint 1 · build sprint 2 (polish) · presentation, playtest, reflection

## Weekly document format

Each `weeks/week-XX/ASSIGNMENT.md` has, in this order:

1. **Learning objectives** — bullet list, observable/testable.
2. **Setup** — `proji check upstream`.
3. **Resources** — real, verified links only (one video + one
   reading). Never fabricate URLs; web-search and confirm before
   citing. Note the runtime/section to watch if a video covers more
   than the week needs.
4. **Functional example** — a skeleton to build *together* with the
   instructor, not a fully solved script, with discussion/talking
   points embedded in comments.
5. **Exercises** — 2–3 small, done in `exercises/`, each with a
   one-line stretch variant where relevant.
6. **Weekly project** — core requirements + optional stretch goals,
   done in `project/`.
7. **Submitting work** — `proji checkin`.

Each `weeks/week-XX/RUBRIC.md` has:

1. **Scoring categories** (typically 4), each with
   Emerging/Developing/Proficient/Advanced descriptions tied to
   *observable* behavior in the code or the student's process — not
   vibes.
2. **Signs of struggle** — specific, diagnosable patterns (e.g.
   "window is a single frozen color" → drawing calls placed before
   `screen.fill()`), written to help the instructor figure out *what
   to re-teach*, not just what to mark down.
3. **Suggested next step** by score pattern.

## Status

| Week | Topic | Status |
|---|---|---|
| 01 | First window & game loop | Done |
| 02 | Sprites & coordinates | Done |
| 03 | Keyboard movement | Done |
| 04 | Game loop internals (bouncing ball) | Done |
| 05–16 | — | Not yet written |

Weeks are built in batches aligned to the phase breaks above (4 at a
time) so content can be reviewed and course-corrected early rather
than all at once.
