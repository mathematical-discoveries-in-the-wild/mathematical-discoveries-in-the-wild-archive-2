#!/usr/bin/env python3
"""Crop the open question from a 180 dpi rendering of source page 21."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp" / "source_page-21.png"
OUTPUT = ROOT / "figures" / "open_question_crop.png"

with Image.open(SOURCE) as image:
    # Includes the authors' displayed estimate and the question immediately below it.
    crop = image.crop((125, 1120, 1370, 1450))
    crop.save(OUTPUT, optimize=True)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")
