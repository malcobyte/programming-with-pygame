# Week 5 Rubric: Functions

## Scoring categories

### 1. Function Definition & Correct Use

- **Emerging** — Functions defined but never called, or called with
  the wrong number/type of arguments (`TypeError`).
- **Developing** — Functions work in isolation but parameters or
  return values are used incorrectly elsewhere (e.g. ignoring a
  return value that was needed, or expecting a return value from a
  function that doesn't have one).
- **Proficient** — `create_ball()`, `update_ball()`, `draw_ball()` (or
  the student's own equivalents) are defined and used correctly and
  consistently.
- **Advanced** — Same, plus a correctly written original function
  (Exercise 1's `random_ball()` or the project's custom function) with
  a sensible parameter list and return value.

### 2. Refactoring / DRY

- **Emerging** — Second/third ball still has hand-written,
  copy-pasted physics code instead of calling the shared functions.
- **Developing** — Some duplication remains (e.g. `draw_ball()` reused
  but ball creation still copy-pasted).
- **Proficient** — Adding a new ball requires only a `create_ball()`
  call plus two function calls in the loop — no duplicated logic.
- **Advanced** — Recognizes and names the benefit unprompted (the
  project's required comment clearly identifies what got easier).

### 3. Scope Understanding

- **Emerging** — Exercise 2 skipped, or the `UnboundLocalError` was
  fixed by guessing rather than understanding.
- **Developing** — Error reproduced and fixed, but the explanation
  comment is vague ("it just didn't work") rather than describing
  *why* Python treats the assignment as creating a new local variable.
- **Proficient** — Correctly explains that assigning to a variable
  inside a function makes it local to that function unless told
  otherwise, and fixes it with the parameter/return pattern.
- **Advanced** — Also completed the `global` keyword stretch and can
  compare the two approaches with a real opinion, not just "they both
  work."

### 4. Craft & Project Completeness

- **Emerging** — Project has fewer than two balls, or doesn't use the
  required functions consistently.
- **Developing** — Core mechanics work but the required
  "what got easier" comment is missing or generic.
- **Proficient** — All core requirements met, including a specific,
  accurate comment about the benefit of functions.
- **Advanced** — Proficient, plus a working stretch goal.

## Signs of struggle

| Observed behavior | Likely cause |
|---|---|
| Ball never appears or moves | `create_ball()`'s return value was never stored in a variable (called but discarded), or `update_ball()`/`draw_ball()` were never called in the loop. |
| A ball's position resets every frame instead of moving smoothly | `create_ball()` is being called *inside* the game loop instead of once before it — this creates a brand-new ball every frame instead of updating the same one. |
| Changes inside `update_ball()` don't seem to affect the ball outside it | Inside the function, the parameter was reassigned to a whole new dict (`ball = create_ball(...)`) instead of having its existing keys modified (`ball["vy"] = ...`) — reassignment breaks the connection to the original object; mutating its contents doesn't. |
| `UnboundLocalError: local variable ... referenced before assignment` outside of Exercise 2 | The same local-vs-global pattern from Exercise 2, showing up unintentionally — a sign the concept hasn't fully stuck yet. |
| `TypeError: create_ball() missing N required positional arguments` | Called without all the required arguments — check whether optional parameters (`vx`, `vy`, which have defaults) were confused with required ones (`x`, `y`, `radius`, `color`, which aren't). |

## Suggested next step by score pattern

- **Weak on Category 1 (function basics):** Before moving on, have the
  student write a trivial function from scratch (e.g. `def double(n): return n * 2`)
  and call it with a few different inputs, predicting the output each
  time.
- **Strong on 1, weak on Category 2 (DRY):** They can write functions
  but aren't yet reaching for them to avoid duplication. Point at a
  specific block of duplicated code in their own project and ask "how
  would you turn this into a function?"
- **Weak on Category 3 (scope):** This is a genuinely tricky Python
  concept — don't rush it. Walk through the `UnboundLocalError`
  together line by line before Week 6.
- **Advanced across the board:** Ready for Week 6. Consider having
  them predict, before being told, why `check_collision()` (next
  week's tool) takes two rects as parameters and returns a boolean
  instead of changing something directly.
