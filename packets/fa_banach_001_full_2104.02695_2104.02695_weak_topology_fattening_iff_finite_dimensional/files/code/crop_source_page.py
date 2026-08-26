#!/usr/bin/env python3
"""Render page 8 of arXiv:2104.02695 and crop Open Question 1.

The crop deliberately retains the full page width.  Only vertical whitespace
and the later material on the page are removed.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

from PIL import Image


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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=Path, default=Path("source_paper.pdf"))
    parser.add_argument(
        "--output", type=Path, default=Path("figures/open_problem_crop.png")
    )
    parser.add_argument("--dpi", type=int, default=240)
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    rendered_prefix = args.output.parent / "page8_render"
    subprocess.run(
        [
            find_pdftoppm(),
            "-f",
            "8",
            "-l",
            "8",
            "-singlefile",
            "-png",
            "-r",
            str(args.dpi),
            str(args.pdf),
            str(rendered_prefix),
        ],
        check=True,
    )

    rendered = rendered_prefix.with_suffix(".png")
    with Image.open(rendered) as image:
        width, height = image.size
        crop = image.crop((0, round(0.09 * height), width, round(0.374 * height)))
        crop.save(args.output)
    rendered.unlink()


if __name__ == "__main__":
    main()
