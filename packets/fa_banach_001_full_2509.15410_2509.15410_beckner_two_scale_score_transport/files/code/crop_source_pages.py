"""Reproduce the two source-evidence crops from rendered arXiv pages.

Run from the packet directory after rendering source pages 21--22 at 180 dpi:

    mkdir -p tmp/source_pages
    pdftoppm -f 21 -l 22 -r 180 -png source_paper.pdf tmp/source_pages/source_page
    python code/crop_source_pages.py
"""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
FIGURES = PACKET / "figures"
SOURCE_PAGES = PACKET / "tmp" / "source_pages"


def crop(source: str, target: str, box: tuple[int, int, int, int]) -> None:
    image = Image.open(SOURCE_PAGES / source)
    image.crop(box).save(FIGURES / target, optimize=True)


crop(
    "source_page-21.png",
    "open_problem_crop_1.png",
    (95, 915, 1435, 1905),
)
crop(
    "source_page-22.png",
    "open_problem_crop_2.png",
    (95, 90, 1435, 620),
)
