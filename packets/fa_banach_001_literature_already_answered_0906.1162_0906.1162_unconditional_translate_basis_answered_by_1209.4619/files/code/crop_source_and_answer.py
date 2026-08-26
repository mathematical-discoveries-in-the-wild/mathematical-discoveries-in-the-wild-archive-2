from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]


def render_crop(pdf_name: str, page_index: int, rect: fitz.Rect, output: str) -> None:
    doc = fitz.open(ROOT / pdf_name)
    page = doc[page_index]
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=rect, alpha=False)
    pix.save(ROOT / "figures" / output)


render_crop(
    "source_paper.pdf",
    26,
    fitz.Rect(96, 690, 548, 742),
    "source_problem_crop.png",
)

render_crop(
    "supporting_paper_1209.4619.pdf",
    4,
    fitz.Rect(60, 512, 551, 562),
    "answer_corollary_crop.png",
)
