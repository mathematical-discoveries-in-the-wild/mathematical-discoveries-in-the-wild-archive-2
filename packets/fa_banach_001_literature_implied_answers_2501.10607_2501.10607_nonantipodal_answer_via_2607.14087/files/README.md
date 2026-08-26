# Full Literature-Implied Answer: Antipodality Is Unnecessary

## Outcome

`literature_implied_answer (full non-antipodal extension)`

Let `U_N(d)` be the largest fraction of `S^{d-1}` covered by `N` arbitrarily centered geodesic caps, each of normalized area `1/N`. If `N=N(d) -> infinity` and `log N=o(sqrt d)`, then

`U_N(d) -> 1-e^{-1}`.

This completely removes the antipodality assumption from Theorem 1 of Hoehner--Kur, arXiv:2501.10607, without changing its asymptotic regime.

## Why this is literature-implied

The decisive comparison is Theorem 2.1 of Abhijeet Mulgund, *Stochastic Domination of Gaussian Maxima: A Resolution of the Weak Simplex Conjecture*, arXiv:2607.14087. The supporting theorem is later literature; the present packet identifies and proves its implication for the source open problem. Targeted searches found no explicit public linkage between the two papers.

## Proof skeleton

1. The source proof supplies a trimmed threshold `u` with `N barPhi(u) -> 1` and shows uniformly for each cap cone `A(x)` and halfspace `H(x)={y:<y,x>>=u}` that `gamma(A(x) Delta H(x))=o(1/N)`.
2. For arbitrary centers, summing these errors reduces the union measure to `P(max_i xi_i >= u)`, where the covariance of `xi` is the centers' Gram matrix `G`.
3. Normalize `R=((N-1)/N)G+J/N`. Then `R-J/N` is positive semidefinite, so Mulgund gives a lower bound by the independent Gaussian lower orthant.
4. Realize the normalized vector as `X_i=sqrt((N-1)/N) xi_i+W/sqrt N`. The common noise changes the extreme-value threshold by `o(1/u)`, yielding `P(max_i xi_i<=u)>=e^{-1}-o(1)`.
5. Independent random cap centers have expected covered fraction `1-(1-1/N)^N`, supplying the matching lower bound.

## Scope

- Fully answers the non-antipodal question in the source regime.
- Does not treat `log N=Omega(sqrt d)`.
- Does not resolve monotonicity of `V_N(d)` or the Laguerre--Dirichlet--Voronoi constant conjecture.
- Requires human review before any external claim of novelty.

## Files

- `main.tex`: proof-complete source.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: arXiv:2501.10607.
- `supporting_paper_2607.14087.pdf`: later Gaussian-maxima theorem.
- `figures/open_problem_crop.png`: page-2 source excerpt locating the open direction.

