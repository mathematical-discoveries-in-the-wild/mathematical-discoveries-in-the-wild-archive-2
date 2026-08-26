"""Render Conjecture 1 from page 16 of arXiv:2407.13457."""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
with fitz.open(ROOT / "source_paper.pdf") as document:
    page = document[15]
    # Full text width; includes the cone-measure representation, Conjecture 1,
    # its displayed inequality, and the authors' precise prior-work note.
    clip = fitz.Rect(60, 270, 552, 470)
    pixmap = page.get_pixmap(matrix=fitz.Matrix(2.7, 2.7), clip=clip, alpha=False)
    pixmap.save(ROOT / "figures" / "open_problem_crop.png")

print(ROOT / "figures" / "open_problem_crop.png")
