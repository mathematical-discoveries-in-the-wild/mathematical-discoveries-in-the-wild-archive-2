from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
OUTPUT = ROOT / "figures" / "problem_6_6_crop.png"

doc = fitz.open(SOURCE)
page = doc[28]  # source PDF page 29
clip = fitz.Rect(70, 102, 548, 153)
pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False)
pix.save(OUTPUT)
print(f"wrote {OUTPUT} ({pix.width}x{pix.height})")
