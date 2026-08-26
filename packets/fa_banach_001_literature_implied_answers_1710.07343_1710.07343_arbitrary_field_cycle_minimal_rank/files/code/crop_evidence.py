"""Create exact evidence crops from rendered source and thesis pages."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
TMP = PACKET / "tmp"
FIGURES = PACKET / "figures"
FIGURES.mkdir(exist_ok=True)

source = Image.open(TMP / "source_page_17.png")
source.crop((210, 1160, 1110, 1575)).save(FIGURES / "open_problem_crop.png")

page_64 = Image.open(TMP / "thesis_page_64.png")
page_65 = Image.open(TMP / "thesis_page_65.png")
upper = page_64.crop((130, 1815, 1570, 1990))
lower = page_65.crop((130, 0, 1570, 270))
support = Image.new("RGB", (max(upper.width, lower.width), upper.height + lower.height), "white")
support.paste(upper, (0, 0))
support.paste(lower, (0, upper.height))
support.save(FIGURES / "supporting_bound_crop.png")
