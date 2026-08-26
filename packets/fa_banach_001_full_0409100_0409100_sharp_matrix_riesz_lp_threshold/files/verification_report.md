# Verification report

Candidate: arXiv:math/0409100 matrix Riesz-potential threshold

## Verdict

**Likely valid candidate full proof.**  The Gaussian smoothing estimate gives
the improved sufficient range, and dyadic rank-one tubes give matching
counterexamples including the endpoint.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Source extraction | verified | PDF page 9 asks whether `p<n/(Re alpha+m-1)` is necessary for `m>1`. |
| Heat/beta reduction | valid | Inversion `r=t^{-1}` gives beta parameters `(n-a)/2` and `a/2`. |
| Gaussian smoothing | likely valid | Schur-complement induction gives one factor `(1+s_j^2)^(-(n-a)/2)` per singular direction; integral Wallach orders use the Stiefel boundary form. |
| Integrability threshold | valid | Matrix beta integral is finite iff `(n-a)q>n+m-1`; the largest-eigenvalue sector is the critical one. |
| Hölder/Tonelli step | valid | A finite Gaussian-weighted integral and strict positivity of the Gaussian imply a.e. finiteness. |
| Rank-one tube volume | valid | A dyadic unit tube around the rank-one stratum has volume comparable to `R^(n+m-1)`. |
| Continuous-order lower bound | valid | On the tube the determinant is at most `C R`, so the negative determinant power is at least `c R^{-(n-a)}`. |
| Integral-order lower bound | valid | The rank-`k` representation contributes a matrix sector of measure `R^(k+m-1)`. |
| Endpoint sequence | valid | `a_j=R_j^{-(a+m-1)}/j` is in `L^{p_c}` and produces a harmonic-series divergence on a ball. |

## Adversarial checks

- The exponent is controlled by the rank-one stratum, not the generic
  full-rank radial scaling.
- The proof establishes absolute convergence, so it also covers nonreal
  orders through the real part of the exponent.
- The zero order is excluded from the sharp-threshold statement because
  `I^0` is the identity.
- The source's old range is nonempty only in the regime addressed by the
  theorem; no claim is needed at pole orders.
- The divergence examples fail on a whole ball, not merely at one point.

## Recommended human review

Expand the Schur-complement induction in the Gaussian smoothing lemma into a
standalone lemma, with special attention to the singular matrix-beta measure
for integral Wallach orders.  The threshold algebra and the counterexample
are elementary once that estimate is accepted.
