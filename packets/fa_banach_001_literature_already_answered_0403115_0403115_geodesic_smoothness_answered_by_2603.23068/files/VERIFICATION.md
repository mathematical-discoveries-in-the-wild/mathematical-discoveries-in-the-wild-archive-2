# Verification report

## Source verification

- Exact target: arXiv:math/0403115, PDF page 10, Remark 14.
- Resolving source: arXiv:2603.23068v3, PDF page 4, Theorem 1.3.
- The current arXiv record was checked on 2026-08-11: v3 dated 30 April 2026
  is the latest version.
- Section 10 of the resolving paper was checked: it constructs a Carnot group
  with two orthonormal horizontal generators and a lift preserving both
  minimality and regularity.

## Mathematical transfer check

- A rank-two step-`s` Carnot group is a stratified quotient of the free
  rank-two step-`s` Carnot group.
- The quotient is a submetry because the two free horizontal basis vectors
  map to the orthonormal frame.
- The distance sandwich `d_G <= d_F <= length = d_G` proves the horizontal
  lift is still minimizing.
- Smoothness descends under the smooth quotient map; therefore a lift of a
  non-smooth curve cannot be smooth.
- In the `b=5` construction, the maximum polynomial coefficient degree is
  `b+3`, and one further generator is needed to extract the central basis
  vector, giving step `b+4=9`.

## Duplicate and scope checks

- No cheap run index contained the source id or the question keywords.
- The packet distinguishes a negative answer to universal smoothness from the
  stronger endpoint-selection question.
- It explicitly leaves the individual cases `3<=m<=8` unresolved.

## Packet/render QA

- `main.tex` was compiled twice with `pdflatex -halt-on-error`.
- The final PDF was checked for warnings and extractable text.
- Every final page was rendered and visually inspected for clipping, overlap,
  missing figures, and illegible mathematics.
