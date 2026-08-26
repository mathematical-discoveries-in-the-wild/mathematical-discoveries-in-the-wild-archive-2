# Robin multiplier approximation and reciprocal resolvents

This packet gives a candidate solution to two explicit components of the
open program in arXiv:1901.04450.

1. For every nonresonant real Robin pair `(alpha,beta)`, the boundary-trace
   approximation error is uniformly equivalent to both the exterior Poisson
   semigroup error and `K(t,h;L2,D(N))`. This gives the exact direct/inverse
   theorem, order-one saturation, and the replacement derivative operator.
2. The displayed reciprocal-resolvent identity holds for every closed
   injective operator at reciprocal resolvent points; it is algebraic and
   needs no semigroup. A bounded generalized-Drazin block version is included.

The result is classified as substantial partial because it does not claim all
inverse-ergodic or unbounded generalized-Drazin counterparts proposed in the
source.

## Files

- `main.tex` / `solution_packet.pdf`: full theorem and proof.
- `verification.md`: independent adversarial audit.
- `code/check_robin_multipliers.py`: symbolic and finite-grid sanity checks.
- `source_paper.pdf`: arXiv source paper.
- `figures/source_open_problem.png`: source problem crop.

## Status

`partial_likely_valid`; operator-theory/approximation-theory review
recommended.

