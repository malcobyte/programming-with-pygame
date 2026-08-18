# Week 4: Game Loop Internals (Bouncing Ball)

## Learning objectives

By the end of this week, you can:

- Explain what velocity is, and how adding it to a position each
  frame produces motion.
- Use `apply_gravity()`, `bounce()`, and `keep_in_bounds()` from
  `shared/physics.py` to build a ball that falls and bounces.
- Explain why the game loop's phases (handle events → update → draw)
  happen in that specific order, and what breaks if you reorder them.
- Trace, frame by frame, why a bouncing ball eventually settles down
  instead of bouncing forever.

## Setup

Pull this week's material:

```bash
proji check upstream
```

## Resources

**Watch:** [Pygame Physics: Gravity & Bouncing in 5 Minutes](https://www.youtube.com/watch?v=o5yb03FvTgM)
by Bit by Bit. Short and focused — this is the whole video, not just a
section.

**Read:** [PyGame Tutorial – How to Build a Bouncing Ball Game](https://www.freecodecamp.org/news/pygame-tutorial-build-a-bouncing-game/)
from freeCodeCamp. Focus on the sections about velocity and bouncing
off the screen edges — that's this week's material. The scoring/level-
progression parts of that article go further than we're going this
week; skim or skip those.

## Functional example: build this together

Open `reference/bouncing_ball.py`. It imports from
`shared/physics.py` the same way last week's file imported from
`input_handler.py`. By the end, you'll have a red ball that falls,
bounces off the floor and walls, and gradually settles down.

Talking points already embedded in the file:

- What is velocity, in your own words? Why do we need both
  `velocity_x` and `velocity_y`?
- Why does `apply_gravity()` only change `velocity_y`, never
  `velocity_x`?
- Why do we check `hit["top"] or hit["bottom"]` before bouncing
  `velocity_y`, instead of always bouncing it every frame?
- What would the ball do if the UPDATE section ran *after* the DRAW
  section instead of before?

## Exercises

Do these in `exercises/`, as separate `.py` files. Copy
`reference/bouncing_ball.py` into each one as your starting point.

**1. Tune the physics.**
Try different values for `BOUNCE_DAMPING` (between 0 and 1) and the
starting `velocity_x`. Write a one-line comment describing how each
change affected the ball's behavior.
*Stretch:* pass a custom `gravity` value into `apply_gravity()` (its
second argument) instead of using the default, and describe the
difference between "moon gravity" (low) and "heavy gravity" (high).

**2. Break the order, then fix it.**
Move the `apply_gravity()`/position-update lines to *after* the DRAW
section instead of before it. Run the program and add a comment
describing what looks wrong (hint: what frame's position is actually
being drawn each time?). Then move the code back.

**3. Add a second ball.**
Copy the ball's variables (`ball_rect`, `velocity_x`, `velocity_y`)
under new names for a second ball, and update/draw both in the same
loop. Give it a different starting position and color.
*Stretch:* make the two balls bounce off *each other* using
`check_collision()` from `shared/physics.py` — when they collide,
swap their `velocity_x` values as a simple (not perfectly realistic)
bounce.

## Weekly project: Bouncing Ball Playground

In `project/`, create `main.py` with your own bouncing-ball scene.

**Core requirements:**

- At least one ball that falls under gravity and bounces off all four
  edges of the screen, using `apply_gravity()`, `bounce()`, and
  `keep_in_bounds()`.
- A background scene (reuse Week 2 skills — at least one shape or
  image that isn't part of the ball itself).
- Physics constants (`gravity`, `BOUNCE_DAMPING`, starting velocity)
  are tuned on purpose, not left at the reference example's defaults —
  add a comment saying what feeling you were going for (bouncy? heavy?
  floaty?).
- Standard game loop rules still apply: locked frame rate, clean quit.

**Stretch goals (optional):**

- Multiple balls, each with independent physics.
- Let the player launch a new ball with a mouse click or key press,
  using `pygame.MOUSEBUTTONDOWN` or a chosen key, at the click/spawn
  position with a random starting velocity.

## Submitting work

When your exercises and project are ready:

```bash
proji checkin
```
