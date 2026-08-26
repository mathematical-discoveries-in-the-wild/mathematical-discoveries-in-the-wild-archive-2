# Verification report

Verdict: `partial_result_likely_valid`

## Mathematical checks

1. Every rotated cross measure is even and isotropic; probability mixtures
   preserve both properties.
2. The support function identity
   `h(S_mu,x) = integral h(R S_nu,x) d pi(R)` follows directly from
   linearity and orthogonal equivariance of the sine transform.
3. Polar volume uses the exact formula
   `V(K*) = (1/n) integral_{S^{n-1}} h_K(u)^(-n) du`.
   Pointwise Jensen for the strictly convex function `s^(-n)` has the stated
   direction.
4. For primal volume, mixed-volume linearity gives
   `V(Kbar) = integral V(Kbar[n-1], R K0) d pi(R)`.  Minkowski's first
   inequality gives the lower bound after integration.
5. If the primal inequality is equality, the nonnegative Minkowski gaps
   vanish almost everywhere.  Equality in Minkowski's first inequality makes
   almost every rotated body homothetic to the average.  Central symmetry,
   common center, and equal volume make them identical.
6. If the polar inequality is equality, strict Jensen makes the rotated
   support functions identical almost everywhere; continuity upgrades this
   to equality of bodies.
7. In either equality case, Proposition 2.1 of the source (injectivity of the
   sine transform on even measures) makes the rotated cross measures
   identical, so the mixture itself is a cross measure.
8. The discrete fractional-basis corollary is exactly the coefficient form
   of a finite convex combination of cross measures.

## Upgrade attempts and obstruction audit

- A counterexample search tested the regular tetrahedral frame and 600 random
  Parseval-frame measures in dimension three (4–9 support lines); none beat
  the cross measure for polar volume.  Independent determinant sampling for
  the zonoid volume placed the tetrahedral value above the cross value, as
  conjectured.
- The proof was upgraded from finite convex combinations to arbitrary Borel
  probability mixtures on `O(n)` using Minkowski integrals and mixed volumes.
- The discrete class was upgraded to an exact fractional orthonormal-basis
  criterion.
- A support-preserving decomposition cannot reach all isotropic measures:
  the regular-simplex frame has no orthonormal basis in its support.  Since
  the mixture class is compact (the continuous image of probability measures
  on compact `O(n)`), approximation does not remove this obstruction.
- Direct rank-`n-1` Brascamp–Lieb extension reaches the same open
  non-divisible-rank problem identified by Li–Xi–Zhang (2017).  No credible
  full-proof route remained after this check.

## Novelty/literature bounds

- Exact-title, exact-conjecture, cross-measure/sine-transform, and
  orthonormal-basis-mixture searches were run through 2026-08-11.
- Huang–He (2015) explicitly described the real and complex cross-measure
  problems as open.
- Li–Xi–Zhang (2017), Theorem 1.2, gives sharp Grassmannian reverse
  inequalities when the rank divides the dimension and explicitly leaves the
  non-divisible case open.  The real sine transform has rank `n-1`, which
  does not divide `n` for `n>=3`.
- Huang–Li–Xi–Ye (arXiv:2206.00185) studies sine polarity and a different
  Blaschke–Santaló problem; it does not state the source conjecture's reverse
  isotropic-measure extremum.
- No prior statement of the basis-mixture theorem was located.  Novelty is
  provisional pending expert bibliographic review.

## Computational check

`conda run --no-capture-output -n sandbox python
code/verify_basis_mixtures.py` passed.  It checks isotropy, pointwise Jensen,
Monte Carlo polar volumes, and a determinant representation of primal zonoid
volume for deterministic mixtures in dimension three.  These checks are
sanity tests only.

## Artifact checks

- Official source PDF opens and has 21 pages.
- The conjecture crop is readable and comes from source PDF page 14.
- LaTeX compilation completed without undefined references or overfull boxes.
- Every rendered packet page was visually inspected.
