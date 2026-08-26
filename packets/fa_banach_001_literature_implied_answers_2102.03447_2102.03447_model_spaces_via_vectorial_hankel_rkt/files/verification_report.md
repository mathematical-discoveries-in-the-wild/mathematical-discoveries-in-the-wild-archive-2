# Verification report

Verdict: `likely valid; full positive answer by a literature-implied operator identification`

## Source and theorem checks

- Dayan's Question 2.5 was checked in the local source and on PDF page 8.
- Treil's arXiv:1201.0063v2 was checked in source form and as a PDF.  Theorem
  1.1 explicitly allows a vectorial pre-Hankel operator from scalar `H^2` to
  `H^2_-(E)` and gives `||Gamma|| <= 2 sqrt(e) A` from normalized-kernel tests
  bounded by `A`.
- Dayan's bibliography was searched for `Treil`, `Bonsall`, and `Hankel`; none
  occurs.

## Proof-obligation audit

1. **The vector symbol is square-integrable.** At `z=0`, the hypothesis gives
   `sum_n (1-|Theta_n(0)|^2) < infinity`.  Since
   `P_- conjugate(Theta_n) = conjugate(Theta_n)-conjugate(Theta_n(0))`, its
   squared `L^2` norm is exactly `1-|Theta_n(0)|^2`.  Thus the assembled symbol
   lies in `H^2_-(ell^2)`.
2. **The operator is genuinely pre-Hankel.** Multiplication by a scalar
   polynomial followed by coordinatewise `P_-` has a Hankel matrix with
   entries in `ell^2`, precisely the setting of Treil's theorem.  Removing the
   constant Fourier coefficient of each conjugate inner function does not
   change `P_-(conjugate(Theta_n) f)` for analytic `f`.
3. **Model projections are the Hankel coordinates.** On the boundary,
   `Theta P_-(conjugate(Theta)f) = f-Theta P_+(conjugate(Theta)f)`, which is
   `P_{K_Theta}f`.  Multiplication by an inner function is an isometry, so the
   norms agree exactly.
4. **The kernel test is the displayed condition.** For normalized `k_z`,
   `||P_{K_Theta}k_z||^2 = 1-|Theta(z)|^2`.  Tonelli applies because every term
   is nonnegative.
5. **The constant is squared correctly.** Treil gives operator norm at most
   `2 sqrt(e) sqrt(C)`; squaring the analysis inequality gives Bessel bound
   `4 e C`.
6. **Passage from polynomials to all of `H^2`.** Treil supplies the bounded
   extension of the pre-Hankel operator; density and coordinatewise continuity
   preserve the projection identity.

No numerical or symbolic computation is used.  The recommended human review
focus is the convention for `P_-` (strictly negative frequencies) and the
componentwise projection identity; both were checked against Treil's notation.

