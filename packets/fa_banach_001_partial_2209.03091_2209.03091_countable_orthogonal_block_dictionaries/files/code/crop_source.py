"""Crop the open characterization question from rendered source page 13."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
image = Image.open(PACKET / "tmp" / "source_page_13.png")
image.crop((175, 1300, 1150, 1665)).save(PACKET / "figures" / "open_question_crop.png")
