# Week 11: Rebuild the Input Handler

Since Week 3, you've called `get_movement_vector()` from
`shared/input_handler.py` without knowing what's inside it. This week,
you write it yourself. This is the first of two "rebuild the
scaffold" weeks — the whole point of the course building up to this
moment.

## Learning objectives

By the end of this week, you can:

- Write a function that reads `pygame.key.get_pressed()` and returns a
  movement direction, from scratch.
- Confirm your version behaves identically to the original in normal
  cases and edge cases (like opposite keys held together).
- Explain, concretely, what used to be a "black box" and now isn't.
- Swap your own tool into a project that used to depend on
  `shared/input_handler.py`, and confirm nothing breaks.

## Setup

Pull this week's material:

```bash
proji check upstream
```

## Resources

**Watch:** [Pygame Tutorial - 6 - Keyboard Input Controls / Key Pressed Event](https://www.youtube.com/watch?v=AvV6UxuzH5c)
by buildwithpython.

**Read:** [Python Pygame Key Get Pressed Guide](https://pytutorial.com/python-pygame-key-get-pressed-guide/)
from PyTutorial. This is the exact function you're about to
reimplement — read it closely.

## Functional example: build this together

Open `reference/my_input_handler.py`. It defines `read_movement()` —
your own version of `get_movement_vector()` — filled in with the
instructor together. Then open `reference/demo.py`, which drives a
square around the screen using `read_movement()` instead of the
shared version, proving it's a real, working replacement.

Talking points already embedded in the files:

- Why check both `pygame.K_LEFT` and `pygame.K_a` for the same
  direction, instead of picking just one?
- What happens to `dx` if both `K_LEFT` and `K_RIGHT` are held at the
  same time? Trace through the code by hand before running it.
- `demo.py` doesn't need the `sys.path.insert(...)` trick every other
  week's file has used since Week 3. Why not, this time?

## Exercises

Do these in `exercises/`, as separate folders (each with its own copy
of `my_input_handler.py` and a small demo script) since this week's
work is about the function itself, not a single file.

**1. Prove it's really the same.**
Copy `demo.py` and, in your copy, temporarily switch the import back
to the original: add the `sys.path.insert(...)` line from earlier
weeks and `from input_handler import get_movement_vector as read_movement`.
Play both versions back to back. Do they feel identical? Switch back
to your own version when you're done.
*Stretch:* add a `normalize` parameter to your own `read_movement()`,
matching the original's optional behavior from Week 3.

**2. Go beyond the original.**
Add support for a *third* key scheme the original doesn't have — for
example, `I`/`J`/`K`/`L` as a second WASD-style layout, so any of
three schemes moves the player.
*Stretch:* have `read_movement()` return a third value along with
`dx, dy` — an `is_moving` boolean — so callers don't have to
recompute `dx != 0 or dy != 0` themselves (this is exactly what Week
9's animation code needed to do manually).

**3. Document an edge case.**
Add a comment directly above your opposite-key-cancellation logic
(the two `if` statements for the same axis) explaining, in your own
words, exactly what happens when both keys on an axis are held, and
why. This is the same kind of thing professional programmers write as
a code comment *or* an automated test — you're practicing the
"document what you verified" habit either way.

## Weekly project: Own Your Input

Pick one of your earlier projects — Week 6, 7, or 8's — and copy it
into `project/`. Then:

**Core requirements:**

- Copy your working `my_input_handler.py` into the project folder.
- Replace the `shared/input_handler` import (and its
  `sys.path.insert(...)` line, if this project doesn't need
  `shared/` for anything else) with your own `read_movement()`.
- Confirm the game behaves exactly as it did before the swap.
- A comment at the top of `main.py` noting: "This project now uses my
  own input handler, built in Week 11."

**Stretch goals (optional):**

- Carry over one of Exercise 2's enhancements (a third key scheme, or
  the `is_moving` return value) into this project.

## Submitting work

When your exercises and project are ready:

```bash
proji checkin
```
