from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "figures" / "source_page_3.png"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"

# The paragraph comparing the needed argument with de Leeuw's theorem and
# ending with the sentence that the general homogeneous problem remains open.
BOX = (125, 775, 1245, 1260)

with Image.open(SOURCE) as image:
    image.crop(BOX).save(OUTPUT)

print(OUTPUT)
