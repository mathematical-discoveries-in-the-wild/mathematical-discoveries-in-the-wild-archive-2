from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT / "tmp"
FIGURES = ROOT / "figures"


def crop(page: int, box: tuple[int, int, int, int], name: str) -> None:
    image = Image.open(TMP / f"source-page-{page}.png")
    image.crop(box).save(FIGURES / name)


crop(16, (145, 655, 905, 1260), "real_square_questions.png")
crop(18, (145, 65, 905, 390), "complex_phase_question.png")
