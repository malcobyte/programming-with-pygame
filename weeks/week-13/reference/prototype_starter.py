"""
Week 13 starter: a gray-box prototype shell.

Copy this into exercises/prototype.py and fill in YOUR core loop --
using only pygame.draw shapes, no images, no sound, no animation. The
goal is answering one question as fast as possible: is the core idea
fun? Everything else can wait.
"""

import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Gray-box Prototype")

clock = pygame.time.Clock()

BACKGROUND_COLOR = (20, 20, 40)

# TODO: set up whatever your core loop needs -- probably a player
# Rect, and maybe a list for the thing(s) it interacts with. Reuse
# whatever Weeks 1-12 tool fits: get_movement_vector(), physics.py,
# a plain list, a class -- whatever gets you a playable loop fastest.

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- UPDATE ---
    # TODO: your core loop's logic goes here.

    # --- DRAW ---
    screen.fill(BACKGROUND_COLOR)
    # TODO: pygame.draw calls only -- rects, circles. No images yet.
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
