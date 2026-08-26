from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "tmp" / "source_page_4.png"
target = ROOT / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Page 4: the complete ordinary-multiplier remark and its open question.
    crop = image.crop((185, 970, 1345, 1245))
    crop.save(target, optimize=True)

print(target)
