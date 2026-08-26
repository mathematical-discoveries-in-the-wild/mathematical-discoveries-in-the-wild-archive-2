"""Render the exact source question from arXiv:2301.05284v3.

PyMuPDF coordinates are in PDF points from the top-left corner.  The source
question occurs on PDF page 11 (zero-based page index 10).
"""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
OUTPUT = ROOT / "figures" / "source_question_crop.png"

with fitz.open(SOURCE) as document:
    page = document[10]
    # Includes the theorem-context paragraph and the boldfaced main question.
    clip = fitz.Rect(45, 405, 550, 555)
    pixmap = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=clip, alpha=False)
    pixmap.save(OUTPUT)

print(OUTPUT)
