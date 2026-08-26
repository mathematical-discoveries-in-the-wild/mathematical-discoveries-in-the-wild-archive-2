# Verification report

## Algebraic checks

- The least power of two `Q` with `Q-1>=n` satisfies `Q<2(n+1)`, so the
  seed space has at most `[2(n+1)]^m` elements.
- Any dependence among at most `2m` coordinate bits forces all odd power
  sums through degree `2m-1` to vanish by nondegeneracy of the trace
  pairing.
- Frobenius squaring supplies every even power sum through degree `2m`.
- The resulting square power matrix is a nonzero diagonal factor times a
  Vandermonde matrix, so the dependence is impossible.
- The seed-to-bit map is linear; its pushforward is uniform on its image,
  so removing duplicate seed outputs does not disturb uniformity.
- `2m`-wise independence exactly matches all monomials in an even
  `2m`-th moment.
- The all-real-`p` extensions use only normalized `L_p` monotonicity and,
  for `p<=2`, the exact second/fourth moments plus log-convexity.

## Scope and novelty

The even-exponent size matches the `n^(p/2)` optimum stated in the source.
The construction is not sharp at `p=1` or at non-even exponents. Bounded
literature searches through 2026-08-11 found the two ingredients—BCH
orthogonal arrays and k-wise Khintchine bounds—but no direct application
recorded as an answer to this exact source problem.

## Artifact check

After the final build, the PDF was rendered page by page and inspected for
clipping, overlap, missing glyphs, figure readability, and unresolved
references. Findings are reflected in the final packet status.

Verdict: substantial partial result, likely valid; prioritize review of the
finite-field independence lemma and novelty classification.
