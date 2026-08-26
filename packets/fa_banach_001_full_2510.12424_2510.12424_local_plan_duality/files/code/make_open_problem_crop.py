#!/usr/bin/env python3
"""Render and crop Remark 5.13 from the official arXiv PDF."""

from pathlib import Path
import subprocess

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
TMP_PAGE = ROOT / "tmp" / "source_page59_200dpi.png"
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
        "-dFirstPage=59",
        "-dLastPage=59",
        f"-sOutputFile={TMP_PAGE}",
        str(SOURCE),
    ],
    check=True,
)

with Image.open(TMP_PAGE) as page:
    # Remark 5.13, including the comparison with B_q^* and the future-work line.
    crop = page.crop((155, 1320, 1545, 1815))
    white = Image.new("RGBA", crop.size, "white")
    white.alpha_composite(crop.convert("RGBA"))
    white.convert("RGB").save(OUTPUT)

print(f"wrote {OUTPUT}")
