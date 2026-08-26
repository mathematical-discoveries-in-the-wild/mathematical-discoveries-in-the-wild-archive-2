"""Crop the exact local-translations question from source_paper.pdf."""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
doc = fitz.open(ROOT / "source_paper.pdf")
page = doc[2]  # PDF page 3
clip = fitz.Rect(58, 425, 555, 535)
pix = page.get_pixmap(matrix=fitz.Matrix(2.4, 2.4), clip=clip, alpha=False)
pix.save(ROOT / "figures" / "local_translation_question_crop.png")

