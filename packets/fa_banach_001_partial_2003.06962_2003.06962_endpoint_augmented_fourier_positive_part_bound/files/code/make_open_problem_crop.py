#!/usr/bin/env python3
"""Render source page 17 and crop Theorem 4.1 plus its open-status paragraph."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
TMP = PACKET / "tmp"
FIGURES = PACKET / "figures"


def find_pdftoppm() -> str:
    configured = os.environ.get("PDFTOPPM")
    candidates = [
        configured,
        shutil.which("pdftoppm"),
        "/Users/pacuaviva/.cache/codex-runtimes/codex-primary-runtime/"
        "dependencies/bin/override/pdftoppm",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return candidate
    raise FileNotFoundError("pdftoppm was not found; set PDFTOPPM explicitly")


def main() -> None:
    TMP.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    prefix = TMP / "source_page_17"
    subprocess.run(
        [
            find_pdftoppm(),
            "-f",
            "17",
            "-singlefile",
            "-png",
            "-r",
            "160",
            str(SOURCE),
            str(prefix),
        ],
        check=True,
    )
    rendered = prefix.with_suffix(".png")
    with Image.open(rendered) as page:
        # Full readable text width; vertically includes Theorem 4.1, its proof,
        # and the paragraph declaring the sharp bound unknown.
        crop = page.crop((135, 160, 1190, 1410))
        crop.save(FIGURES / "open_problem_crop.png", optimize=True)


if __name__ == "__main__":
    main()
