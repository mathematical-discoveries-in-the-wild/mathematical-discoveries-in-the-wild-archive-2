"""Crop the decisive passages from the rendered HAL supporting paper.

Run from the packet directory after rendering PDF pages 3 and 13 at 150 dpi.
"""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]


def crop(source: str, box: tuple[int, int, int, int], destination: str) -> None:
    image = Image.open(ROOT / "tmp" / source)
    # Flatten the Ghostscript alpha channel: leaving it in place can render as
    # a black rectangle when pdfTeX embeds the PNG.
    image.crop(box).convert("RGB").save(ROOT / "figures" / destination)


crop(
    "support_definition_page.png",
    (220, 210, 1080, 1515),
    "weak_disjointness_definition_crop.png",
)
crop(
    "support_chacon_page.png",
    (220, 0, 1100, 825),
    "chacon_universal_crop.png",
)
