from pathlib import Path

from PIL import Image, ImageOps, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT / "tmp"
FIG = ROOT / "figures" / "open_problem_crop.png"


page1 = Image.open(TMP / "source_page-01.png").convert("RGB")
page2 = Image.open(TMP / "source_page-02.png").convert("RGB")

# The open-problem passage begins near the foot of PDF page 1 and completes
# in the first lines of PDF page 2.  Keep the entire text width and enough
# surrounding prose to make the continuation unambiguous.
crop1 = page1.crop((120, 1080, page1.width - 90, 1505))
crop2 = page2.crop((120, 0, page2.width - 90, 300))

separator = 18
canvas = Image.new(
    "RGB",
    (max(crop1.width, crop2.width), crop1.height + separator + crop2.height),
    "white",
)
canvas.paste(crop1, (0, 0))
canvas.paste(crop2, (0, crop1.height + separator))
draw = ImageDraw.Draw(canvas)
draw.line((0, crop1.height + separator // 2, canvas.width, crop1.height + separator // 2), fill="#888888", width=2)
canvas.save(FIG, optimize=True)
print(FIG)
print(canvas.size)
