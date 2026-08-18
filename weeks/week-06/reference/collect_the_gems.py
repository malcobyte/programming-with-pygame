"""
Week 6 reference: build this together with your instructor.

Goal: move a player around and "collect" gems by touching them --
your first real gameplay mechanic. Uses check_collision() from
shared/physics.py to notice when two rectangles overlap.
"""

import sys
from pathlib import Path

import pygame

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "shared"))
from input_handler import get_movement_vector
from physics import check_collision

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Week 6: Collect the Gems")

clock = pygame.time.Clock()

ASSETS_DIR = Path(__file__).resolve().parent / "assets"
gem_image = pygame.image.load(ASSETS_DIR / "gem.png").convert_alpha()

BACKGROUND_COLOR = (20, 20, 40)
PLAYER_COLOR = (240, 120, 60)
PLAYER_SIZE = 40
PLAYER_SPEED = 5

player_rect = pygame.Rect(50, 50, PLAYER_SIZE, PLAYER_SIZE)

# TALK: we're naming each gem individually for now instead of putting
# them in a list -- Week 7 is all about why a list makes this easier
# once you have more than two or three of something.
gem_one_rect = gem_image.get_rect(center=(400, 200))
gem_one_collected = False

gem_two_rect = gem_image.get_rect(center=(650, 450))
gem_two_collected = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- UPDATE ---
    dx, dy = get_movement_vector()
    player_rect.x += dx * PLAYER_SPEED
    player_rect.y += dy * PLAYER_SPEED
    player_rect.clamp_ip(screen.get_rect())

    # TODO (together): check whether the player has touched each gem
    # that hasn't already been collected.
    # TALK: check_collision() just answers TRUE/FALSE -- it doesn't
    # know or care what "collecting" means. Deciding what happens next
    # (setting the flag, printing a message) is up to us.
    if not gem_one_collected and check_collision(player_rect, gem_one_rect):
        gem_one_collected = True
        print("Collected gem one!")

    if not gem_two_collected and check_collision(player_rect, gem_two_rect):
        gem_two_collected = True
        print("Collected gem two!")

    # --- DRAW ---
    screen.fill(BACKGROUND_COLOR)

    # TALK: an already-collected gem shouldn't be drawn anymore --
    # that's what makes it feel "picked up."
    if not gem_one_collected:
        screen.blit(gem_image, gem_one_rect)
    if not gem_two_collected:
        screen.blit(gem_image, gem_two_rect)

    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
