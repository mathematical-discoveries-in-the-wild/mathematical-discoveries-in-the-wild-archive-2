from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
RENDERED = ROOT / "tmp" / "pdfs"
FIGURES = ROOT / "figures"


def crop(source: str, box: tuple[int, int, int, int], output: str) -> None:
    with Image.open(RENDERED / source) as image:
        image.crop(box).save(FIGURES / output)


crop("source_page-03.png", (80, 850, 1408, 1240), "open_problem_crop.png")
crop("source_page-04.png", (80, 960, 1408, 1720), "residual_case_crop.png")
print("wrote source crops")
