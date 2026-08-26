"""Crop Problem 2.17 from page 9 of the source PDF."""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
OUTPUT = ROOT / "figures" / "problem_2_17_crop.png"

doc = fitz.open(SOURCE)
page = doc[8]  # one-based PDF page 9
clip = fitz.Rect(48, 697, 548, 758)
pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=clip, alpha=False)
pix.save(OUTPUT)
print(f"wrote {OUTPUT} ({pix.width}x{pix.height})")
