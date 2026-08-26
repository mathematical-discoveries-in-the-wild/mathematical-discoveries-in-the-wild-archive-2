#!/usr/bin/env python3
"""Render Remark 11.4 from the official arXiv PDF."""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    document = fitz.open(SOURCE)
    page = document[19]  # official PDF page 20
    clip = fitz.Rect(43, 447, 569, 502)
    pixmap = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pixmap.save(OUTPUT)
    print(f"wrote {OUTPUT} ({pixmap.width} x {pixmap.height})")


if __name__ == "__main__":
    main()
