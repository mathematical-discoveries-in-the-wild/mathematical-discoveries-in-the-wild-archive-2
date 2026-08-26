"""Regenerate the printed-page-6 source crop with Pillow.

First render PDF page 6 at 180 dpi to ``tmp/source_page_6.png``.  The crop
coordinates below are in pixels in that 1530 x 1980 rendering.
"""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "tmp" / "source_page_6.png"
target = ROOT / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    crop = image.crop((270, 315, 1260, 650)).convert("RGB")
    crop.save(target)
