# Week 5: Functions

## Learning objectives

By the end of this week, you can:

- Define a function with `def`, including parameters and a `return`
  statement.
- Explain the difference between a function that *returns* a new
  value and a function that *changes* something it was given.
- Refactor duplicated code into a function that's called more than
  once.
- Explain, with an example, what a "local" variable is and why a
  variable created inside a function usually can't be used outside it.

## Setup

Pull this week's material:

```bash
proji check upstream
```

## Resources

**Watch:** [Python Functions Explained – Parameters & Return Values (Beginner Tutorial)](https://www.youtube.com/watch?v=TL79nVEnKv4)
by QA and Dev Tips.

**Read:** [Python Functions](https://www.w3schools.com/python/python_functions.asp)
from W3Schools. Read through the parameters and return-value sections;
the "Function Arguments" advanced sections (`*args`, `**kwargs`) are
beyond this week — skip those for now.

## Functional example: build this together

Open `reference/functions_and_balls.py`. It rebuilds Week 4's
bouncing-ball code as three functions: `create_ball()`,
`update_ball()`, and `draw_ball()`. By the end, you'll have two balls
bouncing independently, both driven by the exact same three functions.

Talking points already embedded in the file:

- `create_ball()` **returns** a new ball. `update_ball()` and
  `draw_ball()` don't return anything — what's the difference in how
  you use them?
- `update_ball()` changes `ball`'s contents without using `return`.
  How is that possible? (Hint: dicts, like lists, are *mutable* — a
  function can reach in and change one without handing back a new
  copy.)
- How many lines of *new* code did it take to add `ball_b` compared to
  writing all its physics out by hand, like Week 4 did?

## Exercises

Do these in `exercises/`, as separate `.py` files. Copy
`reference/functions_and_balls.py` into each one as your starting
point.

**1. Write your own function.**
Write a function `random_ball(screen_width)` that returns a ball
created by calling `create_ball()` with a random x position (`import
random`, use `random.randint`), a random color (three random values
0-255), and a fixed radius of your choosing.
*Stretch:* also randomize the radius, keeping it within a sensible
range (say, 10 to 40) so balls don't get absurdly large or tiny.

**2. Local vs. global.**
Add a variable `bounce_count = 0` before the game loop. Write a
function `count_bounce()` that tries to do `bounce_count = bounce_count + 1`
inside itself and call it whenever a ball bounces. Run it and read the
error carefully. Add a comment explaining, in your own words, why it
happened. Then fix it *without* using the `global` keyword — instead,
have `count_bounce(current_count)` take the count as a parameter and
`return` the new value, and store that return value back into
`bounce_count` in the main loop.
*Stretch:* look up what the `global` keyword does and rewrite a
*second* version of `count_bounce()` using it instead. Which version
do you think is easier to read, and why?

**3. A third ball, almost for free.**
Using `random_ball()` from Exercise 1, create a third ball and add it
to the loop's update/draw calls. Notice how little new code this
takes compared to Week 4.

## Weekly project: Function Library

In `project/`, rebuild your Week 4 Bouncing Ball Playground using
functions.

**Core requirements:**

- At least two balls, both created using the *same*
  `create_ball()` function — no copy-pasted ball-creation code.
- `update_ball()` and `draw_ball()` (or your own equivalents) used for
  every ball, not written out individually.
- One additional function of your own design, with a clear single
  purpose (examples: a function that draws your background scene, or
  a function `has_settled(ball)` that returns `True` once a ball's
  velocity is small enough that it's basically stopped bouncing).
- A short comment explaining one thing that got *easier* once this
  code was split into functions.

**Stretch goals (optional):**

- Write a function that takes a **list** of balls and updates all of
  them in a single call (a sneak peek at Week 7).
- Use your `bounce_count` from Exercise 2 to print a running bounce
  total to the console.

## Submitting work

When your exercises and project are ready:

```bash
proji checkin
```
