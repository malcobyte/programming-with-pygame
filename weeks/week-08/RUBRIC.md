# Week 8 Rubric: Classes & OOP (Midpoint Checkpoint)

## Scoring categories

### 1. Class Definition & Instantiation

- **Emerging** — Class defined but never instantiated correctly, or
  crashes on creation (`TypeError: __init__() missing ...`).
- **Developing** — One class works, but creating multiple independent
  instances causes them to share state unintentionally.
- **Proficient** — At least two classes (one collectible type, one
  original type) correctly defined with `__init__`, and multiple
  independent instances created and stored in a list.
- **Advanced** — Same, plus a correctly parameterized `__init__`
  (e.g. Exercise 1's `points` parameter) used with different values
  across instances.

### 2. Methods & Encapsulation

- **Emerging** — Methods defined without `self`, or called on the
  class instead of an instance (`Gem.draw(screen)` instead of
  `gem.draw(screen)`).
- **Developing** — Methods work but reach outside the object for data
  that should be one of its own attributes (e.g. a global variable
  used where `self.something` belongs).
- **Proficient** — `update()`/`draw()` methods correctly read and
  change only their own object's attributes via `self`.
- **Advanced** — Custom class's methods are well-scoped and named,
  each with a single clear responsibility.

### 3. Integration / Checkpoint Completeness

- **Emerging** — Project doesn't combine movement, physics, collision,
  lists, and classes into one working game — one or more pieces
  missing entirely.
- **Developing** — All pieces present but something is broken or
  incomplete (e.g. the win condition never actually fires, or the
  enemy doesn't use real physics).
- **Proficient** — A genuinely complete small game: player movement,
  a list of class-based collectibles, a physics-driven custom entity,
  and a working win and/or lose condition.
- **Advanced** — Proficient, plus a working stretch goal (score
  tracking, multiple enemies) integrated cleanly.

### 4. Reflection & Process

- **Emerging** — Reflection comment missing, or generic
  ("it was fun") without specifics.
- **Developing** — Reflection present but only addresses one of the
  two prompts (proud-of / would-improve).
- **Proficient** — Both reflection prompts answered specifically,
  referencing actual project details.
- **Advanced** — Reflection is specific and shows genuine self-
  assessment; Exercise 3's manual-loop-vs-`check_collision_group()`
  comparison comment is also thoughtful, not just "they're the same."

## Signs of struggle

| Observed behavior | Likely cause |
|---|---|
| `TypeError: __init__() missing 1 required positional argument: 'self'` (or similar) | A method was called on the class itself (`Gem.draw(screen)`) instead of on an instance (`gem.draw(screen)`) — or `self` was left out of a method's own parameter list. |
| `AttributeError: 'Gem' object has no attribute 'rect'` | `self.rect = ...` was written as `rect = ...` inside `__init__`, creating a local variable that disappears instead of an instance attribute. |
| Collecting one gem "collects" all of them | A mutable default value (e.g. `collected = False` written directly under the class, not inside `__init__`) is being shared by every instance, instead of each instance getting its own `self.collected` in `__init__`. |
| Enemy doesn't move | `enemy.update(...)` was never called in the loop, or the method modifies a local variable instead of `self.rect`/`self.velocity_x`. |
| `check_collision_group()` includes an already-collected gem | The list passed in wasn't filtered to uncollected gems first (`[gem for gem in gems if not gem.collected]`) before calling it. |
| Project feels like separate demos glued together, not one game | Movement, gems, and the enemy might all be technically working but never actually interacting — check whether the win/lose conditions are checked every frame, not just set up once. |

## Suggested next step by score pattern

- **Weak on Category 1 (class basics):** Before the project, have the
  student write a tiny class from scratch (e.g. `class Counter:` with
  `__init__(self, start=0)` and an `increment()` method) and create
  two independent instances, confirming they don't affect each other.
- **Strong on 1-2, weak on Category 3 (integration):** The pieces work
  individually but the game doesn't feel whole. Ask them to describe,
  out loud, the exact sequence of events from game start to a win or
  loss — if they can't, that's the missing connective logic.
- **Weak on Category 4 (reflection):** Don't skip this — a genuine,
  specific reflection is good practice for the actual capstone
  reflection in Week 16, and it's worth modeling now.
- **Advanced across the board:** This is a strong checkpoint. Before
  Week 9, ask what they'd want to add to this project if the course
  gave them unlimited time — this becomes useful raw material for
  Week 13's capstone planning.
