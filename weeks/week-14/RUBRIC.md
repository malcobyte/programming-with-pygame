# Week 14 Rubric: Build Sprint 1

## Scoring categories

### 1. Core Mechanic Implementation

- **Emerging** — Little to nothing from `DESIGN.md`'s Core Mechanics
  table is working; the game doesn't run.
- **Developing** — Movement works, but no other Core Mechanic from the
  design doc is functional yet.
- **Proficient** — Movement plus at least one other Core Mechanic
  (collision, physics, scoring, etc.) is genuinely working.
- **Advanced** — Most or all of the Minimum Viable Version's Core
  Mechanics are working by end of session, ahead of a typical Sprint
  1 pace.

### 2. Debugging Process

- **Emerging** — Got stuck and waited for someone else to solve it,
  with no independent attempt first.
- **Developing** — Attempted to debug independently, but by trial and
  error (randomly changing things) rather than using a technique
  (print statements, isolating the section, reading the error).
- **Proficient** — Used at least one real debugging technique from
  this week's resources, documented in the required code comment.
- **Advanced** — Comment shows genuine reasoning — not just "it was a
  typo" but *how* the typo was found (e.g. "printed the rect's
  position each frame and noticed it wasn't updating, which meant the
  update code was never being called").

### 3. Plan Adherence & Adaptation

- **Emerging** — Sprint Log entry missing or blank.
- **Developing** — Sprint Log filled in, but vague ("worked on stuff")
  rather than specific about what changed from the plan.
- **Proficient** — Sprint Log accurately and specifically describes
  what got built versus what `DESIGN.md` predicted, including any
  deviations.
- **Advanced** — Where the plan changed, the log explains *why* —
  showing the change was a deliberate decision, not an accident.

### 4. Risk-First Building

- **Emerging** — Time was spent entirely on the most comfortable/
  familiar part (usually movement or visuals) with the actually
  uncertain mechanic untouched.
- **Developing** — Attempted the riskier mechanic, but only after
  spending most of the session on easier parts first.
- **Proficient** — Genuinely tackled the mechanic they were least sure
  about early in the session, per `SPRINT_STRUCTURE.md`'s guidance.
- **Advanced** — Can articulate, unprompted, which mechanic was
  riskiest and why they chose to build it first.

## Signs of struggle

| Observed behavior | Likely cause |
|---|---|
| Nothing works because several mechanics were being built at once | Didn't follow the incremental, one-mechanic-at-a-time approach — a natural temptation on a personal project with no imposed structure. |
| Stuck on the same bug for a long stretch with no visible attempt to isolate it | The debugging techniques from this week's reading weren't actually applied — model one (usually print statements) together rather than just pointing at the bug. |
| Core mechanic from the design doc quietly disappeared with no Sprint Log note | A sign the plan is being abandoned rather than adapted — worth a direct conversation about whether that's the right call or just avoidance of a hard problem. |
| Session spent entirely on visuals/art before any mechanic works | Risk-first guidance wasn't followed — redirect toward whatever the design doc's riskiest row is before more polish work. |
| Design doc's Minimum Viable Version turns out to still be too big for one sprint | Not a failure — this is genuinely common. Revisit scope together rather than trying to force it into remaining time; better to cut now than rush later. |

## Suggested next step by score pattern

- **Weak on Category 1 (implementation):** Before Sprint 2, pair on
  finishing just the highest-priority missing mechanic together,
  rather than letting the gap compound.
- **Strong on 1, weak on Category 2 (debugging):** They can build but
  lean on others too quickly when stuck. Practice the "read the error
  out loud, then explain what the code should do" sequence on the next
  bug that comes up, explicitly.
- **Weak on Category 3 (plan adherence):** The Sprint Log habit is
  worth protecting even under time pressure — it's what makes Week 15
  possible to start efficiently. Don't skip it even if the session ran
  long.
- **Advanced across the board:** Ready for Sprint 2. If most Core
  Mechanics are already done, consider previewing Week 15's polish
  toolkit early so there's no idle time.
