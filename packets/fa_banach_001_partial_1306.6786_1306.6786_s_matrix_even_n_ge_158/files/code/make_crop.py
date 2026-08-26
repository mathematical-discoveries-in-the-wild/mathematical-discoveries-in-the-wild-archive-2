#!/usr/bin/env python3
"""Crop the exact conjecture statement from rendered PDF page 2.

Run after rendering at 200 dpi as tmp/source_page-2.png.
"""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "tmp" / "source_page-2.png"
target = ROOT / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Coordinates for the 200-dpi 1700x2200 page render.  This includes the
    # page number and the complete three-line conjecture, with generous margin.
    crop = image.crop((165, 105, 1165, 410))
    crop.save(target)

print(target)
