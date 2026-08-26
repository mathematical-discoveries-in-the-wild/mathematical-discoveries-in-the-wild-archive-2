#!/usr/bin/env python3
"""Create a full-width stitched crop of Theorem 1.5 and the open problem."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
PAGE_10 = ROOT / "tmp" / "source_render" / "source-10.png"
PAGE_11 = ROOT / "tmp" / "source_render" / "source-11.png"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"

page_10 = Image.open(PAGE_10).convert("RGB")
page_11 = Image.open(PAGE_11).convert("RGB")

# Retain the complete page width.  Page 10 contains the referenced inequality
# (1.23), its sharp Gaussian value, and the beginning of the open problem.
# Page 11 contains the two-line continuation of the problem statement.
upper = page_10.crop((0, 300, page_10.width, 1830))
lower = page_11.crop((0, 0, page_11.width, 330))

gap = 18
canvas = Image.new("RGB", (page_10.width, upper.height + gap + lower.height), "white")
canvas.paste(upper, (0, 0))
canvas.paste(lower, (0, upper.height + gap))
canvas.save(OUTPUT)
print(OUTPUT)
