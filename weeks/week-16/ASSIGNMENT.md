# Week 16: Presentation, Playtest, Reflection

The final week. Your game gets played by someone else for the first
time, you act on what you learn from that, and you close out the
course with a real reflection on sixteen weeks of work.

## Learning objectives

By the end of this week, you can:

- Run a playtest session that produces honest, useful feedback —
  observing behavior and asking open-ended questions instead of
  leading the witness.
- Turn a playtest observation into one concrete, traceable change.
- Present your finished game and explain the choices behind it.
- Reflect specifically and honestly on what you learned across the
  whole course.

## Setup

Pull this week's material:

```bash
proji check upstream
```

## Resources

**Watch:** [Playtesting — How to Get Good Feedback on Your Game](https://www.youtube.com/watch?v=on7endO4lPY)
by Extra Credits. Explains exactly why "isn't this fun?" is the wrong
question, and what to do instead.

**Read:** [How To Playtest Your Game](https://gamedevacademy.org/game-playtest-tutorial/)
from GameDev Academy — covers finding testers, avoiding leading
questions, and simple ways to capture feedback.

## Process guide: build this together

Open `reference/PLAYTEST_GUIDE.md` and read it with your instructor
before running your own playtest. It covers what to say (and not say)
before handing over the controls, what to watch for while someone
else plays, and which questions actually produce useful answers
afterward.

Talking points already embedded in the file:

- Why is "isn't this fun?" a bad question to ask after a playtest?
- Why write observations down *during* play instead of trying to
  remember them afterward?
- What's the difference between a playtester getting stuck and a
  playtester doing something you didn't expect? Are both useful?

## Checkpoints

- [ ] Ran at least one playtest with someone who hasn't seen your game
      before (a family member, friend, or your instructor).
- [ ] Filled out `reference/PLAYTEST_NOTES_TEMPLATE.md` (copied into
      `project/PLAYTEST_NOTES.md`) *during* the session, not from
      memory afterward.
- [ ] Asked at least two open-ended questions afterward and recorded
      the answers.
- [ ] Made at least one real, traceable change to `project/main.py`
      based on what you learned.
- [ ] Wrote your final reflection using
      `reference/REFLECTION_PROMPTS.md`, copied into
      `project/REFLECTION.md`.
- [ ] Presented your finished game — live demo plus a walk through
      `project/DESIGN.md` — to your instructor (and anyone else
      who'll watch).

## This week's deliverable

`project/` should now contain your finished game (`main.py`), your
design document (`DESIGN.md`, with all four Sprint Log entries
filled in from Weeks 13–15), your playtest notes
(`PLAYTEST_NOTES.md`), and your final reflection
(`REFLECTION.md`).

## Submitting work

When everything is ready:

```bash
proji checkin
```

That's the last `checkin` of the course. Congratulations — sixteen
weeks ago this repo was an empty folder and `pygame.init()` was a new
idea.
