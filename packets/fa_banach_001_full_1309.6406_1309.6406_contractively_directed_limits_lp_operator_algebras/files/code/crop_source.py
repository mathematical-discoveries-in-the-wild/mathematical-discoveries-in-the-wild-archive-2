"""Render and crop the open-question passage from source PDF page 35."""

from pathlib import Path

import fitz
from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
PDF = PACKET / "source_paper.pdf"
FULL_PAGE = PACKET / "tmp" / "source_page_35.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


document = fitz.open(PDF)
page = document[34]
pixmap = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), alpha=False)
pixmap.save(FULL_PAGE)

image = Image.open(FULL_PAGE)
width, height = image.size
# Keep the full text width and enough context to include the question and the
# following corollary, whose notation identifies the direct limit in question.
crop = image.crop((0, int(0.10 * height), width, int(0.325 * height)))
crop.save(OUTPUT)
print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")
