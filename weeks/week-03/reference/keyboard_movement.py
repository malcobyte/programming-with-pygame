"""
Week 3 reference: build this together with your instructor.

Goal: move a shape around the screen with the keyboard, using
get_movement_vector() from shared/input_handler.py -- one of this
course's "black box" tools. You'll use it for weeks without knowing
exactly how it works inside, then rebuild your own version of it in
Week 11.
"""

import sys
from pathlib import Path

import pygame

# This adds the shared/ folder to Python's search path so the import
# below can find it. Every week from here on starts with these three
# lines -- you don't need to change them.
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "shared"))
from input_handler import get_movement_vector

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Week 3: Keyboard Movement")

clock = pygame.time.Clock()

BACKGROUND_COLOR = (20, 20, 40)
PLAYER_COLOR = (240, 120, 60)
PLAYER_SIZE = 40
PLAYER_SPEED = 5

# TALK: a Rect tracks the player's position AND size in one object.
# We'll move the player each frame by changing player_rect.x and
# player_rect.y.
player_rect = pygame.Rect(
    SCREEN_WIDTH // 2 - PLAYER_SIZE // 2,
    SCREEN_HEIGHT // 2 - PLAYER_SIZE // 2,
    PLAYER_SIZE,
    PLAYER_SIZE,
)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- UPDATE ---
    # TODO (together): call get_movement_vector() to find out which
    # direction keys are held, then move the player by (dx * speed,
    # dy * speed) each frame.
    # TALK: why multiply by PLAYER_SPEED instead of just adding dx and
    # dy directly? (dx and dy are only -1, 0, or 1.)
    dx, dy = get_movement_vector()
    player_rect.x += dx * PLAYER_SPEED
    player_rect.y += dy * PLAYER_SPEED

    # TALK: without this, the player could walk right off the edge of
    # the screen and keep going forever. clamp_ip() pulls a Rect back
    # inside another Rect (in place) if it's escaped.
    # TODO (together): keep the player on screen using clamp_ip().
    play_area = screen.get_rect()
    player_rect.clamp_ip(play_area)

    # --- DRAW ---
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
