from pathlib import Path

from PIL import Image


packet = Path(__file__).resolve().parents[1]
source = packet / "tmp" / "pdfs" / "source_page_29-29.png"
target = packet / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    crop = image.crop((120, 110, 1450, 1080))
    crop.save(target)

print(f"wrote {target} at {crop.width}x{crop.height}")
