"""Render Problem 6.8 and its immediate Lindenstrauss-space context."""

from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    with fitz.open(SOURCE) as document:
        page = document[19]  # PDF page 20.
        clip = fitz.Rect(102, 229, 543, 469)
        pixmap = page.get_pixmap(
            matrix=fitz.Matrix(3.5, 3.5), clip=clip, alpha=False
        )
        pixmap.save(OUTPUT)


if __name__ == "__main__":
    main()
