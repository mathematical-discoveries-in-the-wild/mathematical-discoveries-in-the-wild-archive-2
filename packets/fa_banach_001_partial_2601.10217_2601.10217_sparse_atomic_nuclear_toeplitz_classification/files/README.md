# Sparse atomic nuclear Toeplitz operators: exact classification

**Status:** candidate substantial partial result, likely valid.

**Source:** Tengfei Ma, Yufeng Lu, and Chao Zu, *Nuclear Toeplitz
Operators between Fock Spaces*, arXiv:2601.10217, Question 3.8 (PDF p. 15).

For `1 <= p < q <= infinity`, set

`1/s = 1 - 1/p + 1/q`.

The packet completely answers Question 3.8 for positive measures supported on
an explicit sufficiently sparse sequence.  If `z_j=jR`, with
`R > sqrt(2 log(3)/alpha)`, and

`mu = sum_j c_j delta_{z_j}`, `c_j >= 0`,

then

`T_mu:F_alpha^p -> F_alpha^q` is nuclear exactly when `c in ell^s`.

At the endpoint `(p,q)=(1,infinity)`, `ell^infinity` is replaced by `c_0`.
The proof factors `T_mu` through the diagonal operator
`D_c:ell^p->ell^q`; the Fock analysis and synthesis maps have bounded one-sided
inverses because the Gaussian Gram matrix is strictly diagonally dominant.
Tong's exact diagonal nuclearity theorem then gives both directions.

This yields explicit positive infinite-mass nuclear Toeplitz symbols.  For
finite `s`, take `c_j=j^{-a}` with `1/s<a<=1`; at the endpoint take `c_j=1/j`.
Thus the finite-total-mass condition from the range `q<=p` cannot be the answer
when `p<q`.

## Contents

- `solution_packet.pdf`: expert-facing proof packet.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: Question 3.8 on source PDF p. 15.
- `tmp/`: build and rendering intermediates.

## Verification

The factorization constants were checked directly:

`T_mu = (alpha/pi) S_q D_c A_p`,

`D_c = (pi/alpha) L_q T_mu R_p`.

For the sequence `jR`, `A_t S_t` has matrix
`exp(-alpha R^2(i-j)^2/2)`.  Its off-diagonal row and column sums are bounded by
`2 exp(-u)/(1-exp(-u))<1`, where `u=alpha R^2/2>log 3`; hence it is invertible
on every `ell^t`, including both endpoints.  The defining measure-integrability
condition follows from Gaussian decay and boundedness of `c`.  No computation
is used.

## Scope and novelty

The result is exact for the sparse atomic class and extends to any kernel
sequence with the same complemented `ell^t` property.  It does not classify
arbitrary non-atomic or densely supported measures: the unresolved issue is how
to combine infinite-rank local cell operators with an `ell^s`, rather than
`ell^1`, nuclear bound.

On 2026-08-11, local run indexes and web searches for the exact question,
positive Fock measures, nuclear Toeplitz maps, and the `p<q` range found the
source paper and its July 2026 accepted-manuscript publication, but no later
answer.  The published page listed no citing paper.  Tong's classical diagonal
theorem is prior background.  Novelty confidence is moderate-high for the Fock
reduction and infinite-mass consequence.

## Human-review recommendation

Verify the endpoint form of Tong's theorem (`c_0` for `ell^1 -> ell^infinity`)
and the normalization constant in the Toeplitz factorization.  The Fock
analysis/synthesis and Gram-inverse estimates are written out in the packet.
