from pathlib import Path

from PIL import Image


packet = Path(__file__).resolve().parents[1]
source = packet / "tmp" / "source-page-08.png"
target = packet / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Section 3 heading, the complete open-question paragraph, and the first
    # contextual sentence after it. Coordinates refer to the 180 dpi render.
    crop = image.crop((105, 1015, 1435, 1345))
    crop.save(target)

print(target)
