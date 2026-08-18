# Week 4 Rubric: Game Loop Internals (Bouncing Ball)

## Scoring categories

### 1. Physics Function Usage

- **Emerging** — Ball doesn't move, falls through the floor, or the
  program crashes calling a `physics.py` function.
- **Developing** — Ball moves and falls, but bouncing is wrong (passes
  through walls, bounces on the wrong axis, or never slows down/
  never settles).
- **Proficient** — Ball correctly falls, bounces off all four edges on
  the correct axis, and gradually settles due to damping.
- **Advanced** — Same, plus a correctly tuned/customized `gravity`
  value (Exercise 1 stretch) or a working multi-ball interaction
  (Exercise 3 stretch).

### 2. Game Loop Ordering

- **Emerging** — Cannot identify which lines are "update" vs. "draw,"
  or the reference example's structure was changed in a way that
  broke it without realizing.
- **Developing** — Completed Exercise 2 (reordering) but the
  explanation comment is vague or doesn't describe an actual observed
  symptom.
- **Proficient** — Exercise 2 comment correctly identifies that moving
  update after draw means the screen shows last frame's position, one
  frame behind reality.
- **Advanced** — Can explain, unprompted, why this course's loop
  always follows handle-events → update → draw, and what category of
  bug each reordering would cause.

### 3. Debugging Process

- **Emerging** — Exercise 2's "break it" step skipped, or changes were
  reverted before actually running the broken version.
- **Developing** — Ran the broken version but needed help figuring out
  what was wrong before writing the explanation.
- **Proficient** — Independently ran the broken version, correctly
  diagnosed the symptom, and restored the working code.
- **Advanced** — Proficient, plus applied the same "predict, break,
  observe" process unprompted somewhere in Exercise 1's tuning work.

### 4. Craft & Project Completeness

- **Emerging** — Project uses the reference example's physics values
  unchanged, with no comment on the intended feel.
- **Developing** — Physics values changed but the comment doesn't
  match what actually happens on screen.
- **Proficient** — All core requirements met: tuned physics with an
  accurate comment, a background scene, standard game loop rules.
- **Advanced** — Proficient, plus a working stretch goal (multiple
  balls or click-to-spawn).

## Signs of struggle

| Observed behavior | Likely cause |
|---|---|
| Ball falls straight through the bottom of the screen | `keep_in_bounds()` isn't being called every frame, or its return value (`hit`) isn't checked before the ball exits the visible area. |
| Ball bounces off the top/bottom but keeps moving sideways forever without slowing | Correct, actually — `velocity_x` only changes on a left/right hit. If the ball never reaches a side wall in the observed run, this is expected, not a bug. |
| Ball bounces forever at full height, never settles | `BOUNCE_DAMPING` is `1.0` (or greater) — no energy is being lost each bounce. |
| Ball visibly lags behind where it "should" be | Update code (position/gravity) is running after the draw code — this is exactly Exercise 2's bug, so if it shows up unintentionally elsewhere, the ordering habit hasn't stuck yet. |
| Program crashes with a `TypeError` calling `apply_gravity`/`bounce`/`keep_in_bounds` | Arguments passed in the wrong order, or a variable holding the wrong type (e.g. passing `ball_rect` where a number was expected). |
| Second ball (Exercise 3) moves identically to the first, or only one ball is visible | Variables for the second ball were named the same as the first, so one silently overwrote the other. |

## Suggested next step by score pattern

- **Weak on Category 1 (physics functions):** Re-run the reference
  example together, pausing after each `apply_gravity`/`bounce`/
  `keep_in_bounds` call to predict the ball's next position out loud
  before continuing.
- **Strong on 1, weak on Category 2 (ordering):** The student can use
  the tools but hasn't internalized *why* the loop is shaped the way
  it is. Have them explain the three phases (events/update/draw) back
  to you before starting Week 5.
- **Weak on Category 3 (process):** This is the same "predict, break,
  observe" muscle from Week 1 and Week 3 — if it's still not landing,
  consider doing the next break-it exercise together instead of solo.
- **Advanced across the board:** Ready for Week 5 (functions). Ask
  them to identify which chunks of `bouncing_ball.py` *could* become a
  function (e.g. "update one ball") as an early preview.
