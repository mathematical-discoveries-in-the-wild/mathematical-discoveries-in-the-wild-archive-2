#!/usr/bin/env python3
"""Render source PDF page 18 and retain its full-width scaling-question region."""

from pathlib import Path
import subprocess

from PIL import Image


HERE = Path(__file__).resolve().parent
PACKET = HERE.parent
TMP = PACKET / "tmp"
TMP.mkdir(exist_ok=True)
render_base = TMP / "source_page18"

subprocess.run(
    [
        "pdftoppm",
        "-f",
        "18",
        "-l",
        "18",
        "-singlefile",
        "-png",
        "-r",
        "180",
        str(PACKET / "source_paper.pdf"),
        str(render_base),
    ],
    check=True,
)

with Image.open(render_base.with_suffix(".png")) as page:
    crop = page.crop((0, 0, page.width, round(0.70 * page.height)))
    crop.save(PACKET / "figures" / "open_problem_crop.png")

print(PACKET / "figures" / "open_problem_crop.png")
