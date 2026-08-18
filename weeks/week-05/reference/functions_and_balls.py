"""
Week 5 reference: build this together with your instructor.

Goal: take the bouncing-ball code from Week 4 and pull it apart into
functions -- create_ball(), update_ball(), and draw_ball() -- so that
adding a second ball takes almost no new code.
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
pygame.display.set_caption("Week 5: Functions")

clock = pygame.time.Clock()

BACKGROUND_COLOR = (15, 15, 30)
BOUNCE_DAMPING = 0.85


def create_ball(x, y, radius, color, vx=4, vy=0):
    """Build and return a new ball as a dict of everything it needs."""
    return {
        "rect": pygame.Rect(x, y, radius * 2, radius * 2),
        "radius": radius,
        "color": color,
        "vx": vx,
        "vy": vy,
    }


def update_ball(ball, screen_width, screen_height):
    """
    Move `ball` by one frame of physics, bouncing off any edge it
    hits. Notice this function doesn't return anything -- it changes
    `ball`'s contents directly, since dicts (like lists) are mutable.
    """
    ball["vy"] = apply_gravity(ball["vy"])
    ball["rect"].x += ball["vx"]
    ball["rect"].y += ball["vy"]

    hit = keep_in_bounds(ball["rect"], screen_width, screen_height)
    if hit["top"] or hit["bottom"]:
        ball["vy"] = bounce(ball["vy"], BOUNCE_DAMPING)
    if hit["left"] or hit["right"]:
        ball["vx"] = bounce(ball["vx"], BOUNCE_DAMPING)


def draw_ball(screen, ball):
    """Draw `ball` at its current position."""
    pygame.draw.circle(screen, ball["color"], ball["rect"].center, ball["radius"])


# TALK: create_ball() takes arguments and RETURNS a new ball -- it
# doesn't draw or move anything itself. update_ball() and draw_ball()
# take an existing ball and DO something with it, but don't return
# anything. Both are function calls; what makes the difference?
ball_a = create_ball(200, 50, 20, (250, 90, 90), vx=4)
ball_b = create_ball(500, 100, 30, (90, 200, 250), vx=-3)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- UPDATE ---
    # TODO (together): call update_ball() for both balls. Notice this
    # is the SAME function doing the SAME job for two different balls
    # -- no copy-pasted physics code.
    update_ball(ball_a, SCREEN_WIDTH, SCREEN_HEIGHT)
    update_ball(ball_b, SCREEN_WIDTH, SCREEN_HEIGHT)

    # --- DRAW ---
    screen.fill(BACKGROUND_COLOR)
    draw_ball(screen, ball_a)
    draw_ball(screen, ball_b)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
