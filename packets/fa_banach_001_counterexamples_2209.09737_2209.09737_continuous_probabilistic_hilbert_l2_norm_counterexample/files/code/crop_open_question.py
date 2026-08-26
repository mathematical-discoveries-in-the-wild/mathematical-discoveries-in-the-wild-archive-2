from pathlib import Path

import fitz


root = Path(__file__).resolve().parents[1]
doc = fitz.open(root / "source_paper.pdf")
page = doc[52]
clip = fitz.Rect(87, 654, 527, 706)
pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False)
pix.save(root / "figures" / "open_question_crop.png")
