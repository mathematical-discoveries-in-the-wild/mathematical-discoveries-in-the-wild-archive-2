#!/usr/bin/env python3
"""Render every final packet page to an RGB PNG for visual QA."""

from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
PDF = PACKET / "solution_packet.pdf"
OUTPUT = PACKET / "tmp" / "rendered"


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for old in OUTPUT.glob("page-*.png"):
        old.unlink()
    document = fitz.open(PDF)
    for index, page in enumerate(document):
        pixmap = page.get_pixmap(
            matrix=fitz.Matrix(2, 2), colorspace=fitz.csRGB, alpha=False
        )
        path = OUTPUT / f"page-{index + 1:02d}.png"
        pixmap.save(path)
        if pixmap.n != 3:
            raise RuntimeError(f"expected RGB pixmap for {path}, got n={pixmap.n}")
    print(f"rendered {len(document)} RGB pages to {OUTPUT}")


if __name__ == "__main__":
    main()
