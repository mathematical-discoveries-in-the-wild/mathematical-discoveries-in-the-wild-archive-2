#!/usr/bin/env python3
"""Render and crop PDF page 9 containing the source question."""

from pathlib import Path
import subprocess
import sys

from PIL import Image


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: crop_source.py SOURCE_PDF OUTPUT_PNG")
    source = Path(sys.argv[1]).resolve()
    output = Path(sys.argv[2]).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    stem = output.parent / "source_page"
    subprocess.run(
        [
            "pdftoppm",
            "-f",
            "9",
            "-l",
            "9",
            "-r",
            "180",
            "-png",
            "-singlefile",
            str(source),
            str(stem),
        ],
        check=True,
    )
    page_path = stem.with_suffix(".png")
    with Image.open(page_path) as image:
        crop = image.crop((0, 900, image.width, 1450))
        crop.save(output)
    page_path.unlink()


if __name__ == "__main__":
    main()
