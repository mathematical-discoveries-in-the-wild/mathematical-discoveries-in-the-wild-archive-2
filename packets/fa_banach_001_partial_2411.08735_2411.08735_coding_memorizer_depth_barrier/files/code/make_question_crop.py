from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PAGE = Path("/private/tmp/2411.08735_refs/source-page-01.png")
OUTPUT = ROOT / "question_crop.png"


def main() -> None:
    with Image.open(SOURCE_PAGE) as image:
        # Direct crop of printed page 52: Remark 79, Table 3, and its first
        # explanatory bullet. Coordinates refer to the 144 dpi source render.
        crop = image.crop((145, 820, 1085, 1420))
        crop.save(OUTPUT, optimize=True)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()
