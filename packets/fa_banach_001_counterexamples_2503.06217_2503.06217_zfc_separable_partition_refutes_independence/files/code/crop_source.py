"""Crop the printed Conjecture 4.6 and consequence from source page 19."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp" / "source_page-19.png"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE)
    # Retain the page header, exact conjecture, and stated independence consequence.
    crop = image.crop((115, 105, 1435, 455))
    crop.save(OUTPUT)
    print(f"wrote {OUTPUT} at {crop.size[0]}x{crop.size[1]}")


if __name__ == "__main__":
    main()
