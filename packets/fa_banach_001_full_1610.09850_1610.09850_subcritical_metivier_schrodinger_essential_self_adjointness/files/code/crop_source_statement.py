#!/usr/bin/env python3
"""Crop Corollary 4.7 and Remark 4.8 from rendered source PDF page 12."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp" / "source_render" / "page-12.png"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    with Image.open(SOURCE) as image:
        crop = image.crop((150, 900, 1380, 1275))
        crop.save(OUTPUT)
        print(f"source={image.size}; crop={crop.size}; output={OUTPUT}")


if __name__ == "__main__":
    main()
