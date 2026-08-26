#!/usr/bin/env python3
"""Render Conjecture 2.3 from printed page 6 of the source paper."""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
OUTPUT = ROOT / "question_crop.png"


def main() -> None:
    doc = fitz.open(SOURCE)
    page = doc[5]  # printed page 6
    pix = page.get_pixmap(
        matrix=fitz.Matrix(3.5, 3.5),
        clip=fitz.Rect(116, 340, 496, 415),
        alpha=False,
    )
    pix.save(OUTPUT)
    print(f"wrote {OUTPUT} ({pix.width}x{pix.height})")


if __name__ == "__main__":
    main()
