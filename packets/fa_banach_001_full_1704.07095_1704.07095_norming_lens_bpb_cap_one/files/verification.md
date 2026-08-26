# Verification record

Date: 2026-08-11

Status: candidate full solution, likely valid, subject to human review.

## Mathematical audit

- The lens `C = B_X intersect (x+B_X)` is closed, bounded, and convex, and
  `x/2` lies in the interiors of both balls for every `x in B_X`.
- Bishop--Phelps supplies a nonzero nearby functional supporting `C`. Scaling
  it down to norm at most one preserves its support point and introduces less
  than one further copy of the approximation error.
- The interior-point normal-cone rule decomposes the supporting functional as
  `alpha g + beta h`, with `g` norming the first active ball and `h` norming
  the translated active ball.
- In the two-active-ball case, writing `v=x-u` gives `g(v)<=0` and `h(u)>=0`.
  Evaluation at `u` and `v` forces both coefficients at most one.
- If `alpha>=beta`, the first norming pair is within one of `(x,phi)`; if
  `beta>=alpha`, the translated-ball pair is within one and satisfies
  `h(v)=-1`. The latter is exactly why absolute norm attainment is crucial.
- Letting the support-functional perturbation tend to zero converts the
  `1+eta` construction into an infimum bound of one, matching the strict
  inequalities in the modulus definition.
- For a property-beta-zero range, the rank-one correction changes exactly one
  coordinate functional. The norming family proves the corrected operator has
  norm one and attains it, with correction norm exactly `||g-f||`.
- The classical/source beta-zero estimate supplies the independent
  `sqrt(2 epsilon)` bound.

## Upgrade attempts

1. Reduced the open problem to the residual cap-one geometry for
   `epsilon>1/2`.
2. Explored direct segment and midpoint constructions; these do not control
   the dual displacement in arbitrary nonsmooth norms.
3. Recast the problem as proximity to the union of positive and negative
   norming graphs.
4. Tested random centrally symmetric polygonal norms in dimension two; the
   largest discretized distance observed was exactly one, with no
   counterexample.
5. Introduced the two-ball lens so primal feasibility is automatic for both
   candidate norming points.
6. Applied Bishop--Phelps to obtain an actual supporting functional of the
   lens near the prescribed dual point.
7. Used the normal-cone decomposition and coefficient comparison to obtain a
   complete universal proof, including zero coefficients and `f=0`.
8. Upgraded the scalar result to nonspherical moduli and to all property-beta
   range spaces at parameter zero; audited the positive-parameter obstruction.

## Literature audit

- The registry, solution, attempt, and proof-gap indexes had no hit for the
  arXiv identifier or the exact Section 5 question.
- Exact local-corpus searches found only the source statement and
  bibliographic/citation occurrences, not an answer.
- Bounded primary-source web and citation searches found no later theorem
  matching the scalar cap-one result.
- The novelty statement is deliberately bounded and is not a priority claim.

## Artifact audit

- The archived arXiv source is compiled locally and its Section 5 page is
  embedded as source evidence.
- The final packet is compiled twice and checked for undefined references,
  overfull boxes, and LaTeX errors.
- Every final PDF page and the embedded source page are rendered at high
  resolution and visually inspected for clipping, overlap, and legibility.

## Human-review focus

Check the use of the infinite-dimensional interior-point normal-cone sum rule
and the sign convention for the translated ball. These are the only delicate
joints; the rest is elementary once the decomposition is available.
