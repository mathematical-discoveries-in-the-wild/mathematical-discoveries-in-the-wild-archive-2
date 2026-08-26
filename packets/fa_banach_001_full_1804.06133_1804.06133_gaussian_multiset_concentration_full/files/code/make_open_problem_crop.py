"""Crop the Gaussian multi-set concentration conjecture from source page 15."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp" / "source_page-15.png"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    page = Image.open(SOURCE).convert("RGB")
    # Rendered at 180 dpi.  Keep the section heading, full conjecture, and the
    # following functional-inequality sentence, with comfortable side margins.
    crop = page.crop((50, 900, 1460, 1530))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    crop.save(OUTPUT, optimize=True)


if __name__ == "__main__":
    main()
