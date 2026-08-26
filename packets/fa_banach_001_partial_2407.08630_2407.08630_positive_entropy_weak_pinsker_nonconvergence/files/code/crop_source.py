"""Crop the concluding open-question paragraph from arXiv:2407.08630 page 6.

Run from the packet directory after rendering page 6 at 180 dpi as
tmp/pdfs/source_page-6.png.
"""

from pathlib import Path

from PIL import Image


packet = Path(__file__).resolve().parents[1]
source = packet / "tmp" / "pdfs" / "source_page-6.png"
target = packet / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Preserve the full text width and both margins around the complete
    # concluding paragraph that contains all three questions.
    crop = image.crop((190, 175, 1340, 610))
    crop.save(target)

print(target)
