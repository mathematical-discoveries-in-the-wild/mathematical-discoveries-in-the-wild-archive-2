from pathlib import Path

from PIL import Image


HERE = Path(__file__).resolve().parent
PACKET = HERE.parent
source = PACKET / "tmp" / "source-open-page2.png"
target = PACKET / "figures" / "open_question_crop.png"

with Image.open(source) as image:
    # Source PDF page 2 rendered at 180 dpi.  This crop contains the complete
    # paragraph stating Wojtynski's quasinilpotent representation question.
    crop = image.crop((220, 410, 1320, 795))
    crop.save(target, optimize=True)

print(target)
