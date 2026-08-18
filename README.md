# Programming with Pygame

A 16-week Python game development curriculum for a total-beginner 6th
grader, built around [pygame-ce](https://pyga.me/docs/). This repo is
the instructor's copy: it holds the shared library code every week
builds on, plus each week's assignment and reference material.

Students don't work in this repo directly — they get their own fork
via [`proji`](https://github.com/arobson/proji), the course's
student-facing CLI. It wraps git so a total beginner can pull new
material and turn in work without learning git's full command surface
first.

## Repo layout

```
shared/                  black-box modules every week can import
  input_handler.py         keyboard -> movement direction
  sprite_loader.py         slices a sprite sheet image into frames
  physics.py                gravity, bouncing, collision helpers
  sound.py                  sound effects + background music
weeks/
  week-01/
    ASSIGNMENT.md          this week's lesson: objectives, resources,
                            functional example, exercises, project
    RUBRIC.md               instructor-facing evaluation rubric
    reference/               co-built example code/starter files
    exercises/                where the student does exercise work
    project/                  where the student does the weekly project
  week-02/
    ...
  week-16/
```

## Getting started (student, one time)

1. Install `proji` (see the [proji README](https://github.com/arobson/proji#installation)):
   ```bash
   curl -fsSL https://raw.githubusercontent.com/arobson/proji/main/install.sh | bash
   ```
2. Fork and clone this repo:
   ```bash
   proji copy arobson/programming-with-pygame
   ```
   `proji` prints a `cd <path>` line — run it to move into your new
   local copy.
3. Install Python 3 and pygame-ce:
   ```bash
   pip install pygame-ce
   ```

## Weekly workflow (student)

- **Start of the week**, pull the new assignment: `proji check upstream`
- Do the exercises and project in that week's `exercises/` and
  `project/` folders.
- **When you're ready to turn work in**: `proji checkin` — it commits
  and pushes, prompting for a message (press Enter for a default one).

No git commands are ever needed directly — `proji` is the only tool
students run to sync or submit work.

## The 16-week arc

See [`00_Curriculum_Overview.md`](00_Curriculum_Overview.md) for the
full phase-by-phase breakdown, the scaffold-fading design (why
`shared/` exists and when students rebuild it themselves), and format
conventions for `ASSIGNMENT.md` / `RUBRIC.md`.

## Conventions

- `pygame-ce` is the specified install (`pip install pygame-ce`); code
  still reads `import pygame`.
- Weekly folders are `week-01`, `week-02`, ... `week-16` (zero-padded,
  two digits).
- All resource links are real and verified before inclusion — no
  placeholder or invented URLs.
- Stretch goals are genuinely optional; core requirements fit the
  baseline **~3 hour/week** pace.
