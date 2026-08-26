# Verification report

Verdict: `candidate partial; likely valid`.

## Mathematical checks

- Checked ideal membership in the descent lemma:
  `rb=ab-acab` and `br=ba-baca` are differences of ideal elements.
- Checked both cyclic rotations separately:
  `tau(acab)=tau(caba)` because `cab` lies in the ideal, and
  `tau(caba)=tau(baca)` because `ba` lies in the ideal.
- Checked that regularity modulo the ideal makes `r=a-aca` an ideal element,
  so `tau(rb)=tau(br)` uses the trace definition directly.
- Checked the closed-range corollary with the bounded Moore--Penrose inverse.
- Checked the four `2 x 2` products in the square-zero amplification and the
  diagonal-sum amplified trace.
- Checked the spectral functional-calculus identity
  `A-A f_epsilon(A) A=A 1_[0,epsilon)(A)` and the norm bound.
- Checked polar reduction: both products of `|A|` and `BU` lie in the ideal,
  and the initial cyclic rotation uses the ideal element `|A|B=U^*AB`.

No numerical or symbolic computation is part of the proof.

## Scope check

The packet explicitly remains partial. It covers quotient-regular factors,
including all closed-range factors, and gives exact reductions. It does not
claim that arbitrary elements of `B(H)/J` are von Neumann regular and does not
pass to the limit in the spectral-tail reduction.

## Source and rendering checks

- `source_paper.pdf` is the six-page arXiv:1712.06702 PDF.
- `figures/open_problem_crop.png` is a genuine raster crop of page 1 and shows
  the complete Question 1 statement at readable width.
- The final PDF was compiled with `latexmk`, rendered page by page, and all
  pages were visually inspected for clipping, overlap, broken glyphs, and
  unreadable figures.
- Final packet: 4 pages, SHA-256
  `2b8ec183dfdcc3d21bdcad5f3c9dcbb28eab06f4a90dc8d56b408c756c6bfa7a`.
