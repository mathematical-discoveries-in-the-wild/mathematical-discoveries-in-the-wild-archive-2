# Verification record

## Source and question

- Official source PDF: arXiv:1603.07073.
- Theorem 2.3 and the exact open question are on PDF page 7.
- The source asks whether the residual norms converge to the approximation
  error without the closedness of `A1+A2`.

## Mathematical checks

1. On a one- or two-point fibre, `f o sigma = 2Ff-f`.  The C-property makes
   this continuous for every `f`, which makes the fibre swap `sigma`
   continuous on compact Hausdorff `X`.
2. Stone--Weierstrass identifies the closed unital algebra with all
   functions invariant under the fibre swap.
3. For `P=(I-U)/2`, `Q=(I-V)/2`, `T=QP`, the odd residuals are `T^n h`.
4. With `R=VU`, a `V`-fixed vector satisfies
   `Tv=(R-R^{-1})v/4`; on the anti-`V` subspace, `T` equals
   `(2I+R+R^{-1})/4`.
5. The Laurent coefficients of `L^mD` have absolute sum
   `(p_m(0)+p_m(1))/2`, by symmetry and unimodality, and this is at most
   `binom(2m,m)/4^m <= 1/sqrt(m+1)`.
6. The limit of `||T^n h||` is a 1-Lipschitz seminorm.  It vanishes on both
   algebras and therefore on the closure of their sum.  The reverse
   inequality follows because every residual represents the same quotient
   class as `h`.
7. In the nonclosed example, the two reflections generate the full cyclic
   rotation, so their common fixed functions on each finite cycle are
   constants.  The phase-difference blocks tend to zero, while any putative
   decomposition has a component at distance one from constants on every
   block, contradicting continuity at the compactification point.

## Computational check

`code/verify_involution_decay.py` performs exact rational checks of the
coefficient identity for `0<=m<=100`.  It also tests the operator formulas,
the `1/sqrt(n)` rate, and the nonclosed-sum phase witnesses on finite
dihedral cycles of several sizes.

Command:

`conda run --no-capture-output -n sandbox python code/verify_involution_decay.py`

Result: `verified coefficients m=0..100 and finite involution cycles`.

## Literature audit

The cheap run indexes and bounded searches on 2026-08-17 used the exact
question and combinations of `Diliberto-Straus`, `without closedness`,
`two-point fibres`, `involution invariant algebras`, later citations, and
the authors' later bolt-duality work.  No later explicit solution or this
two-point-fibre theorem was located.  This is a bounded novelty audit, not
an exhaustive bibliographic claim.

## Human-review boundary

The involution and Laurent-polynomial proof is considered mathematically
high-confidence.  A human expert should especially review the topological
step turning two-point fibres into a continuous involution and the
nonclosed-sum example.  The packet does not settle the question for fibres
of size three or larger.
