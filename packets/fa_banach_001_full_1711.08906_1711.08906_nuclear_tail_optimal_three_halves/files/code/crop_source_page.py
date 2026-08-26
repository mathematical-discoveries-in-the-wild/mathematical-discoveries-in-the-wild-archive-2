"""Crop the source-paper page containing Theorem 2.1(c) and its question."""

from pathlib import Path

from PIL import Image


HERE = Path(__file__).resolve().parent.parent
source = HERE / "tmp" / "source_page5.png"
target = HERE / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Preserve the full text block and both margins.  Coordinates are for the
    # 180 dpi letter-sized rendering produced by the packet build notes.
    crop = image.crop((230, 300, 1335, 1190))
    crop.save(target)

print(f"wrote {target} ({crop.width}x{crop.height})")
