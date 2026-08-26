#!/usr/bin/env python3
"""Crop the singularizing-channel open direction from source PDF page 13."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "pdfs" / "source_page_13.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE)
    # Retain full readable line width and the entire concluding discussion of
    # Cesaro convergence and quasi-compactness for singularizing channels.
    crop = image.crop((55, 525, image.width - 55, 1350))
    crop.save(OUTPUT, optimize=True)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()
