"""Crop Remark 2.20 from rendered source page 21."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
image = Image.open(PACKET / "tmp" / "source_page_21.png")
image.crop((110, 585, 1090, 735)).save(
    PACKET / "figures" / "open_question_crop.png"
)
