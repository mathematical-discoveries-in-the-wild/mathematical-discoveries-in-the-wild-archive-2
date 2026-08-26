"""Crop Corollary 2.8 and Question 2.9 from source page 6."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp" / "source_page-06.png"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE)
    crop = image.crop((235, 1030, 1355, 1800))
    crop.save(OUTPUT)
    print(f"wrote {OUTPUT} at {crop.size[0]}x{crop.size[1]}")


if __name__ == "__main__":
    main()
