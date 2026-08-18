"""
sound.py — loads and plays sound effects and background music.

A "black box" tool used starting in Week 10 (sound & score).
"""

import pygame

_sound_cache = {}


def load_sound(path, volume=1.0):
    """
    Load a short sound effect file (WAV or OGG work best) and cache it
    so loading the same file twice is free the second time.

    Args:
        path: File path to the sound file.
        volume: Playback volume from 0.0 (silent) to 1.0 (full).

    Returns:
        A pygame.mixer.Sound object. Call .play() on it whenever you
        want the effect to happen (e.g. on a collision).
    """
    if path not in _sound_cache:
        _sound_cache[path] = pygame.mixer.Sound(path)

    sound = _sound_cache[path]
    sound.set_volume(volume)
    return sound


def play_sound(path, volume=1.0):
    """
    Convenience one-liner: load (or reuse) a sound effect and play it
    immediately.

    Args:
        path: File path to the sound file.
        volume: Playback volume from 0.0 to 1.0.
    """
    sound = load_sound(path, volume)
    sound.play()


def play_music(path, volume=0.5, loop=True):
    """
    Start playing a background music track. Only one music track can
    play at a time -- starting a new one stops whatever was playing.

    Args:
        path: File path to the music file (MP3 or OGG work best).
        volume: Playback volume from 0.0 to 1.0.
        loop: If True, the track repeats forever. If False, it plays
            once and stops.
    """
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1 if loop else 0)


def stop_music():
    """Stop whatever background music is currently playing."""
    pygame.mixer.music.stop()
