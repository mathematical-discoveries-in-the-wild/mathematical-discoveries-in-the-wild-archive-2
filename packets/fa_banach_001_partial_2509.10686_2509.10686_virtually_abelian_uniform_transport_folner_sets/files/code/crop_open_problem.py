#!/usr/bin/env python3
"""Crop the motivation and Problem 10.8 from rendered source page 32."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "source-page-32.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(SOURCE) as image:
        crop = image.crop((245, 885, 1210, 1505))
        crop.save(OUTPUT)
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
