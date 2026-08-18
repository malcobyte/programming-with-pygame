# Week 12: Rebuild the Sprite Loader

This is the second and final "rebuild the scaffold" week. By the end
of today, you'll have written your own version of *both* black-box
tools this whole course was built on — `get_movement_vector()` last
week, and `load_sheet()` this week.

## Learning objectives

By the end of this week, you can:

- Write a function that slices a sprite sheet image into individual
  frames, from scratch, using `pygame.image.load()`, `Surface`, and
  `Rect` math.
- Compute a frame's pixel location on a sheet from its row, column,
  and frame size.
- Confirm your version produces frames identical to the original.
- Combine both of your rebuilt tools (this week's and last week's) in
  one project, with no dependency on `shared/` for either one.

## Setup

Pull this week's material:

```bash
proji check upstream
```

## Resources

**Watch:** [How to Crop an Image in Python's Pygame](https://www.youtube.com/watch?v=taee5LxJglk)
by Sam Whitby Coding.

**Read:** [Using Sprite Sheets in Pygame](https://ehmatthes.github.io/pcc_2e/beyond_pcc/pygame_sprite_sheets/)
from the *Python Crash Course* companion site. It computes frame
positions using margin and padding — more general than what you need
this week (our sheets have no margin or padding), but the row/column
math is the same idea `load_sheet()` uses.

## Functional example: build this together

Open `reference/my_sprite_loader.py`. It defines `slice_sheet()` —
your own version of `load_sheet()` — built together with the
instructor. Then open `reference/demo.py`, which uses `slice_sheet()`
*and* last week's `read_movement()` together to animate a walking
character with zero imports from `shared/` for either tool.

Talking points already embedded in the file:

- `columns = sheet_width // frame_width` — why integer division (`//`)
  instead of regular division (`/`)?
- The `area` Rect describes a position *on the sheet*. What's the
  difference between that and a Rect that describes where something
  gets *drawn on screen*?
- Why loop over `rows` on the outside and `columns` on the inside,
  instead of the other way around? What would change about the frame
  order if you swapped them?

## Exercises

Do these in `exercises/`, each in its own subfolder (like Week 11),
with your own copy of `my_sprite_loader.py`.

**1. Prove it's really the same.**
Load `assets/walker.png` with both your `slice_sheet()` and the
original `load_sheet()` (you'll need the `sys.path` trick to reach
`shared/` for this comparison only), and compare the frames — do they
look identical? Add a comment stating what you checked and what you
found.
*Stretch:* write a check that compares the actual pixel data of each
frame (`pygame.image.tobytes(frame, "RGBA")`) between the two
versions, instead of just looking at them.

**2. A different grid.**
Make (or find) a sprite sheet with a different layout than 4-in-a-row
— for example, 2 rows of 3 frames each — and confirm your nested loop
still produces frames in the correct reading order (left-to-right,
then top-to-bottom).
*Stretch:* draw your own tiny custom sheet using `pygame.draw` calls
saved with `pygame.image.save()`, at dimensions you choose yourself.

**3. Add something the original doesn't have.**
Write a new function, `load_row(path, frame_width, frame_height, row_index)`,
that returns only the frames from *one* row of a multi-row sheet —
useful for sheets that stack multiple animations (walk, jump, idle) in
separate rows.

## Weekly project: Own Your Sprite Loader

In `project/`, bring together everything from Weeks 9-12: take your
Week 9 Animated Character project (or start fresh) and rebuild it
using **both** of your own tools.

**Core requirements:**

- Copy `my_sprite_loader.py` into the project folder, and
  `my_input_handler.py` from Week 11 alongside it.
- No imports from `shared/input_handler.py` or
  `shared/sprite_loader.py` remain — `shared/physics.py` and
  `shared/sound.py` are still fine to use, since you haven't rebuilt
  those.
- An animated, direction-aware character, driven entirely by your own
  code.
- A short reflection comment at the top of `main.py`: what was the
  hardest part of rebuilding these two tools, and what do you
  understand now that you didn't back in Week 3 or Week 9?

**Stretch goals (optional):**

- Implement `load_row()` (Exercise 3) and use it for a character with
  more than one animation (e.g. walk and idle on separate rows).

## Submitting work

When your exercises and project are ready:

```bash
proji checkin
```
