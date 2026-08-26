"""Crop and stitch the two-page open-problem remark from rendered source pages."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT / "tmp"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    page4 = Image.open(TMP / "source_page-4.png").convert("RGB")
    page5 = Image.open(TMP / "source_page-5.png").convert("RGB")

    # Preserve the complete readable text width and a generous margin.
    part4 = page4.crop((210, 1540, 1280, 2055))
    part5 = page5.crop((210, 55, 1280, 470))

    label_height = 36
    gap = 24
    canvas = Image.new(
        "RGB",
        (max(part4.width, part5.width),
         label_height + part4.height + gap + label_height + part5.height),
        "white",
    )
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default(size=20)
    draw.text((8, 6), "Source paper, p. 4 (Remark 2.2 begins)", fill="black", font=font)
    canvas.paste(part4, (0, label_height))
    second_y = label_height + part4.height + gap
    draw.text((8, second_y + 6), "Source paper, p. 5 (continuation and question)", fill="black", font=font)
    canvas.paste(part5, (0, second_y + label_height))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUT, optimize=True)


if __name__ == "__main__":
    main()
