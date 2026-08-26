from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "tmp" / "source_page-22.png"
target = ROOT / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Complete text of Question (B) and its note, PDF page 22.
    crop = image.crop((170, 628, 1360, 855))
    crop.save(target)
