# Week 10 Rubric: Sound & Score

## Scoring categories

### 1. Sound Playback

- **Emerging** — No sound plays, or the program crashes loading an
  audio file.
- **Developing** — Sound plays but incorrectly — stutters/repeats
  rapidly while touching a gem, or music restarts every frame.
- **Proficient** — Sound effect plays exactly once per collection
  event; music starts once and loops correctly.
- **Advanced** — Same, plus a correctly implemented win sound
  (Exercise 2) that plays exactly once, at the right moment.

### 2. Score Tracking & Display

- **Emerging** — Score doesn't update, or text doesn't appear on
  screen.
- **Developing** — Score updates but display is wrong somehow (stale
  value, unreadable position/color, crashes on `render()`).
- **Proficient** — Score accurately reflects collected gems and
  updates live, readably, every frame.
- **Advanced** — Same, plus score-based visual feedback (Exercise 3)
  implemented correctly.

### 3. Event-Triggered Feedback

- **Emerging** — Exercise 2 skipped, or the win sound/message
  triggers every frame after winning instead of once.
- **Developing** — Win condition detected, but the "only once" guard
  is fragile (works sometimes, breaks if gems are collected in a
  different order).
- **Proficient** — Win sound and any accompanying message/visual
  change fire exactly once, reliably, regardless of collection order.
- **Advanced** — Music fadeout (Exercise 1) correctly sequenced with
  the win sound so they don't clash.

### 4. Craft & Completeness

- **Emerging** — Missing one of: music, sound effect, or score
  display.
- **Developing** — All present but the experience feels disconnected
  (e.g. score display doesn't relate visually to the rest of the
  scene).
- **Proficient** — All core requirements met with a cohesive win
  state.
- **Advanced** — Proficient, plus a working stretch goal.

## Signs of struggle

| Observed behavior | Likely cause |
|---|---|
| Sound stutters or repeats rapidly while touching a gem | `play_sound()` isn't guarded by the same `not gem["collected"]` check that prevents re-collecting — it's re-triggering every frame the rects overlap. |
| No sound at all, no error either | This can be an environment/hardware issue rather than a code bug — confirm the system's audio output is working and unmuted before assuming the code is wrong. |
| `FileNotFoundError` loading a sound | Path isn't built from `ASSETS_DIR`, so it only works when run from one specific folder. |
| Score always shows 0, or never changes | `score +=` line missing, misindented outside the collision check, or a local/global scope mixup (Week 5's `UnboundLocalError` pattern can resurface here). |
| Score text is invisible | Rendered in a color too close to the background, or blitted at a position off-screen. |
| Win sound/message repeats every frame after winning | Missing an "already handled this" flag — the check for "all collected" is true on *every* frame once it's true, not just the first one. |

## Suggested next step by score pattern

- **Weak on Category 1 (sound):** Isolate sound from everything else —
  have the student write a 5-line test script that just loads and
  plays one sound effect, confirming the mechanism works before
  wiring it into the full game.
- **Strong on 1-2, weak on Category 3 (once-only triggers):** This is
  the third time this pattern has come up (Weeks 6, 7, now 10) — if
  it's still not landing, spend extra time here rather than pushing
  forward, since Weeks 11-12 assume this instinct is solid.
- **Weak on Category 4 only:** Mechanically correct but feels
  disjointed. Ask what a "satisfying" win moment feels like in a game
  they've played, and how that maps to code changes here.
- **Advanced across the board:** Ready for Week 11 — the first
  "rebuild the scaffold" week. Give them a heads-up: next week they'll
  write their own version of `get_movement_vector()` from scratch.
