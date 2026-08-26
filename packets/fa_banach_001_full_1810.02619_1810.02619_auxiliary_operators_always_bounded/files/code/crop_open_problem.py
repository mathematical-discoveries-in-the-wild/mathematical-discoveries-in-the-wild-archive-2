#!/usr/bin/env python3
"""Crop the theorem hypotheses and open boundedness question from source pages."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"


def crop(source: str, box: tuple[int, int, int, int], output: str) -> None:
    image = Image.open(FIGURES / source)
    image.crop(box).save(FIGURES / output)


def main() -> None:
    # Rendered at 180 dpi from source_paper.pdf.  The first crop gives all of
    # Theorem 3.3's assumptions and the definitions of the auxiliary operators.
    crop(
        "source_page-09.png",
        (235, 700, 1305, 1885),
        "theorem_hypotheses_crop.png",
    )
    # The second crop includes the end of the mutual-adjoint proof and the
    # complete paragraph that explicitly leaves boundedness open.
    crop(
        "source_page-10.png",
        (235, 720, 1305, 1345),
        "open_question_crop.png",
    )
    print("wrote theorem_hypotheses_crop.png and open_question_crop.png")


if __name__ == "__main__":
    main()
