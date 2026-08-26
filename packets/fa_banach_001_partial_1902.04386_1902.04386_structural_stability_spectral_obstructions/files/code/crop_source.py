from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT / "tmp"
FIGURES = ROOT / "figures"


def crop(source: str, box: tuple[int, int, int, int], output: str) -> None:
    image = Image.open(TMP / source).convert("RGB")
    image.crop(box).save(FIGURES / output, quality=95)


crop("source_page-12.png", (105, 1075, 1150, 1165), "question_13_crop.png")
crop("source_page-13.png", (105, 915, 1150, 1125), "questions_15_16_crop.png")
