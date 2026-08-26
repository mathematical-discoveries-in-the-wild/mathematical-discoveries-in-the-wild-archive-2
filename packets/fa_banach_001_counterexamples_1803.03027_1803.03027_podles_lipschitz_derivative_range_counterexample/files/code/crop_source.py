#!/usr/bin/env python3
"""Crop the complete Section 3 range question from rendered PDF page 7."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp" / "source_page_7.png"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE)
    # Full readable text width; includes the definition of the two extensions
    # and the complete two-line question immediately below it.
    crop = image.crop((115, 635, 1375, 1210))
    crop.save(OUTPUT)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()
