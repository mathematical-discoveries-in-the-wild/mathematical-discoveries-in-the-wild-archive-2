from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path("/private/tmp/1510_page18.png")
TARGET = ROOT / "figures" / "open_problem_crop.png"

with Image.open(SOURCE) as image:
    # Full-width passage on source PDF page 18: the end of the GFA1 argument,
    # the analytic obstruction for GFA2, and the numerical-only status.
    crop = image.crop((120, 155, 1215, 745))
    crop.save(TARGET)

