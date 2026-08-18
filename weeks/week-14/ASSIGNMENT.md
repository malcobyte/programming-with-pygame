# Week 14: Build Sprint 1

## Learning objectives

By the end of this week, you can:

- Implement your Minimum Viable Version's core mechanics from
  `project/DESIGN.md`, working independently from your own plan.
- Debug your own code without immediately asking for the answer —
  reading error messages, adding print statements, explaining your
  code out loud.
- Recognize when a plan needs to change, and update it deliberately
  (the Sprint Log) instead of silently drifting from it.

## Setup

Pull this week's material:

```bash
proji check upstream
```

## Resources

**Read:** [Teaching Kids Strategies for Debugging Code](https://www.dummies.com/article/technology/programming-web-design/coding/teaching-kids-strategies-debugging-code-253831/)
from *Dummies*. Covers three concrete techniques — disabling/
commenting out code to isolate a problem, testing with sample data,
and adding print statements — all directly usable this week.

**Watch:** [Bug and Debugging: Finding and Fixing Code Errors for Beginners](https://www.youtube.com/watch?v=ERm0K7N_l0g)
by CodeLucky.

## Process guide: build this together

Open `reference/SPRINT_STRUCTURE.md` and read it with your instructor
before starting to build. It lays out how to spend this session:
reconnecting with your plan, building the riskiest mechanic first (not
the most fun one), a midpoint check-in, and closing with a Sprint Log
update instead of just stopping.

Talking points already embedded in the file:

- Why build the *riskiest* mechanic first instead of the most exciting
  one?
- What's the difference between getting stuck and being stuck *too
  long without doing anything about it*?
- Why write down what changed from the plan, instead of just quietly
  building something different?

## Checkpoints

Work through these during your session — they don't need to happen in
this exact order, but all should be true by the end.

- [ ] Your window opens and shows your game's starting scene.
- [ ] The player can be controlled the way `DESIGN.md` describes.
- [ ] At least one core mechanic *beyond* movement is working
      (collision, physics, scoring — whatever your design doc lists).
- [ ] You hit at least one real bug and debugged it mostly on your
      own. Add a one-sentence comment in your code describing what the
      bug was and how you found it.
- [ ] `project/DESIGN.md`'s Sprint 1 Sprint Log entry is filled in.

## This week's deliverable

By the end of this week, `project/main.py` should implement as much of
your Minimum Viable Version's core mechanics as you got to. It's
allowed to look rough — Week 15 is specifically for finishing gaps and
polish. What matters is that the *mechanics* work.

## Submitting work

When your checkpoints and deliverable are ready:

```bash
proji checkin
```
