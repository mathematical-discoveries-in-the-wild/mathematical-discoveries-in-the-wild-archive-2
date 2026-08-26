# Verification Report

Candidate: Appendix C stability conjecture in arXiv:2110.06008.

## Verdict

`likely valid`

Confidence: 94/100.

## Step audit

| Step | Status | Notes |
| --- | --- | --- |
| Selector is defined on all of `D_+` | valid | `0<=x<=1/2`, `y>0`; the formula is smooth. |
| Line condition | valid | `z1+x z2=1/2` holds by definition. |
| Monotonicity | valid | With `G=4x(1-x)`, `partial_x z2=-(100/(8y^2))G^99 4(1-2x)<=0`. |
| Hexagonal-boundary condition | valid | At `x=1/2`, `G=1`, giving exactly the circumcenter coordinates. |
| Rectangular-boundary condition | valid | At `x=0`, `z=(1/2,1/2)`, satisfying either the natural scalar reading for `z2` or the coordinatewise reading of the source's dimensionally ambiguous interval condition. |
| Convergence to the deep hole | valid | Continuity gives `z -> (1/3,1/3)` as `(x,y)->(1/2,sqrt(3)/2)`. |
| Extra boundary criticality | valid | `G'(1/2)=0`, so `partial_x z2=0` at `x=1/2`. |
| Test lattice lies in `D_+` | valid | `(9/20)^2+(sqrt(319)/20)^2=1`. |
| Candidate theta lower bound | valid | The 25 terms with `-2<=k,l<=2` are positive terms of the full sum. |
| Hexagonal tail majorant | valid | The quadratic form dominates `(u^2+v^2)/sqrt(3)`; a union bound separates the complement of the square into two one-dimensional tails. |
| One-dimensional tail bound | valid | Both half-tails are dominated by a geometric series whose first term is `exp[-c(N+2/3)^2]` and whose ratio is at most `exp[-c(2N+7/3)]`. |
| Directed interval result | valid | At 60 decimal digits, the lower enclosure for the reversed gap is greater than `0.00384725734969546`. |

## Adversarial checks

- The proof never truncates the candidate sum from above; its finite square is
  used only as a lower bound.
- The hexagonal tail is bounded over the entire complement, including the
  overlap of the two coordinate tails; the union bound merely overcounts.
- The strict inequality is at `alpha=1`, so a single certified point suffices
  to refute a claim asserted for every positive `alpha` and all admissible
  selectors.
- The construction is not exploiting the boundary point `Lambda=Lambda_2`:
  the test lattice has `x=0.45` and is nonhexagonal.
- The counterexample survives the possible additional hypothesis mentioned
  immediately after the conjecture, namely boundary criticality of the
  selector in the `x` direction.
- Strictness and local uniform convergence imply an open neighborhood of
  counterexample parameters; this is not an isolated equality-rounding issue.

## Reproduction

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2110.06008_stability_selector_counterexample/code/check_counterexample.py
```

The checker contains no random choices and asserts positivity of the lower
endpoint of the interval gap.

## Novelty caution

A bounded search covered the four cheap run indexes and web searches combining
the paper title/arXiv id with `stability conjecture`, `widetilde z`, and
`counterexample`.  It found later work on stable cold spots that cites the
source theorem but no resolution of this Appendix selector conjecture.  This
supports, but cannot certify, novelty.

## Human review recommendation

Verify the interpretation of the source's final displayed boundary condition,
which writes a vector-valued selector as belonging to a scalar interval.  The
constructed endpoint `(1/2,1/2)` satisfies both plausible interpretations, so
this ambiguity does not appear to affect the result.  Then audit the short
Gaussian tail estimate and interval implementation.

