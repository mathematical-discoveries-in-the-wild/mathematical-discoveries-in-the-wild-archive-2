from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "tmp" / "pdfs" / "source_page12.png"
target = ROOT / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Full text width, including margins, and enough vertical context to show
    # the end of the curve theorem and the complete open-question paragraph.
    crop = image.crop((210, 1040, 1325, 1545))
    crop.save(target)

print(f"wrote {target} ({crop.width}x{crop.height})")
