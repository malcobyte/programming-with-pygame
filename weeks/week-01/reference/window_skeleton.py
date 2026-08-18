"""
Week 1 reference: build this together with your instructor.

Goal: open a window, give it a color, and keep it open until you click
the close button. This is the skeleton every pygame project starts
from -- you'll type variations of this same shape for the whole
course.
"""

import pygame

# --- Setup -------------------------------------------------------------
# pygame.init() turns on all of pygame's internal systems (graphics,
# sound, input, timers). Nothing else works until this runs.
pygame.init()

# TALK: why store width/height in variables instead of typing 800 and
# 600 directly into set_mode()? (Hint: what if five other lines also
# needed to know the window size?)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# TODO (together): create the window with pygame.display.set_mode().
# It takes one argument: a (width, height) tuple.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# TODO (together): give the window a title with pygame.display.set_caption().
pygame.display.set_caption("Week 1: My First Window")

# TALK: colors in pygame are (red, green, blue) tuples, 0-255 each.
# What color is (0, 0, 0)? What about (255, 255, 255)?
BACKGROUND_COLOR = (30, 30, 60)

# clock.tick(60) below caps the game at 60 frames per second. Without
# it, the loop runs as fast as the computer possibly can, which wastes
# battery/CPU for no visual benefit.
clock = pygame.time.Clock()

# --- The Game Loop -------------------------------------------------------
# TALK: every game ever made has some version of this loop. It runs
# once per *frame* -- for a 60fps game, that's 60 times every second.
running = True
while running:
    # 1. HANDLE EVENTS
    # TODO (together): loop over pygame.event.get() and set running to
    # False when you see a pygame.QUIT event (the user clicked the X).
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. UPDATE
    # (nothing to update yet -- this is where game logic will go
    # starting in Week 3)

    # 3. DRAW
    # TODO (together): fill the whole screen with BACKGROUND_COLOR.
    screen.fill(BACKGROUND_COLOR)

    # TODO (together): flip the display so the drawing actually shows up.
    pygame.display.flip()

    # 4. TICK THE CLOCK
    clock.tick(60)

# --- Shutdown ------------------------------------------------------------
pygame.quit()
