# Harmonic-Near-Symmetric Order Obstruction at the Critical Sobolev Index

Source paper: S. Ivanov and N. Kalton, *Interpolation of subspaces and
applications to exponential bases in Sobolev spaces*, arXiv:math/0104130.

Status: likely valid partial result. The packet proves a negative theorem for
the standard lattice at the critical index `s=1/2`. It does not settle the
source question for arbitrary highly nonlocal permutations or for general
frequency sets.

## Result

Let `pi` enumerate the integers and let `A_k` be the set of frequencies in
its first `k` terms. If some prefixes approach symmetric intervals in the
critical harmonic metric,

```text
sum_{0 != n in A_{k_j} symmetric_difference [-N_j,N_j]} 1/|n| -> 0,
```

then the ordered exponentials cannot be a Schauder basis of
`H^(1/2)(-pi,pi)`. This rules out the symmetric order and every bounded- or
sublinear-positional-displacement perturbation of it.

The proof tests the prefix projections on the smooth function `f(x)=x`.
Symmetric Fourier sums develop a nonconstant boundary profile at spatial
scale `1/N`, producing a fixed positive Slobodeckij defect. Harmonic-nearby
frequency sets differ by a perturbation tending to zero in `H^(1/2)`.

## Files

- `main.tex`: full proof and precise scope.
- `solution_packet.pdf`: rendered solution packet.
- `source_paper.pdf`: local copy of arXiv:math/0104130.
- `figures/open_problem_crop.png`: source-paper crop containing the question.
- `code/verify_boundary_profile.py`: numerical consistency check for the
  boundary profile and its separation.
- `verification.md`: reproducibility and visual-QA record.

## Human Review Recommendation

Check the boundary rescaling in the Slobodeckij seminorm and the comparison
between the interval norm and the periodic Fourier norm. The result should be
reviewed as a substantial ordering-sensitive obstruction, not as a solution
of the arbitrary-order existence question.
