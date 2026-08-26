from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
doc = fitz.open(ROOT / "source_paper.pdf")
page = doc[9]  # PDF page 10
clip = fitz.Rect(38, 390, 308, 535)
pix = page.get_pixmap(matrix=fitz.Matrix(3.2, 3.2), clip=clip, alpha=False)
pix.save(ROOT / "figures" / "problem_2_q6_crop.png")
