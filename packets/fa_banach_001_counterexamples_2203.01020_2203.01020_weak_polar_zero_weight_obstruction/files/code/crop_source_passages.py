#!/usr/bin/env python3
"""Crop the target statement and the zero-weight allowance from source pages."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]

jobs = [
    (
        ROOT / "tmp" / "source_page-03.png",
        ROOT / "figures" / "theorem_and_direct_proof_request_crop.png",
        (125, 585, 1370, 1210),
    ),
    (
        ROOT / "tmp" / "source_definition-05.png",
        ROOT / "figures" / "weak_polar_zero_weight_definition_crop.png",
        (125, 180, 1370, 765),
    ),
]

for source, output, box in jobs:
    with Image.open(source) as image:
        crop = image.crop(box)
        crop.save(output, optimize=True)
        print(f"wrote {output} ({crop.width}x{crop.height})")
