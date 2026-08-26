# Verification report

## Source audit

- The retained source is arXiv:2511.23121v1, Matthew Daws, *Quantum graphs
  in infinite-dimensions: Hilbert--Schmidts and Hilbert modules*.
- Question 4.14 is on PDF page 17.  It asks how to describe the
  representation-independent operation `e -> e^hsc` at the level of
  `M tensor M^op`.
- Proposition 4.11, on PDF pages 16--17, proves the exact starting identity
  `V^hsc = (B(H)_* intersection V^perp)^perp`; the paper identifies
  `B(H)_*` with the trace-class operators inside the Hilbert--Schmidt
  space.
- Example 4.12 gives a particular strict closure based on the diagonal
  Hilbert--Schmidt vector `(1/n)`, which is not trace class.

## Proof audit

1. Under the source correspondence, `V=eK`, so `V^perp=(1-e)K`.
2. Proposition 4.11 therefore makes the orthogonal complement of
   `V^hsc` equal to the Hilbert--Schmidt closure of
   `S_1(H) intersection (1-e)K`.
3. The trace class is stable under all bounded left and right
   multiplications.  Because `e` commutes with the commutant `A'`, the
   displayed intersection and its closure are `A'`-invariant.
4. A closed invariant subspace for the self-adjoint algebra `A'` is
   reducing; its orthogonal projection lies in `(A')'=A`.
5. For a vector `xi`, the support of its vector functional on `A` is the
   projection onto `closure(A' xi)`: this projection is in `A`, fixes
   `xi`, and is minimal among projections in `A` that fix `xi`.
6. Since the relevant trace-class-vector set is already `A'`-invariant,
   the projection onto its closed span is the join of those support
   projections.  Taking the complementary projection proves the formula.
7. For `M=B(H)`, `A=B(S_2(H))`, giving the ordinary projection onto the
   closed trace-class part of `ker e`.
8. A subspace of a finite-dimensional kernel is closed.  For a
   one-dimensional kernel, its trace-class intersection is either the
   whole line or zero, proving the dichotomy.

No logical gap was found in these steps.

## Scope audit

- The result exactly reformulates the closure as a lattice operation in
  `A` and completely handles the full-factor finite-corank case.
- The family of vector functionals used in the join is still selected by
  trace-class membership in the chosen representation.  Although the
  resulting projection is representation-independent by the source's
  Theorem 4.16, the packet does not claim an intrinsic classification for
  arbitrary von Neumann algebras.
- The source's separate question about reconstructing operator-valued
  weights from abstract self-dual modules is not solved.  The nearby
  equality `T(alpha*alpha)=hat(alpha)*hat(alpha)` is already proved in the
  source.
- The support-join formula and finite-corank corollary were not found in
  the cheap run indexes.  Because they are close consequences of the
  source proposition, novelty confidence is moderate.

## File hashes

- Source PDF SHA-256:
  `c840122c5beee2406aa716bdc2d4866d2859fac085e8595b2e1e263325fdcf1b`.
- Final solution packet SHA-256:
  `f07f44f7137fc7790a04e64b4cb17f1d7dd4256a65aafed5a90ad740dcea5460`.

## PDF and render audit

- Final packet: 3 letter-size pages.
- Latexmk completed after two passes.  The final log contains no warnings,
  undefined references, overfull boxes, or underfull boxes.
- The bundled `pypdf` runtime reopened the final PDF and extracted nonempty
  text from all three pages.
- All three pages were rendered with bundled Poppler at 144 dpi after the
  final edit and inspected individually.  The status banner, theorem and
  corollary statements, joins, closures, citations, URL, and page boundaries
  are legible.  No clipping, overlap, broken glyph, or malformed spacing was
  found.
