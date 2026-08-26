#!/usr/bin/env python3
"""Crop the page-19 open-status passage from a 180-dpi page render."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]

crops = (
    (
        PACKET / "tmp" / "source_page2.png",
        PACKET / "figures" / "frame_set_conjecture_crop.png",
        (110, 765, 1420, 1525),
    ),
    (
        PACKET / "tmp" / "source_page19.png",
        PACKET / "figures" / "open_problem_crop.png",
        (115, 420, 1415, 900),
    ),
)

for source, destination, box in crops:
    with Image.open(source) as image:
        width, height = image.size
        if (width, height) != (1530, 1980):
            raise SystemExit(f"unexpected render size {(width, height)}")
        image.crop(box).save(destination)
    print(destination)
