#!/usr/bin/env python3
"""Render the two-page source excerpt containing Conjecture 2 and its status."""

from pathlib import Path

import fitz
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
OUTPUT = ROOT / "question_crop.png"


def render_clip(page: fitz.Page, rect: fitz.Rect, scale: float = 3.2) -> Image.Image:
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), clip=rect, alpha=False)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def main() -> None:
    doc = fitz.open(SOURCE)
    # Printed pages 22--23.  The conjecture is at the foot of p. 22 and the
    # paragraph identifying the proved and missing halves continues on p. 23.
    clips = [
        ("Source p. 22", render_clip(doc[21], fitz.Rect(125, 500, 482, 646))),
        ("Source p. 23", render_clip(doc[22], fitz.Rect(125, 88, 482, 177))),
    ]

    margin, label_h, gap = 28, 36, 24
    width = max(im.width for _, im in clips) + 2 * margin
    height = sum(im.height + label_h for _, im in clips) + gap + 2 * margin
    canvas = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default(size=22)
    y = margin
    for index, (label, im) in enumerate(clips):
        draw.text((margin, y), label, fill=(70, 70, 70), font=font)
        y += label_h
        canvas.paste(im, (margin, y))
        draw.rectangle((margin - 1, y - 1, margin + im.width, y + im.height), outline=(180, 180, 180), width=2)
        y += im.height
        if index + 1 < len(clips):
            y += gap

    canvas.save(OUTPUT, quality=95)
    print(f"wrote {OUTPUT} ({canvas.width}x{canvas.height})")


if __name__ == "__main__":
    main()

