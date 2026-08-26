from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
source = PACKET / "tmp" / "source-open-25.png"
destination = PACKET / "figures" / "open_conjecture_crop.png"

# Physical page 25 at 170 dpi.  The crop contains the start of Section 7,
# equation (7.1), and Conjecture 7.1 in full.
with Image.open(source) as image:
    image.crop((235, 900, 1225, 1650)).save(destination)
