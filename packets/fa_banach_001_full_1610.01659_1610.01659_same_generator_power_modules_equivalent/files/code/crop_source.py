"""Crop Question 2.10 and its immediate context from source page 7."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp" / "source_page-07.png"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE)
    crop = image.crop((230, 165, 1375, 610))
    crop.save(OUTPUT)
    print(f"wrote {OUTPUT} at {crop.size[0]}x{crop.size[1]}")


if __name__ == "__main__":
    main()
