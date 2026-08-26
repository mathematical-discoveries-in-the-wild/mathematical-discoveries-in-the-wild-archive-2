#!/usr/bin/env python3
"""Render source PDF page 7 and crop Theorem 1.2 plus Conjecture 1.3."""

from pathlib import Path
import subprocess

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
RENDERED = PACKET / "tmp" / "source_page_07.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    RENDERED.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "/opt/homebrew/bin/gs",
            "-q",
            "-dSAFER",
            "-dBATCH",
            "-dNOPAUSE",
            "-dFirstPage=7",
            "-dLastPage=7",
            "-sDEVICE=png16m",
            "-r200",
            f"-sOutputFile={RENDERED}",
            str(SOURCE),
        ],
        check=True,
    )
    with Image.open(RENDERED) as image:
        # Full readable text width, with enough context to show the proved
        # sector list immediately preceding every line of Conjecture 1.3.
        crop = image.crop((120, 130, 1580, 1460))
        crop.save(OUTPUT)
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
