from pathlib import Path

import fitz


root = Path(__file__).resolve().parents[1]
doc = fitz.open(root / "source_paper.pdf")
page = doc[21]
clip = fitz.Rect(58, 108, 554, 145)
pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False)
pix.save(root / "figures" / "open_question_crop.png")
