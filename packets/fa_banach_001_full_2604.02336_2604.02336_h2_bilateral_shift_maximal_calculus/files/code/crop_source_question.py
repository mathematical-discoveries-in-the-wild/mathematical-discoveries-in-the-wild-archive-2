from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "tmp" / "source_page-7.png"
target = ROOT / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Conclusion and the complete future-work statement, PDF page 7.
    crop = image.crop((65, 545, 760, 1062))
    crop.save(target)
