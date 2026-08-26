from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
FIGURES = ROOT / "figures"


def containing_page(doc: fitz.Document, needle: str):
    for index, page in enumerate(doc):
        if needle in page.get_text("text"):
            return index, page
    raise RuntimeError(f"Could not locate source phrase: {needle!r}")


def render_question(doc: fitz.Document) -> tuple[int, fitz.Rect, int, int]:
    page_index, page = containing_page(doc, "It is thus a natural question")
    example_hits = page.search_for("Example 4.11")
    if not example_hits:
        raise RuntimeError("Could not locate the following example.")
    rect = fitz.Rect(
        page.rect.x0,
        page.rect.y0 + 28,
        page.rect.x1,
        example_hits[0].y0 - 7,
    )
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=rect, alpha=False)
    pix.save(FIGURES / "open_problem_crop.png")
    return page_index, rect, pix.width, pix.height


def render_scope(doc: fitz.Document) -> tuple[int, fitz.Rect, int, int]:
    phrase = "We do expect to have settings"
    page_index, page = containing_page(doc, phrase)
    hits = page.search_for(phrase)
    if not hits:
        raise RuntimeError("Could not locate the expected-settings paragraph.")
    hit = hits[0]
    endings = page.search_for("details.")
    if not endings:
        raise RuntimeError("Could not locate the end of the expected-settings paragraph.")
    rect = fitz.Rect(
        page.rect.x0,
        max(page.rect.y0, hit.y0 - 8),
        page.rect.x1,
        min(page.rect.y1, endings[0].y1 + 8),
    )
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=rect, alpha=False)
    pix.save(FIGURES / "open_problem_scope_crop.png")
    return page_index, rect, pix.width, pix.height


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF)
    question = render_question(doc)
    scope = render_scope(doc)
    metadata = [
        f"source={PDF}",
        (
            "open_problem_crop.png: page_number={} crop_points={} pixels={}x{}"
        ).format(
            question[0] + 1,
            tuple(round(value, 2) for value in question[1]),
            question[2],
            question[3],
        ),
        (
            "open_problem_scope_crop.png: page_number={} crop_points={} pixels={}x{}"
        ).format(
            scope[0] + 1,
            tuple(round(value, 2) for value in scope[1]),
            scope[2],
            scope[3],
        ),
    ]
    (FIGURES / "crop_metadata.txt").write_text(
        "\n".join(metadata) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
