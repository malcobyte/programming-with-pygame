# Week 9 Rubric: Sprite Sheets & Animation

## Scoring categories

### 1. Sprite Sheet Loading & Frame Indexing

- **Emerging** — `load_sheet()` crashes (`ValueError` about uneven
  division), or the sprite doesn't appear at all.
- **Developing** — Sheet loads but frames are wrong (sheared, showing
  the wrong portion of the image) due to mismatched `frame_width`/
  `frame_height`.
- **Proficient** — Sprite sheet loads correctly with all frames intact
  and correctly sized.
- **Advanced** — Successfully loads and uses a *different* sprite
  sheet (their own or a modified one) with different dimensions than
  the reference example.

### 2. Animation Timing

- **Emerging** — Animation doesn't advance at all, or crashes with an
  `IndexError` (missing the `% len(frames)` wraparound).
- **Developing** — Animation advances but timing is clearly broken
  (way too fast to see, or so slow it looks frozen) without the
  student noticing on their own.
- **Proficient** — Animation advances at a deliberately chosen,
  reasonable speed, correctly wrapping around the frame list.
- **Advanced** — Implements a distinct idle vs. walk animation speed
  (Exercise 2), or the `get_ticks()`-based timing stretch from
  Exercise 1.

### 3. Direction / Visual Feedback

- **Emerging** — Character always faces the same direction regardless
  of movement.
- **Developing** — Flip logic present but glitchy (flickers between
  directions while stationary, or flips on the wrong axis).
- **Proficient** — Character correctly and stably faces the direction
  it's moving, using `pygame.transform.flip()` or an equivalent visual
  cue.
- **Advanced** — Correctly reasons about the limits of simple
  transforms (Exercise 3) and can explain why real games often use
  separate sprite sheets per direction instead of rotating one.

### 4. Craft & Completeness

- **Emerging** — Project doesn't animate, or reuses the reference
  example with no changes.
- **Developing** — Core mechanics present but animation and movement
  feel disconnected (e.g. animation timing unrelated to actual speed).
- **Proficient** — All core requirements met; the character reads as
  a cohesive, animated, direction-aware sprite.
- **Advanced** — Proficient, plus a working stretch goal (idle
  animation, or integration with an earlier week's gem mechanic).

## Signs of struggle

| Observed behavior | Likely cause |
|---|---|
| `ValueError` from `load_sheet()` about uneven division | `FRAME_SIZE` (or separate width/height) doesn't match the actual pixel dimensions of the sheet — check the image's real size first. |
| Character looks sheared or shows the wrong part of the sheet | `frame_width`/`frame_height` passed to `load_sheet()` are swapped, or don't match the sheet's actual per-frame size. |
| `IndexError: list index out of range` | `current_frame` isn't wrapped with `% len(walk_frames)`, so it eventually counts past the last valid index. |
| Animation plays even while standing completely still | The `is_moving` check is missing, or `is_moving` is computed incorrectly (e.g. checking `PLAYER_SPEED` instead of `dx`/`dy`). |
| Animation flickers unreadably fast | `FRAME_DELAY` is too small (or `frame_timer` is being reset every frame regardless of whether it reached the delay). |
| Character always faces the same way | `facing_left` is set once and never updated, or the flip check happens before `facing_left` is updated that frame. |

## Suggested next step by score pattern

- **Weak on Category 1 (loading):** Before debugging further, have the
  student open the sprite sheet image in any image viewer, count the
  frames and measure one frame's pixel size by hand, and compare that
  to what's passed into `load_sheet()`.
- **Strong on 1, weak on Category 2 (timing):** They can load frames
  but the animation loop math isn't landing. Walk through
  `frame_timer`/`FRAME_DELAY`/`current_frame` together, frame by
  frame, predicting each value before running the code.
- **Weak on Category 3 (direction):** Isolate the flip logic from
  everything else — have them print `facing_left` and `dx` every
  frame while moving left and right, to see exactly when it changes.
- **Advanced across the board:** Ready for Week 10. Ask them to
  predict what new "black box" concept comes next, based on what
  hasn't been touched yet (sound, in this case).
