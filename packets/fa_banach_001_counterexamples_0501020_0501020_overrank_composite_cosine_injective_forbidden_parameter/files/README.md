# A forbidden parameter is nevertheless injective in the over-rank case

**Status:** candidate full counterexample, likely valid; human review
requested.

Ournycheva and Rubin ask whether their sufficient condition

`lambda_j + m - j not in {0,2,4,...}`

is necessary for injectivity of the composite cosine transform when
`2m > n`. It is not.

For `(n,m)=(3,2)` and `lambda=(alpha,0)`, identifying a plane with its
unit normal turns the composite transform into the spherical sine-power
transform with kernel

`(1-(w dot u_1)^2)^(alpha/2)`.

The packet computes every even spherical-harmonic multiplier and proves that
this transform is injective exactly when `alpha` is not a nonnegative even
integer. In particular, `lambda=(1,0)` violates both exclusions in the
source condition but still gives an injective transform.

Files:

- `solution_packet.pdf`: review-ready statement and proof.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source question on PDF page 19.
- `code/crop_source.py`: reproducible source-page crop.
- `code/verify_multipliers.py`: numerical audit of the exact multiplier formula.
- `tmp/`: build and rendered-page QA artifacts.

A bounded exact/current literature search found no later explicit resolution
of the multiparameter `2m>n` question. Novelty confidence is moderate-high,
subject to expert review.
