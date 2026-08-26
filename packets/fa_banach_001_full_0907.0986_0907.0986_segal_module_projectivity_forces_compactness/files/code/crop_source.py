from pathlib import Path
import subprocess

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
TMP_PREFIX = ROOT / "tmp" / "source_page"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"

subprocess.run(
    [
        "pdftoppm",
        "-f",
        "2",
        "-l",
        "2",
        "-r",
        "200",
        "-png",
        str(SOURCE),
        str(TMP_PREFIX),
    ],
    check=True,
)

page = Image.open(ROOT / "tmp" / "source_page-02.png")
# Introduction paragraph containing the complete open question and its context.
crop = page.crop((300, 195, 1390, 735))
crop.save(OUTPUT)
print(OUTPUT)
