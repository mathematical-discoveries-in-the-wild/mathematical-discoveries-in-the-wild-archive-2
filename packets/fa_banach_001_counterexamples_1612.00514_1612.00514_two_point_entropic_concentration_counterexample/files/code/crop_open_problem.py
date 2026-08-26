#!/usr/bin/env python3
"""Crop the full-width Conjectures 6.9--6.10 region from rendered page 23."""

from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
PACKET = HERE.parent
source = PACKET / "tmp" / "source-page-23.png"
target = PACKET / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Preserve both page margins and the full conjecture statements.
    crop = image.crop((105, 870, image.width - 105, 1780))
    crop.save(target)

print(f"wrote {target} ({crop.width}x{crop.height})")
