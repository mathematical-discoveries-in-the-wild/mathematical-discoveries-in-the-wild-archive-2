#!/usr/bin/env python3
"""Render the exact fixed-weight DSS question from source page 34."""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    document = fitz.open(SOURCE)
    # PDF page 34 is zero-based page 33.  The clip keeps both side margins and
    # all of item 4, with neighboring labels retained as source context.
    page = document[33]
    clip = fitz.Rect(28, 380, 568, 585)
    pixmap = page.get_pixmap(matrix=fitz.Matrix(3.2, 3.2), clip=clip, alpha=False)
    pixmap.save(OUTPUT)
    print(f"rendered {OUTPUT} ({pixmap.width}x{pixmap.height})")


if __name__ == "__main__":
    main()
