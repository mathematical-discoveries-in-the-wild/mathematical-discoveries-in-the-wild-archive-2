#!/usr/bin/env python3
"""Crop the source theorem/question from the rendered official arXiv page."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp" / "source_audit" / "page-14.png"
OUTPUT = ROOT / "source_question_crop.png"


def main() -> None:
    image = Image.open(SOURCE).convert("RGB")
    # Includes the geometric lead-in, Corollary 4.7, and Remark 4.8.
    crop = image.crop((175, 230, 1370, 825))
    crop.save(OUTPUT, optimize=True)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height}, {crop.mode})")


if __name__ == "__main__":
    main()
