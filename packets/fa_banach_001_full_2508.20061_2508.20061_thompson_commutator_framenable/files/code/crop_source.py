from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp" / "source_page_21.png"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


with Image.open(SOURCE) as image:
    # Remark 4.11 and items (iv)--(vi), including the complete statement of
    # Problem (v), on source PDF page 21.
    crop = image.crop((135, 825, 1395, 1740))
    crop.save(OUTPUT)

print(f"wrote {OUTPUT} ({crop.width} x {crop.height})")
