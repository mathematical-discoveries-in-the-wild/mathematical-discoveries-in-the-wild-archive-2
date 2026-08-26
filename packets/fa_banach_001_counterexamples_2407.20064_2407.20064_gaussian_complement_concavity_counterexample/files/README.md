# Gaussian balls refute the complement-concavity conjecture

**Status:** candidate full counterexample, likely valid; human review
requested.

The final conjecture of arXiv:2407.20064 proposes extending
`(1/n)`-concavity from origin-symmetric convex bodies to a Minkowski
combination involving the complement of one body.

This packet gives a full negative answer.  In dimension two, take the
standard Gaussian measure, `K = 6 B_2^2`, `L = 2 B_2^2`, and `t = 1/2`.
Then

`(1-t)(R^2 \ int K) + tL = R^2 \ int(2 B_2^2)`.

The left side of the proposed inequality is therefore `exp(-2)`, whereas the
right side is strictly greater than `(1-exp(-2))/4`, which itself is greater
than `exp(-2)` because `exp(2)>5`.

The example meets the premise: Eskenazis and Moschidis proved that the
standard Gaussian is `(1/n)`-concave over origin-symmetric convex bodies.
The packet also proves a stronger ball obstruction: every absolutely
continuous probability measure satisfying the premise violates the proposed
extension for some pair of concentric balls.

Files:

- `solution_packet.pdf`: review-ready counterexample and proof.
- `main.tex`: complete LaTeX source.
- `source_paper.pdf`: original arXiv paper.
- `supporting_paper_2004.07146.pdf`: Gaussian dimensional
  Brunn--Minkowski theorem.
- `figures/source_conjecture_crop.png`: source's final conjecture.
- `code/crop_source.py`: reproducible source-page crop.
- `code/verify_gaussian_counterexample.py`: exact set-radius and elementary
  inequality checks.
- `tmp/`: build and rendered-page QA artifacts.

Exact/current searches found no existing refutation.  Novelty confidence is
moderate-high, subject to human review.

