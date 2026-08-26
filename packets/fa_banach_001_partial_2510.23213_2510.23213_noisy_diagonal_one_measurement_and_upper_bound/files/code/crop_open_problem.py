"""Create the full-width page-12 crop containing the source open question."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "source_page-12.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    with Image.open(SOURCE) as image:
        # Preserve both text margins and the complete lead-in, question, and
        # immediately following scope remark from source page 12.
        crop = image.crop((235, 235, 1295, 1575))
        crop.save(OUTPUT)
        print({"source_size": image.size, "crop_size": crop.size, "output": str(OUTPUT)})


if __name__ == "__main__":
    main()
