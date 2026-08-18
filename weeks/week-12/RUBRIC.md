# Week 12 Rubric: Rebuild the Sprite Loader

## Scoring categories

### 1. Correct Reimplementation

- **Emerging** — `slice_sheet()` crashes, returns an empty list, or
  frames are visibly wrong (sheared, garbled, wrong colors).
- **Developing** — Frames extracted but in the wrong order (columns
  and rows swapped), or missing `convert_alpha()`/`SRCALPHA` so
  transparency breaks.
- **Proficient** — `slice_sheet()` produces correctly ordered,
  correctly sized frames with transparency intact, matching the
  original's behavior.
- **Advanced** — Verified (Exercise 1) to be pixel-identical to
  `load_sheet()`'s output, not just visually similar.

### 2. Understanding the Math

- **Emerging** — Can't explain what `col * frame_width` computes, or
  the Rect's role in cropping.
- **Developing** — Can walk through the math with help, but makes
  errors when applied to a new sheet layout (Exercise 2).
- **Proficient** — Correctly explains why `//` (integer division) is
  used for `columns`/`rows`, and why the loop order matters for frame
  ordering.
- **Advanced** — Successfully applies the same logic to a sheet with a
  different grid shape (Exercise 2) without guidance.

### 3. Testing / Verification Process

- **Emerging** — Exercise 1 skipped, or comparison is purely visual
  ("looks about the same") with no specific check.
- **Developing** — Comparison attempted but not conclusive (e.g. only
  checked frame count, not actual pixel content).
- **Proficient** — Systematically confirmed frames match the original,
  with a comment stating exactly what was checked.
- **Advanced** — Completed the pixel-byte-comparison stretch and can
  explain why that's a stronger check than looking at the images.

### 4. Integration & Reflection

- **Emerging** — Project still imports from `shared/input_handler.py`
  or `shared/sprite_loader.py`, or doesn't run.
- **Developing** — Both rebuilt tools integrated, but the reflection
  comment is missing or generic.
- **Proficient** — Project runs entirely on the student's own input
  handler and sprite loader; reflection comment is specific and
  genuine.
- **Advanced** — Proficient, plus `load_row()` (Exercise 3) or another
  self-designed extension working in the final project.

## Signs of struggle

| Observed behavior | Likely cause |
|---|---|
| Frames appear in the wrong order | The `for row in range(rows):` / `for col in range(columns):` loop nesting was swapped, producing column-major instead of row-major order. |
| Frames are sheared or show overlapping content | The `area` Rect's `col * frame_width, row * frame_height` math has the row/column or width/height terms swapped. |
| Frames render as solid black or white boxes | `convert_alpha()` missing on the loaded sheet, or the new per-frame `Surface` wasn't created with `pygame.SRCALPHA`. |
| `slice_sheet()` returns fewer frames than expected | Integer division (`//`) truncated `columns`/`rows` because the sheet's actual size doesn't evenly divide by the frame size passed in — same class of bug as the original's `ValueError`, just silent here since this version doesn't check for it. |
| `ImportError` for `my_input_handler` in the Week 12 demo/project | The Week 11 file wasn't copied alongside `my_sprite_loader.py` — both need to live in the same folder as whatever script imports them. |

## Suggested next step by score pattern

- **Weak on Category 1-2 (reimplementation/math):** Have the student
  compute, on paper, the exact pixel `Rect` for frame index 2 of a
  4-frame, 32-pixel sheet by hand, before touching the code.
- **Strong on 1-2, weak on Category 3 (testing):** They can write it
  but aren't verifying rigorously. This is the last "black box" to
  fall in this course — model real verification discipline here,
  since it won't come up as a dedicated topic again.
- **Weak on Category 4 (integration):** Don't let this slide — a
  project that still silently imports from `shared/` defeats the
  purpose of the whole Weeks 11-12 arc. Check the actual import lines.
- **Advanced across the board:** This closes out Phase 3. Before
  Week 13's capstone planning, ask the student to describe, in their
  own words, what "scaffold fading" meant across these two weeks —
  it's good preparation for the kind of self-directed thinking the
  capstone requires.
