from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
source = PACKET / "tmp" / "source_page-10.png"
target = PACKET / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    crop = image.crop((135, 790, 1090, 1430))
    crop.save(target)

print(target)

