"""Crop Final Remarks item 5 from the rendered source page."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
source = PACKET / "tmp" / "source_page-25.png"
destination = PACKET / "figures" / "open_problem_crop.png"

with Image.open(source) as page:
    # Preserve the full page width.  The vertical interval contains all of
    # item 5, its label, and a small amount of surrounding whitespace.
    crop = page.crop((0, 1000, page.width, 1305))
    crop.save(destination)

print(destination)
