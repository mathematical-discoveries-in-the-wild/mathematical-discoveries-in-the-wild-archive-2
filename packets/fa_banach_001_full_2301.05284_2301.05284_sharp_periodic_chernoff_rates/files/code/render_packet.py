"""Render every proof-packet page for visual inspection."""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "rendered"
OUTPUT.mkdir(exist_ok=True)

with fitz.open(ROOT / "solution_packet.pdf") as document:
    for index, page in enumerate(document):
        pixmap = page.get_pixmap(matrix=fitz.Matrix(1.7, 1.7), alpha=False)
        pixmap.save(OUTPUT / f"page-{index + 1}.png")

print(f"rendered {index + 1} pages to {OUTPUT}")
