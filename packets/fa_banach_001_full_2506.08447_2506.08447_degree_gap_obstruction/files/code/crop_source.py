from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "figures" / "source_page_10.png"
target = ROOT / "figures" / "question_4_6_crop.png"

image = Image.open(source)
# Full-width context surrounding the failed quadratic route, Question 4.6,
# and the authors' statement that their negative examples miss its ordering.
crop = image.crop((220, 225, 1280, 1115))
crop.save(target)
print(target)
