#!/usr/bin/env python3
"""Render and crop Remark 2.3 from the source paper."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    renderer = shutil.which("pdftoppm")
    if renderer is None:
        raise SystemExit("pdftoppm is required")
    with tempfile.TemporaryDirectory(prefix="arxiv-1008.5241-crop-") as raw:
        prefix = Path(raw) / "page"
        subprocess.run(
            [renderer, "-f", "4", "-singlefile", "-r", "160", "-png",
             str(SOURCE), str(prefix)],
            check=True,
        )
        with Image.open(prefix.with_suffix(".png")) as page:
            # PDF page 4: Remark 2.3 and the following Volterra paragraph.
            crop = page.crop((105, 805, 1255, 1480))
            OUTPUT.parent.mkdir(parents=True, exist_ok=True)
            crop.save(OUTPUT, optimize=True)
            print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()

