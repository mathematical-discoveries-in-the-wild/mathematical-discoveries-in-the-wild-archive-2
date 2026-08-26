#!/usr/bin/env python3
"""Render and crop official PDF page 17 containing Remark 4.4."""

from pathlib import Path
import subprocess

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
TMP_PAGE = ROOT / "tmp" / "source_page17_200dpi.png"
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
        "-dFirstPage=17",
        "-dLastPage=17",
        f"-sOutputFile={TMP_PAGE}",
        str(SOURCE),
    ],
    check=True,
)

with Image.open(TMP_PAGE) as page:
    # Full text width: Remark 4.4 and the block-conjugation proof of Lemma 4.3.
    crop = page.crop((120, 165, 1585, 660))
    white = Image.new("RGBA", crop.size, "white")
    white.alpha_composite(crop.convert("RGBA"))
    white.convert("RGB").save(OUTPUT)

print(f"wrote {OUTPUT}")
