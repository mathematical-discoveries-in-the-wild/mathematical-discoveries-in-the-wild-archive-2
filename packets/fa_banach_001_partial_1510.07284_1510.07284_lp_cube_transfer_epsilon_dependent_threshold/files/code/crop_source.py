"""Crop the open-question passage from rendered PDF page 39."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
source = PACKET / "tmp" / "source_page_39.png"
target = PACKET / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Full text width, including side margins; item 5 and Proposition 6.2.
    crop = image.crop((300, 540, 1430, 880))
    crop.save(target)

print(f"wrote {target} ({crop.width}x{crop.height})")
