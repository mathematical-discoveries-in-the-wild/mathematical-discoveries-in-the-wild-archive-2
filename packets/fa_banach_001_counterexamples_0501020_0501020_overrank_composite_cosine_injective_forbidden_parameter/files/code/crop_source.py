#!/usr/bin/env python3
"""Render and crop PDF page 19 containing the source open question."""

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
            "19",
            "-l",
            "19",
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
        # Keep the full page width and enough context to display the equivalent
        # forbidden values, the question, and the following scalar theorem.
        crop = image.crop((0, 35, image.width, min(image.height, 1510)))
        crop.save(output)
    page_path.unlink()


if __name__ == "__main__":
    main()
