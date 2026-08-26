#!/usr/bin/env python3
"""Render the Definition 4.12 / Conjecture 4.13 crop from PDF page 23."""

from pathlib import Path
import subprocess


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
OUTPUT_PREFIX = PACKET / "figures" / "open_problem_crop"

subprocess.run(
    [
        "pdftoppm",
        "-f", "23",
        "-l", "23",
        "-singlefile",
        "-png",
        "-r", "160",
        "-x", "0",
        "-y", "90",
        "-W", "1360",
        "-H", "650",
        str(SOURCE),
        str(OUTPUT_PREFIX),
    ],
    check=True,
)
print(f"wrote {OUTPUT_PREFIX}.png")

