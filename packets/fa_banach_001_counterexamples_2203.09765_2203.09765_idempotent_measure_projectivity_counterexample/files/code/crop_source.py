#!/usr/bin/env python3
"""Crop the source proposition and conjecture from rendered PDF page 99."""

from pathlib import Path

from PIL import Image


packet = Path(__file__).resolve().parents[1]
source = packet / "tmp" / "source_page_99.png"
target = packet / "figures" / "source_conjecture_crop.png"

with Image.open(source) as image:
    crop = image.crop((215, 1050, 1370, 1980))
    crop.save(target)

print(target)
