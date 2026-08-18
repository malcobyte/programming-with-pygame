# Week 7: Lists & Multiple Objects

## Learning objectives

By the end of this week, you can:

- Store many similar things (gems, balls, enemies) in a single Python
  list instead of one variable per thing.
- Use a `for` loop to update or draw every item in a list with one
  block of code.
- Build a list from another list using a loop (turning a list of
  positions into a list of gems).
- Use a list comprehension to count or filter items in a list (e.g.
  "how many gems are still uncollected?").

## Setup

Pull this week's material:

```bash
proji check upstream
```

## Resources

**Watch:** [Lists in Python EXPLAINED | Python Lists | Python Tutorial for Beginners #9](https://www.youtube.com/watch?v=jgNB4GN1UaQ)
by techTFQ.

**Read:** [Python - Loop Lists](https://www.w3schools.com/python/python_lists_loop.asp)
from W3Schools. Focus on the basic `for x in list:` loop — that's most
of what this week uses. The list comprehension section near the
bottom previews what the reference example does to count collected
gems; skim it for now, you'll use it directly in Exercise 3.

## Functional example: build this together

Open `reference/gems_as_a_list.py`. It rebuilds Week 6's two named
gems as a list of five, built from a list of `(x, y)` positions using
a `for` loop. By the end, the window's title bar will show a live
"X/5 collected" count.

Talking points already embedded in the file:

- This handles 5 gems with about the same amount of code Week 6 used
  for 2. What would it take to make it 20 gems instead?
- `check_collision_group()` in `shared/physics.py` checks a rect
  against a whole list at once — but it needs each item to have a
  `.rect` **attribute**, not a `["rect"]` **dict key**. Why doesn't it
  work with our list of dicts yet? (You'll fix this in Week 8.)
- `collected_count` is built with a list comprehension:
  `[gem for gem in gems if gem["collected"]]`. What would change if
  you swapped `if gem["collected"]` for `if not gem["collected"]`?

## Exercises

Do these in `exercises/`, as separate `.py` files. Copy
`reference/gems_as_a_list.py` (and its `assets/` folder) into each one
as your starting point.

**1. Change the count without touching the loop.**
Add or remove entries from `gem_positions` to change the number of
gems (try 3, then 10). Confirm you didn't need to change any other
line of code — that's the entire point of the refactor.
*Stretch:* generate `gem_positions` with a loop using
`random.randint()` instead of typing them by hand, for a fixed count
of your choosing (e.g. 8 random positions).

**2. Print progress, not just show it.**
In addition to the title bar, print a message to the terminal the
*first* time `collected_count` reaches the total number of gems (not
every frame after) — something like `"You collected everything!"`.
*Stretch:* end the game (`running = False`) once everything is
collected, after showing the message.

**3. Remove instead of hide.**
Replace the `"collected"` boolean flag approach with actually removing
collected gems from the list. After the collision-checking loop, add:
`gems = [gem for gem in gems if not gem["collected"]]` — this builds a
brand new list containing only the gems still around, instead of
keeping collected ones in the list forever. Confirm the game still
behaves the same way from the player's perspective.
*Stretch:* explain, in a comment, one reason you might prefer keeping
a `"collected"` flag (Week 6/Exercise 1-2's approach) over actually
removing items — think about what information you'd lose.

## Weekly project: Gem Collector, Take Two

In `project/`, rebuild (or extend) your Week 6 Collector Game project
using a **list** of at least five collectibles.

**Core requirements:**

- Collectibles are built from a list (of positions, or however you'd
  like) using a `for` loop — not five/six separately named variables.
- A live collected-count shown somewhere (title bar, terminal, or
  on-screen text if you want to try something new).
- A clear win condition once every item in the list has been
  collected.
- Standard game loop rules still apply.

**Stretch goals (optional):**

- A second list — obstacles/enemies — handled the same way.
- Randomly generated collectible positions (Exercise 1's stretch).

## Submitting work

When your exercises and project are ready:

```bash
proji checkin
```
