from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
source = Image.open(ROOT / "tmp" / "source_page_12.png").convert("RGB")
source.crop((135, 120, 1360, 625)).save(
    ROOT / "figures" / "open_problem_crop.png", quality=95
)
