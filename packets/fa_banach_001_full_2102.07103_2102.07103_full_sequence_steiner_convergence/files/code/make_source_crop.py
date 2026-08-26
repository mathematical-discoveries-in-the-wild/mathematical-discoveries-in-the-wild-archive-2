from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "problem_1_crop.png"
NEEDLE = "Problem 6.1"


doc = fitz.open(PDF)
for page in doc:
    hits = page.search_for(NEEDLE)
    if not hits:
        continue
    hit = hits[0]
    clip = fitz.Rect(42, max(35, hit.y0 - 90), page.rect.width - 42, min(page.rect.height - 35, hit.y1 + 150))
    pix = page.get_pixmap(matrix=fitz.Matrix(2.4, 2.4), clip=clip, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"saved {OUT} from PDF page {page.number + 1}")
    break
else:
    raise SystemExit(f"could not find {NEEDLE!r}")
