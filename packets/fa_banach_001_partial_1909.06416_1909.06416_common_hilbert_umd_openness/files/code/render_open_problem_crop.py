#!/usr/bin/env python3
"""Render the full-width Conjecture 8.9/Remark 8.10 passage from PDF page 67."""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    document = fitz.open(SOURCE)
    page = document[66]
    # The endpoint question, Conjecture 8.9, and its immediate consequence.
    # Keep the full page width so neither text nor equation margins are lost.
    rectangle = fitz.Rect(0, 190, page.rect.width, 495)
    pixmap = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=rectangle, alpha=False)
    pixmap.save(OUTPUT)
    print(f"wrote {OUTPUT} ({pixmap.width}x{pixmap.height})")


if __name__ == "__main__":
    main()
