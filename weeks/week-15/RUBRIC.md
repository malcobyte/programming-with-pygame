# Week 15 Rubric: Build Sprint 2 (Polish)

## Scoring categories

### 1. MVP Completion

- **Emerging** — Mechanics still missing from Sprint 1 remain missing.
- **Developing** — Some gaps closed, but at least one Core Mechanic
  from `DESIGN.md` still doesn't work by end of session.
- **Proficient** — All Minimum Viable Version Core Mechanics are
  working.
- **Advanced** — MVP complete with room left in the session for polish
  beyond the two-technique minimum.

### 2. Polish Technique Application

- **Emerging** — No polish techniques added.
- **Developing** — Techniques copied from `polish_toolkit.py` mostly
  unchanged, not connected to the student's own game events.
- **Proficient** — At least two techniques thoughtfully applied to the
  student's own game's actual moments (their hit event, their
  collection event, their win/lose state).
- **Advanced** — Techniques combined effectively (like the toolkit's
  `trigger_hit()`) rather than applied in isolation, and clearly
  improve how a specific moment in the game feels.

### 3. Self-Playtesting Process

- **Emerging** — No evidence of the student playing their own game
  more than once.
- **Developing** — Played multiple times, but no specific change
  resulted from it.
- **Proficient** — At least one concrete, traceable change was made
  because of something noticed while playing (a Sprint Log note or
  code comment should reflect this).
- **Advanced** — Multiple such changes, showing an iterative
  play-notice-fix loop rather than a single pass.

### 4. Craft / Overall Game Feel

- **Emerging** — Game functions but feels flat/unfinished even
  accounting for scope.
- **Developing** — Some improvement over Sprint 1's rough version, but
  polish feels tacked-on rather than integrated.
- **Proficient** — The game reads as a complete, cohesive small
  experience — someone unfamiliar with the project could pick it up
  and understand what to do.
- **Advanced** — Proficient, with a clear personal touch or detail
  that goes beyond the minimum (a specific sound choice, a particular
  color, a small joke or flourish).

## Signs of struggle

| Observed behavior | Likely cause |
|---|---|
| Adding a polish effect broke a working mechanic | Effects were added without testing incrementally — same lesson as every earlier "test as you go" moment in this course, now at higher stakes with less time left. |
| Screen shake never stops | `shake_timer` isn't being decremented every frame, or the offset calculation doesn't shrink toward zero as the timer counts down. |
| Particles pile up and never disappear | The expired-particle filter (`particles[:] = [p for p in particles if ...]`) is missing, or checks the wrong condition. |
| `global` keyword causes confusing behavior elsewhere in the file | A sign the local-vs-global distinction from Week 5 needs a quick refresher — `global` should be used narrowly and deliberately, not sprinkled everywhere a variable "isn't working." |
| No changes made this week at all | Possibly unsure how to start polishing an already-working game — walk through `polish_toolkit.py`'s techniques one at a time and pick the single most relevant one to their game's biggest moment. |

## Suggested next step by score pattern

- **Weak on Category 1 (MVP completion):** Prioritize closing gaps over
  adding polish — an unfinished mechanic matters more for Week 16's
  playtest than any amount of screen shake.
- **Strong on 1, weak on Category 2 (polish):** They have a working
  game but it may feel under-baked. Ask them to identify their game's
  single most important moment (a hit, a win) and apply one technique
  there specifically, rather than polishing randomly.
- **Weak on Category 3 (self-playtesting):** This is a preview of Week
  16's whole focus — if the habit of noticing and fixing isn't there
  yet, spend extra time here rather than pushing forward underprepared.
- **Advanced across the board:** Ready for Week 16. Encourage them to
  think about what they'll want a first-time player to notice, since
  that's exactly what next week's playtest will surface.
