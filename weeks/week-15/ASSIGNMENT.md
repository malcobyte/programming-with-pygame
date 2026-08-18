# Week 15: Build Sprint 2 (Polish)

## Learning objectives

By the end of this week, you can:

- Finish any Minimum Viable Version mechanics left over from Sprint 1.
- Apply at least two "juice" techniques — screen shake, color flash,
  squash & stretch, particles, layered sound — using only tools from
  Weeks 1–12.
- Self-playtest your own game repeatedly and act on what you notice,
  rather than assuming your first working version is done.

## Setup

Pull this week's material:

```bash
proji check upstream
```

## Resources

**Watch:** [Juice it or lose it — a talk by Martin Jonasson & Petri Purho](https://www.youtube.com/watch?v=Fy0aCDmgnxg)
— the original, famous talk on this topic. They take a completely
plain Breakout clone and, live on stage, add effect after effect until
it feels alive. Nothing about the *rules* of the game changes — only
how it feels to play.

**Read:** [How To Improve Game Feel In Three Easy Ways](https://gamedevacademy.org/game-feel-tutorial/)
from GameDev Academy. It's written for Unity, not pygame — read it for
the *ideas* (screen shake, squash/stretch animation, sound feedback),
not the exact code. `reference/polish_toolkit.py` translates these
same three ideas into pygame code you already know how to write.

## Process guide: build this together

Open `reference/polish_toolkit.py` and run it — press SPACE repeatedly
and watch what happens. It combines four techniques on one event:
screen shake, a color flash, a squash-and-grow animation, and a burst
of particles, plus a sound effect. Copy whichever pieces fit your
game.

Talking points already embedded in the file:

- None of these techniques change what the game *does* — the target
  doesn't do anything new when hit. What do they change instead?
- `trigger_hit()` uses the `global` keyword to change variables
  defined outside the function. Why is that a deliberate choice here,
  rather than something to use by default (revisit Week 5 if this
  feels fuzzy)?
- The particle list uses `particles[:] = [p for p in particles if p["life"] > 0]`
  — the same "keep only what's still valid" idea as Week 7's gem
  collecting. What would happen if expired particles were never
  removed from the list?

## Checkpoints

- [ ] Any Minimum Viable Version mechanics still missing from Sprint 1
      are finished.
- [ ] At least two polish techniques from the toolkit are added to
      your own project — not copy-pasted unchanged, but applied to
      *your* game's actual events (a hit, a collection, a win).
- [ ] You played your own game start to finish at least three times
      and changed one specific thing that bothered you.
- [ ] `project/DESIGN.md`'s Sprint 2 Sprint Log entry is filled in.

## This week's deliverable

By the end of this week, `project/main.py` should be a feature-
complete, polished version of your Minimum Viable Version — ready to
hand to someone else to play next week.

## Submitting work

When your checkpoints and deliverable are ready:

```bash
proji checkin
```
