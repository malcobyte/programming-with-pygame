# Week 1 Rubric: Your First Window & Game Loop

## Scoring categories

### 1. Window & Game Loop Correctness

- **Emerging** — Program crashes on run, or the window never appears.
- **Developing** — Window appears, but closing requires force-quitting
  (Ctrl+C / Task Manager), or the loop is missing a piece (no
  `clock.tick`, no `display.flip`/`update`, event loop absent).
- **Proficient** — Window opens with a chosen size/title/background,
  closes cleanly via the X button, and runs at a locked frame rate.
- **Advanced** — All of the above, plus a second quit method (e.g.
  Escape key) or another self-directed correct addition to the loop.

### 2. Reading & Modifying Code

- **Emerging** — Could not change size/title/color without help, or
  changes were made by guessing rather than editing the right
  variable.
- **Developing** — Successfully changed some values (e.g. color) but
  not others (e.g. size), or changed values in a way that broke the
  program.
- **Proficient** — Correctly modified size, title, color, and frame
  rate across the exercises and project, matching what they described
  wanting to change.
- **Advanced** — Also completed at least one stretch variant
  correctly (e.g. `random.randint` colors, `screen.get_size()`).

### 3. Process: The "Break It, Then Fix It" Exercise

- **Emerging** — Skipped the exercise, or didn't actually run the
  broken version before fixing it.
- **Developing** — Ran the broken version but the explanation comment
  is missing, vague ("it broke"), or describes the wrong cause.
- **Proficient** — Ran the broken version, observed the window
  wouldn't close, and wrote a comment correctly explaining that the
  loop had no way to know the user wanted to quit.
- **Advanced** — Same as Proficient, plus correctly implemented the
  Escape-key stretch goal as a second, independent quit condition.

### 4. Craft & Personalization

- **Emerging** — Project is an unmodified copy of the reference
  skeleton (same title, same color, same comment or no comment block).
- **Developing** — Minor personalization (e.g. only the title
  changed); comment block missing or incomplete.
- **Proficient** — Distinct size, title, and color from the reference;
  comment block present with name, week, and a real one-sentence game
  idea.
- **Advanced** — Proficient, plus at least one stretch goal (animated
  background color or custom window icon) attempted and working.

## Signs of struggle

Use these to figure out *what to re-teach*, not just what to mark
down.

| Observed behavior | Likely cause |
|---|---|
| Window won't close without force-quitting | The `pygame.QUIT` check is missing, misindented (outside the `for` loop), or checking the wrong attribute/value. |
| Program crashes immediately with `pygame.error: video system not initialized` | `pygame.init()` is missing, or a display call runs before it. |
| Window opens and closes instantly, no visible pause | The `while running:` loop body isn't actually looping — check indentation, or `running` is being set to `False` unconditionally somewhere inside the loop. |
| Window appears to flicker or flash | `screen.fill()` is being called outside the loop (so old frames never clear), or `pygame.display.flip()`/`update()` is missing so nothing new ever shows. |
| Fan spins up / high CPU use while the window is open | `clock.tick(60)` is missing from the loop, so it runs unthrottled. |
| Color or size change "didn't work" | Value was changed in the wrong place (e.g. a local copy or a value used after `set_mode()`/`set_caption()` already ran), or the file that was edited isn't the file that was run. |
| Can't explain what the game loop does, even after building it together | The `TALK` discussion points were skipped or rushed — worth re-doing the reference example out loud before moving to the exercises. |

## Suggested next step by score pattern

- **Mostly Emerging/Developing on Category 1:** Re-do the reference
  example together line-by-line before assigning more exercises —
  don't move to Week 2 yet. The game loop shape is load-bearing for
  the rest of the course.
- **Strong on 1–2, weak on Category 3:** The student can *operate* the
  loop but doesn't yet understand *why* it's shaped that way. Ask them
  to explain the loop out loud, in their own words, before Week 2.
- **Strong on 1–3, weak on Category 4 (Craft):** Mechanically solid but
  rushing personalization. Prompt for their game idea sentence
  specifically — it matters more later (Week 13) than it seems now.
- **Advanced across the board:** Ready to move faster. Consider having
  them preview the Week 2 reading early, or attempt an extra stretch
  goal of their own design (e.g. two windows' worth of color palettes
  to choose between).
