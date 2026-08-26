#!/usr/bin/env python3
"""Render the official arXiv PDF page containing Questions 4.4 and 4.5."""

from pathlib import Path
import subprocess

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
TMP_PAGE = ROOT / "tmp" / "source_page15_200dpi.png"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"

TMP_PAGE.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

subprocess.run(
    [
        "/opt/homebrew/bin/gs",
        "-q",
        "-dNOPAUSE",
        "-dBATCH",
        "-sDEVICE=pngalpha",
        "-r200",
        "-dFirstPage=15",
        "-dLastPage=15",
        f"-sOutputFile={TMP_PAGE}",
        str(SOURCE),
    ],
    check=True,
)

with Image.open(TMP_PAGE) as page:
    # Full text width, from the end of Proposition 4.2 through both questions.
    crop = page.crop((145, 1090, 1510, 2190))
    white = Image.new("RGBA", crop.size, "white")
    white.alpha_composite(crop.convert("RGBA"))
    white.convert("RGB").save(OUTPUT)

print(f"wrote {OUTPUT}")
