# Coordinate Riesz transform for a separated Schrödinger operator

This packet fully answers the concrete unknown case displayed on page 8 of
arXiv:1503.02508.

For `L = -Delta + V(x2)` with `V >= 0`, the transform
`T = partial_x1 L^{-1/2}` is bounded on every `L^p(R^2)`, `1 < p < infinity`.
The source already recalls the estimate below two.  Because the potential is
independent of `x1`, the derivative commutes with `L`; since it is
skew-adjoint, `T* = -T`.  Duality reflects every below-two estimate to the
conjugate exponent above two.

Status: `candidate_full_likely_valid`, pending human review.

Files:

- `main.tex`: complete proof and separated-coordinate extension.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: readable source excerpt.
- `VERIFICATION.md`: proof, build, visual-QA, and hash record.
