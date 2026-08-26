from pathlib import Path
import shutil
import subprocess
import tempfile

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
FIGURES = ROOT / "figures"


def main() -> None:
    pdftoppm = shutil.which("pdftoppm")
    if pdftoppm is None:
        raise RuntimeError("pdftoppm is required")
    FIGURES.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="besov-crop-") as tmp:
        prefix = Path(tmp) / "source"
        subprocess.run(
            [
                pdftoppm,
                "-f",
                "6",
                "-l",
                "6",
                "-png",
                "-r",
                "180",
                str(SOURCE),
                str(prefix),
            ],
            check=True,
        )
        page = Image.open(Path(tmp) / "source-6.png")
        page.crop((115, 930, 1415, 1860)).save(
            FIGURES / "open_problem_crop.png"
        )


if __name__ == "__main__":
    main()
