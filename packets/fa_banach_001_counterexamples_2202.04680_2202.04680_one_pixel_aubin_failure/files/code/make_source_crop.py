"""Reproduce the open-problem crop from a 200-dpi source-page render."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "source_render" / "page200-17.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"

with Image.open(SOURCE) as page:
    page.crop((100, 980, 1550, 1350)).save(OUTPUT)
