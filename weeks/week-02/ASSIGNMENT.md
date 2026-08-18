# Week 2: Sprites & Coordinates

## Learning objectives

By the end of this week, you can:

- Explain pygame's coordinate system: (0, 0) is the top-left corner,
  x grows to the right, y grows *downward*.
- Load an image file with `pygame.image.load()` and draw it on screen
  with `blit()`.
- Use a `Rect` to position something by its `.center`, `.topleft`, or
  `.x`/`.y`, instead of guessing numbers until it looks right.
- Draw basic shapes (`rect`, `circle`) with `pygame.draw` and place
  them at coordinates you chose on purpose.
- Combine images and shapes into a single still scene.

## Setup

Pull this week's material:

```bash
proji check upstream
```

## Resources

**Watch:** [Pygame Tutorial #1 - Basic Movement and Key Presses](https://www.youtube.com/watch?v=i6xMBig-pP4)
by Tech With Tim. This week, watch only the **opening section**:
setting up the window, drawing a rectangle "player" at an (x, y)
position, and the explanation of pygame's coordinate system. **Stop
once keyboard input shows up** — that's next week's video, picked up
right where you left off.

**Read:** [Help! How Do I Move An Image?](https://pyga.me/docs/tutorials/en/move-it.html)
from the official pygame-ce docs. Read through the Surface, `blit()`,
and `Rect` sections carefully — that's this week's material. You can
skim the part about animating movement in a loop; that's Week 3.

## Functional example: build this together

Open `reference/sprites_and_coordinates.py`. Like last week, the
`TODO` comments mark lines to write together and the `TALK` comments
mark discussion points. By the end, you'll have a still scene with:

- a sky-colored background,
- a green "ground" rectangle along the bottom,
- a yellow "sun" circle,
- and a gem image (`reference/assets/gem.png`) positioned by its
  `.center`.

Talking points already embedded in the file:

- Why is (0, 0) the *top-left* corner instead of the bottom-left,
  unlike a math class graph?
- What's the difference between `pygame.draw.rect()` (draws a shape
  directly) and `blit()` (draws an already-loaded image)?
- Why set `gem_rect.center` instead of doing the math for `.x`/`.y`
  yourself?
- What would happen if `screen.blit(gem_image, gem_rect)` ran *before*
  `screen.fill(SKY_COLOR)` instead of after?

## Exercises

Do these in `exercises/`, as separate `.py` files. Copy
`reference/sprites_and_coordinates.py` (and its `assets/` folder) into
each one as your starting point.

**1. Rearrange the scene.**
Change the position of the ground, the sun, and the gem so it looks
like a *different* scene (e.g. turn the sun into a moon in a night
sky). Use at least one Rect attribute (`.center`, `.topleft`,
`.midbottom`, etc.) rather than only `.x`/`.y`.
*Stretch:* instead of hardcoding numbers, position something using an
expression like `SCREEN_WIDTH // 2` so it stays centered even if you
change the window size.

**2. Reuse the same image twice.**
Add a second `Rect` for a second gem, positioned somewhere else on
screen, and blit the *same* `gem_image` at both rects. (You only need
to load the image once — the same picture can be drawn in more than
one place.)
*Stretch:* add a third gem, and position all three using a loop over a
list of coordinates instead of writing each one out by hand.

**3. Add a shape on purpose.**
Use `pygame.draw` to add one new shape (a rectangle "house," a line
"horizon," anything you like) positioned using a calculation — for
example, exactly centered horizontally with `SCREEN_WIDTH // 2` — not
a number you found by trial and error.
*Stretch:* build your shape out of a `Rect` first (so it has a
`.center`/`.midbottom`/etc. you can query), then draw using that Rect,
instead of passing raw numbers to `pygame.draw.rect()`.

## Weekly project: Static Scene

In `project/`, create `main.py` (and a `project/assets/` folder if you
add your own images) with an original still scene.

**Core requirements:**

- Uses at least one image, loaded with `pygame.image.load()` and drawn
  with `blit()`, positioned using a `Rect`. (Reusing `gem.png` is
  fine — or find/make your own small PNG.)
- Uses at least three `pygame.draw` shapes to build the rest of the
  scene.
- Every element is positioned deliberately — no overlapping mess. Add
  a comment near at least one element explaining *why* you picked that
  position (e.g. "centered horizontally using SCREEN_WIDTH // 2").
- Still follows Week 1's rules: opens at a locked frame rate and quits
  cleanly when the X button is clicked.

**Stretch goals (optional):**

- Make the whole scene re-center itself automatically if you change
  `SCREEN_WIDTH`/`SCREEN_HEIGHT` (everything positioned by expression,
  nothing hardcoded).
- Find or make a second image asset and include it alongside the gem.

## Submitting work

When your exercises and project are ready:

```bash
proji checkin
```
