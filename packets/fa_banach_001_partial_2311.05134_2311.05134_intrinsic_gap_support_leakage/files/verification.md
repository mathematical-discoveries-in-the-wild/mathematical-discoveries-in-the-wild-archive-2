# Verification report

Status: `candidate partial result, likely valid`  
Date: 2026-08-11  
Verifier: `agent_lane_12`, model `GPT5.6`

## Checked claims

1. **Quantile embedding.** For `Q_mu(theta,s)` the quantile of the projection
   `R_theta mu`, the standard one-dimensional identity gives
   `||Q_mu-Q_nu||_L2 = SW(mu,nu)`.

2. **Support box.** If `mu` is supported in the unit ball, every projected
   quantile lies in `[-1,1]`. Conversely, zero leakage implies unit-ball
   support: every point `x` with `|x|>1` has a positive-measure open set of
   directions satisfying `|theta dot x|>1`; Tonelli then excludes positive
   mass outside the ball.

3. **Distance to the box.** The nearest point in the closed convex box
   `C={q: |q|<=1 a.e.}` is pointwise clipping. Hence its squared distance from
   `Q_mu` is exactly the stated average of `(|r|-1)_+^2`.

4. **Hilbert projection inequality.** If `x,y` lie in a closed convex set `C`,
   `z` is arbitrary, `D=|x-y|`, and `r=dist(z,C)`, then
   `|z-x|+|z-y| >= sqrt(D^2+4r^2)`. For `p=P_C z`, the projection inequality
   makes both squared distances at least `r^2+|p-x_i|^2`; convexity of
   `u -> sqrt(r^2+u^2)` and the triangle inequality finish the estimate.

5. **Use of intrinsic geodesicity.** A constant-speed `ell_SW` geodesic has
   sublengths `tL` and `(1-t)L`. Since `SW<=ell_SW`, its two ambient Hilbert
   chord lengths sum to at most `L`, yielding
   `Leak(mu_t)<=sqrt(L^2-D^2)/2`. Comparing to either endpoint separately
   also gives the two `t`-dependent bounds.

6. **Equality subclasses.** For a Dirac endpoint, common-line supports, or a
   positive homothety, one-dimensional monotonicity and spherical averaging
   give `SW=W/sqrt(d)`. The standard comparison
   `SW<=ell_SW<=W/sqrt(d)` forces `ell_SW=SW`.

## Stress checks and limitations

- The estimate is sharp as a Hilbert-space statement; no unjustified claim is
  made that the clipped quantile family is Radon-consistent.
- The theorem controls integrated leakage, not the essential support radius
  when a very small amount of mass escapes far from the ball.
- The general open question is not resolved when `ell_SW>SW`.
- No numerical computation is used as a proof step.

Verdict: the partial theorem is internally consistent and ready for expert
review. The primary novelty-sensitive point is literature status, not the
proof itself.

