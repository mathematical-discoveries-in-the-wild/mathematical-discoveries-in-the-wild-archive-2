"""Crop Conjecture 5.8 from rendered source page 20."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
image = Image.open(PACKET / "tmp" / "source_page_20.png")
image.crop((135, 555, 1095, 735)).save(
    PACKET / "figures" / "conjecture_crop.png"
)

