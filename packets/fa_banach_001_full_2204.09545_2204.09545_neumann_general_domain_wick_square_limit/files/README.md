# Neumann Wick-square convergence on every smooth planar domain

Status: candidate full answer, likely valid, awaiting specialist review.

Blömker and Tölle ask in Section 6 of arXiv:2204.09545 for the missing
general-domain estimate on the stochastic convolution square in their
two-dimensional Cahn--Hilliard/Allen--Cahn homotopy with Neumann boundary
conditions.

This packet proves it for every connected bounded smooth planar domain.  If
`L=-Delta_N`,

`B_epsilon=L(1-epsilon+epsilon L)`,

and the mean-zero stochastic convolution driven by space-time white noise has
amplitude `sigma_epsilon`, then

`sigma_epsilon^2 log(1/epsilon) -> kappa`

implies

`Z_epsilon^2 -> kappa/(8 pi)`

in every finite `L^p(0,T;H^{-1})`, in every sufficiently large finite
probability moment.  An explicit bound is

`O(|sigma_epsilon^2 log(1/epsilon)-kappa| + sigma_epsilon^2)`.

The proof uses the Neumann heat kernel twice: its diagonal isolates the
universal logarithm while confining the boundary correction to an
`L^2`-bounded layer, and its off-diagonal logarithmic Green bound controls the
centered Wick square by Wick's formula.

Contents:

- `main.tex` and `solution_packet.pdf`: expert-facing theorem and proof.
- `source_paper.pdf`: arXiv:2204.09545.
- `figures/open_problem_crop.png`: the complete source statement on PDF page
  18.
- `code/verify_square_spectral_constant.py`: independent square-domain
  spectral sanity check for the coefficient `1/(8 pi)`.
- `VERIFICATION.md`: proof, literature, source, and PDF QA record.

Scope is exact: smooth bounded planar domains, homogeneous Neumann boundary
conditions, and mean-zero space-time white noise.  The constant Neumann mode
is harmless and can be restored.  Nonsmooth domains and colored noise that
does not commute with the Neumann Laplacian are not claimed.
