#!/usr/bin/env python3
"""Render and crop Question 6.2 from physical page 25 of arXiv:2012.14413."""

from pathlib import Path
import shutil
import subprocess

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
TMP = PACKET / "tmp"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    TMP.mkdir(parents=True, exist_ok=True)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    renderer = shutil.which("pdftoppm")
    if renderer is None:
        raise SystemExit("pdftoppm is required")
    prefix = TMP / "source_page25"
    subprocess.run(
        [
            renderer,
            "-f",
            "25",
            "-l",
            "25",
            "-singlefile",
            "-r",
            "220",
            "-png",
            str(SOURCE),
            str(prefix),
        ],
        check=True,
    )
    rendered = prefix.with_suffix(".png")
    with Image.open(rendered) as image:
        # Keep the full page width and both margins.  The vertical window
        # includes the motivation, all of Question 6.2, and its equivalent
        # center-index-four formulation.
        top = int(image.height * 0.50)
        bottom = int(image.height * 0.78)
        crop = image.crop((0, top, image.width, bottom))
        crop.save(OUTPUT, dpi=(220, 220))
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()
