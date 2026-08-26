from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "tmp" / "source_page_4.png"
target = ROOT / "figures" / "problem_2_6_crop.png"

with Image.open(source) as image:
    # Page 4: symmetric-group comparison, Problem 2.6, and its concrete form.
    crop = image.crop((145, 895, 1395, 1535))
    crop.save(target, optimize=True)

print(target)
