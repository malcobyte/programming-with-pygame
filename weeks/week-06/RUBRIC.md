# Week 6 Rubric: Collision Detection

## Scoring categories

### 1. Collision Detection Correctness

- **Emerging** — Collisions never trigger, or trigger constantly
  regardless of position.
- **Developing** — Collisions work for some objects but not others, or
  only work approximately (wrong rect compared, off-by-one feel).
- **Proficient** — Every collectible correctly detects overlap with
  the player and only the player.
- **Advanced** — Same, plus Exercise 2's shrink-the-hitbox stretch
  implemented and explained correctly.

### 2. Collectible State Management

- **Emerging** — A collected gem reappears later, or collecting one
  gem affects others.
- **Developing** — Gems disappear correctly but the "collected" state
  isn't checked consistently in both the update and draw sections.
- **Proficient** — Each collectible's collected state is tracked
  independently and checked both before detecting a new collision and
  before drawing.
- **Advanced** — Same, plus a working win/end condition that correctly
  fires only once all collectibles are gone.

### 3. Black Box vs. Built-in Understanding

- **Emerging** — Exercise 2 skipped, or `check_collision()` and
  `colliderect()` are treated as unrelated tools.
- **Developing** — Swapped to `colliderect()` correctly but can't
  explain the relationship to `check_collision()`.
- **Proficient** — Can explain that `check_collision()` is a thin
  wrapper around `colliderect()`, and correctly guesses/verifies its
  implementation.
- **Advanced** — Also completed the hitbox-shrinking stretch and can
  explain *why* a slightly forgiving hitbox often feels better to
  play, even though it's technically less "accurate."

### 4. Craft & Game Feel

- **Emerging** — Project has fewer than three collectibles, or no
  feedback when the game is "won."
- **Developing** — Core mechanics present but the win state feels
  abrupt or unclear (e.g. only a console print with no visible
  connection to what just happened).
- **Proficient** — All core requirements met; collecting everything
  feels like a clear, satisfying end state.
- **Advanced** — Proficient, plus a working stretch (enemy/obstacle or
  point-value scoring).

## Signs of struggle

| Observed behavior | Likely cause |
|---|---|
| Gem disappears, then reappears later | The collected flag isn't checked before drawing, or it's accidentally being reset somewhere inside the main loop instead of only once before it starts. |
| Collision never triggers even when clearly touching | Comparing the wrong rects (e.g. `screen.get_rect()` instead of the gem's rect), or checking collision *before* the player's position is updated that same frame. |
| Player can collect a gem from far across the screen | A rect was accidentally sized to the whole screen, or a copy-paste error left two gems sharing the same rect variable. |
| Collecting one gem "collects" all of them | Copy-paste error where every gem's `collected` flag is actually the same variable, or the draw/check logic for one gem was accidentally applied to all of them. |
| The collection message prints repeatedly while touching a gem | The `not gem_x_collected` guard is missing from the `if` condition, so the block re-runs every frame the rects overlap instead of only once. |

## Suggested next step by score pattern

- **Weak on Category 1 (detection):** Walk through `check_collision()`
  together with print statements showing both rects' positions each
  frame, so the student can see *why* a particular check does or
  doesn't fire.
- **Strong on 1, weak on Category 2 (state):** The detection logic
  works but state tracking is fragile. Ask them to trace, on paper,
  what value `gem_one_collected` holds at three different points in
  time during a playthrough.
- **Weak on Category 3:** Don't skip Exercise 2 — understanding that
  "black box" tools are just regular code underneath is a core habit
  for the rest of the course, especially heading into Week 11-12's
  rebuild weeks.
- **Advanced across the board:** Ready for Week 7. Ask them to predict
  how much of `collect_the_gems.py` could shrink if all the gems lived
  in one list instead of separate variables.
