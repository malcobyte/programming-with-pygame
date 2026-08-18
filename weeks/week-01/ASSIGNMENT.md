# Week 1: Your First Window & Game Loop

## Learning objectives

By the end of this week, you can:

- Install pygame-ce and run a program that uses it.
- Open a window with a specific size, title, and background color.
- Explain, in your own words, what a "game loop" is and why a game
  needs one instead of just running its code once.
- Explain why a game loop needs to check for the "quit" event, and
  what happens if it doesn't.
- Change simple variables (width, height, colors, frame rate) and
  predict what will change on screen before running the code.

## Setup

Pull this week's material:

```bash
proji check upstream
```

Make sure pygame-ce is installed:

```bash
pip install pygame-ce
```

Quick check that it worked — run this in a terminal:

```bash
python3 -c "import pygame; print(pygame.ver)"
```

If that prints a version number instead of an error, you're ready.

## Resources

**Watch:** [Pygame in 90 Minutes - For Beginners](https://www.youtube.com/watch?v=jO6qQDNa2UY)
by Tech With Tim. You only need the **opening section** — installing
pygame, creating the window, and building the basic game loop. Stop
once the video starts adding images and moving objects; that's a
Week 2+ topic. (The rest of the video is worth a rewatch later in the
course if you want to see where this is headed.)

**Read:** [Introduction to Pygame](https://pyga.me/docs/tutorials/en/intro-to-pygame.html)
from the official pygame-ce docs. It walks through the exact same
window + game loop shape as this week's example, in about 25 lines of
code, using a bouncing-ball example. Skim past anything about actually
moving the ball — that's Week 4.

## Functional example: build this together

Open `reference/window_skeleton.py`. It's a skeleton, not a finished
program — the `TODO` comments mark lines to write together, and the
`TALK` comments mark questions to stop and discuss out loud before
moving on. By the end, you should have a window that:

- is 800x600 pixels,
- has the title "Week 1: My First Window",
- fills with a dark blue-purple background,
- and closes cleanly when you click the X button.

Talking points already embedded in the file:

- Why store screen size in variables instead of typing numbers
  everywhere?
- What do RGB color tuples mean, and what do a few example colors look
  like?
- Why does the loop need to *run continuously* instead of just drawing
  once?
- What would happen if the `pygame.QUIT` check was missing?

## Exercises

Do these in `exercises/`, as separate `.py` files (`exercise1.py`,
`exercise2.py`, `exercise3.py`). Copy `reference/window_skeleton.py`
into each one as your starting point.

**1. Make it yours.**
Change the window title and background color to something you picked
yourself (not black or white).
*Stretch:* pick the background color using `random.randint(0, 255)`
for each of red/green/blue, so it's different every time you run the
program.

**2. Resize and report.**
Change `SCREEN_WIDTH` and `SCREEN_HEIGHT` to a size of your choice,
then add a `print()` statement, right after creating the window, that
reports the size in a sentence (e.g. `"Window is 1024x768"`).
*Stretch:* instead of printing the `SCREEN_WIDTH`/`SCREEN_HEIGHT`
variables, call `screen.get_size()` and print *that* — it asks the
window itself, instead of trusting the variables weren't changed
somewhere else.

**3. Break it, then fix it.**
Comment out the `if event.type == pygame.QUIT: running = False` line.
Run the program and try to close the window normally with the X
button. Add a one-line comment above the commented-out code explaining
what happened and why. Then uncomment it to fix it.
*Stretch:* add a second way to quit — check for the Escape key
(`event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE`) and
set `running = False` for that too.

## Weekly project: Design Your Game Window

In `project/`, create `main.py` with your own window — don't just copy
the skeleton file verbatim.

**Core requirements:**

- A window with a size you chose (not necessarily 800x600).
- A custom title.
- A background color that isn't black or white.
- Correctly quits when the X button is clicked (no force-quitting
  needed).
- Runs at a locked frame rate (`clock.tick(...)`).
- A comment block at the top of the file with: your name, "Week 1",
  and one sentence about a kind of game you might want to build by the
  end of this course. (You'll revisit this sentence in Week 13 when
  you plan your capstone project — it doesn't need to be your final
  answer, just a real guess.)

**Stretch goals (optional):**

- Make the background color slowly change over time using a counter
  that increases each frame (this is a sneak peek at Week 4).
- Set a custom window icon with `pygame.display.set_icon()` (you'll
  need to load a small image first with `pygame.image.load()`).

## Submitting work

When your exercises and project are ready:

```bash
proji checkin
```
