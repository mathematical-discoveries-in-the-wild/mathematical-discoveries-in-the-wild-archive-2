# Sharp interior power-zero threshold for free Poincare

Status: `candidate_partial_solution_likely_valid`

Source: Michel Ledoux and Ionel Popescu, *The One Dimensional Free Poincare
Inequality*, arXiv:1105.2031, Remark 2 (PDF page 15).

## Result

Let `mu = w alpha`, where `alpha` is the semicircle law on `[-2,2]`. Two
results are proved.

1. If `W(theta) = w(2 cos(theta))` and `1/W` belongs to `L^r(0,pi)` for some
   `r>1`, then `mu` satisfies `P(rho)` for some `rho>0`. No continuity or
   differentiability of `w` is assumed.
2. If `w` is bounded above and below away from finitely many interior points
   and is comparable to `|x-a_j|^(gamma_j)` at those points, then `P(rho)`
   holds for some positive `rho` if and only if every `gamma_j<1`.

Thus the exact one-zero family proportional to `|x-a|^gamma` satisfies the
free Poincare inequality exactly for `gamma<1`. The continuous density with a
linear zero (`gamma=1`) shows that merely dropping the `C^2` hypothesis does
not preserve the inequality automatically. Conversely, sublinear zeros show
that positivity everywhere is not necessary once `C^2` is removed.

## Proof mechanism

After `x=2 cos(theta)`, the source Chebyshev identities realize the free
energy as the weighted sine coefficient sum `sum n|b_n|^2`. Hausdorff--Young
and a weighted sequence estimate control every finite `L^p` norm of the sine
series, which combines with `1/W in L^r` and weighted Cauchy--Schwarz.

For a zero of order greater than one, a compressed step has weighted
Dirichlet energy `O(epsilon^(gamma-1))`. At order one, a logarithmic profile
has energy `O(1/log(1/epsilon))`. The source bound
`Q(f) >= (1/2) Var_beta(f)` prevents the free energy of these step-like tests
from vanishing.

## Scope and novelty

This is a full theorem for the stated finite power-law class, but only a
substantial partial answer to the source's broad regularity question. It does
not characterize arbitrary rough or oscillatory densities, endpoint zeros,
singular components, or multi-interval supports.

A bounded search used the exact source question and close combinations of
`free Poincare`, `density regularity`, `power weight`, `semicircle`,
`fractional Hardy`, and `interior zero`. It also inspected arXiv:1311.4585,
which studies higher-order and Brascamp--Lieb refinements. No statement of the
criterion or threshold above was found. Novelty is therefore plausible but
not certified.

## Packet contents

- `main.tex`, `solution_packet.pdf`: theorem and complete proof.
- `source_paper.pdf`: arXiv:1105.2031.
- `figures/open_problem_crop.png`: source Remark 2.
- `VERIFICATION.md`: mathematical and rendering checks.

Human review should focus on the Chebyshev normalization, the finite-`p`
sine-series estimate, and smoothing of the borderline logarithmic profile.
