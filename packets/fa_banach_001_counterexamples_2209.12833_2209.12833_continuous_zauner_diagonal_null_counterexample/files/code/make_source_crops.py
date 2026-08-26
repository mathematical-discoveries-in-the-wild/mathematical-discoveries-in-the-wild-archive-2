from pathlib import Path

import fitz
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
doc = fitz.open(ROOT / "source_paper.pdf")


def render(page_number: int, rect: fitz.Rect) -> Image.Image:
    pix = doc[page_number].get_pixmap(matrix=fitz.Matrix(2.2, 2.2), clip=rect, alpha=False)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def stack(parts: list[Image.Image], destination: str) -> None:
    width = max(part.width for part in parts)
    height = sum(part.height for part in parts)
    joined = Image.new("RGB", (width, height), "white")
    y = 0
    for part in parts:
        joined.paste(part, (0, y))
        y += part.height
    joined.save(ROOT / destination)

# Printed pages 7--8: Conjectures 2.8 and 2.9, joined across the page break.
stack(
    [render(6, fitz.Rect(35, 480, 575, 780)), render(7, fitz.Rect(35, 25, 575, 750))],
    "source_nonarch_crop.png",
)

# Printed pages 14--15: Conjectures 3.7 and 3.8, joined across the page break.
stack(
    [render(13, fitz.Rect(35, 420, 575, 780)), render(14, fitz.Rect(35, 25, 575, 500))],
    "source_padic_crop.png",
)

print("wrote source_nonarch_crop.png and source_padic_crop.png")
