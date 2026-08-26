"""Crop Problem 3.11 from the rendered arXiv source page.

Run from the packet directory after rendering PDF page 13 at 180 dpi as
``tmp/source_page-13.png``.
"""

from pathlib import Path

from PIL import Image


SOURCE = Path("tmp/source_page-13.png")
OUTPUT = Path("figures/open_problem_crop.png")


def main() -> None:
    image = Image.open(SOURCE).convert("RGB")
    # Retain the complete page width and enough surrounding text to show that
    # Problem 3.11 is one of the paper's proposed general composition problems.
    crop = image.crop((0, 800, image.width, 1395))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    crop.save(OUTPUT)
    print(f"saved {OUTPUT} at {crop.width}x{crop.height}")


if __name__ == "__main__":
    main()
