from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "tmp" / "source_page6.png"
output = ROOT / "figures" / "open_problem_crop.png"

image = Image.open(source)
# Page 6 at 170 dpi.  This includes (1.15), Lemma 1.5, and Open Problem 1.6.
crop = image.crop((220, 735, 1230, 1170))
crop.save(output)
print(f"wrote {output} ({crop.width}x{crop.height})")
