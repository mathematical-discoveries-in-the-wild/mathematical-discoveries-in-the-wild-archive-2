from pathlib import Path

import fitz
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
pdf = fitz.open(ROOT / "source_paper.pdf")
pixmap = pdf[12].get_pixmap(matrix=fitz.Matrix(2.5, 2.5), alpha=False)
full_page = ROOT / "tmp" / "source_page_13.png"
pixmap.save(full_page)

with Image.open(full_page) as image:
    crop = image.crop((250, 650, 1280, 1445))
    crop.save(ROOT / "figures" / "source_question_crop.png")
