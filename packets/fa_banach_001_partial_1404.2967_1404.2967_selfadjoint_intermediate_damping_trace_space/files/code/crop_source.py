from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
source = PACKET / "tmp" / "source_page13.png"
target = PACKET / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Full-width evidence crop: printed page header plus the source's exact
    # open-problem sentence. Coordinates refer to the 180 dpi rendering.
    crop = image.crop((175, 145, 1360, 390))
    crop.save(target)

print(f"wrote {target} ({crop.width}x{crop.height})")
