#!/usr/bin/env python3
"""Crop the Problem 4.7 region from the rendered source page."""

from pathlib import Path
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp" / "source_page_13.png"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE)
    # Preserve the full text width and the complete Remark 4.6 / Problem 4.7
    # context while removing unrelated proof material above.
    crop = image.crop((215, 1260, 1320, 1805))
    crop.save(OUTPUT)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()

