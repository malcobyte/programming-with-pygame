# Week 9: Sprite Sheets & Animation

## Learning objectives

By the end of this week, you can:

- Use `load_sheet()` from `shared/sprite_loader.py` to slice a sprite
  sheet image into a list of individual frames.
- Cycle through animation frames over time using a frame counter and a
  delay, wrapping around with the modulo operator (`%`).
- Explain why animation is about *time*, not position — a sprite can
  stand still and still animate, or move without animating at all.
- Flip a sprite horizontally with `pygame.transform.flip()` to face
  the direction it's moving.

## Setup

Pull this week's material:

```bash
proji check upstream
```

## Resources

**Watch:** [PyGame Beginner Tutorial in Python - Sprite Animation](https://www.youtube.com/watch?v=nXOVcOBqFwM)
by Coding With Russ.

**Read:** [Pygame Animations using a Spritesheet](https://www.101computing.net/pygame-animations-using-a-spritesheet/)
from 101 Computing. Focus on how it extracts frames and cycles through
them with a counter — that's exactly what `load_sheet()` and this
week's example do, just already built for you inside `shared/`.

## Functional example: build this together

Open `reference/sprite_animation.py`. It loads `reference/assets/walker.png`
— a 4-frame walk-cycle sheet (each frame 32x32 pixels) — and animates
a little character that walks around with the keyboard, facing the
direction it's moving.

Talking points already embedded in the file:

- Why does the animation only advance while `is_moving` is `True`?
  What would it look like if frames advanced every frame regardless of
  movement?
- `current_frame = (current_frame + 1) % len(walk_frames)` — what does
  `%` (modulo) do here, and why do we need it instead of just
  `current_frame + 1`?
- Why flip the *image* (`pygame.transform.flip`) instead of, say,
  redrawing the character differently for each direction?

## Exercises

Do these in `exercises/`, as separate `.py` files. Copy
`reference/sprite_animation.py` (and its `assets/` folder) into each
one as your starting point.

**1. Tune the animation speed.**
Try a few different values for `FRAME_DELAY` (try 2, then 20) and
describe how the walk cycle feels at each extreme.
*Stretch:* replace the frame-counter approach with
`pygame.time.get_ticks()` (milliseconds since the program started) to
control timing instead — this makes the animation speed consistent
even if the frame rate changes, unlike counting game-loop frames.

**2. Give the character an idle animation.**
Instead of freezing on frame 0 when the player stops moving, keep
cycling through frames, but more slowly (a bigger delay) than the walk
animation — like gentle breathing instead of walking.
*Stretch:* use only two of the four frames for the idle animation
(e.g. frames 0 and 2) instead of all four, and compare how it looks.

**3. Push a transform past where it makes sense.**
Try using `pygame.transform.rotate(sprite_image, angle)` to rotate the
character 90 degrees when moving up or down, in addition to flipping
for left/right. Run it and look closely. Add a comment describing why
this looks *wrong* for a side-view walking character (hint: think
about what real games do instead — separate up/down sprite sheets,
not a rotated side view).

## Weekly project: Animated Character

In `project/`, create `main.py` with a character that:

**Core requirements:**

- Uses `load_sheet()` to load a sprite sheet with at least two frames
  (reusing `walker.png` is fine, or make/find your own).
- Animates while moving, using a frame counter and delay.
- Holds still (or plays a distinct idle animation) when not moving.
- Faces the direction it's moving, using `pygame.transform.flip()` or
  another visual cue of your choosing.
- Standard game loop rules still apply.

**Stretch goals (optional):**

- A distinct idle animation (Exercise 2).
- Combine this with an earlier week's gem-collecting mechanic
  (Weeks 6-8) so your now-animated character can also collect things.

## Submitting work

When your exercises and project are ready:

```bash
proji checkin
```
