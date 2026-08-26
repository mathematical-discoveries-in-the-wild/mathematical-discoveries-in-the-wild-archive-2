# Exact incompressible smoothing for triangular maps and radial twists

Status: **candidate partial result; likely valid; human review requested**

Source: Stanislav Hencl, *Ball-Evans approximation problem: recent progress
and open problems*, arXiv:2502.01336v1. The target is Open Problem 5 on PDF
page 6.

## Result

This packet proves two structured subcases of the incompressible Ball-Evans
approximation problem for every dimension `n >= 2` and every finite
`1 <= p < infinity`.

1. Every continuous Sobolev unitriangular deformation on a rectangle,

   ```text
   F_i(x) = x_i + u_i(x_{i+1},...,x_n),   F_n(x) = x_n + c,
   ```

   is a `W^{1,p}` and uniform limit of smooth unitriangular diffeomorphisms.
   Every approximant has Jacobian exactly one. This includes arbitrary
   one-dimensional incompressible rank-one laminates after affine changes of
   coordinates.

2. Every radial twist of the ball

   ```text
   T_theta(x) = R_{theta(|x|)} x
   ```

   satisfying

   ```text
   integral_0^1 r^(n-1+p) |theta'(r)|^p dr < infinity
   ```

   is a `W^{1,p}` and uniform limit of smooth incompressible diffeomorphisms
   of the ball onto itself. The approximants preserve the boundary trace.
   The angle may rotate infinitely often near the origin; no limit of
   `theta(r)` at zero is needed.

The determinant is protected algebraically. Unitriangular Jacobians have
diagonal entries one. For radial twists, the matrix determinant lemma reduces
the rank-one correction to `x^T S x` with `S` skew-symmetric, hence to zero.
Global injectivity is protected by back-substitution in the first class and by
radius preservation in the second.

## Scope

This is not a solution of Open Problem 5 for arbitrary incompressible Sobolev
homeomorphisms. The triangular approximants need not have the same image as
the original map; each is a diffeomorphism onto its own image. The radial
twist theorem does have a fixed source and target ball and preserves the
boundary trace.

A bounded search found no exact determinant-preserving strong Sobolev
approximation theorem for these two classes. Nearby literature gives uniform
volume-preserving approximation in a different high-dimensional setting
(arXiv:0901.1002) and general piecewise-affine strong approximation in
dimensions 3 and 4 without exact incompressibility (arXiv:2507.02854). Novelty
is therefore plausible but not certified; the elementary mechanism may be
folklore.

## Files

- `main.tex`, `solution_packet.pdf`: complete proof packet.
- `verification.md`: adversarial verifier report.
- `source_paper.pdf`: local copy of arXiv:2502.01336v1.
- `figures/open_problem_crop.png`: source evidence from PDF page 6.
- `code/check_jacobians.py`: symbolic sanity checks for both determinant
  mechanisms.
- `tmp/`: LaTeX build and rendered QA intermediates.

## Human review recommendation

Review as a likely valid structured partial result. Focus on the weighted
freezing/smoothing argument at the origin for radial twists, the `p=1`
density endpoint, and the specialist-literature novelty check.

Ledger:
`runs/fa_banach_001/ledger/results/2502.01336_incompressible_triangular_and_radial_twist_approximation.json`.
