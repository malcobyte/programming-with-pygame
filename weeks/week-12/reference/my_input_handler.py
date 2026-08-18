"""
Week 11 reference: build this together with your instructor.

Goal: write your own version of get_movement_vector() from
shared/input_handler.py, using nothing but pygame.key.get_pressed().
This is the first of two "rebuild the scaffold" weeks -- the payoff
the whole course has been building toward since Week 3.
"""

import pygame


def read_movement():
    """
    Return (dx, dy) based on which movement keys are held down right
    now. Supports arrow keys and WASD, same as the original.
    """
    # TODO (together): get the current state of every key.
    keys = pygame.key.get_pressed()

    # TODO (together): start both directions at 0, then adjust based
    # on which keys are held.
    dx = 0
    dy = 0

    # TALK: why check BOTH pygame.K_LEFT and pygame.K_a instead of
    # picking just one? What would happen to a player who only uses
    # WASD if we only checked the arrow keys?
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dx -= 1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dx += 1
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        dy -= 1
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        dy += 1

    # TALK: what happens to dx if BOTH K_LEFT and K_RIGHT are held at
    # the same time? Trace through the two `if` statements above by
    # hand to check your answer.
    return dx, dy
