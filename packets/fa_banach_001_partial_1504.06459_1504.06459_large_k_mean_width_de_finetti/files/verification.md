# Verification report

Verdict: candidate substantial partial result, likely valid pending expert
review.

## Formal checks

1. `Sep_d subset E_k(d)`, so the mean-width difference is nonnegative.
2. Quantitative finite de Finetti gives, uniformly in `rho in E_k(d)`, a
   separable `sigma` with unhalved trace norm at most `C d^2/k`; the trivial
   diameter bound gives `C min(1,d^2/k)`.
3. For every Hermitian `G`, Hölder duality yields
   `Tr(G(rho-sigma)) <= ||G||_infinity ||rho-sigma||_1`. Taking the supremum
   over `rho` is legitimate even though `sigma` depends on `rho`.
4. Averaging and dividing by `gamma(d^2)` gives the claimed width difference.
   Standard GUE estimates give
   `E||GUE(d^2)||_infinity / gamma(d^2) <= C/d`.
5. Aubrun--Szarek gives `c d^(-3/2) <= w(Sep_d) <= C d^(-3/2)`.
   Dividing the additive estimate by the lower bound gives the relative error
   `O(d^(5/2)/k)`.
6. Lancien's all-`k` lower bound gives
   `w(E_k)/w(Sep_d) >= c sqrt(d/k)`, proving divergence for `k=o(d)`.

## Convention check

Christandl--König--Mitchison--Renner use a trace-distance convention with a
factor `1/2`, while Lancien records an unhalved Schatten-1 estimate with an
explicit constant. The packet uses a universal constant `C_0`; no conclusion
depends on this factor.

## Upgrade and literature checks

Eight focused routes are recorded in
`attempts/1504.06459_growing_k_mean_width_upgrade_attempts.md`. In particular,
the stronger noisy-separability theorem for Bose-symmetric extensions was not
applied to Lancien's ordinary permutation-invariant hierarchy. The August 2026
argmax-rounding theorem (arXiv:2608.02590) was checked directly and does not
improve the one-sided endpoint exponent.

Cheap run indexes and bounded searches for the exact source wording, arXiv id,
title, author, `growing k`, `mean width`, `k-extendible`, and quantitative de
Finetti combinations found no explicit statement of the `d^(5/2)` sufficient
regime. Novelty confidence is modest because the proof is a short corollary of
known results.

## Highest-value human checks

- Confirm the precise finite de Finetti theorem used for an extension that is
  permutation-invariant relative to the retained `A` system.
- Confirm the GUE normalization in Lancien's definition of `gamma(d^2)`.
- Decide whether the result should be described as a new partial theorem or an
  unstated literature-implied corollary.
