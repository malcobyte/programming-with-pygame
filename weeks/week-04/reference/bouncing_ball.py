"""
Week 4 reference: build this together with your instructor.

Goal: a ball that falls under gravity and bounces off the walls and
floor, using shared/physics.py -- another "black box" tool. This week
is also about looking closely at the game loop itself: where does
"update" end and "draw" begin, and why does the order matter?
"""

import sys
from pathlib import Path

import pygame

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "shared"))
from physics import apply_gravity, bounce, keep_in_bounds

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Week 4: Bouncing Ball")

clock = pygame.time.Clock()

BACKGROUND_COLOR = (15, 15, 30)
BALL_COLOR = (250, 90, 90)
BALL_RADIUS = 20
BOUNCE_DAMPING = 0.85

ball_rect = pygame.Rect(SCREEN_WIDTH // 2 - BALL_RADIUS, 50, BALL_RADIUS * 2, BALL_RADIUS * 2)

# TALK: velocity is how much something moves each frame, split into x
# and y. velocity_x won't change on its own here; velocity_y will,
# because of gravity.
velocity_x = 4
velocity_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- UPDATE ---
    # TODO (together): call apply_gravity() every frame to increase
    # velocity_y, then move the ball by velocity_x and velocity_y.
    velocity_y = apply_gravity(velocity_y)
    ball_rect.x += velocity_x
    ball_rect.y += velocity_y

    # TODO (together): call keep_in_bounds() to pull the ball back
    # onto the screen, and find out which edges it hit this frame.
    hit = keep_in_bounds(ball_rect, SCREEN_WIDTH, SCREEN_HEIGHT)

    # TALK: bounce() just flips a velocity's sign (and shrinks it a
    # little, using damping, so the ball settles down over time
    # instead of bouncing forever). We only want to flip velocity_y on
    # a top/bottom hit -- flipping it on a left/right hit would send
    # the ball the wrong way. Same idea for velocity_x.
    # TODO (together): bounce velocity_y on a top/bottom hit, and
    # velocity_x on a left/right hit.
    if hit["top"] or hit["bottom"]:
        velocity_y = bounce(velocity_y, BOUNCE_DAMPING)
    if hit["left"] or hit["right"]:
        velocity_x = bounce(velocity_x, BOUNCE_DAMPING)

    # --- DRAW ---
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.circle(screen, BALL_COLOR, ball_rect.center, BALL_RADIUS)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
