"""Crop Theorem 7 and the Kronecker endpoint question from source page 8."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp" / "source_page-08.png"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    page = Image.open(SOURCE).convert("RGB")
    crop = page.crop((245, 835, 1265, 1310))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    crop.save(OUTPUT, optimize=True)


if __name__ == "__main__":
    main()
