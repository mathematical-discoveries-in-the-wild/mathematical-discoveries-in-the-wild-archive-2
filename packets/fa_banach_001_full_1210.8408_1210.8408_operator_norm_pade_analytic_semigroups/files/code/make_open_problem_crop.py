"""Crop the open-problem passage from the rendered source-paper page 13."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "source_page_13.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE)
    if image.size != (2040, 2640):
        raise RuntimeError(f"unexpected render size: {image.size}")
    # Preserve the full text-column width.  The crop includes the end of
    # Theorem 4.6, all of Remark 4.7, and the heading that follows it.
    crop = image.crop((285, 655, 1755, 1125))
    crop.save(OUTPUT, optimize=True)
    print(f"wrote {OUTPUT} at {crop.size[0]}x{crop.size[1]}")


if __name__ == "__main__":
    main()
