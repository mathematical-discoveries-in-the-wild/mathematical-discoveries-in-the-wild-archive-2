# Verification Report

Candidate: arXiv:2509.20849, locally length Baire-envelope extension and
inverse-problem obstructions

## Claims checked

1. Local asymptotic `C`-quasiconvexity implies
   `LLip f(x) <= C (lip f)^vee(x)` for metric-valued maps.
2. Locally length domains satisfy
   `(lip f)^vee=(Lip f)^vee=LLip f`.
3. The triple `1_{0},1_{0},1_{0}` on an interval satisfies the source's
   necessary conditions but is not realizable.
4. The tangential double arc gives a compact connected domain where the two
   pointwise Baire envelopes are zero at the origin and `LLip f=1`.

## Verdict

`likely valid` (substantial partial result)

## Adversarial step check

| Step | Status | Notes |
| --- | --- | --- |
| Source scope | valid | The Introduction explicitly asks which triples are realizable and calls the Baire-envelope identity a necessary criterion. Theorem 7.1 restricts it to locally convex normed domains and real-valued maps. |
| Curve composition | valid | An arc-length parametrization is 1-Lipschitz, so the radius-`r` oscillation of `f o c` is bounded by the ambient radius-`r` oscillation of `f`. Taking lower limits preserves the inequality. |
| Metric codomain | valid | For fixed `q`, `t -> d_Y(g(t),q)` is real-valued and has little lip no larger than that of `g`. The real interval theorem applied with `q=g(s)` recovers the full metric distance. |
| Curve integration | valid by source plus scalarization | Source Theorem 6.4 gives the interval local-to-global result. The scalarization closes the mismatch between its real-valued ingredient and metric-valued statement. |
| Quantitative bound | valid | Choose a neighborhood on which `lip f<gamma`, then a smaller neighborhood with `(C+eta)`-short joining curves staying inside it. Curve integration makes `f` locally `(C+eta)gamma`-Lipschitz. Passing `gamma` and `eta` down gives the claim. |
| Locally length reduction | valid | A small inner ball inside a length-space neighborhood has nearly shortest curves between still smaller points. A curve with length at most `1.25 d(y,z)` cannot leave the containing ball by the triangle inequality. Letting the excess tend to zero yields `C=1`. |
| Lower Baire chain | valid | Pointwise `lip<=Lip<=LLip`; monotonicity of upper envelopes and upper semicontinuity of `LLip` give `(lip)^vee<=(Lip)^vee<=LLip`. |
| Singleton regularity | valid | `{0}` is closed and `F_sigma`; its complement is open and hence `F_sigma` in the interval. This verifies the source's `F_sigma`-lower/upper definitions. The indicator is upper semicontinuous and equals its upper Baire envelope. |
| Singleton nonrealizability | valid | `lip f<=1` makes `f` Lipschitz by source Theorem 6.4. Rademacher plus source Theorem 3.2 gives derivative zero almost everywhere off one point, so absolute continuity makes `f` constant. |
| Double-arc pointwise derivatives | valid | At the origin the radial quotient is `t^alpha/sqrt(t^2+t^(2alpha)) -> 0`. Away from the origin each branch is smooth and the normalized vertical tangent has the displayed magnitude tending to zero. |
| Double-arc local derivative | valid | Opposite points have vertical difference and Euclidean distance both `2t^alpha`, giving quotient one. Coordinate projection is globally 1-Lipschitz, so the local derivative is exactly one. |
| Path-distortion explanation | valid | The branches intersect only at the origin. Every joining path passes through it and has length at least `2t`, while the cross chord is `2t^alpha`, so the ratio diverges for `alpha>1`. |

## Computational verification

`code/verify_double_arc.py` checks the radial quotient, exact tangent slope,
cross-branch quotient, and path/chord lower bound for `alpha=1.5,2,3` down to
`t=1e-9`.  It also independently compares the tangent formula with centered
finite differences at three nonzero parameters.  All checks passed; the
largest finite-difference error was below `2.6e-11`.

## Counterexample / loophole search

- A snowflaked line does not by itself produce the required strict Baire gap;
  radial and pairwise quotients collapse together.  The double arc succeeds
  because two sheets are ambiently close but intrinsically far.
- Isolated-point examples are too degenerate under the source's convention
  that all derivatives vanish at isolated points.  The double arc has no
  isolated point and is connected.
- The singleton-spike obstruction uses the convex interval itself, so it
  cannot be dismissed as a failure of domain geometry.
- The quantitative theorem keeps the joining curves inside the neighborhood
  where the little-lip bound holds; omitting that containment would be a gap.
- A converse characterizing every domain from its optimal quasiconvex factor
  was attempted but not claimed.

## External dependencies

- Source Theorem 6.4: a uniform little-lip bound on a convex interval implies
  a global Lipschitz bound.
- Source Theorem 3.2: at a Fréchet differentiability point, big Lip equals the
  derivative norm.
- Standard Rademacher/absolute-continuity facts for real Lipschitz functions.

The metric geometry and both counterexamples are otherwise elementary and
self-contained.

## Gaps and scope limitations

No proof gap was found in the promoted statements.  They do not classify all
realizable triples, and the domain condition is proved sufficient rather than
necessary for the universal Baire identity.  Novelty is plausible, not
certified.

## Confidence

Score: 98/100

Residual uncertainty concerns literature novelty and whether a standard
metric-analysis reference already packages the same local quasiconvex
argument under different terminology.

## Human review recommendation

`send to human`

Primary review focus: curve scalarization, local neighborhood containment,
and the singleton indicator's generalized semicontinuity classes.
