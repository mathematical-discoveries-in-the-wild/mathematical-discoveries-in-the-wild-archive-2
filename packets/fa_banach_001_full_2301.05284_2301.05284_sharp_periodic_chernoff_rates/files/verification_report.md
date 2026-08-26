# Verification report

## Verdict

Likely valid sharp full result for the periodic family studied numerically in
arXiv:2301.05284. Human review is recommended before dissemination.

## Claim audited

For every fixed `t>0` and `f_xi(x)=|sin x|^xi`, the source's first-order
scheme `G` has uniform error
`Theta(n^{-min(1,(xi+1)/2)})`. Its second-order scheme `S` has error
`Theta(n^{-min(2,(xi+1)/2)})`, except at `xi=2`, where it is
`Theta(n^{-2})` because the Fourier series terminates.

## Adversarial checks

1. **Fourier normalization.** For the period-pi expansion
   `f=a_0/2+sum a_k cos(2kx)`, beta integration gives exactly the coefficient
   formula displayed in the packet. Direct 60-digit quadrature agrees for six
   representative exponents and the first five nonconstant modes.

2. **Tail exponent and exceptional set.** Reflection gives
   `a_k = -c_xi Gamma(k-xi/2)/Gamma(k+xi/2+1)`, hence
   `|a_k| asymp k^{-xi-1}` whenever `sin(pi xi/2)` is nonzero. At positive even
   integers the original gamma formula instead terminates, as required. The
   only even integer for which the generic `S` exponent would be below 2 is
   `xi=2`, explaining the theorem's single exception.

3. **Multiplier formulas.** Applying either three-point operator to
   `cos(2kx)` gives exactly
   `cos(2k sqrt(t/n))^(2n)` for `G` and
   `[2/3+(1/3)cos(2k sqrt(6t/n))]^n` for `S`. The heat multiplier is
   `exp(-4tk^2)`.

4. **Low-frequency orders and signs.** Symbolic logarithmic series give
   `2 log cos z=-z^2-z^4/6+O(z^6)` and
   `log[2/3+(1/3)cos(sqrt(6a))]=-a+a^3/15+O(a^4)`. At `k=1` these yield the
   nonzero constants `-(8/3)t^2 exp(-4t)/n` and
   `(64/15)t^3 exp(-4t)/n^2`. Direct high-precision evaluations converge to
   both constants.

5. **Revival locations.** The first positive maxima occur at
   `pi sqrt(n)/(2 sqrt(t))` for `G` and
   `pi sqrt(n)/sqrt(6t)` for `S`. Rounding to an integer incurs phase error
   `O(n^-1/2)`, so the nth power remains bounded below by a positive constant.
   The heat multiplier there is exponentially small in `n`.

6. **Why one Fourier coefficient is enough for the lower bound.** A cosine
   coefficient of a pi-periodic continuous error is at most twice its uniform
   norm. Thus the fixed first mode gives the tangency-order lower bound, while
   the rounded first revival gives the `n^{-(xi+1)/2}` lower bound. No
   cancellation among modes can invalidate either estimate.

7. **All revivals are included in the upper bound.** Away from the central
   cell, each multiplier is bounded by a Gaussian in the distance to its
   `sqrt(n)`-spaced revival lattice. A cell has uniformly bounded Gaussian
   mass; weighting its center by `k^{-xi-1}` gives
   `n^{-(xi+1)/2} ell^{-xi-1}`. The sum over `ell` converges because `xi>0`.

8. **Central cell does not hide a worse term.** On a fixed small phase
   neighborhood, analytic logarithmic expansion gives a polynomial times
   `exp(-c k^2)`, summable uniformly after extracting `n^-1` or `n^-2`. The
   remainder of the central cell is exponentially small in `n`.

9. **Fixed time and uniform norm.** All constants may depend on the fixed
   `t>0`, exactly as stated. The proof is for the true supremum on the whole
   line (equivalently one period), not the source's 1000-point grid surrogate.

10. **Interpretive claims are kept separate.** The theorem proves the exact
    envelope orders. Moving revival centers explain a plausible oscillation
    mechanism, but the packet does not claim a limit or prove oscillations of
    the normalized error.

## Independent executable QA

`code/verify_formulas.py` checks the two symbolic multiplier expansions,
Fourier coefficient formula, gamma-ratio tail, fixed-mode leading constants,
and positive first-revival bounds. It is supporting QA, not a substitute for
the analytic argument.

The four-page packet compiled twice with no LaTeX, reference, overfull, or
underfull warnings. Every rendered page and the source-question crop were
visually inspected at readable resolution; no clipping, overlap, or malformed
formula remains.

## Literature and novelty check

The four run indexes had no entry for arXiv:2301.05284. Targeted arXiv searches
for these exact schemes, `|sin x|^xi`, and sharp nonsmooth heat-semigroup rates
found the source and adjacent general Chernoff-rate papers, but no matching
primary-source theorem. The source archive is a late-2025 revision and still
labels the numerical effects theoretically unexplained. Novelty remains
provisional.

## Recommended verifier focus

Check the weighted revival lemma's partition into the central cell and the
`sqrt(n)`-spaced noncentral cells. Once that estimate is accepted, both sharp
lower bounds are immediate from individual Fourier coefficients.
