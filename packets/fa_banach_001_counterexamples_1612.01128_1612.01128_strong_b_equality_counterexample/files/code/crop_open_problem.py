from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"


def label(text: str, width: int) -> Image.Image:
    strip = Image.new("RGB", (width, 44), "white")
    draw = ImageDraw.Draw(strip)
    draw.text((12, 10), text, fill="black", font=ImageFont.load_default())
    return strip


page8 = Image.open(FIGURES / "open_problem_page8.png").convert("RGB")
page9 = Image.open(FIGURES / "open_problem_page.png").convert("RGB")

# The conjecture starts at the foot of PDF page 8 and continues at the top of
# PDF page 9.  Keep both pieces so the crop contains the complete statement,
# including the equality characterization that the packet refutes.
top = page8.crop((145, 1580, 1405, 1970))
bottom = page9.crop((145, 90, 1405, 665))
width = max(top.width, bottom.width)
parts = [label("arXiv:1612.01128, PDF page 8", width), top,
         label("arXiv:1612.01128, PDF page 9", width), bottom]
height = sum(part.height for part in parts)
out = Image.new("RGB", (width, height), "white")
y = 0
for part in parts:
    out.paste(part, (0, y))
    y += part.height

out.save(FIGURES / "open_problem_crop.png", optimize=True)
