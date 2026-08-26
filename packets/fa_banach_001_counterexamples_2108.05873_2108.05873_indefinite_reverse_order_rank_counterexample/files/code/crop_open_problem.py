"""Crop Section 4 from the 180-dpi rendering of source PDF page 10."""

import argparse
from pathlib import Path

from PIL import Image


parser = argparse.ArgumentParser()
parser.add_argument("input_png", type=Path)
parser.add_argument("output_png", type=Path)
args = parser.parse_args()

with Image.open(args.input_png) as image:
    # Coordinates retain the full readable text width and the complete
    # Section 4 statement, including the displayed rank equality.
    crop = image.crop((150, 1220, 1380, 1510))
    args.output_png.parent.mkdir(parents=True, exist_ok=True)
    crop.save(args.output_png)
