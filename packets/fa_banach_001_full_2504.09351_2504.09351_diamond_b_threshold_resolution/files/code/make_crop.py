#!/usr/bin/env python3
"""Render source PDF page 9 and crop the open-question passage."""

from pathlib import Path
import subprocess

from PIL import Image


HERE = Path(__file__).resolve().parent
PACKET = HERE.parent
POPPLER = Path(
    "/Users/pacuaviva/.cache/codex-runtimes/codex-primary-runtime/"
    "dependencies/native/poppler/poppler/bin/pdftoppm"
)
RENDER_PREFIX = PACKET / "tmp" / "rendered" / "source_page_9_crop_source"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    RENDER_PREFIX.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            str(POPPLER),
            "-f",
            "9",
            "-singlefile",
            "-png",
            "-r",
            "180",
            str(PACKET / "source_paper.pdf"),
            str(RENDER_PREFIX),
        ],
        check=True,
    )
    rendered = RENDER_PREFIX.with_suffix(".png")
    with Image.open(rendered) as image:
        width, height = image.size
        crop = image.crop(
            (
                int(0.16 * width),
                int(0.34 * height),
                int(0.84 * width),
                int(0.62 * height),
            )
        )
        crop.save(OUTPUT)


if __name__ == "__main__":
    main()
