"""Create reproducible, non-synthetic crops from rendered source-PDF pages."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parent.parent
TMP = PACKET / "tmp"
FIGURES = PACKET / "figures"

# Coordinates refer to 1530 x 1980 PNG pages rendered at 180 DPI.
CROPS = {
    "source_weight_definition_crop.png": ("source_page-03.png", (120, 80, 1410, 760)),
    "source_theorem_crop.png": ("source_page-06.png", (120, 1020, 1410, 1910)),
    "open_problem_crop.png": ("source_page-07.png", (120, 60, 1410, 770)),
    "source_proof_flaw_crop.png": ("source_page-26.png", (120, 60, 1410, 710)),
}


def main() -> None:
    FIGURES.mkdir(exist_ok=True)
    for output_name, (input_name, box) in CROPS.items():
        source = TMP / input_name
        with Image.open(source) as page:
            if page.size != (1530, 1980):
                raise ValueError(f"unexpected render size for {source}: {page.size}")
            crop = page.crop(box)
            crop.save(FIGURES / output_name, optimize=True)
            print(f"{output_name}: source={input_name}, box={box}, size={crop.size}")


if __name__ == "__main__":
    main()
