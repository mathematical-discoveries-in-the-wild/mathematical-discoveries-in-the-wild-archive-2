from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_question_crop.png"
NEEDLES = ("Identification of the best constants", "best constants")


doc = fitz.open(PDF)
for page in doc:
    hits = []
    for needle in NEEDLES:
        hits = page.search_for(needle)
        if hits:
            break
    if not hits:
        continue
    hit = hits[0]
    clip = fitz.Rect(42, max(36, hit.y0 - 135), page.rect.width - 42, min(page.rect.height - 38, hit.y1 + 72))
    pix = page.get_pixmap(matrix=fitz.Matrix(2.4, 2.4), clip=clip, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"saved {OUT} from PDF page {page.number + 1}")
    break
else:
    raise SystemExit(f"could not find any of {NEEDLES!r}")
