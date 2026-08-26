#!/usr/bin/env python3
"""Crop Remark 4.2 from the rendered twentieth source-paper page."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "source_page20.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    with Image.open(SOURCE) as image:
        # Keep the full text width and the complete Remark 4.2 question.
        crop = image.crop((90, 700, 1440, 965))
        crop.save(OUTPUT)
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
