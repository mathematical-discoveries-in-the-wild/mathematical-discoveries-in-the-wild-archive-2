# Verification report

Status: `candidate_strong_partial_likely_valid`

## Proof audit

- A boundedness-determining `G` separates points by applying the definition
  to `{n x}`.
- Every `G`-null sequence is norm bounded, so the relative Schur hypothesis
  applies to every sequence used in the proof.
- Difference quotients are norm Cauchy because any two vanishing-parameter
  subsequences have `G`-null differences.
- The candidate derivative is linear by separation and bounded because its
  unit-ball image is `G`-bounded.
- Frechet remainders and derivative-continuity failures reduce to `G`-null
  sequences after choosing witnessing unit directions.
- The higher-order induction repeats this argument in evaluated multilinear
  directions, avoiding any unproved Schur property for an operator space.
- In the converse, `t_n=2^-n` and `w_n=2^-3n` give disjoint supports and
  `w_n/t_n=2^-2n -> 0`.
- The derivatives below order `k` have scale `w_n^(k-j)`; the kth derivative
  has scalar amplitude `g(x_n) -> 0` but vector amplitude bounded away from
  zero at the centers.
- `c_0` determines boundedness of `ell_1` by uniform boundedness on the
  Banach space `c_0`, while the unit vectors are `sigma(ell_1,c_0)`-null.

## Literature audit

The primary closest result is Bachir--Lancien, *On the Composition of
Differentiable Functions*, Canadian Mathematical Bulletin 46 (2003),
481--494, DOI `10.4153/CMB-2003-047-2`. Its Theorem 2.1 and Corollaries
2.2--2.3 cover the full-dual Schur case. The packet makes no novelty claim for
that special case.

Bounded exact-phrase and keyword searches on 2026-08-09 found no primary
source stating the arbitrary boundedness-determining `(E,G)` classification.
This is not a publication-level novelty certification.

## Render audit

The packet was compiled with `latexmk` into a six-page PDF. The log has no
undefined references, layout warnings, overfull boxes, or underfull boxes.
All six final pages were rendered at 144 dpi and visually inspected. The
source question is legible and not clipped, equations and multilinear
remainders are readable, hyperlinks do not obscure text, and no page has
overlapping or missing content. A Ghostscript text extraction also recovered
the theorem, bump converse, corollary, novelty section, and references.
