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
    with tempfile.TemporaryDirectory(prefix="gw-outside-crop-") as tmp_name:
        prefix = Path(tmp_name) / "source"
        subprocess.run(
            [
                pdftoppm,
                "-f",
                "49",
                "-l",
                "49",
                "-png",
                "-r",
                "180",
                str(SOURCE),
                str(prefix),
            ],
            check=True,
        )
        page = Image.open(Path(tmp_name) / "source-49.png")
        page.crop((105, 1125, 1425, 1695)).save(
            FIGURES / "open_problem_crop.png"
        )


if __name__ == "__main__":
    main()
