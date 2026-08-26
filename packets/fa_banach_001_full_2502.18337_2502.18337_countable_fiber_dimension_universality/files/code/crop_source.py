"""Render and crop the Section 5 open questions from source PDF page 12."""

from pathlib import Path
import shutil
import subprocess

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
PDF = PACKET / "source_paper.pdf"
TMP = PACKET / "tmp"
PREFIX = TMP / "source_page"
RENDERED = TMP / "source_page-12.png"
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
        "12",
        "-l",
        "12",
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
# Preserve full text width and both complete Section 5 questions.
crop = image.crop((0, int(0.035 * height), width, int(0.69 * height)))
crop.save(OUTPUT)
print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")
