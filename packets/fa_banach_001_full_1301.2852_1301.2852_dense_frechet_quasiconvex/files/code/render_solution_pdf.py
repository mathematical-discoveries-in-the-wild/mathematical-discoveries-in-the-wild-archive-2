#!/usr/bin/env python3
"""Render every final packet page to an RGB PNG for visual inspection."""

from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "solution_packet.pdf"
OUTPUT_DIR = PACKET / "tmp" / "pdfs"


def main() -> None:
    with fitz.open(SOURCE) as document:
        assert document.page_count > 0
        for page_index, page in enumerate(document):
            pixmap = page.get_pixmap(
                matrix=fitz.Matrix(2, 2),
                colorspace=fitz.csRGB,
                alpha=False,
            )
            output = OUTPUT_DIR / f"render-{page_index + 1}.png"
            pixmap.save(output)
            print(
                f"rendered final page {page_index + 1}: {output} "
                f"({pixmap.width}x{pixmap.height}, RGB)"
            )


if __name__ == "__main__":
    main()
