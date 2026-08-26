#!/usr/bin/env python3
"""Crop the formula and open zero-distribution problem from source page 6."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "pdfs" / "source-page-6.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(SOURCE) as image:
        # Full text width and enough vertical context to retain formula (8),
        # the examples p_2,p_3, and the complete open-problem statement.
        crop = image.crop((255, 300, 1275, 930))
        crop.save(OUTPUT)
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
