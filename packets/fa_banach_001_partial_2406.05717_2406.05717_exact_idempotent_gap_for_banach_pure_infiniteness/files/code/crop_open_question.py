from pathlib import Path

from PIL import Image


HERE = Path(__file__).resolve().parent
PACKET = HERE.parent

crops = [
    (
        PACKET / "tmp" / "source-open-page-27.png",
        PACKET / "figures" / "source_assumption_crop.png",
        (145, 1010, 1385, 1558),
    ),
    (
        PACKET / "tmp" / "source-open-page-28.png",
        PACKET / "figures" / "open_problem_crop.png",
        (145, 1115, 1385, 1265),
    ),
]

for source, target, box in crops:
    with Image.open(source) as image:
        image.crop(box).save(target, optimize=True)
    print(target)
