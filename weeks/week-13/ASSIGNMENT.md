# Week 13: Design & Planning

This starts the capstone: your own original game, planned this week
and built across Weeks 14–15. See the note in
[`00_Curriculum_Overview.md`](../../00_Curriculum_Overview.md) on how
this week's document is structured differently from Weeks 1–12 — it's
one continuous project from here to Week 16, not four separate ones.

## Learning objectives

By the end of this week, you can:

- Scope an ambitious game idea down to a "minimum viable version" that
  is genuinely buildable in two ~3-hour sprints.
- Write a one-page game design document naming the specific Weeks
  1–12 skills your plan depends on.
- Separate "must have for this to be a complete game" from "nice to
  have if there's time" — and explain why each stretch goal isn't
  required.
- Build a rough, unpolished "gray-box" prototype of just the core loop
  to test whether an idea is fun *before* investing in art and sound.

## Setup

Pull this week's material:

```bash
proji check upstream
```

## Resources

**Read:** [Game Jam Advice for Beginners](https://www.gamedeveloper.com/design/game-jam-advice-for-beginners)
by Nadya Primak, *Game Developer*. Written for game jams (very short
deadlines), but the core advice — keep scope small, cut aggressively,
plan before you build — applies directly to a two-sprint capstone.

**Template:** [Simple Game Design Document Template](https://artsybarrels.itch.io/simple-gdd-template)
by artsybarrels — a real, minimal one-page GDD format aimed at
beginners. `reference/DESIGN_TEMPLATE.md` in this folder is a version
of this template adapted specifically for this course's skills.

**Watch (optional):** [Game Design Document Template — One Page + Super Easy](https://www.youtube.com/watch?v=q96lz725gIw)
by Tim Ruswick — a short walkthrough of filling out a one-page GDD
live, if you'd like to see the process in video form too.

## Process guide: build this together

Open `reference/WORKED_EXAMPLE.md`. Read and discuss it with your
instructor *before* touching your own idea — it walks through scoping
a made-up game ("Gem Runner") from an unrealistically huge idea down
to something buildable in two sprints, including a "cut it in half"
sanity check.

Talking points already embedded in the file:

- What's the difference between something cut as a stretch goal and
  something cut *entirely*, not even as a stretch goal? Why does that
  distinction matter?
- The worked example's Core Mechanics table names a Weeks 1–12 skill
  for every mechanic. What happens to a mechanic that doesn't map to
  anything you've learned yet?
- If you had to cut *one more row* from the worked example's Core
  Mechanics table and still have a playable game, which would it be?

## Checkpoints

Work through these in order — each one unlocks the next.

**1. Brainstorm & choose.**
In `exercises/brainstorm.md`, write three different one-sentence
pitches for original game ideas ("It's a game where you ___," no
"and"). Pick one using this test: can you say it in one sentence
without "and"? If not, keep narrowing it until you can. Write one
sentence explaining why you picked the one you did.

**2. Fill out your design doc.**
Copy `reference/DESIGN_TEMPLATE.md` to `project/DESIGN.md` and
complete it for your chosen idea — Core Loop, Core Mechanics (with a
Weeks 1–12 skill named for each row), Win/Lose Condition, Assets
Needed, Stretch Goals, and the Two-Sprint Plan. Leave the Sprint Log
section blank; that's for Weeks 14–15.

**3. Gray-box prototype.**
Copy `reference/prototype_starter.py` to `exercises/prototype.py` and
build the smallest possible playable version of just your core loop —
shapes only, no images or sound. Play it. If it's not fun even in this
ugly form, that's useful information *now*, while changing course is
cheap — go back and adjust `project/DESIGN.md` if needed.

## This week's deliverable

By the end of this week, `project/` should contain:

- `DESIGN.md` — your completed design document.
- A working gray-box prototype (copy `exercises/prototype.py` here,
  or reference it) proving your core loop is at least worth building
  further.

## Submitting work

When your checkpoints and deliverable are ready:

```bash
proji checkin
```
