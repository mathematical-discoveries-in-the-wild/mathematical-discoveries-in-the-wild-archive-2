"""Make the two review crops from rendered arXiv source pages."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    page22 = Image.open(ROOT / "tmp" / "source_page-22.png")
    page24 = Image.open(ROOT / "tmp" / "source_page-24.png")

    # Corollary 4.11 and its two alternatives, retaining full page width.
    page22.crop((0, 650, page22.width, 1530)).save(
        ROOT / "figures" / "source_corollary_crop.png"
    )
    # Page number, the complete conjecture sentence, and section transition.
    page24.crop((0, 105, page24.width, 430)).save(
        ROOT / "figures" / "open_problem_crop.png"
    )


if __name__ == "__main__":
    main()
