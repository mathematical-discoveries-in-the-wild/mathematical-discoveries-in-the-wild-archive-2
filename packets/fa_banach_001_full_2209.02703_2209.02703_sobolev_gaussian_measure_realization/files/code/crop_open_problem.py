from pathlib import Path

from PIL import Image


root = Path(__file__).resolve().parents[1]
page = Image.open(root / "figures" / "open_problem_page.png").convert("RGB")
# Concluding paragraph on PDF page 29, including both numbered questions.
page.crop((175, 760, 1390, 1160)).save(
    root / "figures" / "open_problem_crop.png", optimize=True
)
