# Week 6: Collision Detection

## Learning objectives

By the end of this week, you can:

- Use `check_collision()` from `shared/physics.py` to detect when two
  rectangles overlap.
- Explain that detecting a collision and deciding what happens because
  of it are two separate steps.
- Build a "collectible" object that disappears once touched, and stays
  gone.
- Use `pygame.Rect.colliderect()` directly, and explain how it relates
  to `check_collision()`.

## Setup

Pull this week's material:

```bash
proji check upstream
```

## Resources

**Watch:** [Collisions in Pygame - Beginner Tutorial](https://www.youtube.com/watch?v=BHr9jxKithk)
by Coding With Russ.

**Read:** the [`colliderect()`](https://www.pygame.org/docs/ref/rect.html)
entry in the official pygame `Rect` reference (search the page for
"colliderect"). It's short — a couple of sentences plus the method
signature — but it's exactly what `check_collision()` wraps.

## Functional example: build this together

Open `reference/collect_the_gems.py`. It combines Week 3's player
movement with two named gems that disappear when the player touches
them. By the end, walking your player into a gem should make it
vanish and print a message to the terminal.

Talking points already embedded in the file:

- `check_collision()` only answers true/false. What decides that a
  "true" means "make the gem disappear and print a message"?
- Why do we check `not gem_one_collected` *before* checking for a
  collision, instead of just checking the collision alone?
- Why does an already-collected gem need its own check before
  drawing, separate from the collision check?

## Exercises

Do these in `exercises/`, as separate `.py` files. Copy
`reference/collect_the_gems.py` (and its `assets/` folder) into each
one as your starting point.

**1. A third gem.**
Add `gem_three_rect` and `gem_three_collected`, following the exact
same pattern as gems one and two. Notice how much repeated code it
takes to add just *one* more gem this way — that's the setup for next
week.
*Stretch:* give each gem a point value (a number) and print a running
total collected so far each time one is picked up.

**2. Skip the black box.**
Replace every `check_collision(a, b)` call with `a.colliderect(b)`
directly — pygame's own built-in `Rect` method. Confirm the game
behaves identically. Add a one-line comment saying what you now
believe `check_collision()`'s source code looks like inside
`shared/physics.py` (you can check your guess by opening the file).
*Stretch:* try `player_rect.colliderect(gem_one_rect.inflate(-10, -10))`
instead — this shrinks the gem's hitbox slightly smaller than what's
drawn. Why might games often do this on purpose?

**3. Something that isn't good to collide with.**
Add an `enemy_rect` (drawn as a different-colored shape) that also
uses `check_collision()` against the player — but instead of
collecting it, a collision sets `running = False`, ending the game.

## Weekly project: Collector Game

In `project/`, create `main.py` for a small collection game.

**Core requirements:**

- A moving player (Week 3 skills).
- At least three collision-checked collectibles, each individually
  named (like the reference example) — they properly disappear once
  collected and stay gone.
- Feedback when *everything* has been collected — at minimum, a
  message printed to the terminal; a background color change or other
  visible effect is even better.
- Standard game loop rules still apply.

**Stretch goals (optional):**

- An enemy/obstacle (Exercise 3) that ends the game on touch.
- Point values per gem with a running total printed to the console.

## Submitting work

When your exercises and project are ready:

```bash
proji checkin
```
