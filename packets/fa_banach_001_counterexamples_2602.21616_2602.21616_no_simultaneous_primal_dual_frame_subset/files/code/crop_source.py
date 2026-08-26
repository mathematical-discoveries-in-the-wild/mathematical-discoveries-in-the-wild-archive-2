"""Render and crop the exact open question from arXiv:2602.21616 PDF page 12."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PAGE = ROOT / "tmp" / "source_page-02.png"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE_PAGE)
    if image.size != (1530, 1980):
        raise RuntimeError(f"unexpected rendered-page dimensions: {image.size}")
    # Remark 3.4, including the complete simultaneous-frame question in part (b).
    crop = image.crop((130, 410, 1400, 985))
    crop.save(OUTPUT, optimize=True)
    print(f"wrote {OUTPUT} with size {crop.size}")


if __name__ == "__main__":
    main()
