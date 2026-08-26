"""Crop Theorem 3.5 from rendered source PDF page 10."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "source_render" / "page10-10.png"
OUTPUT = PACKET / "source_theorem_crop.png"

with Image.open(SOURCE) as image:
    crop = image.convert("RGB").crop((120, 1400, 1420, 1585))
    crop.save(OUTPUT, optimize=True)

print(f"wrote {OUTPUT} ({crop.width}x{crop.height}, {crop.mode})")
