#!/usr/bin/env python3
"""Crop the two-page source statement from rendered source pages."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
TMP = PACKET / "tmp"
FIGURES = PACKET / "figures"


def main() -> None:
    FIGURES.mkdir(exist_ok=True)
    page3 = Image.open(TMP / "source_page-03.png").convert("RGB")
    page4 = Image.open(TMP / "source_page-04.png").convert("RGB")

    # Retain the complete text width and comfortable side margins.
    crop3 = page3.crop((150, 1100, 1380, 1915))
    crop4 = page4.crop((150, 170, 1380, 400))
    crop3.save(FIGURES / "open_problem_crop_page3.png")
    crop4.save(FIGURES / "open_problem_crop_page4.png")

    print("wrote", FIGURES / "open_problem_crop_page3.png", crop3.size)
    print("wrote", FIGURES / "open_problem_crop_page4.png", crop4.size)


if __name__ == "__main__":
    main()
