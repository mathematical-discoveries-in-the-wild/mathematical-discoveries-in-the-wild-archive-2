"""Crop the concluding open question from page 32 of the source paper.

Run from the repository root after rendering page 32 at 180 dpi as
``tmp/source_page-32.png``.
"""

from pathlib import Path

from PIL import Image


PACKET = Path(
    "runs/fa_banach_001/solutions/full/"
    "1405.2731_block_clustered_c0_group_generator"
)
SOURCE = PACKET / "tmp/source_page-32.png"
OUTPUT = PACKET / "figures/open_problem_crop.png"


with Image.open(SOURCE) as page:
    # Keep the full text width and both margins.  The vertical window includes
    # the lead-in, the complete question, and the authors' semigroup contrast.
    crop = page.crop((155, 985, 1375, 1205))
    crop.save(OUTPUT, optimize=True)

print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")
