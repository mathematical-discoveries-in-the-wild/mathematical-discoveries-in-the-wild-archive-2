#!/usr/bin/env python3
"""Create full-width evidence crops from 180-dpi packet source renders."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
RENDER = ROOT / "tmp" / "source_render"
FIGURES = ROOT / "figures"


def crop(source: str, target: str, top: int, bottom: int) -> None:
    image = Image.open(RENDER / source)
    width, height = image.size
    if not (0 <= top < bottom <= height):
        raise ValueError((source, image.size, top, bottom))
    # Retain the complete rendered page width, including both margins.
    image.crop((0, top, width, bottom)).save(FIGURES / target)


FIGURES.mkdir(exist_ok=True)
crop(
    "source-04.png",
    "source_printed_constant_and_corollary_crop.png",
    780,
    2070,
)
crop(
    "source-05.png",
    "source_question_crop.png",
    500,
    1430,
)
crop(
    "suguro-06.png",
    "suguro_candidate_value_crop.png",
    650,
    1880,
)

for path in sorted(FIGURES.glob("*.png")):
    with Image.open(path) as image:
        print(path.name, image.size)
