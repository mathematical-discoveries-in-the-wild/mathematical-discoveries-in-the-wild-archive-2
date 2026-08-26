"""Crop Definition 2.10 and Remark 2.11 from arXiv:2210.08687 PDF page 12."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PAGE = ROOT / "tmp" / "source_page-12.png"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE_PAGE)
    if image.size != (1530, 1980):
        raise RuntimeError(f"unexpected rendered-page dimensions: {image.size}")
    # Full implication definition plus the complete 1-implied open question.
    crop = image.crop((145, 295, 1390, 990))
    crop.save(OUTPUT, optimize=True)
    print(f"wrote {OUTPUT} with size {crop.size}")


if __name__ == "__main__":
    main()
