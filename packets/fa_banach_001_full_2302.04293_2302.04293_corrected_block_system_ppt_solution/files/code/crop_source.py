"""Crop Problem 7 and Proposition 8 from source PDF page 6."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
source = PACKET / "tmp" / "source_page-06.png"
target = PACKET / "figures" / "problem_and_claimed_solution_crop.png"

with Image.open(source) as image:
    crop = image.crop((260, 775, 1015, 1138))
    crop.save(target)

print(target)
