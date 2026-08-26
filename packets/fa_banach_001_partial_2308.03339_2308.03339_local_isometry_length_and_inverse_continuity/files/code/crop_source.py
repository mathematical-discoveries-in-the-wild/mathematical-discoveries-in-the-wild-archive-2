from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "tmp" / "source_page1.png"
target = ROOT / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Abstract, modern transcription, and the explicit nonseparable status.
    crop = image.crop((280, 520, 1390, 1660))
    crop.save(target)

print(target)
