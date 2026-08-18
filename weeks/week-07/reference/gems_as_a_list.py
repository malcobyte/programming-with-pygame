"""
Week 7 reference: build this together with your instructor.

Goal: rebuild Week 6's two hand-named gems as a LIST of gems instead
-- so that going from 2 gems to 20 takes one line, not twenty.
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
pygame.display.set_caption("Week 7: Lists & Multiple Objects")

clock = pygame.time.Clock()

ASSETS_DIR = Path(__file__).resolve().parent / "assets"
gem_image = pygame.image.load(ASSETS_DIR / "gem.png").convert_alpha()

BACKGROUND_COLOR = (20, 20, 40)
PLAYER_COLOR = (240, 120, 60)
PLAYER_SIZE = 40
PLAYER_SPEED = 5

player_rect = pygame.Rect(50, 50, PLAYER_SIZE, PLAYER_SIZE)

# TODO (together): build a list of gems from a list of positions,
# using a for loop. Each gem is a small dict, same shape as Week 6's
# gem_one/gem_two, just stored as items in a list instead of separate
# variables.
gem_positions = [(150, 150), (400, 100), (650, 200), (200, 450), (600, 400)]

gems = []
for x, y in gem_positions:
    gems.append({"rect": gem_image.get_rect(center=(x, y)), "collected": False})

# TALK: this handles 5 gems with about the same amount of code Week 6
# used for 2. What would it take to make it 20 gems instead?

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

    # TODO (together): loop over every gem and check it individually.
    # TALK: shared/physics.py also has check_collision_group(), which
    # checks a rect against a whole list at once -- but it expects
    # each item to have a `.rect` ATTRIBUTE (like `gem.rect`), not a
    # dict KEY (like `gem["rect"]`). We'll meet the version of this
    # that works with check_collision_group() next week, once gems are
    # objects instead of dicts.
    for gem in gems:
        if not gem["collected"] and check_collision(player_rect, gem["rect"]):
            gem["collected"] = True

    # --- DRAW ---
    screen.fill(BACKGROUND_COLOR)

    for gem in gems:
        if not gem["collected"]:
            screen.blit(gem_image, gem["rect"])

    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)

    # TODO (together): count how many gems are left using a list
    # comprehension, and show progress in the window's title bar.
    collected_count = len([gem for gem in gems if gem["collected"]])
    pygame.display.set_caption(f"Week 7: Lists & Multiple Objects  ({collected_count}/{len(gems)} collected)")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
