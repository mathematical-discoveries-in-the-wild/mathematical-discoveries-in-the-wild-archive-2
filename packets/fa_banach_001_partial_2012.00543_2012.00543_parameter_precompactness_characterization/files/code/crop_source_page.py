from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "tmp" / "source_page26.png"
output = ROOT / "figures" / "open_problem_crop.png"

image = Image.open(source)
# Page 26 at 170 dpi; retain full text width and the whole converse question.
crop = image.crop((220, 1320, 1235, 1655))
crop.save(output)
print(f"wrote {output} ({crop.width}x{crop.height})")
