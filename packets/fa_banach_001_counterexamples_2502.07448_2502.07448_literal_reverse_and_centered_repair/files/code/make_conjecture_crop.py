from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "tmp" / "source_page-03.png"
target = ROOT / "figures" / "open_conjecture.png"

with Image.open(source) as image:
    # Full text width and the complete conjecture on source PDF page 3.
    image.crop((115, 590, 1420, 955)).save(target, optimize=True)

print(target)
