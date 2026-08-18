"""
Week 15 reference: a "juice" toolkit.

Run this file and press SPACE repeatedly. Each press triggers a "hit"
on the circle in the middle, combining several small polish
techniques at once -- the same idea "Juice it or Lose it" demonstrates
on a plain Breakout clone. None of these change what the game DOES;
they only change how it FEELS. Copy whichever pieces you want
straight into your own project.
"""

import math
import random
import sys
from pathlib import Path

import pygame

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "shared"))
from sound import play_sound

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Week 15: Polish Toolkit -- press SPACE")

clock = pygame.time.Clock()

ASSETS_DIR = Path(__file__).resolve().parent / "assets"

BACKGROUND_COLOR = (20, 20, 40)
TARGET_COLOR = (90, 200, 250)
FLASH_COLOR = (255, 255, 255)
TARGET_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
BASE_RADIUS = 40

# --- Technique 1: screen shake ---
# TALK: shake is just "draw everything slightly offset, by a random
# amount that shrinks back to zero over a few frames."
shake_timer = 0
SHAKE_DURATION = 10
SHAKE_STRENGTH = 8

# --- Technique 2: color flash ---
flash_timer = 0
FLASH_DURATION = 6

# --- Technique 3: squash & stretch ---
squash_timer = 0
SQUASH_DURATION = 12

# --- Technique 4: particle burst ---
# TALK: each particle is just a small dict -- a list of them, updated
# and drawn with a for loop, expired ones dropped with a list
# comprehension. Same shape as Week 7's gems, different purpose.
particles = []


def trigger_hit():
    # TALK: this function changes shake_timer, flash_timer, and
    # squash_timer, all defined outside it -- that's Week 5's
    # local-vs-global lesson again. `global` here is a deliberate
    # choice, not something to reach for by default.
    global shake_timer, flash_timer, squash_timer
    shake_timer = SHAKE_DURATION
    flash_timer = FLASH_DURATION
    squash_timer = SQUASH_DURATION

    for _ in range(12):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 6)
        particles.append({
            "x": TARGET_CENTER[0],
            "y": TARGET_CENTER[1],
            "vx": speed * math.cos(angle),
            "vy": speed * math.sin(angle),
            "life": 20,
        })

    # TODO (together): play a sound on the same event that triggers
    # every other effect -- juice usually means MULTIPLE senses
    # reacting to one moment, not just one visual trick alone.
    play_sound(str(ASSETS_DIR / "collect.wav"), volume=0.5)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            trigger_hit()

    # --- UPDATE ---
    shake_timer = max(0, shake_timer - 1)
    flash_timer = max(0, flash_timer - 1)
    squash_timer = max(0, squash_timer - 1)

    for p in particles:
        p["x"] += p["vx"]
        p["y"] += p["vy"]
        p["life"] -= 1
    # TALK: this is the same "keep only what's still valid" pattern
    # from Week 7's gem collecting, applied to expiring particles
    # instead of collected gems.
    particles[:] = [p for p in particles if p["life"] > 0]

    # --- DRAW ---
    screen.fill(BACKGROUND_COLOR)

    # screen shake: offset EVERYTHING drawn this frame by a random
    # amount that shrinks as shake_timer counts down to 0.
    shake_offset = (0, 0)
    if shake_timer > 0:
        strength = SHAKE_STRENGTH * (shake_timer / SHAKE_DURATION)
        shake_offset = (
            random.uniform(-strength, strength),
            random.uniform(-strength, strength),
        )

    # squash & stretch: briefly grow the radius, then settle back to
    # BASE_RADIUS as squash_timer counts down.
    radius = BASE_RADIUS
    if squash_timer > 0:
        radius = BASE_RADIUS + int(15 * (squash_timer / SQUASH_DURATION))

    color = FLASH_COLOR if flash_timer > 0 else TARGET_COLOR

    center = (
        int(TARGET_CENTER[0] + shake_offset[0]),
        int(TARGET_CENTER[1] + shake_offset[1]),
    )
    pygame.draw.circle(screen, color, center, radius)

    for p in particles:
        fade = max(0, p["life"] / 20)
        particle_radius = max(1, int(4 * fade))
        pygame.draw.circle(screen, TARGET_COLOR, (int(p["x"]), int(p["y"])), particle_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
