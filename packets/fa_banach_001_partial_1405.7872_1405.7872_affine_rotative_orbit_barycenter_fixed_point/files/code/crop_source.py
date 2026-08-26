from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
source = Image.open(ROOT / "tmp" / "source_page_4.png").convert("RGB")
source.crop((205, 410, 1330, 885)).save(
    ROOT / "figures" / "open_questions_crop.png", quality=95
)
