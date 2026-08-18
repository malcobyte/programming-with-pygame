# Week 3: Keyboard Movement

## Learning objectives

By the end of this week, you can:

- Use `get_movement_vector()` from `shared/input_handler.py` to read
  arrow-key/WASD input as a `(dx, dy)` direction.
- Move a shape each frame by adding a speed-scaled direction to its
  position.
- Keep a moving object inside the screen using `Rect.clamp_ip()`.
- Explain the difference between *continuous* input
  (`pygame.key.get_pressed()`, what `get_movement_vector()` uses
  internally) and *event-based* input (`pygame.KEYDOWN`), and when
  you'd want each one.

## Setup

Pull this week's material:

```bash
proji check upstream
```

## Resources

**Watch:** finish [Pygame Tutorial #1 - Basic Movement and Key Presses](https://www.youtube.com/watch?v=i6xMBig-pP4)
by Tech With Tim — pick up right where you stopped last week, at the
keyboard input section.

**Read:** [PyGame Keyboard Input](https://ryanstutorials.net/pygame-tutorial/pygame-keyboard-input.php)
from Ryan's Tutorials. Pay close attention to the difference between
`pygame.key.get_pressed()` (continuous — true every frame a key is
held) and `KEYDOWN`/`KEYUP` events (fire once, on the press/release).
`get_movement_vector()` uses the first kind; Exercise 3 below has you
try the second kind yourself.

## Functional example: build this together

Open `reference/keyboard_movement.py`. Notice the three new lines at
the top, before `import pygame`:

```python
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "shared"))
from input_handler import get_movement_vector
```

That's boilerplate that tells Python where to find the `shared/`
folder. You don't need to understand exactly how it works yet — just
that it needs to come *before* the `from input_handler import ...`
line, and it'll appear at the top of every file from here on.

By the end, you'll have an orange square that moves around the screen
with the arrow keys or WASD, and can't walk off the edge.

Talking points already embedded in the file:

- Why multiply `dx`/`dy` by `PLAYER_SPEED` instead of adding them
  directly? (`dx` and `dy` are only ever -1, 0, or 1.)
- What would happen without `clamp_ip()`?
- `get_movement_vector()` is a black box right now — what do you think
  it's doing inside, based on how you're using it?

## Exercises

Do these in `exercises/`, as separate `.py` files. Copy
`reference/keyboard_movement.py` into each one as your starting point.

**1. Speed experiments.**
Try a few different values for `PLAYER_SPEED` and notice how movement
feels. Then change the call to `get_movement_vector(normalize=True)`
and move diagonally — what's different?
*Stretch:* using `pygame.key.get_pressed()` directly (peeking past the
black box), make the player move faster while Left Shift is held —
e.g. double `PLAYER_SPEED` for that frame.

**2. Boundaries without the black box.**
Comment out `player_rect.clamp_ip(play_area)`, run the program, and
move off-screen. Add a one-line comment describing what happened.
Then restore the line — but this time, replace it with your own
`if` statements that clamp each of `player_rect.left`, `.right`,
`.top`, and `.bottom` individually, so you can see what `clamp_ip()`
was doing for you.
*Stretch:* print a message to the terminal the moment the player
touches an edge (but not on every frame after — only when it first
happens).

**3. Two ways to move.**
In a copy of your file, replace the movement code with a version that
only moves the player *inside the event loop*, using
`event.type == pygame.KEYDOWN` and checking `event.key` against
`pygame.K_LEFT` / `K_RIGHT` / `K_UP` / `K_DOWN`, moving a fixed number
of pixels per press. Compare holding a key down in this version versus
the `get_movement_vector()` version. Write a one-sentence comment on
which one you'd use for a fast action game and why.
*Stretch:* support diagonal movement in the `KEYDOWN` version too.

## Weekly project: Player Controller

In `project/`, create `main.py`. You can reuse art/shape ideas from
your Week 2 static scene if you'd like.

**Core requirements:**

- Uses `get_movement_vector()` for continuous keyboard movement.
- The player can never leave the screen.
- `PLAYER_SPEED` is a single named variable used consistently — no
  speed numbers typed directly into the movement math.
- At least one static element on screen (an image or `pygame.draw`
  shape from your Week 2 skills) that the player can move around —
  it doesn't need to *interact* with the player yet; that's Week 6.
- Standard game loop rules still apply: locked frame rate, clean quit.

**Stretch goals (optional):**

- Add a Shift-to-move-faster "sprint" mode using
  `pygame.key.get_pressed()` directly, like Exercise 1's stretch.
- Change the player's color depending on which direction it's
  currently moving.

## Submitting work

When your exercises and project are ready:

```bash
proji checkin
```
