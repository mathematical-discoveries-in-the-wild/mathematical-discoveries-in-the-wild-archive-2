"""Render the Kruglov-necessity problem from source PDF page 4."""

from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    with fitz.open(SOURCE) as document:
        page = document[3]  # PDF page 4.
        clip = fitz.Rect(76, 382, 537, 462)
        pixmap = page.get_pixmap(matrix=fitz.Matrix(3.5, 3.5), clip=clip, alpha=False)
        pixmap.save(OUTPUT)


if __name__ == "__main__":
    main()
