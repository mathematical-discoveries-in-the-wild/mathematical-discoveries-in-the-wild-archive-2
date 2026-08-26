#!/usr/bin/env python3
"""Render source PDF page 26 and crop the full Problem 7.3 passage."""

from pathlib import Path
import shutil
import subprocess
import sys

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
TMP_IMAGE = PACKET / "tmp" / "source_page_26.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    renderer = shutil.which("gs") or "/opt/homebrew/bin/gs"
    if not Path(renderer).exists():
        raise SystemExit("Ghostscript (gs) was not found")
    TMP_IMAGE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            renderer,
            "-q",
            "-dNOPAUSE",
            "-dBATCH",
            "-dFirstPage=26",
            "-dLastPage=26",
            "-sDEVICE=pngalpha",
            "-r180",
            f"-sOutputFile={TMP_IMAGE}",
            str(SOURCE),
        ],
        check=True,
    )
    with Image.open(TMP_IMAGE) as page:
        width, height = page.size
        # Keep the complete readable width and the full theorem/question context.
        crop = page.crop((0, round(0.55 * height), width, round(0.91 * height)))
        # Flatten Ghostscript's alpha channel so PDF renderers cannot interpret
        # transparent white pixels as black blocks.
        crop.convert("RGB").save(OUTPUT)
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
