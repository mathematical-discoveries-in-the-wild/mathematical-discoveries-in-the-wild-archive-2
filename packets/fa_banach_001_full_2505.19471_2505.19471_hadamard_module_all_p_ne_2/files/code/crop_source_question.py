#!/usr/bin/env python3
"""Crop the full-width open-question region from rendered source PDF page 18."""

from pathlib import Path

from PIL import Image


HERE = Path(__file__).resolve().parent
PACKET = HERE.parent
RENDERED_PAGE = PACKET / "tmp" / "source_page_18.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(RENDERED_PAGE)
    width, height = image.size
    if (width, height) != (2040, 2640):
        raise SystemExit(f"expected a 240 dpi letter page, got {(width, height)}")
    # Retain both page margins and the complete conclusion/question paragraph.
    crop = image.crop((190, 610, 1850, 1285))
    crop.save(OUTPUT)
    print(f"wrote {OUTPUT} at {crop.size}")


if __name__ == "__main__":
    main()
