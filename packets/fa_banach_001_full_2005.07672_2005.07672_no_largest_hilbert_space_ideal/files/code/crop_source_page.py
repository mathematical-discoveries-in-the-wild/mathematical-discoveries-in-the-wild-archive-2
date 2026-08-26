#!/usr/bin/env python3
"""Crop Ferenczi's Question 6.2 from a rendered full-width source page."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "pdfs" / "source_page_22.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE)
    # Preserve the complete readable page width.  The vertical interval includes
    # the section heading, Question 6.1 context, the definition of H, and all of
    # Question 6.2.
    crop = image.crop((70, 1080, image.width - 70, 1870))
    crop.save(OUTPUT, optimize=True)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()
