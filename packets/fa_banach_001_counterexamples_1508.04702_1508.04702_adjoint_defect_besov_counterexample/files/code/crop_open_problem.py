#!/usr/bin/env python3
"""Combine the bottom of source page 18 and top of page 19 into one crop."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
page18 = Image.open(ROOT / "tmp" / "source-1.png").convert("RGB")
page19 = Image.open(ROOT / "tmp" / "source-2.png").convert("RGB")

# At 144 dpi the letter pages are 1224 by 1584 pixels.  The first crop starts
# at Section 6 and the second retains the one-line continuation of Problem 2.
lower = page18.crop((120, 700, 1110, 1515))
upper = page19.crop((120, 65, 1110, 295))
gap = 20
out = Image.new("RGB", (max(lower.width, upper.width), lower.height + gap + upper.height), "white")
out.paste(lower, (0, 0))
out.paste(upper, (0, lower.height + gap))
out.save(ROOT / "figures" / "open_problem_crop.png")
