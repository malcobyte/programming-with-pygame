"""
physics.py — small physics helpers: gravity, bouncing, and collisions.

A "black box" tool used starting in Week 4 (the bouncing-ball game loop)
and leaned on again in Week 6 (collision detection).
"""


def apply_gravity(velocity_y, gravity=0.5, terminal_velocity=15):
    """
    Increase downward velocity by `gravity` each frame, capped at
    `terminal_velocity` so falling objects don't speed up forever.

    Args:
        velocity_y: Current vertical velocity (positive = falling down).
        gravity: How much velocity increases each frame.
        terminal_velocity: Maximum falling speed.

    Returns:
        The new velocity_y.
    """
    velocity_y += gravity
    return min(velocity_y, terminal_velocity)


def bounce(velocity, damping=1.0):
    """
    Reverse a velocity component to simulate a bounce, optionally
    losing some energy each bounce.

    Args:
        velocity: The velocity component to reverse (x or y).
        damping: Fraction of velocity kept after the bounce (1.0 = no
            energy lost, 0.8 = loses 20% of speed each bounce).

    Returns:
        The new, reversed velocity.
    """
    return -velocity * damping


def check_collision(rect_a, rect_b):
    """
    Check whether two rectangles overlap.

    Args:
        rect_a, rect_b: pygame.Rect objects (or anything with a
            .colliderect() method, like a Sprite's .rect).

    Returns:
        True if the rectangles overlap at all, False otherwise.
    """
    return rect_a.colliderect(rect_b)


def check_collision_group(rect, group):
    """
    Check whether a rectangle overlaps any rect in a list/group of
    objects that each have a .rect attribute (e.g. a pygame.sprite.Group).

    Args:
        rect: A pygame.Rect to test.
        group: An iterable of objects with a .rect attribute.

    Returns:
        A list of the objects from `group` that overlap `rect` (empty
        list if there are no collisions).
    """
    return [obj for obj in group if rect.colliderect(obj.rect)]


def keep_in_bounds(rect, screen_width, screen_height):
    """
    Clamp a rect so it stays fully inside the screen, and report which
    edges it hit -- handy for bouncing off walls.

    Args:
        rect: A pygame.Rect. Modified in place (clamped position).
        screen_width, screen_height: Size of the play area in pixels.

    Returns:
        A dict of which edges were hit this call, e.g.
        {"left": False, "right": True, "top": False, "bottom": False}
    """
    hit = {"left": False, "right": False, "top": False, "bottom": False}

    if rect.left < 0:
        rect.left = 0
        hit["left"] = True
    if rect.right > screen_width:
        rect.right = screen_width
        hit["right"] = True
    if rect.top < 0:
        rect.top = 0
        hit["top"] = True
    if rect.bottom > screen_height:
        rect.bottom = screen_height
        hit["bottom"] = True

    return hit
