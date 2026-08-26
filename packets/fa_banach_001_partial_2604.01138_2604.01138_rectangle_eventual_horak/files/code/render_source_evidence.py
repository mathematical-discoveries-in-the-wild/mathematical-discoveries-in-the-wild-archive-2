#!/usr/bin/env python3
"""Render Bobkov's exact Horak-conjecture remark as a high-resolution crop."""

from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with fitz.open(SOURCE) as document:
        assert document.page_count == 13
        page = document[10]  # PDF page 11, zero-based index 10.
        pixmap = page.get_pixmap(
            matrix=fitz.Matrix(3, 3),
            clip=fitz.Rect(75, 260, 528, 378),
            colorspace=fitz.csRGB,
            alpha=False,
        )
        pixmap.save(OUTPUT)
        print(
            f"rendered source page 11: {OUTPUT} "
            f"({pixmap.width}x{pixmap.height}, RGB)"
        )


if __name__ == "__main__":
    main()
