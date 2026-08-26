#!/usr/bin/env python3
"""Render the two decisive source passages as high-resolution RGB crops."""

from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
FIGURES = PACKET / "figures"

# PyMuPDF uses zero-based page indices and PDF point coordinates.
CROPS = (
    (
        4,
        fitz.Rect(108, 271, 504, 450),
        "open_problem_crop.png",
    ),
    (
        24,
        fitz.Rect(108, 430, 504, 574),
        "near_counterexample_crop.png",
    ),
)


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    with fitz.open(SOURCE) as document:
        assert document.page_count == 28
        for page_index, clip, filename in CROPS:
            page = document[page_index]
            pixmap = page.get_pixmap(
                matrix=fitz.Matrix(3, 3),
                clip=clip,
                colorspace=fitz.csRGB,
                alpha=False,
            )
            output = FIGURES / filename
            pixmap.save(output)
            print(
                f"rendered source page {page_index + 1}: {output} "
                f"({pixmap.width}x{pixmap.height}, RGB)"
            )


if __name__ == "__main__":
    main()
