#!/usr/bin/env python3
"""Crop Conjecture 1.1 from rendered page 3 of the source PDF."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "tmp" / "source-page3.png"
target = ROOT / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # At 180 dpi the US-Letter page is 1530 by 1980 pixels.  This rectangle
    # contains the complete conjecture heading and displayed inequality.
    crop = image.crop((270, 265, 1260, 410))
    crop.save(target)

print(target)
