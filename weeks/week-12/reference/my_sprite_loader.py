"""
Week 12 reference: build this together with your instructor.

Goal: write your own version of load_sheet() from
shared/sprite_loader.py. This is the second and final "rebuild the
scaffold" week -- by the end, you'll have written your own version of
both black-box tools this whole course was built on.
"""

import pygame


def slice_sheet(path, frame_width, frame_height):
    """
    Load an image and cut it into equal-sized frames, left to right,
    then top to bottom.
    """
    # TODO (together): load the sheet and turn on transparency.
    sheet = pygame.image.load(path).convert_alpha()

    # TALK: get_size() returns (width, height). How do we figure out
    # how many columns and rows of frames that gives us, if we know
    # each frame's size?
    sheet_width, sheet_height = sheet.get_size()
    columns = sheet_width // frame_width
    rows = sheet_height // frame_height

    frames = []
    # TODO (together): loop over every row, then every column within
    # that row, cutting out one frame each time.
    for row in range(rows):
        for col in range(columns):
            # TALK: this Rect describes WHERE on the SHEET this one
            # frame lives -- not where it'll be drawn on screen later.
            # TODO (together): build that Rect from col, row, and the
            # frame's width/height.
            area = pygame.Rect(col * frame_width, row * frame_height, frame_width, frame_height)

            # TODO (together): make a new, blank Surface the size of
            # one frame, and copy just that area of the sheet onto it.
            frame = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA)
            frame.blit(sheet, (0, 0), area)
            frames.append(frame)

    return frames
