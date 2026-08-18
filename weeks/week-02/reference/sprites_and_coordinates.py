"""
Week 2 reference: build this together with your instructor.

Goal: draw a still scene made of shapes and an image, each positioned
using coordinates you chose on purpose -- not by trial and error.
"""

from pathlib import Path

import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Week 2: Sprites & Coordinates")

clock = pygame.time.Clock()

# TALK: (0, 0) is the TOP-LEFT corner in pygame, not the bottom-left
# like a math graph. x grows to the right, y grows DOWNWARD. Where
# would (SCREEN_WIDTH, SCREEN_HEIGHT) land on this screen?

SKY_COLOR = (25, 25, 60)
GROUND_COLOR = (40, 120, 60)
GROUND_HEIGHT = 120

# ASSETS_DIR points at this file's own folder, so the image loads
# correctly no matter where you run the program from.
ASSETS_DIR = Path(__file__).resolve().parent / "assets"

# TODO (together): load the gem image with pygame.image.load(). Call
# .convert_alpha() on it so its transparent background actually stays
# transparent when drawn.
gem_image = pygame.image.load(ASSETS_DIR / "gem.png").convert_alpha()

# TALK: get_rect() hands back a Rect the same size as the image,
# positioned at (0, 0) by default. A Rect is just a labeled box --
# x, y, width, height -- plus handy shortcuts like .center and
# .topleft.
gem_rect = gem_image.get_rect()

# TODO (together): move the gem by SETTING its .center instead of its
# .x/.y directly -- centering is often easier than doing the math
# yourself.
gem_rect.center = (650, 150)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- DRAW ---
    screen.fill(SKY_COLOR)

    # TODO (together): draw the "ground" as a rectangle along the
    # bottom of the screen with pygame.draw.rect(). A pygame.Rect here
    # is (left, top, width, height).
    ground_rect = pygame.Rect(0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT)
    pygame.draw.rect(screen, GROUND_COLOR, ground_rect)

    # TODO (together): draw a "sun" as a circle near the top with
    # pygame.draw.circle(screen, color, (center_x, center_y), radius).
    pygame.draw.circle(screen, (250, 220, 90), (100, 90), 40)

    # TODO (together): blit the gem onto the screen at gem_rect. blit
    # always draws using a Rect's (or a plain (x, y) pair's) top-left
    # corner, which is exactly what gem_rect.center just adjusted.
    screen.blit(gem_image, gem_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
