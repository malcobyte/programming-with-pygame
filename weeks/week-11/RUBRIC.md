# Week 11 Rubric: Rebuild the Input Handler

## Scoring categories

### 1. Correct Reimplementation

- **Emerging** — `read_movement()` returns `None` (missing `return`),
  or crashes.
- **Developing** — Function returns values but behavior differs from
  the original (e.g. only WASD or only arrows work, not both; or
  opposite keys don't cancel out to 0).
- **Proficient** — `read_movement()` matches the original's behavior
  exactly: both key schemes work, opposite keys on the same axis
  cancel to 0.
- **Advanced** — Same, plus a correct `normalize` parameter (Exercise
  1 stretch) matching the original's optional behavior.

### 2. Testing / Verification Process

- **Emerging** — Exercise 1's side-by-side comparison skipped, or the
  student can't describe whether the two versions actually matched.
- **Developing** — Comparison attempted but not systematic — vague
  impressions rather than checking specific key combinations.
- **Proficient** — Comparison confirms matching behavior, including at
  least the opposite-keys edge case (Exercise 3's documentation
  comment is accurate and specific).
- **Advanced** — Proactively checked additional edge cases beyond what
  was asked (e.g. all four keys held at once, or no keys held).

### 3. Extension Beyond the Original

- **Emerging** — Exercise 2 skipped.
- **Developing** — Third key scheme added but implemented by copying
  the existing pattern without understanding why it works (can't
  explain it back).
- **Proficient** — Third key scheme correctly added and integrated
  without breaking the original two.
- **Advanced** — Also implements the `is_moving` return-value stretch,
  correctly updating every place that used to compute it manually.

### 4. Integration

- **Emerging** — Project swap not attempted, or the swapped project no
  longer runs.
- **Developing** — Swap technically works but required trial-and-error
  debugging the student can't explain afterward.
- **Proficient** — Chosen project runs identically after swapping in
  `read_movement()`, with the reflection comment present and accurate.
- **Advanced** — Proficient, plus a working stretch enhancement
  (Exercise 2's extension) carried into the swapped project.

## Signs of struggle

| Observed behavior | Likely cause |
|---|---|
| `read_movement()` always returns `None` | The starter's `pass` placeholder was never replaced with real logic and a `return` statement. |
| Player responds to arrow keys but not WASD (or vice versa) | Only one of the two `or` conditions was written per direction — e.g. `if keys[pygame.K_LEFT]:` instead of `if keys[pygame.K_LEFT] or keys[pygame.K_a]:`. |
| Diagonal movement doesn't work | Used `elif` instead of separate `if` statements for the x-axis and y-axis checks — this makes one axis block the other instead of letting both apply independently. |
| Opposite keys don't cancel to 0 | Used `elif`/`else` between the two directions on the same axis, so only the first one checked ever takes effect, instead of both being allowed to adjust `dx`/`dy` independently. |
| `ImportError: No module named 'my_input_handler'` after the project swap | The file wasn't actually copied into the new project folder, or the demo/main file is being run from a different directory than where `my_input_handler.py` lives. |
| Swapped project behaves subtly differently from before | This is worth investigating directly rather than dismissing — ask what's different and why; it may reveal a real behavior gap between the student's version and the original. |

## Suggested next step by score pattern

- **Weak on Category 1 (reimplementation):** Don't move to the project
  yet. Sit down together and trace `read_movement()` line by line
  against a specific key state, predicting `dx`/`dy` at each step.
- **Strong on 1, weak on Category 2 (testing):** They can write
  correct code but aren't yet verifying it systematically. Model the
  habit: "how would you convince someone else this works?"
- **Weak on Category 3 (extension):** This is a confidence step, not
  just a skill step — some students hesitate to change something that
  "already works." Reassure them the goal is exploration, not
  perfection.
- **Advanced across the board:** Ready for Week 12 — the second and
  final rebuild week. Preview that they'll be doing the same thing for
  `load_sheet()` next.
