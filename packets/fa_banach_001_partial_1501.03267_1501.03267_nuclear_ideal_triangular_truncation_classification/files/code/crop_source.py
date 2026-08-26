"""Crop Problem 7.4 from source PDF page 25 of arXiv:1501.03267."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PAGE = ROOT / "tmp" / "source-page-02.png"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE_PAGE)
    if image.size != (1530, 1980):
        raise RuntimeError(f"unexpected rendered-page dimensions: {image.size}")
    crop = image.crop((180, 835, 1390, 1115))
    crop.save(OUTPUT, optimize=True)
    print(f"wrote {OUTPUT} with size {crop.size}")


if __name__ == "__main__":
    main()
