#!/usr/bin/env python3
"""Crop the exact greedy question from official arXiv PDF page 27."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp" / "source_audit" / "page-27.png"
OUTPUT = ROOT / "source_question_crop.png"


def main() -> None:
    image = Image.open(SOURCE).convert("RGB")
    crop = image.crop((205, 235, 1325, 835))
    crop.save(OUTPUT, optimize=True)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height}, {crop.mode})")


if __name__ == "__main__":
    main()
