"""Render and crop Remark 3.6 from source PDF page 14 with Poppler."""

from pathlib import Path
import shutil
import subprocess

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
PDF = PACKET / "source_paper.pdf"
TMP = PACKET / "tmp"
PREFIX = TMP / "source_page"
RENDERED = TMP / "source_page-14.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def find_pdftoppm() -> str:
    executable = shutil.which("pdftoppm")
    if executable:
        return executable
    bundled = Path(
        "/Users/pacuaviva/.cache/codex-runtimes/codex-primary-runtime/"
        "dependencies/bin/override/pdftoppm"
    )
    if bundled.exists():
        return str(bundled)
    raise FileNotFoundError("pdftoppm was not found")


TMP.mkdir(parents=True, exist_ok=True)
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
subprocess.run(
    [
        find_pdftoppm(),
        "-f",
        "14",
        "-l",
        "14",
        "-r",
        "240",
        "-png",
        str(PDF),
        str(PREFIX),
    ],
    check=True,
)

image = Image.open(RENDERED)
width, height = image.size
# Preserve the full page width and generous vertical context: Definition 3.5,
# all of Remark 3.6(i), and the uniqueness theorem immediately below it.
crop = image.crop((0, int(0.055 * height), width, int(0.67 * height)))
crop.save(OUTPUT)
print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")
