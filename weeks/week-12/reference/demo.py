"""
Week 12 reference: prove your sprite loader works.

Nearly identical to Week 9's sprite_animation.py -- except it imports
BOTH of your own rebuilt tools now: slice_sheet() from right here in
this folder, and read_movement(), copied over from Week 11.
"""

from pathlib import Path

import pygame

from my_sprite_loader import slice_sheet
from my_input_handler import read_movement

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Week 12: My Own Sprite Loader")

clock = pygame.time.Clock()

ASSETS_DIR = Path(__file__).resolve().parent / "assets"
FRAME_SIZE = 32
walk_frames = slice_sheet(ASSETS_DIR / "walker.png", FRAME_SIZE, FRAME_SIZE)

BACKGROUND_COLOR = (20, 20, 40)
PLAYER_SPEED = 4

player_rect = pygame.Rect(
    SCREEN_WIDTH // 2 - FRAME_SIZE // 2,
    SCREEN_HEIGHT // 2 - FRAME_SIZE // 2,
    FRAME_SIZE,
    FRAME_SIZE,
)

current_frame = 0
frame_timer = 0
FRAME_DELAY = 8
facing_left = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dx, dy = read_movement()
    player_rect.x += dx * PLAYER_SPEED
    player_rect.y += dy * PLAYER_SPEED
    player_rect.clamp_ip(screen.get_rect())

    is_moving = dx != 0 or dy != 0
    if dx < 0:
        facing_left = True
    elif dx > 0:
        facing_left = False

    if is_moving:
        frame_timer += 1
        if frame_timer >= FRAME_DELAY:
            frame_timer = 0
            current_frame = (current_frame + 1) % len(walk_frames)
    else:
        current_frame = 0

    screen.fill(BACKGROUND_COLOR)
    sprite_image = walk_frames[current_frame]
    if facing_left:
        sprite_image = pygame.transform.flip(sprite_image, True, False)
    screen.blit(sprite_image, player_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
