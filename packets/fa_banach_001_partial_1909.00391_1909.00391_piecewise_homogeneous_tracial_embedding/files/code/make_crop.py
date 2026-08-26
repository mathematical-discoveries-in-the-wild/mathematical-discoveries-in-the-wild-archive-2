from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
doc = fitz.open(ROOT / "source_paper.pdf")
page = doc[26]  # printed and PDF page 27
clip = fitz.Rect(70, 510, 535, 642)
pix = page.get_pixmap(matrix=fitz.Matrix(2.4, 2.4), clip=clip, alpha=False)
pix.save(ROOT / "figures" / "open_conjecture_crop.png")
