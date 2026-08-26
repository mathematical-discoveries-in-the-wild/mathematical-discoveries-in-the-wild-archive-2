from pathlib import Path
import subprocess

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
RENDER_PREFIX = ROOT / "tmp" / "source_page"
SOURCE_16 = ROOT / "tmp" / "source_page-16.png"
SOURCE_17 = ROOT / "tmp" / "source_page-17.png"


def crop(source: Path, box: tuple[int, int, int, int], output: Path) -> None:
    with Image.open(source) as image:
        image.crop(box).save(output)


subprocess.run(
    [
        "pdftoppm",
        "-f",
        "16",
        "-l",
        "17",
        "-png",
        "-r",
        "160",
        str(ROOT / "source_paper.pdf"),
        str(RENDER_PREFIX),
    ],
    check=True,
)

crop(
    SOURCE_16,
    (80, 748, 1280, 930),
    ROOT / "figures" / "open_problem_q51_crop.png",
)
crop(
    SOURCE_17,
    (80, 1220, 1280, 1440),
    ROOT / "figures" / "open_problem_q54_crop.png",
)
