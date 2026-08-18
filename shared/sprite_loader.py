"""
sprite_loader.py — loads a sprite sheet image and slices it into frames.

Another "black box" tool, used starting in Week 9 (sprite sheets &
animation). You'll rebuild a simplified version of it yourself in
Week 12.
"""

import pygame


def load_sheet(path, frame_width, frame_height):
    """
    Load an image file and cut it into equal-sized frames, left to
    right, then top to bottom -- like cutting a comic strip into
    individual panels.

    Args:
        path: File path to the sprite sheet image (PNG works best,
            since it supports transparency).
        frame_width: Width of a single frame, in pixels.
        frame_height: Height of a single frame, in pixels.

    Returns:
        A list of pygame.Surface objects, one per frame, in reading
        order (left-to-right, then top-to-bottom).

    Raises:
        FileNotFoundError: If path doesn't point to a real file.
        ValueError: If the sheet's dimensions aren't evenly divisible
            by frame_width / frame_height -- this usually means the
            frame size passed in doesn't match the actual sheet.
    """
    sheet = pygame.image.load(path).convert_alpha()
    sheet_width, sheet_height = sheet.get_size()

    if sheet_width % frame_width != 0 or sheet_height % frame_height != 0:
        raise ValueError(
            f"Sheet size {sheet_width}x{sheet_height} isn't evenly "
            f"divisible by frame size {frame_width}x{frame_height}. "
            "Double-check the frame dimensions you passed in."
        )

    columns = sheet_width // frame_width
    rows = sheet_height // frame_height

    frames = []
    for row in range(rows):
        for col in range(columns):
            rect = pygame.Rect(
                col * frame_width, row * frame_height, frame_width, frame_height
            )
            frame = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA)
            frame.blit(sheet, (0, 0), rect)
            frames.append(frame)

    return frames
