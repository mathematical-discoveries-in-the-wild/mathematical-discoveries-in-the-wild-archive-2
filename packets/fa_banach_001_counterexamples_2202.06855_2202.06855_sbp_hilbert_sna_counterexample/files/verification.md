# Verification record

Date: 2026-08-11

Status: candidate full counterexample, likely valid, subject to human review.

## Mathematical audit

- For each fixed `k`, the union of the open balls centered at the dense
  sequence `(x_n)` is open and dense, regardless of how fast their positive
  radii shrink.
- Baire category therefore makes the intersection `M` a dense `G_delta`.
- A sufficiently late row of the construction covers `M` by closed balls
  whose radii are uniformly below any prescribed `epsilon_0` and tend to zero.
  This is exactly the small ball property.
- For each `u in X`, the sets `M` and `M-u` are dense `G_delta` subsets of the
  complete Banach space `X`. Their intersection is nonempty, proving `M-M=X`.
- Reflexivity makes every `x* in X*` norm-attaining on `B_X`.
- The attaining unit vector is a difference `p-q` of two points of `M`, so the
  restricted evaluation functional attains its Lipschitz norm strongly at
  `(p,q)`.
- The restriction map `J:X* -> Lip_0(M)` is linear and isometric; its range is
  therefore closed.
- With `X=ell_2`, the range is reflexive. An infinite-dimensional
  isomorphically polyhedral Banach space contains `c_0`, so the range cannot
  be isomorphically polyhedral.
- The printed Question 4.3 does not assume completeness of `M`; no hidden
  completeness step is used.

## Literature audit

- The registry, solution, attempt, and proof-gap indexes had no hit for
  arXiv:2202.06855 or the small-ball/polyhedrality question.
- Exact searches across the locally parsed arXiv corpus found the source and
  later citing works, but no resolution of Question 4.3.
- arXiv:2204.12529 answers the source's Questions 4.1 and 4.2, not Question 4.3.
- arXiv:2208.02916 and the later surveys/results in arXiv:2312.00393,
  arXiv:2404.07599, and arXiv:2410.16607 discuss spaceability and copies of
  `c_0`; none mentions a solution of the small-ball/polyhedrality question.
- The primary Behrends--Kadets paper was inspected in full. Its Proposition
  5.1 supplies precisely the dense `G_delta` small-ball set used here.

This is a bounded novelty check, not an exhaustive bibliographic priority
claim.

## Artifact audit

- The archived arXiv source was compiled twice to a clean 12-page source PDF.
- Printed source page 10, containing Question 4.3, was rendered at high
  resolution and embedded as source evidence.
- The final packet was compiled twice and checked for undefined references,
  overfull boxes, and LaTeX errors.
- Every page of the final packet and the embedded source page was rendered at
  high resolution and visually inspected for clipping, overlap, and legibility.

## Human-review focus

Check the translation convention in the `M-M=X` Baire argument and the use of
the standard Fonf theorem that every infinite-dimensional isomorphically
polyhedral space contains an isomorphic copy of `c_0`. These are the only
substantive external joints.
