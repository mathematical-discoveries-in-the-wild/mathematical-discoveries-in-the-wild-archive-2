"""Crop the exact open assertion from page 3 of the official source PDF.

Run from the repository root after rendering page 3 at 180 dpi as
``tmp/source_page_3.png``.
"""

from pathlib import Path

from PIL import Image


PACKET = Path(
    "runs/fa_banach_001/solutions/full/"
    "1601.02972_theta4_scaled_log_derivative_decreasing_convex"
)
source = PACKET / "tmp/source_page_3.png"
target = PACKET / "figures/open_problem_crop.png"

with Image.open(source) as image:
    # Theorem 2.4, its discussion, and the two-line stronger assertion.
    crop = image.crop((175, 1300, 1365, 1905))
    crop.save(target)

print(target)
