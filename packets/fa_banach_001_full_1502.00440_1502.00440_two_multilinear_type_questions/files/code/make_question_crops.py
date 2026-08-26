from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]

crops = {
    "question_1.png": (ROOT / "tmp" / "source_page_9.png", (150, 1590, 1390, 1830)),
    "question_2.png": (ROOT / "tmp" / "source_page_12.png", (150, 505, 1390, 615)),
}

for name, (source, box) in crops.items():
    target = ROOT / "figures" / name
    with Image.open(source) as image:
        image.crop(box).save(target, optimize=True)
    print(target)
