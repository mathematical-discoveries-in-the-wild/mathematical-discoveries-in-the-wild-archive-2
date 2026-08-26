"""Render the exact definition and Question 1 from arXiv:1003.5588."""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"

doc = fitz.open(SOURCE)
page = doc[15]  # source PDF page 16
clip = fitz.Rect(92, 66, 520, 202)
pix = page.get_pixmap(matrix=fitz.Matrix(3.2, 3.2), clip=clip, alpha=False)
pix.save(OUTPUT)
print(f"wrote {OUTPUT} ({pix.width} x {pix.height})")

