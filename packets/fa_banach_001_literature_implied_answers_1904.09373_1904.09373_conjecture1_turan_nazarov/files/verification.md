# Verification

- Checked the exact source text in the local arXiv source archive. Conjecture
  `conj1` is at `source.tex` lines 304--306 and on page 2 of the locally
  compiled `source_paper.pdf`.
- Checked the supporting result in arXiv:1107.0039. Theorem `turan` is at
  `source.tex` lines 72--79 and on page 1 of
  `supporting_paper_1107.0039.pdf`.
- The supporting theorem has exponent `m` for `m+1` exponential terms and one
  absolute constant. Its exponential prefactor is one because all exponents
  here are purely imaginary.
- Stress-tested the limit step: the Bohr coefficient formula gives
  `H_f <= liminf M_T`, and the source explicitly defines `J_f(u)` as the limit
  of the centered-interval relative sublevel measures.
- Scope is intentionally limited to Conjecture 1. Conjectures 2 and 3 are not
  claimed solved.
- The source and supporting PDFs were compiled twice from local source
  archives. The original source contained a legacy Windows-1252 dash byte;
  this was sanitized only in a temporary build copy.
- The compact packet was compiled twice, checked for LaTeX warnings and bad
  boxes, rendered page-by-page, and visually inspected.

