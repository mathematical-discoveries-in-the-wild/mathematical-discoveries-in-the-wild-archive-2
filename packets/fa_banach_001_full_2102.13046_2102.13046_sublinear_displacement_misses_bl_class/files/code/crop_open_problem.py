#!/usr/bin/env python3
"""Render source page 7 and crop the BL/displacement intersection question."""

from pathlib import Path
import subprocess

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
FULL = ROOT / "tmp" / "source_page_07.png"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    FULL.parent.mkdir(exist_ok=True)
    subprocess.run(
        [
            "/opt/homebrew/bin/gs",
            "-q",
            "-dNOPAUSE",
            "-dBATCH",
            "-dFirstPage=7",
            "-dLastPage=7",
            "-sDEVICE=png16m",
            "-r180",
            f"-sOutputFile={FULL}",
            str(SOURCE),
        ],
        check=True,
    )
    with Image.open(FULL) as image:
        crop = image.crop((230, 620, 1325, 950))
        crop.save(OUT)
    print(f"wrote {OUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()
