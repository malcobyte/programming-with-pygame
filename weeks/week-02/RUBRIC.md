# Week 2 Rubric: Sprites & Coordinates

## Scoring categories

### 1. Coordinate System Understanding

- **Emerging** — Cannot explain why (0, 0) is the top-left corner, or
  positions everything by randomly changing numbers until it "looks
  right."
- **Developing** — Can explain the coordinate system out loud, but
  project elements still overlap or land off-screen unintentionally.
- **Proficient** — Correctly reasons about x/y placement, including at
  least one position calculated from screen size (e.g.
  `SCREEN_WIDTH // 2`) rather than a magic number.
- **Advanced** — All elements positioned deliberately, with a working
  explanation for each; scene would still look correct if the window
  size changed.

### 2. Image Loading & Blit

- **Emerging** — Image doesn't appear, or program crashes trying to
  load it.
- **Developing** — Image appears but with visual bugs (opaque black/
  white box instead of transparency, wrong position, flickering).
- **Proficient** — Image loads with `convert_alpha()`, is positioned
  with a `Rect`, and displays correctly with transparency intact.
- **Advanced** — Same image reused at multiple positions/rects
  correctly (Exercise 2), showing the student understands a loaded
  image isn't "used up" by one `blit()` call.

### 3. Use of `pygame.draw`

- **Emerging** — No shapes drawn beyond the reference example, or
  shapes drawn with syntax errors/incorrect arguments.
- **Developing** — At least one new shape added, but positioned by
  trial and error with no explanation.
- **Proficient** — At least three shapes drawn (project requirement),
  positioned with intent, at least one built from a `Rect` rather than
  raw coordinates.
- **Advanced** — Shapes and image work together as a coherent scene,
  not just placed independently.

### 4. Scene Composition / Craft

- **Emerging** — Scene is the reference example, unmodified or barely
  changed.
- **Developing** — Scene is different from the reference but sparse or
  visually incoherent (elements don't relate to each other).
- **Proficient** — A recognizable, original scene combining image(s)
  and shapes, with the required position-explanation comment present.
- **Advanced** — Proficient, plus at least one stretch goal (auto-
  recentering scene, or a second original image asset) working.

## Signs of struggle

| Observed behavior | Likely cause |
|---|---|
| Image doesn't appear at all | `blit()` call is missing, or it runs *before* `screen.fill()` (so it gets immediately painted over that frame). |
| `FileNotFoundError` loading the image | The path to the image is wrong — check it's using `ASSETS_DIR / "gem.png"` (or an equivalent path relative to the script file), not a bare filename that only works from one specific folder. |
| Image shows as a plain black or white box | `.convert_alpha()` was left off, so the image's transparency information wasn't applied. |
| Everything is bunched in the top-left corner | A `Rect` was created but its `.center`/`.topleft`/`.x`/`.y` was never actually set, so it's sitting at the default `(0, 0)`. |
| Shapes/image flicker or leave trails | Draw calls happening in the wrong order relative to `screen.fill()`, or `screen.fill()` missing from the loop entirely. |
| Can't explain *why* something is where it is | Position was found by trial and error rather than reasoning — have the student describe the scene's layout in words first, *then* match it to code. |

## Suggested next step by score pattern

- **Weak on Category 1 (coordinates):** Before Week 3, have the
  student predict where a shape will land *before* running the code,
  for 3-4 different `(x, y)` values — build the mental model
  explicitly rather than relying on trial and error.
- **Weak on Category 2 (image/blit) but strong on Category 3 (draw):**
  The drawing/coordinate concepts are solid; the gap is specifically
  image-file handling. Re-do just the image-loading part of the
  reference example together.
- **Strong on 1–3, weak on Category 4 (craft):** Technically correct
  but rushed the composition. Ask them to sketch the scene on paper
  first next time, *then* code it.
- **Advanced across the board:** Ready to move faster into Week 3.
  Consider a bonus challenge: reposition every element using only Rect
  attributes (`.midtop`, `.bottomright`, etc.), no raw `.x`/`.y` at
  all.
