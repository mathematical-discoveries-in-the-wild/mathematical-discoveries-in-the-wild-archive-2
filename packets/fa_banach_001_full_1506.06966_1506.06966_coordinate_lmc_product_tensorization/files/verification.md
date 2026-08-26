# Verification Report

Candidate: arXiv:1506.06966 coordinate-LMC complexity conjecture

## Claim Checked

Under the intended strong-convexity sign in Proposition 12, its exact
random-coordinate Rademacher chain reaches Wasserstein error `epsilon` using
step size `h` proportional to `epsilon^2/d` and
`O(epsilon^-2 d^2 log(d/epsilon))` scalar-coordinate updates.

## Verdict

**Likely valid.** Recommended for human review as a candidate full solution.

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Interpret the printed monotonicity sign as strong convexity | valid with explicit source caveat | The printed sign contradicts both the Gaussian clause and the inequalities used in the proof of Proposition 12. |
| Coordinate Lipschitz assumption forces separability | valid | Setting `x_i=y_i` forces `partial_i u(x)=partial_i u(y)`; integrating the coordinate derivatives gives `u=c+sum u_i`. |
| Target and discrete invariant laws are products | valid | The target factorization is immediate. Each one-dimensional invariant law is preserved by its coordinate kernel, so their product is invariant for every coordinate update. |
| One-dimensional stationary bias is `O(sqrt(h))` | external, verified in source | The proof of Proposition 12 obtains `W2(pi_h,mu) <= C d^(3/2) sqrt(h)`; at `d=1` this is the needed estimate, with `C` depending only on the common `rho,L`. |
| Bias tensorizes to `O(sqrt(d h))` | valid | Quadratic cost is additive, and product optimal couplings give equality of squared product distance with the sum of coordinate squared distances. |
| Random-scan mixing rate is `exp(-c h n/d)` | valid | Synchronous use of the selected coordinate and Rademacher sign gives squared contraction factor `1-(2 rho h-L^2 h^2)/d`. |
| Initial distance is `O(sqrt(d))` | valid | The stationary second-moment identity gives `(2 rho-L^2 h) E X_i^2 <= 2` coordinatewise. |
| Final parameter choice | valid | `h=a epsilon^2/d` makes the bias at most `epsilon/4`; `n >= 2d/(rho h) log(C sqrt(d)/epsilon)` makes mixing at most `epsilon/2`. |

## Counterexample Search

Small structural cases checked analytically:

- `d=1` reduces exactly to the source's proved bias estimate.
- Quadratic product potentials produce independent affine Bernoulli
  convolutions; the product and contraction calculations agree exactly.
- A genuinely interacting potential cannot satisfy the source's all-pairs
  coordinate Lipschitz hypothesis, because changing another coordinate while
  fixing `x_i` would have to leave `partial_i u` unchanged.

No counterexample was found.

## External Dependencies

- Thomas Bonis, arXiv:1506.06966v6, proof of Proposition 12: the
  one-dimensional stationary-bias estimate. Verified from the local source TeX
  and source PDF pages 46--47.
- No theorem from the later random-coordinate LMC literature is used in the
  proof.

## Residual Risks

- The result resolves the intended nonvacuous statement, not the literally
  printed negative-sign inequality. The packet must not hide this source typo.
- The bounded novelty search may have missed a later paper that notes the same
  product reduction.
- The source's bias theorem is taken as established; this packet does not
  reprove its Stein-method estimate.
- The promoted theorem retains the source's smooth-density hypothesis; it does
  not claim the elementary product argument extends the Stein estimate to
  merely `C^1` potentials.

## Confidence

Score: **92/100**.

The argument after the source's dimension-one estimate is elementary and all
dimension factors are explicit. Remaining uncertainty is primarily literature
novelty and human confirmation of the evident sign correction.

## Human Review Recommendation

Send to human review, focusing on the sign interpretation and on whether the
source's constant in the dimension-one bias estimate depends only on the
common `rho,L` parameters.
