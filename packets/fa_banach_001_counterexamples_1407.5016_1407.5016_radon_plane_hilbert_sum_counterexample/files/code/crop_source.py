"""Crop the exact Conjecture 2.11 excerpt from source page 6."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
source = PACKET / "tmp" / "source_page-6.png"
target = PACKET / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Coordinates refer to the 150-dpi rendering of source PDF page 6.
    crop = image.crop((245, 1000, 1035, 1148))
    crop.save(target)

print(target)
