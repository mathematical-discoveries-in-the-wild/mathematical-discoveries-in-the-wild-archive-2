from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "tmp" / "source_page_14.png"
target = ROOT / "figures" / "open_question_and_poincare.png"

with Image.open(source) as image:
    # arXiv PDF page 14 rendered at 180 dpi (1530 x 1980).  Keep the end of
    # Lemma 3.2, the exact C^{1,1} question, and Theorem 3.3.
    crop = image.crop((155, 1010, 1380, 1405))
    crop.save(target, optimize=True)

print(target)
