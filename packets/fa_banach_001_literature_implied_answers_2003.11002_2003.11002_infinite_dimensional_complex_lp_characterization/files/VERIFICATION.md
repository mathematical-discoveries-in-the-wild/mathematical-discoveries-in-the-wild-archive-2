# Verification report

Verdict: `valid literature_implied_answer (partial subcase)`.

## Sources independently checked

- arXiv:2003.11002, official PDF page 17: Problem 17 asks for the spaces with
  Bernstein's inequality for every homogeneous polynomial and states the
  equivalence with equality between a symmetric multilinear form and its
  polynomial norm.
- arXiv:1908.08107, official PDF pages 11--13: the symmetric operator norm
  property is explicitly identified with `c(2,X)=1`, and Theorem 3.1 proves
  that an infinite-dimensional complex space with this property has optimal
  type and cotype exponents both equal to two.

The supporting theorem's proof and its warning that the converse fails for
general spaces were inspected.  The packet uses only the necessary direction.

## Implication checked

1. The all-degree source property implies its degree-two instance.
2. The supporting theorem therefore applies.
3. For an infinite-dimensional complex `L_p(mu)`, the optimal type/cotype
   exponents are `min(p,2)` and `max(p,2)` (with the standard endpoints), so
   both equal two only at `p=2`.
4. At `p=2`, the space is Hilbert and Banach polarization gives equality in
   every degree.

The infinite-dimensional hypothesis is essential: optimal type/cotype
exponents do not distinguish finite-dimensional `L_p` spaces.  The packet
does not claim a converse to Theorem 3.1 for arbitrary Banach spaces.

## Provenance classification

The supporting paper predates Problem 17 and does not say it answers that
problem.  `literature_implied_answers/` is therefore the correct bucket;
`literature_already_answered/` would be incorrect.

## Artifact QA

The interrupted `tmp/main.pdf` was treated as untrusted and its missing
source was not reconstructed by copying its claims.  `main.tex` was written
again from the two official PDFs, compiled anew, rendered page by page, and
visually inspected on 2026-08-21.  No clipping, overlap, missing glyph, or
placeholder text remains.
