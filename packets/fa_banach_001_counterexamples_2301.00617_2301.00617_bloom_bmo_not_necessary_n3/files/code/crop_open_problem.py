#!/usr/bin/env python3
"""Render source page 19 and crop Remark 7.11 reproducibly."""

from pathlib import Path
import subprocess

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
FULL = ROOT / "tmp" / "source_page_19.png"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    FULL.parent.mkdir(exist_ok=True)
    subprocess.run(
        [
            "/opt/homebrew/bin/gs",
            "-q",
            "-dNOPAUSE",
            "-dBATCH",
            "-dFirstPage=19",
            "-dLastPage=19",
            "-sDEVICE=pngalpha",
            "-r180",
            f"-sOutputFile={FULL}",
            str(SOURCE),
        ],
        check=True,
    )
    with Image.open(FULL) as image:
        crop = image.crop((225, 1245, 1320, 1850))
        crop.save(OUT)
    print(f"wrote {OUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()
