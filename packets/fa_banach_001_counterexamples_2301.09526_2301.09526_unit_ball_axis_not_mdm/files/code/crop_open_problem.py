#!/usr/bin/env python3
"""Crop Definition 7 and the ensuing unit-ball conjecture from source page 3."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "figures" / "source_page-03.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE)
    # Preserve the full typeset text width and include Definition 7, the
    # polynomial-hull obstruction, the conjecture, and the unit-ball question.
    crop = image.crop((115, 150, 1210, 1000))
    crop.save(OUTPUT, optimize=True)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()
