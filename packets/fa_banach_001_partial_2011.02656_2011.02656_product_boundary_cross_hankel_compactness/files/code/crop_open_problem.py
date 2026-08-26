#!/usr/bin/env python3
"""Crop Theorem 1 and Remark 2 from rendered source page 2."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "source-page-02.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(SOURCE) as image:
        # Full text width; theorem through the end of Remark 2.
        crop = image.crop((92, 160, 1440, 1025))
        crop.save(OUTPUT)
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
