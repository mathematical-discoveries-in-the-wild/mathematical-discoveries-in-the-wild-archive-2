# Hardy-range saturation infimum equals one

Status: candidate full solution, likely valid, awaiting specialist review.

This packet resolves Open Problem 2 (“Saturation infimum”) of arXiv:2601.01821
for every exponent in the stated Hardy range. Under the source hypotheses,

\[
\varepsilon_p(A;r,R)=1 \qquad (0<p\le1).
\]

The key is scalar damping. For one smooth annular radial generator with bounded
Hardy-space frame operator \(U\), the generator \(t\psi\) remains admissible,
its frame operator is \(t^2U\), and the exact \(p\)-triangle inequality gives

\[
\|t^2U-I\|^p\le1+t^{2p}\|U\|^p.
\]

Letting \(t\) decrease to zero matches the source's lower bound of one.

Contents:

- `main.tex` and `solution_packet.pdf`: self-contained proof packet.
- `source_paper.pdf`: locally compiled arXiv source.
- `figures/open_problem_crop.png`: readable full-width crop containing Open
  Problem 2 and its endpoint comparison.
- `VERIFICATION.md`: proof and artifact checks.
- `source_tex/`: archived source TeX used to compile the source PDF.

The source's separate Open Problem 3, concerning removal of radiality, remains
open and is not claimed here.
