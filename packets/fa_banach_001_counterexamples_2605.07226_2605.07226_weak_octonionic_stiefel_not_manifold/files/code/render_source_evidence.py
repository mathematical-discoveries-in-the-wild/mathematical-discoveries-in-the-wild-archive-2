#!/usr/bin/env python3
"""Render the modified James question and the 2x2 classification."""

from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
FIGURES = PACKET / "figures"


def render(page, clip, output):
    pixmap = page.get_pixmap(
        matrix=fitz.Matrix(3, 3),
        clip=fitz.Rect(*clip),
        colorspace=fitz.csRGB,
        alpha=False,
    )
    pixmap.save(output)
    print(f"wrote {output} ({pixmap.width}x{pixmap.height}, RGB)")


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    document = fitz.open(SOURCE)
    render(
        document[22],
        (65, 330, 550, 575),
        FIGURES / "source_question.png",
    )
    render(
        document[21],
        (65, 35, 550, 260),
        FIGURES / "source_classification.png",
    )


if __name__ == "__main__":
    main()
