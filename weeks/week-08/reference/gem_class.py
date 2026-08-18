"""
Week 8 reference: build this together with your instructor.

Goal: turn Week 7's gem dicts into a Gem CLASS, and meet a second
class, Enemy. A class bundles related data and behavior together in
one place, instead of keeping them as separate dict keys or parallel
lists that have to be kept in sync by hand.

This week is also the course's midpoint checkpoint: the project
combines nearly everything from Weeks 1-7 into one small, complete
game.
"""

import sys
from pathlib import Path

import pygame

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "shared"))
from input_handler import get_movement_vector
from physics import bounce, check_collision, check_collision_group, keep_in_bounds

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Week 8: Classes & OOP")

clock = pygame.time.Clock()

ASSETS_DIR = Path(__file__).resolve().parent / "assets"
gem_image = pygame.image.load(ASSETS_DIR / "gem.png").convert_alpha()

BACKGROUND_COLOR = (20, 20, 40)
PLAYER_COLOR = (240, 120, 60)
ENEMY_COLOR = (200, 60, 60)
PLAYER_SIZE = 40
PLAYER_SPEED = 5


class Gem:
    """
    One collectible gem. Bundles its image, position, and collected
    state together in one object, instead of keeping them as separate
    dict keys.
    """

    def __init__(self, x, y, image):
        # TALK: __init__ runs automatically every time a new Gem is
        # created. `self` refers to THIS particular gem -- the one
        # being built right now, not any other Gem.
        self.image = image
        self.rect = image.get_rect(center=(x, y))
        self.collected = False

    def draw(self, screen):
        if not self.collected:
            screen.blit(self.image, self.rect)


class Enemy:
    """A simple back-and-forth patrolling obstacle."""

    def __init__(self, x, y, size, speed):
        self.rect = pygame.Rect(x, y, size, size)
        self.velocity_x = speed

    def update(self, screen_width, screen_height):
        self.rect.x += self.velocity_x
        hit = keep_in_bounds(self.rect, screen_width, screen_height)
        if hit["left"] or hit["right"]:
            self.velocity_x = bounce(self.velocity_x)

    def draw(self, screen):
        pygame.draw.rect(screen, ENEMY_COLOR, self.rect)


player_rect = pygame.Rect(50, 50, PLAYER_SIZE, PLAYER_SIZE)

# TODO (together): build a list of Gem OBJECTS the same way Week 7
# built a list of gem dicts -- just calling Gem(...) instead of
# writing out a dict literal.
gem_positions = [(150, 150), (400, 100), (650, 200), (200, 450), (600, 400)]
gems = [Gem(x, y, gem_image) for x, y in gem_positions]

enemy = Enemy(400, 300, 30, 3)

game_over = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # --- UPDATE ---
        dx, dy = get_movement_vector()
        player_rect.x += dx * PLAYER_SPEED
        player_rect.y += dy * PLAYER_SPEED
        player_rect.clamp_ip(screen.get_rect())

        enemy.update(SCREEN_WIDTH, SCREEN_HEIGHT)

        # TALK: because Gem objects have a REAL .rect ATTRIBUTE (not a
        # dict key), check_collision_group() can check them directly
        # -- something last week's dict-based gems couldn't do.
        # TODO (together): find every uncollected gem the player is
        # touching, and mark each one collected.
        uncollected = [gem for gem in gems if not gem.collected]
        touched = check_collision_group(player_rect, uncollected)
        for gem in touched:
            gem.collected = True

        if check_collision(player_rect, enemy.rect):
            game_over = True
            print("Ouch! The enemy caught you.")

    # --- DRAW ---
    screen.fill(BACKGROUND_COLOR)
    for gem in gems:
        gem.draw(screen)
    enemy.draw(screen)
    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
