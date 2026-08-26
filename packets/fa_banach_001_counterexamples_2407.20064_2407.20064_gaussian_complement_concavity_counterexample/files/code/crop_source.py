#!/usr/bin/env python3
"""Render and crop the final conjecture from source PDF page 51."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
OUTPUT = ROOT / "figures" / "source_conjecture_crop.png"


def main() -> None:
    renderer = shutil.which("pdftoppm")
    if renderer is None:
        raise SystemExit("pdftoppm is required")
    with tempfile.TemporaryDirectory(prefix="arxiv-2407.20064-crop-") as raw:
        prefix = Path(raw) / "page"
        subprocess.run(
            [renderer, "-f", "51", "-singlefile", "-r", "160", "-png",
             str(SOURCE), str(prefix)],
            check=True,
        )
        with Image.open(prefix.with_suffix(".png")) as page:
            crop = page.crop((150, 790, 1220, 925))
            OUTPUT.parent.mkdir(parents=True, exist_ok=True)
            crop.save(OUTPUT, optimize=True)
            print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()

