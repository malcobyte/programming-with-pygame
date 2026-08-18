# Week 7 Rubric: Lists & Multiple Objects

## Scoring categories

### 1. List Construction & Iteration

- **Emerging** — Gems still individually named, or a list exists but
  isn't actually looped over (each item accessed by hardcoded index
  instead).
- **Developing** — List and loop present, but built incorrectly (e.g.
  the loop variable is unused, or the list is rebuilt from scratch
  every frame instead of once at the start).
- **Proficient** — Gems are built from a list of positions via a `for`
  loop, and both the collision-check and draw steps use `for gem in
  gems:` loops.
- **Advanced** — Same, plus Exercise 1's stretch (randomly generated
  position list) implemented correctly.

### 2. Refactoring Payoff (DRY)

- **Emerging** — Changing the gem count (Exercise 1) required editing
  code beyond the `gem_positions` list itself.
- **Developing** — Gem count changes correctly, but other list-based
  logic (counting, drawing) needed matching hand-edits to keep working.
- **Proficient** — Changing `gem_positions` alone correctly changes
  gem count everywhere in the game with zero other edits.
- **Advanced** — Can articulate, unprompted, why this works (the loop
  doesn't care how many items are in the list).

### 3. Collision + State Tracking Within a List

- **Emerging** — Only the first gem in the list responds to
  collision, or touching one gem "collects" all of them.
- **Developing** — Per-gem state works but the collected-count logic
  is inaccurate (counts wrong, or updates on the wrong frame).
- **Proficient** — Every gem tracks its own state correctly; the
  collected count and win condition are both accurate.
- **Advanced** — Completed Exercise 3 (remove-from-list approach)
  correctly and can explain a real tradeoff versus the flag approach.

### 4. Craft & Completeness

- **Emerging** — Fewer than five collectibles, or no visible win
  condition.
- **Developing** — Core mechanics present but the collected-count
  display is missing or not live-updating.
- **Proficient** — All core requirements met with a working win
  condition and live count.
- **Advanced** — Proficient, plus a working stretch (second list of
  obstacles, or randomized positions).

## Signs of struggle

| Observed behavior | Likely cause |
|---|---|
| `IndexError` or `TypeError` building/using the gem list | Mismatched unpacking in `for x, y in gem_positions:` (e.g. a position tuple with the wrong number of values), or trying to call a dict like a function. |
| Only the first gem ever responds to touch | Collision check uses `gems[0]` directly instead of a `for gem in gems:` loop, or an `if` was used where a `for` loop was needed. |
| Touching one gem "collects" all of them | All gem dicts accidentally share the same `"collected"` value — often from building the list with the *same* dict object repeated (e.g. `[same_dict] * 5`) instead of a new dict per position. |
| Adding a 6th gem breaks something else | A second, separate list (e.g. of colors) is being matched to gems by index and wasn't updated to match — a natural motivator for Week 8's classes, which bundle related data together instead of keeping parallel lists in sync by hand. |
| Collected count is off by one, or updates on the wrong frame | Counting logic placed outside the loop that updates `collected` flags, so it's reading last frame's state instead of this frame's. |

## Suggested next step by score pattern

- **Weak on Category 1 (lists/loops):** Before moving on, have the
  student write a simple, non-game `for` loop over a list of numbers
  that prints each one doubled — build the mental model outside of
  pygame's complexity first.
- **Strong on 1, weak on Category 2 (DRY payoff):** They can write the
  loop but haven't internalized *why* it decouples "how many" from
  "how the code works." Have them change the gem count live, several
  times, and describe what did and didn't need to change each time.
- **Weak on Category 3 (state):** This is the same "each item needs
  its own independent state" idea from Week 6, now inside a
  collection. Walk through what happens to a *specific* gem in the
  list, by index, across several frames.
- **Advanced across the board:** Ready for Week 8. Ask them to predict
  what `check_collision_group()` will need to change about how gems
  are stored (dict → object with `.rect`) before it'll work.
