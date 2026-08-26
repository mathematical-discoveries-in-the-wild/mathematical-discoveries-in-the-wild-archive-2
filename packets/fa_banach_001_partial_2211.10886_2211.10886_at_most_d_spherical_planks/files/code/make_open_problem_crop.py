"""Crop the statement of Conjecture 1.15 from page 5 of the source paper."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp" / "source-page5-hi.png"
OUTPUT = ROOT / "figures" / "source_conjecture_1_15.png"


def main() -> None:
    image = Image.open(SOURCE)
    # Coordinates for the 180 dpi A4 rendering.  Include the lead-in paragraph
    # so that the source's attribution to Conjecture 1.17 is visible.
    crop = image.crop((110, 700, 1415, 880))
    crop.save(OUTPUT, optimize=True)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()
