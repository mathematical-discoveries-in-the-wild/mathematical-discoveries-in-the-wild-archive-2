"""Render the complete open question from source PDF page 27."""

from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    with fitz.open(SOURCE) as document:
        page = document[26]  # PDF page 27, printed page 26.
        # Stop above the following References heading while retaining the
        # complete final sentence of the question.
        clip = fitz.Rect(66, 62, 548, 170)
        pixmap = page.get_pixmap(matrix=fitz.Matrix(3.4, 3.4), clip=clip, alpha=False)
        pixmap.save(OUTPUT)


if __name__ == "__main__":
    main()
