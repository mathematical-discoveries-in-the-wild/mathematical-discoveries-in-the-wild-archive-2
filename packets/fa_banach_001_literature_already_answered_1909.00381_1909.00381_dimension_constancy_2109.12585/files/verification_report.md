# Verification report

## Source and answer checks

- Confirmed the open paragraph on source PDF page 4.  It asks for constancy of
  tangent dimension on finite-perimeter boundaries and a sharper perimeter
  representation based on the top-dimensional case.
- Confirmed the source's stratified representation formula in Corollary 3.15:
  `|D chi_E|` is the sum over the strata `F_k E`, weighted by
  `omega_{k-1}/omega_k` and restricted codimension-one Hausdorff-type measure.
- Confirmed answering arXiv:2109.12585 PDF page 3.  Its introduction explicitly
  identifies the source question and Theorem 1.3 proves
  `|D chi_E|(F_k E)=0` for every `k != n`.
- Confirmed answering PDF pages 15--16.  Theorem 3.1 proves the stronger BV
  total-variation concentration theorem, and Corollary 3.2 gives the exact
  one-stratum perimeter formula.
- Confirmed answering Theorem 3.4 on PDF page 16: the tangent module over the
  boundary has constant dimension equal to ambient essential dimension `n`.
- Checked the scope boundary: for general collapsed spaces, the later formula
  retains the reference-measure-dependent `H^h`; ordinary `(n-1)`-Hausdorff
  measure is recorded only in the non-collapsed specialization.

## Literature checks

- Cheap run indexes contained no prior result for arXiv:1909.00381 or this
  question.
- Title, exact-phrase, and theorem searches all identified arXiv:2109.12585 by
  the same authors as the direct answering paper.
- Both full PDFs were inspected at the theorem level; this classification is
  not based on titles or abstracts alone.

## Artifact checks

- `main.tex` compiled under `latexmk -halt-on-error`.
- The final LaTeX log contains no undefined references, multiply defined
  labels, overfull boxes, LaTeX errors, emergency stops, or fatal errors.
- `solution_packet.pdf` has 2 pages with extractable text.
- Both packet pages were rendered at 1.8x and visually inspected; all text,
  formulae, references, and page breaks are legible with no clipping.
- `source_paper.pdf` has 42 pages and
  `supporting_paper_2109.12585.pdf` has 33 pages.
- Both evidence crops were rendered at 2.2x and visually inspected.  They show
  the complete source question, the later paper's explicit identification of
  it, Theorem 1.3, and Corollary 3.2 with the one-stratum formula.
- The result ledger parses as valid JSON and uses model `GPT5.6`.
