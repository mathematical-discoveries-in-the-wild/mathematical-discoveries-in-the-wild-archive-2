"""Crop the final open question from arXiv:2406.06859v2, PDF page 20."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    page = Image.open(ROOT / "tmp" / "source-1.png")
    page.crop((0, 895, page.width, 1435)).save(
        ROOT / "figures" / "open_problem_crop.png"
    )


if __name__ == "__main__":
    main()
