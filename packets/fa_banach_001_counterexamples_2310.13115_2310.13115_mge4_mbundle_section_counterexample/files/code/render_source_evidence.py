#!/usr/bin/env python3
"""Render the exact source conjecture from PDF page 15."""

from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
OUTPUT = PACKET / "figures" / "source_conjecture.png"


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    document = fitz.open(SOURCE)
    page = document[14]
    # PDF coordinates: retain Theorem 3.5 and the following conjecture.
    clip = fitz.Rect(72, 335, 540, 510)
    pixmap = page.get_pixmap(
        matrix=fitz.Matrix(3, 3), clip=clip, colorspace=fitz.csRGB, alpha=False
    )
    pixmap.save(OUTPUT)
    print(f"wrote {OUTPUT} ({pixmap.width}x{pixmap.height}, RGB)")


if __name__ == "__main__":
    main()
