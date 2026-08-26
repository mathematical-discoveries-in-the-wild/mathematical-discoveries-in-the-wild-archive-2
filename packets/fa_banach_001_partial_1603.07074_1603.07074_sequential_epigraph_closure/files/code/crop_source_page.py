#!/usr/bin/env python3
"""Render source PDF page 10 and crop the full Remark 2.14 evidence block."""

from pathlib import Path
import subprocess

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
TMP = PACKET / "tmp"
FIGURE = PACKET / "figures" / "open_problem_crop.png"
PDFTOPPM = Path(
    "/Users/pacuaviva/.cache/codex-runtimes/"
    "codex-primary-runtime/dependencies/bin/override/pdftoppm"
)


def main() -> None:
    TMP.mkdir(exist_ok=True)
    FIGURE.parent.mkdir(exist_ok=True)
    prefix = TMP / "source_page"
    subprocess.run(
        [
            str(PDFTOPPM),
            "-f",
            "10",
            "-l",
            "10",
            "-png",
            "-r",
            "180",
            str(SOURCE),
            str(prefix),
        ],
        check=True,
    )
    image = Image.open(TMP / "source_page-10.png")
    image.crop((180, 900, 1350, 1680)).save(FIGURE)


if __name__ == "__main__":
    main()
