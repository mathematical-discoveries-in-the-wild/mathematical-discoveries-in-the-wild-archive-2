from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "tmp" / "source_page-07.png"
target = ROOT / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Full text width around item (2) on printed page 7, including its complete
    # statement and the immediately following sentence on known off-diagonal work.
    crop = image.crop((285, 700, 1265, 970))
    crop.save(target)

print(f"wrote {target.relative_to(ROOT)}")
