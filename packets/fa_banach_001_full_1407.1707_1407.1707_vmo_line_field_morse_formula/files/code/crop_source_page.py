#!/usr/bin/env python3
"""Crop the Section 4 proposal from rendered source-paper page 17."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "source_p17-17.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE)
    # Coordinates at 180 dpi.  Includes the section heading and the complete
    # paragraph containing the proposed extension, with context on both sides.
    crop = image.crop((190, 920, 1325, 1690))
    crop.save(OUTPUT)
    print(f"source_size={image.size}")
    print(f"crop_size={crop.size}")
    print(f"wrote={OUTPUT}")


if __name__ == "__main__":
    main()
