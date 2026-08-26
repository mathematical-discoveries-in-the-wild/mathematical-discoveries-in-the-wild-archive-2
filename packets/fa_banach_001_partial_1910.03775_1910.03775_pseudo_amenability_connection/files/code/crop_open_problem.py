#!/usr/bin/env python3
"""Render arXiv PDF page 24 and crop the open question."""

from pathlib import Path
import shutil
import subprocess

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
FIGURES = PACKET / "figures"
RENDER_STEM = FIGURES / "source_page24"
OUTPUT = FIGURES / "open_problem_crop.png"


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    renderer = shutil.which("pdftoppm")
    if renderer is None:
        raise SystemExit("pdftoppm is required")
    subprocess.run(
        [
            renderer,
            "-f",
            "24",
            "-l",
            "24",
            "-singlefile",
            "-png",
            "-r",
            "180",
            str(SOURCE),
            str(RENDER_STEM),
        ],
        check=True,
    )
    rendered = RENDER_STEM.with_suffix(".png")
    with Image.open(rendered) as image:
        # Section heading plus Questions 1--3, including the exact target.
        crop = image.crop((270, 530, 1265, 865))
        crop.save(OUTPUT)
    rendered.unlink()
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
