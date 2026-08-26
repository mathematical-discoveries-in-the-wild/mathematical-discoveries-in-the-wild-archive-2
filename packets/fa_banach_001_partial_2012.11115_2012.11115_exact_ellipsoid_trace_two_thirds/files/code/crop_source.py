from pathlib import Path

import fitz
from PIL import Image


HERE = Path(__file__).resolve().parent
PACKET = HERE.parent
SOURCE = PACKET / "source_paper.pdf"

pages = {
    28: (150, 1198, 1130, 1338),
    29: (85, 105, 1135, 535),
}

document = fitz.open(SOURCE)
for page_number, box in pages.items():
    page = document[page_number - 1]
    pixmap = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
    full_page = PACKET / "tmp" / f"source-page-{page_number}.png"
    pixmap.save(full_page)

    output_name = (
        "source_numerical_crop.png"
        if page_number == 28
        else "source_conjecture_crop.png"
    )
    with Image.open(full_page) as image:
        image.crop(box).save(PACKET / "figures" / output_name, optimize=True)
    print(PACKET / "figures" / output_name)
