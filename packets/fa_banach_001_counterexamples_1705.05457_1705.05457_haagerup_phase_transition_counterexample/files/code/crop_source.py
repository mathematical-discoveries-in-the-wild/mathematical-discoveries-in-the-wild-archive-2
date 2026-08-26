"""Crop the exact open-question paragraph from rendered source PDF page 42."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "source_render" / "page42.png"
OUTPUT = PACKET / "source_question_crop.png"

with Image.open(SOURCE) as image:
    crop = image.convert("RGB").crop((180, 830, 1540, 1200))
    crop.save(OUTPUT, optimize=True)

print(f"wrote {OUTPUT} ({crop.width}x{crop.height}, {crop.mode})")
