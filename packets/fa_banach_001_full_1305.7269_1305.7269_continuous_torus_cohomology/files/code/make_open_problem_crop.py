#!/usr/bin/env python3
"""Render the published Question 10.1 from physical PDF page 91."""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    document = fitz.open(SOURCE)
    page = document[90]  # physical page 91, zero based
    clip = fitz.Rect(103, 185, 523, 418)
    pixmap = page.get_pixmap(matrix=fitz.Matrix(3.2, 3.2), clip=clip, alpha=False)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pixmap.save(OUTPUT)
    print(f"wrote {OUTPUT} ({pixmap.width} x {pixmap.height})")


if __name__ == "__main__":
    main()
