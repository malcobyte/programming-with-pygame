"""
Week 9 reference: build this together with your instructor.

Goal: load a sprite sheet with load_sheet() from
shared/sprite_loader.py, and animate a character by cycling through
its frames over time as it walks around.
"""

import sys
from pathlib import Path

import pygame

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "shared"))
from input_handler import get_movement_vector
from sprite_loader import load_sheet

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Week 9: Sprite Sheets & Animation")

clock = pygame.time.Clock()

ASSETS_DIR = Path(__file__).resolve().parent / "assets"

# TODO (together): load the walk-cycle sprite sheet. It's 4 frames,
# each 32x32 pixels, side by side in one image.
FRAME_SIZE = 32
walk_frames = load_sheet(ASSETS_DIR / "walker.png", FRAME_SIZE, FRAME_SIZE)

BACKGROUND_COLOR = (20, 20, 40)
PLAYER_SPEED = 4

player_rect = pygame.Rect(
    SCREEN_WIDTH // 2 - FRAME_SIZE // 2,
    SCREEN_HEIGHT // 2 - FRAME_SIZE // 2,
    FRAME_SIZE,
    FRAME_SIZE,
)

# TALK: animation is about TIME, not position -- a sprite can stand
# still and still cycle frames (an idle animation), or move fast with
# no animation at all if you don't wire the two together on purpose.
current_frame = 0
frame_timer = 0
FRAME_DELAY = 8  # how many game frames each animation frame lasts

facing_left = False

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

    is_moving = dx != 0 or dy != 0
    if dx < 0:
        facing_left = True
    elif dx > 0:
        facing_left = False

    # TODO (together): only advance the animation while the player is
    # actually moving -- otherwise just show frame 0 (standing still).
    if is_moving:
        frame_timer += 1
        if frame_timer >= FRAME_DELAY:
            frame_timer = 0
            current_frame = (current_frame + 1) % len(walk_frames)
    else:
        current_frame = 0

    # --- DRAW ---
    screen.fill(BACKGROUND_COLOR)

    sprite_image = walk_frames[current_frame]
    # TODO (together): flip the sprite horizontally when facing left,
    # using pygame.transform.flip().
    if facing_left:
        sprite_image = pygame.transform.flip(sprite_image, True, False)

    screen.blit(sprite_image, player_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
