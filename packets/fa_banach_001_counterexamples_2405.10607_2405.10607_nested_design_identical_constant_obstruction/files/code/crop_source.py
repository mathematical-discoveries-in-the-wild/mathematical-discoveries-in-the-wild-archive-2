#!/usr/bin/env python3
"""Render and crop the source definition and conjecture."""

from pathlib import Path
import shutil
import subprocess

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
FIGURES = PACKET / "figures"


def render(page: int, stem: str) -> Path:
    renderer = shutil.which("pdftoppm")
    if renderer is None:
        raise SystemExit("pdftoppm is required")
    output = FIGURES / stem
    subprocess.run(
        [
            renderer,
            "-f",
            str(page),
            "-l",
            str(page),
            "-singlefile",
            "-png",
            "-r",
            "180",
            str(SOURCE),
            str(output),
        ],
        check=True,
    )
    return output.with_suffix(".png")


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)

    page6 = render(6, "source_page6")
    with Image.open(page6) as image:
        image.crop((270, 620, 1265, 765)).save(
            FIGURES / "order_definition_crop.png"
        )
    page6.unlink()

    page12 = render(12, "source_page12")
    with Image.open(page12) as image:
        image.crop((270, 970, 1265, 1420)).save(FIGURES / "conjecture_crop.png")
    page12.unlink()

    print("wrote source crops")


if __name__ == "__main__":
    main()
