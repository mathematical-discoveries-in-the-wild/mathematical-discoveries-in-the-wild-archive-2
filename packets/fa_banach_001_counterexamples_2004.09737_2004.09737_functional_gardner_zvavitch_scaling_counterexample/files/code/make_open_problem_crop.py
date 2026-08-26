#!/usr/bin/env python3
"""Render page 29 of the source PDF and crop Conjecture 6.2."""

from pathlib import Path

import pypdfium2 as pdfium


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    document = pdfium.PdfDocument(str(SOURCE))
    page = document[28]  # PDF page 29, zero based.
    image = page.render(scale=2.5).to_pil()  # 180 dpi for a 72 dpi PDF.
    crop = image.crop((110, 285, 1430, 835))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    crop.save(OUTPUT)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()
