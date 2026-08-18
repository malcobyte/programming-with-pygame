# Week 3 Rubric: Keyboard Movement

## Scoring categories

### 1. Correct Use of the Black-Box Input Handler

- **Emerging** — Player doesn't move, or the program crashes on
  import (`ModuleNotFoundError: No module named 'input_handler'`).
- **Developing** — Player moves but incorrectly — e.g. only moves
  once per key press instead of continuously, or speed is applied
  inconsistently.
- **Proficient** — `get_movement_vector()` is called once per frame,
  its result scaled by a named `PLAYER_SPEED` variable, and applied to
  the player's position smoothly.
- **Advanced** — Same, plus a correct, working stretch feature (sprint
  key, `normalize=True` toggle, etc.) layered on top without breaking
  base movement.

### 2. Boundary Handling

- **Emerging** — Player can leave the screen entirely (disappears).
- **Developing** — Boundaries work on some edges but not others, or
  only after the student was shown the bug.
- **Proficient** — Player is correctly kept on screen on all four
  edges, via `clamp_ip()` or equivalent manual `if` logic (Exercise 2).
- **Advanced** — Completed Exercise 2's manual-clamping version
  correctly, and can explain what `clamp_ip()` does in their own
  words.

### 3. Continuous vs. Event-Based Input

- **Emerging** — Exercise 3 skipped, or the `KEYDOWN` version behaves
  identically to the continuous version (meaning it isn't actually
  event-based).
- **Developing** — `KEYDOWN` version implemented but the comparison
  comment is missing or doesn't reflect an actual observed difference.
- **Proficient** — Correctly implements fixed-step `KEYDOWN` movement,
  and the comment accurately describes the felt difference (choppier/
  more precise vs. smooth/continuous).
- **Advanced** — Same, plus diagonal movement working in the
  `KEYDOWN` version (requires combining two separate key checks).

### 4. Craft & Project Completeness

- **Emerging** — Project is the reference example with no static
  element added, or `PLAYER_SPEED` values hardcoded in multiple
  places.
- **Developing** — Static element present but the scene feels
  disconnected from Week 2's work, or `PLAYER_SPEED` is inconsistent.
- **Proficient** — All core requirements met; the project reads as a
  small, coherent scene the player moves around in.
- **Advanced** — Proficient, plus a working stretch goal.

## Signs of struggle

| Observed behavior | Likely cause |
|---|---|
| `ModuleNotFoundError: No module named 'input_handler'` | The `sys.path.insert(...)` line is missing, was moved *after* the `from input_handler import ...` line, or the file was moved to a folder at a different depth than `weeks/week-XX/<subfolder>/`, breaking the `parents[3]` count. |
| Player barely creeps across the screen | `dx`/`dy` (each only -1, 0, or 1) are being added directly to position without multiplying by `PLAYER_SPEED`. |
| Player teleports or moves unreasonably fast | `PLAYER_SPEED` is being applied more than once (e.g. also multiplied in `clamp_ip` logic by mistake), or a leftover speed value from an earlier draft is still in the code. |
| Player can walk off-screen and disappear | `clamp_ip()` (or the manual replacement in Exercise 2) is missing, misindented outside the loop, or applied to the wrong Rect. |
| Diagonal movement looks "faster" than straight movement | Expected default behavior (`normalize=False`) — not a bug, unless the assignment specifically called for `normalize=True`. |
| `KEYDOWN` version moves continuously, same as the black-box version | The movement code is still inside the main loop body unconditionally, rather than inside the `for event in pygame.event.get():` block, guarded by `event.type == pygame.KEYDOWN`. |

## Suggested next step by score pattern

- **Weak on Category 1 (import errors):** Don't debug this alone —
  walk through the `sys.path.insert` line together and count the
  folder levels out loud (`reference/` → `week-03/` → `weeks/` →
  repo root) so the pattern is understood, not just copy-pasted.
- **Strong on 1–2, weak on Category 3:** The student can operate
  input but hasn't internalized *why* there are two kinds. Have them
  narrate, out loud, what happens on-screen for each key-hold pattern
  before writing the comment.
- **Strong on 1–3, weak on Category 4:** Comfortable with the
  mechanics, rushing the project. Ask what game idea from Week 1's
  comment this project is edging toward — reconnect the skill to their
  own goal.
- **Advanced across the board:** Ready for Week 4. Consider having
  them try `get_movement_vector(normalize=True)` in their actual
  project and describe, precisely, what changes about diagonal speed
  and why.
