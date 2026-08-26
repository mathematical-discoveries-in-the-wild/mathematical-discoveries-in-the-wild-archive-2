#!/usr/bin/env python3
"""Render Section 7, item (6), from source PDF page 27."""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    document = fitz.open(SOURCE)
    page = document[26]
    # Keep the full text width and all of item (6), without neighboring items.
    # Coordinates are PDF points.
    clip = fitz.Rect(30, 388, 565, 494)
    pixmap = page.get_pixmap(matrix=fitz.Matrix(3.2, 3.2), clip=clip, alpha=False)
    pixmap.save(OUTPUT)
    print(f"rendered {OUTPUT} ({pixmap.width}x{pixmap.height})")


if __name__ == "__main__":
    main()
