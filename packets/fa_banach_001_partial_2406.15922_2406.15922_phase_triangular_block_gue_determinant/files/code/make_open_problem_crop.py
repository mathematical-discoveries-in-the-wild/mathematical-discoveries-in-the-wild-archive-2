#!/usr/bin/env python3
"""Render the Conjecture 1 passage from source PDF page 17."""

from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    with fitz.open(SOURCE) as doc:
        page = doc[16]
        rect = page.rect
        clip = fitz.Rect(
            0.105 * rect.width,
            0.075 * rect.height,
            0.91 * rect.width,
            0.455 * rect.height,
        )
        pix = page.get_pixmap(matrix=fitz.Matrix(2.4, 2.4), clip=clip, alpha=False)
        pix.save(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    main()
