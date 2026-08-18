"""
input_handler.py — reads the keyboard and turns it into a movement direction.

This is one of the course's "black box" tools: you'll use
get_movement_vector() starting in Week 3, long before you understand how
it works, and you'll rebuild a simplified version of it yourself in
Week 11.
"""

import pygame


def get_movement_vector(normalize=False):
    """
    Check which movement keys are currently held down and return a
    direction as (dx, dy).

    Supports both arrow keys and WASD. Each of dx and dy is -1, 0, or 1:
      dx = -1  -> left is held        dx = 1 -> right is held
      dy = -1  -> up is held          dy = 1 -> down is held

    If both keys on an axis are held at once (e.g. left AND right), they
    cancel out to 0, same as if neither were pressed.

    Multiply the result by a speed value and add it to a sprite's
    position each frame to move it around the screen.

    Args:
        normalize: If True, diagonal movement is scaled down so moving
            diagonally isn't faster than moving in a straight line.
            Defaults to False to keep the math simple in early weeks.

    Returns:
        (dx, dy) tuple of numbers.
    """
    keys = pygame.key.get_pressed()

    dx = 0
    dy = 0

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dx -= 1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dx += 1
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        dy -= 1
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        dy += 1

    if normalize and (dx != 0 or dy != 0):
        length = (dx ** 2 + dy ** 2) ** 0.5
        dx /= length
        dy /= length

    return dx, dy
