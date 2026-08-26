"""Reproduce the two evidence crops from 200-dpi source-page renders."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
RENDER = PACKET / "tmp" / "source_render"
FIGURES = PACKET / "figures"


def crop(source: str, box: tuple[int, int, int, int], output: str) -> None:
    with Image.open(RENDER / source) as page:
        page.crop(box).save(FIGURES / output)


crop("page200-1.png", (50, 300, 1650, 1080), "equation_context_crop.png")
crop("page200-4.png", (50, 595, 1650, 715), "open_problem_crop.png")
