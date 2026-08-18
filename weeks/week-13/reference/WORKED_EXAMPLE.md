# Worked Example: Filling Out a Design Doc Together

Do this with your instructor *before* touching your own idea. It's
about a made-up game, "Gem Runner," so you can see the scoping process
happen without getting attached to the result.

## Start with the big, exciting idea

A brand new game developer's first instinct is usually something like:

> "An open-world RPG where you explore a whole kingdom, collect gems
> to buy upgrades, fight different kinds of enemies, unlock new areas,
> and there's a day/night cycle and multiple levels."

TALK: this is a completely reasonable thing to *want* to build. It's
also, realistically, a multi-year project for a professional team. The
skill this week is not "want smaller things" — it's **cutting a big
idea down to a small one that still captures the fun part.**

## Find the one sentence

Ask: out of everything in that big idea, what's the *one verb* the
player does over and over that makes it fun? Here, it's probably
"dodge and collect while things get harder." Everything else (RPG
progression, day/night, multiple zones) is optional decoration around
that core loop, not the core loop itself.

**Pitch:** *"It's a game where you dodge falling obstacles while
collecting gems."*

## Fill out the rest, cutting aggressively

| Mechanic | Skill it uses |
|---|---|
| Player moves left/right along the bottom of the screen | Week 3 — keyboard movement |
| Obstacles fall from the top and bounce isn't needed — they just disappear off the bottom | Week 4 — game loop internals |
| Gems fall too; touching one adds to score | Week 6/7 — collision + lists |
| Touching an obstacle ends the game | Week 6 — collision detection |
| Score shown on screen | Week 10 — sound & score |
| Obstacle class with its own fall speed | Week 8 — classes |

**Win/lose condition:** there's no "win" — it's a survive-as-long-
as-possible game. It ends when you touch an obstacle. Score is how
long you lasted / how many gems you got.

**Cut from the big idea entirely (not even a stretch goal):** RPG
progression, day/night cycle, multiple zones, upgrades, different
enemy types. These aren't "maybe later" — they're a different, bigger
game. Naming that explicitly is part of the exercise.

**Stretch goals (small, actually reachable):** obstacles speed up
the longer you survive; a second obstacle *type* that moves
sideways instead of straight down.

## TALK: the "cut it in half" check

Even this scoped-down version — look at the Core Mechanics list one
more time. If you had to cut ONE more row and still have a playable
game, which would it go? (Probably the `Obstacle` class — a first pass
could just use plain rects and a list, no class needed yet.) You don't
have to actually cut it. The point is proving to yourself there's
margin in the plan before you commit to it.
