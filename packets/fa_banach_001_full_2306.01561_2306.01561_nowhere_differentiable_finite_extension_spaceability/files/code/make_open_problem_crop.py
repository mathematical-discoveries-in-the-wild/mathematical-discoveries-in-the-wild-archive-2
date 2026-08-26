"""Render the complete open-question passage from source PDF page 4."""

from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    with fitz.open(SOURCE) as document:
        page = document[3]  # PDF page 4
        # Full text-block width, from the section heading through the complete
        # paragraph that ends with the (1,c)-spaceability question.
        clip = fitz.Rect(66, 198, 570, 370)
        pixmap = page.get_pixmap(matrix=fitz.Matrix(3.2, 3.2), clip=clip, alpha=False)
        pixmap.save(OUTPUT)


if __name__ == "__main__":
    main()
