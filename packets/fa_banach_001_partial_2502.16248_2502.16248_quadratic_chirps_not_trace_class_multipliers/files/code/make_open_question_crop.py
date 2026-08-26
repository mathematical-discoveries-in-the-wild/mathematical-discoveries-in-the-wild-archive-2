#!/usr/bin/env python3
"""Render source PDF page 21 and crop the candidate/Question 1 passage."""

from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
TMP = PACKET / "tmp"
OUTPUT = PACKET / "figures" / "open_question_crop.png"


def locate_pdftoppm() -> str:
    explicit = os.environ.get("PDFTOPPM")
    if explicit:
        return explicit
    found = shutil.which("pdftoppm")
    if found:
        return found
    bundled = Path(
        "/Users/pacuaviva/.cache/codex-runtimes/codex-primary-runtime/"
        "dependencies/native/poppler/bin/pdftoppm"
    )
    if bundled.exists():
        return str(bundled)
    raise RuntimeError("pdftoppm was not found")


def main() -> None:
    TMP.mkdir(parents=True, exist_ok=True)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    prefix = TMP / "source-page"
    subprocess.run(
        [
            locate_pdftoppm(),
            "-f", "21", "-l", "21", "-png", "-r", "160",
            str(SOURCE), str(prefix),
        ],
        check=True,
    )
    rendered = TMP / "source-page-21.png"
    with Image.open(rendered) as page:
        # At 160 dpi, retain the last setup line, nonmeasure statement,
        # candidate discussion, and the complete displayed Question 1.
        crop = page.crop((125, 100, 1235, 640))
        crop.save(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    main()

