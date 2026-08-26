from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
FIGURES.mkdir(exist_ok=True)


def crop(pdf_name: str, page_index: int, rectangle, output_name: str) -> None:
    document = fitz.open(ROOT / pdf_name)
    page = document[page_index]
    pixmap = page.get_pixmap(matrix=fitz.Matrix(2.4, 2.4), clip=fitz.Rect(*rectangle), alpha=False)
    pixmap.save(FIGURES / output_name)


crop(
    "source_paper.pdf",
    3,
    (105, 140, 515, 450),
    "source_conjectures_crop.png",
)
crop(
    "supporting_paper_1807.05469.pdf",
    1,
    (105, 150, 515, 215),
    "later_refutation_statement_crop.png",
)
crop(
    "supporting_paper_1807.05469.pdf",
    2,
    (105, 145, 515, 275),
    "later_two_refutations_crop.png",
)
crop(
    "supporting_paper_1807.05469.pdf",
    3,
    (105, 410, 515, 485),
    "later_hindman_conclusion_crop.png",
)
