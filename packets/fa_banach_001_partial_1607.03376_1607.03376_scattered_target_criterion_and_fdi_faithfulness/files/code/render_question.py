#!/usr/bin/env python3
"""Render Question 2.6 from source PDF page 5."""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
OUTPUT = ROOT / "figures" / "question_2_6_crop.png"


def main() -> None:
    document = fitz.open(SOURCE)
    page = document[4]
    clip = fitz.Rect(105, 393, 510, 468)
    pixmap = page.get_pixmap(matrix=fitz.Matrix(3.2, 3.2), clip=clip, alpha=False)
    pixmap.save(OUTPUT)
    print(f"rendered {OUTPUT} ({pixmap.width}x{pixmap.height})")


if __name__ == "__main__":
    main()
