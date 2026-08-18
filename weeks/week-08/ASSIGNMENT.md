# Week 8: Classes & OOP (Midpoint Checkpoint)

This is the halfway point of the course. This week's project asks you
to combine nearly everything from Weeks 1-7 into one small, complete
game — consider it a checkpoint, not just another assignment.

## Learning objectives

By the end of this week, you can:

- Define a class with `__init__`, using `self` to set up instance
  attributes.
- Write instance methods (like `update()` and `draw()`) that use and
  change an object's own data.
- Create multiple independent objects from the same class and store
  them in a list.
- Explain why bundling related data into a class avoids the
  "parallel lists get out of sync" problem from Week 7.

## Setup

Pull this week's material:

```bash
proji check upstream
```

## Resources

**Watch:** [Python Tutorial for Beginners 25 - Python `__init__` and self in class](https://www.youtube.com/watch?v=oE_dWWWqxQ0)
by ProgrammingKnowledge.

**Read:** [Python `__init__()` Method](https://www.w3schools.com/python/python_class_init.asp)
from W3Schools.

## Functional example: build this together

Open `reference/gem_class.py`. It rebuilds Week 7's gem dicts as a
`Gem` class, and introduces a second class, `Enemy`, that patrols back
and forth using `shared/physics.py` — the same `bounce()` and
`keep_in_bounds()` you used for Week 4's ball. By the end, you'll have
a player collecting gems (now built with `check_collision_group()`,
which finally works because `Gem` objects have a real `.rect`
attribute) while avoiding a patrolling enemy.

Talking points already embedded in the file:

- `__init__` runs automatically whenever a new `Gem` or `Enemy` is
  created. What is `self` referring to inside it?
- Why does `check_collision_group()` work with a list of `Gem`
  objects, when it *didn't* work with last week's list of gem dicts?
- `Enemy.update()` calls `bounce()` and `keep_in_bounds()` — the exact
  same functions Week 4's bouncing ball used. What's different about
  how they're being used here?

## Exercises

Do these in `exercises/`, as separate `.py` files. Copy
`reference/gem_class.py` (and its `assets/` folder) into each one as
your starting point.

**1. Give gems a point value.**
Add a `points` parameter to `Gem.__init__()` (default it to `10`), and
track a `score` variable in the main loop that increases by a gem's
`points` value whenever it's collected. Print the score to the
console when it changes.
*Stretch:* give different gems different point values when you create
them (e.g. `Gem(x, y, gem_image, points=25)`).

**2. A second Enemy.**
Create a second `Enemy` instance with a different starting position
and speed, and add both to a list so they update and draw in a loop
(combining this week's classes with Week 7's lists).
*Stretch:* give each `Enemy` a random starting `speed` using
`random.choice([-4, -3, 3, 4])` so they don't all move in sync.

**3. Manual loop vs. `check_collision_group()`.**
Rewrite the gem-collision section to use your own `for gem in gems:`
loop (like Week 7) instead of `check_collision_group()`. Confirm it
behaves the same way. Add a one-sentence comment on which version you
find easier to read, and why.

## Weekly project (Midpoint Checkpoint): Mini Game, Milestone 1

In `project/`, build a small, complete game that combines:

**Core requirements:**

- Player movement (`get_movement_vector()`).
- At least one class-based collectible type, created as a **list** of
  instances (like `Gem` this week).
- At least one additional class of your own design — an enemy,
  moving obstacle, or something else entirely — using **physics**
  (`shared/physics.py`) for at least part of its movement.
- A clear win condition (collect everything) **and/or** lose condition
  (touch an enemy/obstacle).
- Standard game loop rules still apply.
- A short written reflection as a comment block at the top of
  `main.py`: one sentence on something you're proud of in this
  project, and one sentence on something you'd still like to improve
  if you had more time.

**Stretch goals (optional):**

- A running score (Exercise 1).
- Multiple enemies/obstacles (Exercise 2).

## Submitting work

When your exercises and project are ready:

```bash
proji checkin
```
