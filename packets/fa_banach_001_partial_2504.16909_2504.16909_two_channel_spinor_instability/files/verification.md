# Verification Report

Candidate: arXiv:2504.16909, mixed-channel instability problem in Remark 26,
PDF page 30.

## Claim checked

The explicit two-channel instability theorem in `README.md` and `main.tex`.

## Verdict

Likely valid. This proves a genuine enlargement of the published
single-channel region but not the full optimal mixed-channel region.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Angular basis formulas | valid | Substitution into Appendix B gives the displayed formulas for `chi_1^(1/2)` and `chi_-2^(1/2)` with the probability surface measure. |
| Channel cancellation | valid | Weighting by `sqrt(2/3)` and `sqrt(1/3)` makes the upper coefficient `2/3+1/3=1` and the lower coefficient `sqrt(2)/3-sqrt(2)/3=0`. |
| Normalization and mean | valid | `sqrt(4 pi) Y_1^0` is real, normalized for probability surface measure, and has zero spherical mean. Thus the Hessian's positive rank-one term vanishes and `delta=1`. |
| Angular energy | valid | Orthogonality and the eigenvalues `1` and `-2` of `sigma dot L` give `(2/3)(3/2-alpha)^2+(1/3)(-3/2-alpha)^2=alpha^2-alpha+9/4=(1/2-alpha)^2+2`. |
| Radial reduction | valid | The baseline potential is `A` and the real-part term adds `(p-2)A`, so the total is `(p-1)A`; no cross term has been omitted. |
| Pöschl--Teller minimization | valid | Applying the source paper's scalar formula with `C=(p-1)A` and `B=(p-2)(1/2-alpha)/2` gives the stated closed energy. |
| Threshold algebra | valid | The energy's unique zero in `(2,6)` is `2 sqrt(1+2/(1/2-alpha)^2)`; the relevant square-root expression is strictly increasing for `p>2`. |
| Nonempty new interval | valid | The threshold is below `6` exactly because `1/2-alpha>1/2`, i.e. `alpha<0`. The source's Theorem 27 has no negative-alpha single-channel region when `alpha >= (1-sqrt(3))/4`. |
| Scope classification | valid | Independent channel profiles yield a noncommuting matrix Schrödinger operator, so the packet does not claim the optimal mixed-channel region. |

## Computational checks

Executed:

`conda run --no-capture-output -n sandbox python code/check_two_channel_instability.py`

The script checks the exact cancellation coefficients, verifies the threshold
identity on six alpha values, and tests four points at which the mixed energy
is negative while both constituent one-channel energies are positive. For
`alpha=-0.10`, `p=5.50`, it also integrates the explicit Pöschl--Teller ground
state on a 200,001-point grid. The numerical Rayleigh quotient agrees with
the closed energy to better than `2e-9`. These are sanity checks, not proof.

## Counterexample and failure-mode search

- Replacing probability surface measure by ordinary area measure was checked;
  the `sqrt(4 pi)` normalization cancels exactly, so `delta=1` is correct.
- The final positive Hessian rank-one term was checked separately. It vanishes
  because `Y_1^0` has zero spherical mean, not merely because the channels are
  orthogonal.
- The two channel eigenvalues have different squared angular masses for
  `alpha != 0`; therefore diagonalizing only the negative rank-one potential
  would be invalid. The packet does not make that false full-optimization step.
- At `alpha=0`, the threshold equals the excluded endpoint `p=6`, so the proof
  does not spuriously claim an open instability interval there.

## External dependencies

Only formulas explicitly proved in the source paper are used: the Hessian,
the spinor spherical harmonics, and the scalar Pöschl--Teller eigenvalue.

## Gaps

No proof gap was found in the scoped theorem. The principal uncertainty is
novelty rather than validity: the source's v2 added-in-proof footnote mentions
recent Esteban--Frank work suggesting the same qualitative phenomenon.

## Confidence

Score: 97/100 for mathematical validity; moderate novelty confidence.

## Human review recommendation

Send to a human. Verify the normalization/cancellation lines first, then the
one-line threshold algebra. Contact the source authors before an originality
claim because their cited recent work was not found as a separate public
paper in the bounded search.
