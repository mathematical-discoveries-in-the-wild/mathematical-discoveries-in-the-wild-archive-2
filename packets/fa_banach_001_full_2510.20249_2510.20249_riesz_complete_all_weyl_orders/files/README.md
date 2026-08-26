# Riesz-complete extensions realize every Weyl order

Status: `candidate_full_solution_likely_valid`

This packet answers the open question at the end of Section 5 of
arXiv:2510.20249. The existence of a Riesz-complete non-self-adjoint
extension imposes no restriction on Weyl order: every value in the full
range `[0,infinity]` occurs.

The construction starts with arbitrary increasing real locations `x_n` and
puts poles at `lambda_n=x_n-i y_n`, where `y_n` is exponentially small
relative to the nearest-neighbor gap. An elementary pseudohyperbolic-product
estimate makes the conjugate sequence uniformly interpolating, so the
source's criterion gives Riesz completeness. The source's phase formula for
Weyl height then reduces the order calculation to the radial density of the
chosen `x_n`.

Choices `x_n=n^(1/rho)`, `x_n=exp(sqrt(n))`, and `x_n=log(n+1)` give,
respectively, every positive finite order, order zero, and infinite order.

Files:

- `main.tex`: full construction and proof.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: arXiv:2510.20249v1.
- `code/verify_construction.py`: finite truncation checks of the separation
  bound and growth regimes.
- `tmp/`: build and page-render intermediates.

