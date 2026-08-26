"""Regenerate the printed-page-3 open-problem crop with Pillow."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "tmp" / "source_page_3.png"
target = ROOT / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    image.crop((175, 690, 1350, 1425)).convert("RGB").save(target)
