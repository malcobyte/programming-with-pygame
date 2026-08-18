"""
Week 11 reference: prove your input handler works.

This is nearly identical to Week 3's keyboard_movement.py -- except
the import at the top now points at YOUR function, in this same
folder, instead of shared/input_handler.py.

TALK: notice there's no sys.path/parents[3] trick here. That's only
needed to reach into the shared/ folder, three levels up. This file
lives right next to my_input_handler.py, so a plain import finds it.
"""

import pygame

from my_input_handler import read_movement

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Week 11: My Own Input Handler")

clock = pygame.time.Clock()

BACKGROUND_COLOR = (20, 20, 40)
PLAYER_COLOR = (90, 200, 250)
PLAYER_SIZE = 40
PLAYER_SPEED = 5

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

    dx, dy = read_movement()
    player_rect.x += dx * PLAYER_SPEED
    player_rect.y += dy * PLAYER_SPEED
    player_rect.clamp_ip(screen.get_rect())

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
