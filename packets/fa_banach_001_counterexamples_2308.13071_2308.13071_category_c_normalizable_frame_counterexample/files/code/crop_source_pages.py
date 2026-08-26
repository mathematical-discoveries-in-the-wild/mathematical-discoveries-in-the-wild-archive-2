"""Render and crop the source passages used in the solution packet.

Run from the packet directory.  The script needs Pillow and Poppler's
``pdftoppm`` executable.  It writes all disposable full-page renders to
``tmp/`` and only the two review crops to ``figures/``.
"""

from pathlib import Path
import subprocess

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
TMP = ROOT / "tmp"
FIGURES = ROOT / "figures"
PDFTOPPM = Path(
    "/Users/pacuaviva/.cache/codex-runtimes/codex-primary-runtime/"
    "dependencies/bin/override/pdftoppm"
)


def main() -> None:
    TMP.mkdir(exist_ok=True)
    FIGURES.mkdir(exist_ok=True)
    prefix = TMP / "source-page"
    subprocess.run(
        [
            str(PDFTOPPM),
            "-f",
            "8",
            "-l",
            "9",
            "-png",
            "-r",
            "180",
            str(PDF),
            str(prefix),
        ],
        check=True,
    )

    page8 = Image.open(TMP / "source-page-08.png")
    page9 = Image.open(TMP / "source-page-09.png")

    # Theorem 3.13, including the complete definition of category (c).
    page8.crop((140, 1315, 1395, 1670)).save(
        FIGURES / "category_c_theorem_crop.png"
    )

    # The closing observation and Conjecture 3.14.
    page9.crop((135, 1655, 1405, 1820)).save(
        FIGURES / "open_problem_crop.png"
    )


if __name__ == "__main__":
    main()
