"""Create the source-evidence crops used in the review packet."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT / "tmp"
FIGURES = ROOT / "figures"


def crop(source: str, box: tuple[int, int, int, int], target: str) -> None:
    image = Image.open(TMP / source)
    image.crop(box).save(FIGURES / target)


crop("source-ratio-23.png", (25, 600, 1250, 1540), "ratio_single_requirements.png")
crop("source-ratio-24.png", (25, 565, 1250, 1630), "ratio_averaged_requirement_81.png")
crop("source-ratio-25.png", (25, 65, 1250, 500), "ratio_averaged_requirement_82.png")
crop("source-page-29.png", (30, 455, 1500, 760), "open_problem_crop.png")

print("created four source-evidence crops")
