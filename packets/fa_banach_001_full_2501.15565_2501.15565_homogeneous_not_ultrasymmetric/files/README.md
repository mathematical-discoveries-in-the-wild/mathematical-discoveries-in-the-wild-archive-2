# A homogeneous r.i. space that is not ultrasymmetric

This packet gives a candidate full negative resolution of Remark 2.14 in
arXiv:2501.15565.  It constructs an exact 2-homogeneous
rearrangement-invariant Banach function norm

`||f||_X = sup_I |I|^{-1/2} integral_I exp(s/2) f**(exp(s)) ds`.

The logarithmic Morrey functional is translation invariant, so the norm has
exact dilation homogeneity.  It is not ultrasymmetric: two families built
from the same multiset of logarithmic gaps have uniformly comparable
rearrangements of `exp(s/2) f*(exp(s))`, but clustering the small gaps makes
the defining norm grow like `sqrt(m)`, while alternating small and very large
gaps keeps it uniformly bounded.  This contradicts Pustylnik's r.i.-parameter
representation of every ultrasymmetric space.

Files:

- `solution_packet.pdf` — self-contained construction and counterexample.
- `main.tex` — LaTeX source.
- `source_paper.pdf` — arXiv:2501.15565v2.
- `figures/open_problem_crop.png` — source PDF page 8, Remark 2.14.
- `VERIFIER_REPORT.md` — mathematical, source, novelty, and visual checks.
