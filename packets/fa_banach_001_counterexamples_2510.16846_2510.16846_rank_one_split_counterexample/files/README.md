# Rank-one splitting disproves Conjecture 3.1 for every `1<p<2`

Status: `candidate_counterexample_likely_valid`

Source: Quanyu Tang and Shu Zhang, *Generalizing Lee's conjecture on the
sum of absolute values of matrices*, arXiv:2510.16846v2, *Linear Algebra and
its Applications* 731 (2026), 196--204,
<https://doi.org/10.1016/j.laa.2025.11.015>.

Target: Conjecture 3.1 on page 4 of the source PDF.

## Result

For every `1<p<2`, the formula proposed in Conjecture 3.1 is strictly too
small already for `m=n=2` and real rank-one matrices.  Hence the conjecture,
which is stated for all `p>1` and `m>=2`, is false.

Let `x>1` solve `x^p=2x+1`, put `beta=(x-1)/(x+1)`, and let
`q=p/2`.  Choose a sufficiently small `delta>0`, set `alpha=1-delta`,
and take unit vectors

```text
u1=v1=e1,
u2=alpha e1+sqrt(1-alpha^2)e2,
v2=beta e1+sqrt(1-beta^2)e2,
A1=u1 v1^T,  A2=u2 v2^T.
```

The eigenvalues of `|A1|+|A2|` are `1+beta,1-beta`, while the squared
singular values of `A1+A2` are
`(1+alpha)(1+beta),(1-alpha)(1-beta)`.  At `alpha=1` the ratio is exactly
the conjectured value.  Replacing `alpha` by `1-delta` adds a positive term
of order `delta^(p/2)` and costs only `O(delta)`.  Since `p/2<1`, the gain
strictly dominates for small `delta`.

The packet gives an explicit valid choice of `delta`, so no limiting or
computational assumption remains.

## Files

- `solution_packet.pdf`: review-ready statement and proof.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: page-4 crop containing Conjecture 3.1.
- `code/verify_rank_one_split.py`: deterministic 100-digit check of the closed
  formulas and a simple `p=4/3` illustration.
- `code/lee_cp_extremal_search.py`: seeded exploratory optimizer that first
  exposed the split-left-vector pattern.
- `VERIFICATION.md`: commands, outputs, and proof-check focus.

## Scope and novelty

This disproves the proposed formula throughout `1<p<2`; it does not determine
the true value of `c_p(2)`, settle the proposed formula for `p>2`, or determine
`c_p(m)` for general `m`.

The run indexes were searched for the arXiv id, exact title, Lee's conjecture,
and the displayed scalar equation.  On 2026-08-09, bounded web searches used
the exact title, DOI plus “counterexample,” “Generalizing Lee's conjecture”
plus “counterexample Schatten p,” and the exact equation
`x^p-2x-(m-1)`.  They found the source arXiv/publisher records but no later
resolution or this construction.  Novelty remains subject to expert review.

## Human-review recommendation

High priority.  The proof is two-dimensional and elementary.  The decisive
checks are the two Gram-matrix eigenvalue calculations and the scalar estimate
in the final perturbation step.

