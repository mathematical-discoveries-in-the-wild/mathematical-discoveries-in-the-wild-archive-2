# Fourier-frame self-affine measures are self-affine tiles

This packet gives a candidate full affirmative resolution of Q2 in
arXiv:1103.4691 under the equal-weight, common-matrix definition naturally
extending the class treated in the paper.  If the common expansive matrix is
`R`, there are `N` distinct digits, and `q = |det R|`, positive measure gives
`q <= N`.  A generic linear functional produces an address isolated in a
unique cylinder at every depth.  On a positive-measure neighborhood of that
point, the iterated density equation has one summand and multiplies the
density by `(q/N)^n`.  The Fourier-frame density bounds therefore force
`q >= N`.

Thus `q = N`, the cylinders partition the attractor almost everywhere, and
uniqueness of the invariant probability makes the measure normalized
Lebesgue measure on its attractor.  The attractor is consequently a
self-affine tile.  Probability normalization means the density is
`|K|^{-1} chi_K` (literally `chi_K` only when `|K| = 1`).

Files:

- `solution_packet.pdf` — self-contained proof, scope, and novelty audit.
- `main.tex` — LaTeX source.
- `source_paper.pdf` — arXiv:1103.4691.
- `figures/question_q2.png` — source PDF page 13, Q2.
- `VERIFIER_REPORT.md` — mathematical, source, novelty, and visual checks.
