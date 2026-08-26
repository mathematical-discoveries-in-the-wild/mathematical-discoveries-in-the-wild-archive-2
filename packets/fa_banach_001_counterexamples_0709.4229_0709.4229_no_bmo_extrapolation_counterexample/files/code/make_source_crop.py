#!/usr/bin/env python3
"""Render a full-width crop of the open question on source PDF page 9."""

from pathlib import Path

import fitz


HERE = Path(__file__).resolve().parent
PACKET = HERE.parent
PDF = PACKET / "source_paper.pdf"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[8]
    hits = page.search_for("Open Question")
    assert hits, "Open Question was not found on source PDF page 9"

    # The source is single-column.  Preserve essentially the entire readable
    # width and include the preceding discussion, the complete question, and
    # the following section heading.
    clip = fitz.Rect(46, 350, 566, 482)
    pix = page.get_pixmap(matrix=fitz.Matrix(3.0, 3.0), clip=clip, alpha=False)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUTPUT)
    print(f"source_page=9 clip={clip}")
    print(OUTPUT)


if __name__ == "__main__":
    main()
