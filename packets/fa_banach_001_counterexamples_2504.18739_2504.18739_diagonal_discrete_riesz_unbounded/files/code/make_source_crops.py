#!/usr/bin/env python3
"""Render and crop the exact source definition, conjecture, and proof flaw."""

from __future__ import annotations

from pathlib import Path

import fitz
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures"


def render_crop(page_number: int, box: tuple[int, int, int, int], name: str) -> None:
    document = fitz.open(PDF)
    page = document[page_number - 1]
    pixmap = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
    rendered = ROOT / "tmp" / f"source_page_{page_number}.png"
    rendered.parent.mkdir(parents=True, exist_ok=True)
    pixmap.save(rendered)
    with Image.open(rendered) as image:
        image.crop(box).save(OUT / name)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    render_crop(4, (205, 980, 1035, 1515), "source_definition.png")
    render_crop(6, (205, 0, 1035, 790), "source_conjecture.png")
    render_crop(21, (205, 105, 1035, 805), "source_proof_flaw.png")


if __name__ == "__main__":
    main()
