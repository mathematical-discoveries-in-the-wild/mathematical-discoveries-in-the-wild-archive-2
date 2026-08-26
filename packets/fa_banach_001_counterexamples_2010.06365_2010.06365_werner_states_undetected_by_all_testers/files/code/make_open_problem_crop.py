"""Crop the exact completeness question from source paper page 35."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp" / "source_page-35.png"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    page = Image.open(SOURCE).convert("RGB")
    # Retain the full text width and the complete question, including the
    # authors' factorization-through-ell_2 reformulation.
    crop = page.crop((145, 655, 1385, 1205))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    crop.save(OUTPUT, optimize=True)


if __name__ == "__main__":
    main()
