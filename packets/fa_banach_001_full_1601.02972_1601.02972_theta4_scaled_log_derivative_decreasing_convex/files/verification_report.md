# Verification report

## Verdict

Likely valid full positive solution to the precise stronger theta-function
assertion on source PDF page 3 of arXiv:1601.02972. Human review is recommended
before dissemination.

## Claim audited

For `theta_4(s)=sum_{k in Z}(-1)^k exp(-pi k^2 s)`, the function
`H(s)=s^2 theta_4'(s)/theta_4(s)` is strictly decreasing and strictly convex
for every `s>0`.

## Adversarial checks

1. **Positivity and smoothness.** Jacobi's product shows `theta_4(s)>0` for
   `s>0`, so its logarithmic derivative is defined. All product and geometric
   series used in the proof, together with every fixed finite number of
   derivatives, converge locally uniformly on `(0,infinity)`.

2. **Large-parameter product coefficients.** Differentiating
   `prod_n (1-e^{-2 pi n s})(1-e^{-(2n-1)pi s})^2` gives exactly
   `2 pi n/(e^{2 pi n s}-1)` and
   `2 pi(2n-1)/(e^{(2n-1)pi s}-1)`. Multiplication by `s^2` converts each into
   a positive multiple of `phi(c s)= (c s)^2/(e^{c s}-1)`.

3. **The threshold for the elementary kernel is sufficient.** The derivative
   of `phi` is negative for `x>2`. Its second derivative has numerator
   `N=(x^2-4x+2)e^{2x}+(x^2+4x-4)e^x+2`. Symbolic differentiation gives
   `N'=x e^x((2x-6)e^x+x+6)`, hence `N` increases for `x>=pi`. The packet's
   rational bounds prove `N(pi)>0`, so no numerical root assumption is hidden.

4. **Modular transformation signs.** From
   `theta_4(s)=s^{-1/2}theta_2(1/s)` and the product for `theta_2`, direct
   logarithmic differentiation gives
   `H=pi/4-s/2+2pi sum_n n[2/(E+1)-1/(E-1)]`, with
   `E=e^{2pi n/s}`. The bracket is `(E-3)/(E^2-1)`, whose geometric expansion
   has coefficients `+1,-3,+1,-3,...`. This confirms the crucial factor `3`.

5. **Every paired correction has the asserted signs.** The displayed formulas
   for `P'` and `P''` were independently differentiated. On `s<=1`, the ratios
   satisfy `D/C<=2`, `D-C>=2pi`, and
   `D(D-2s)/(C(C-2s))<5`. Since `e^{-2pi}<1/500`, the two residual brackets are
   bounded below by `1-6/500` and `1-15/500`, respectively.

6. **The global slope bound retains all outer factors.** Dropping the negative
   exponential from `R'` yields the prefactor `4 pi^2`, the outer weight `n^2`,
   and the odd-index weight `2j+1`. Enlarging odd indices to all positive
   indices gives `q^n/(1-q^n)^2`. The identity
   `sum n^2 q^n=q(1+q)/(1-q)^3` then gives exactly the fifth power of `1-q` in
   the denominator. The coarse final bound is `0.32`, safely below `1/2`.

7. **The join at `s=1` is covered.** The small-parameter proof is valid through
   `s=1`, while the product proof begins at `s=1`; both give strict signs there.
   No gluing argument or one-sided derivative assumption is needed because
   `H` is analytic.

8. **The conclusion is genuinely strict.** For `s>=1`, every term has negative
   first derivative and positive second derivative. For `s<=1`, the correction
   has positive curvature and slope below `1/2`. Thus the proof establishes
   strict decrease and strict convexity, stronger than weak monotonicity and
   convexity.

## Independent computational smoke test

`code/verify_numerics.py` evaluates the two stable analytic expansions at 121
logarithmically spaced points from `10^-3` to `10^3` at 60 decimal digits and
checks `H'<0`, `H''>0`. It also checks the symbolic numerator identities used
for `phi''`, `P'`, and `P''`. This is supporting QA, not a substitute for the
analytic proof.

## Literature and novelty check

The run indexes contained no entry for arXiv:1601.02972. On 11 August 2026,
targeted arXiv searches for the exact expressions involving
`s^2 theta_4'(s)/theta_4(s)`, decreasingness, and convexity returned the source
paper but no later primary-source proof. The headline hexagonal-lattice
conjecture is separately recorded in this run as a flagship open problem; this
packet deliberately makes no claim about it. Novelty is provisional.

## Recommended verifier focus

Check the modular-expansion line and the uniform `R'<1/2` estimate. Once those
two calculations are confirmed, the remainder is a direct sign argument.

