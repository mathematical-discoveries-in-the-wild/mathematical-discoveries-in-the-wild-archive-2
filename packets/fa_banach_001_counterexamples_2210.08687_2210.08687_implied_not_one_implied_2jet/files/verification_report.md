# Verification report

## Verdict

Likely valid full negative answer to Remark 2.11 of arXiv:2210.08687. Human
review is recommended before dissemination.

## Claim audited

In `P^2_0(R^3)`, the ideal
`I=span{xz,yz,x^2+y^2}` implies `p=x^2+2y^2`, but `p` is not 1-implied by
`I` under the exact scale-local definition in the source.

## Adversarial checks

1. **Ring and ideal.** The ring is nonunital and multiplication is truncated
   after degree 2. Every element of `I` has degree 2, so multiplying it by any
   positive-order jet gives degree at least 3 and hence zero. Therefore every
   linear subspace of the homogeneous quadratic layer, including `I`, is an
   ideal.

2. **The jet is genuinely outside the ideal.** The `xz` and `yz` generators
   do not affect the `x^2,y^2` coefficients. A scalar multiple of
   `x^2+y^2` cannot have coefficients 1 and 2, so `p` is not already in `I`.

3. **Exact allowed set.** Away from the two poles, the single element
   `x^2+y^2` has a uniform positive `|X|^2` lower bound on a smaller cone, so
   every such direction is forbidden. On either pole ray every element of
   `I` vanishes, so no finite family can obey Definition 2.6's positive lower
   bound throughout any cone containing that ray. Thus `Allow(I)` is exactly
   the two poles.

4. **Global smoothness of the two coefficients.** A degree-zero angular
   cutoff is chosen to vanish outside `|z|>=|X|/3`; the expressions
   `chi*x/z` and `2 chi*y/z` therefore extend smoothly by zero to the entire
   punctured space. The cutoff is identically one near both poles.

5. **Tame bounds at every scale.** Derivatives of order `k<=2` of a smooth
   degree-zero function are homogeneous of degree `-k`. On `Ann_4(rho)`, this
   gives a single fixed bound `A rho^{-k}`. The fixed generators and `A` work
   for every epsilon and rho; `F=0` satisfies all epsilon-small bounds.

6. **All possible single generators are covered.** Every `Q in I` has the
   unique form `a xz+b yz+c(x^2+y^2)`. The proof divides into
   `sqrt(a^2+b^2)>0` and `a=b=0`, with `Q=0` included in the second case.

7. **Quantifier order.** To disprove 1-implication, the proof first fixes the
   hypothetical `Q` and `A`, then chooses epsilon depending on the fixed
   coefficients of `Q`. The definition must work for that epsilon. Delta,
   radius, scale, and functions are taken only afterward, exactly as allowed.

8. **The pole is an interior equality point.** For every positive scale,
   `v=(0,0,rho)` lies strictly inside `Ann_2(rho)` and has distance zero from
   `Allow(I)`. Both defining inequalities are strict in a neighborhood of
   `v`, so the identity may legitimately be differentiated there.

9. **First directional derivative.** When `d=sqrt(a^2+b^2)>0`, the unit
   direction `e=(a,b,0)/d` satisfies `D_e Q(v)=rho*d`, while `Q(v)=0` and
   `D_e p(v)=0`. Hence `|S(v)|<=sqrt(2) epsilon/d`; the `sqrt(2)` is the
   sharp elementary conversion from componentwise first-derivative bounds
   in the two transverse coordinates.

10. **Perpendicular second derivative.** For
    `t=(-b,a,0)/d`, both `Q(v)` and `D_t Q(v)` vanish, so all product-rule
    terms except `S(v)D_t^2Q(v)=2cS(v)` vanish. Since
    `D_t^2p` lies in `[2,4]` and the componentwise Hessian bounds give
    `|D_t^2F|<=2 epsilon`, sufficiently small epsilon contradicts the
    identity, including when `c=0`.

11. **Pure radial-quadratic case.** If `a=b=0`, both transverse first
    derivatives of `Q` vanish at the pole. The `xx` and `yy` identities are
    `2=F_xx+2cS` and `4=F_yy+2cS`. Their difference says
    `2=F_yy-F_xx`, impossible when epsilon is below 1.

12. **One pole suffices.** Although the allowed set has two poles, a
    1-implication identity must hold near both. Contradiction at the positive
    pole alone is decisive; no compatibility assumption between the poles is
    used.

## Literature and novelty check

The four cheap run indexes had no entry resolving this arXiv id or the exact
implied/1-implied terminology. Targeted searches through 11 August 2026 for
the exact question, source title, and follow-up paper found no resolution.
This bounded search is not a substitute for expert literature review.

## Recommended verifier focus

Confirm the source's componentwise derivative convention and the smooth
zero extension of the angularly cut off ratios. Once those are fixed, the
two exhaustive derivative contradictions are local and exact.
