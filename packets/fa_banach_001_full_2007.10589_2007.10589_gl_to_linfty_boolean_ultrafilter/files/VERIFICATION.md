# Verification report

Verdict: `candidate_full_likely_valid` for the explicit forward implication
`X GL => L_infinity(mu,X) GL` stated as unknown on page 3 of arXiv:2007.10589.

## Proof audit

- For a fixed slice `S`, the function
  `D(y)=dist(y,S)+dist(y,-S)` is convex and even.  Writing a point of the unit
  ball as a convex combination of `z` and `-z` extends the GL distance bound
  from the sphere to the entire ball.
- For `f` of L-infinity norm one, the near-norm set
  `A={||f(t)||>1-delta}` is non-null.  Its class can therefore be extended to
  an ultrafilter on the measure algebra.
- The normalized map `f/||f||` is strongly measurable on `A` and essentially
  separably valued.  A countably valued uniform approximation exists; a GL
  witness functional is selected for each of its countably many values.
- The resulting functional field is countably valued, so
  `t -> phi(t)(h(t))` is measurable for every strongly measurable `h`.
  Ultrafilter limits are linear, ignore null modifications, and are bounded
  by the essential supremum, giving a well-defined element of the dual of
  `L_infinity(mu,X)`.
- On the ultrafilter-large set `A`, the field pairs with `f` by more than
  `(1-delta)(1-2delta)>1-3delta`; normalizing the functional therefore puts
  `f` in the desired slice.
- The normalized functional depends only on `f`, not on the later test
  function `g`.  This is essential for the GL quantifiers.
- For arbitrary `g`, a countably valued uniform approximation and the
  countably valued functional field yield measurable pointwise positive and
  negative slice witnesses.  Their two pointwise distances sum to less than
  `2+4delta`.
- Partitioning the first distance into finitely many bins of width `delta`
  produces one ultrafilter-large bin.  Patching only there leaves both
  witnesses in the unit ball and gives global distance sum at most
  `2+5delta<2+epsilon`; the field pairings on that same bin put the two
  functions in the positive and negative slices.
- No step uses sigma-finiteness.  The argument applies to every nonzero
  measure space under the standard strongly measurable/Bochner definition of
  vector-valued L-infinity.

## Upgrade attempts

1. Averaging a slice functional over a positive-measure set fails because a
   pointwise sum of two distances does not control the sum of their separate
   essential suprema.
2. For finite-dimensional `X`, compactness gives an X-valued ultrafilter
   limit and permits local patching; this proves the implication only in that
   special case.
3. The decisive deep upgrade replaces the X-valued limit by a countably
   valued field of slice functionals and uses a finite distance bin selected
   by the Boolean ultrafilter.  This removes both finite-dimensionality and
   sigma-finiteness.
4. Restriction and averaging routes for the three converse questions lose a
   single slice functional valid simultaneously on a nonseparable sphere, so
   those directions are explicitly excluded from the claim.

## Novelty check

A bounded primary-source search used the exact source statement and the terms
`generalized-lush`, `GL-space`, `L_infinity(mu,X)`, vector-valued function
spaces, and later arXiv citations.  It found arXiv:1210.7324 for the original
GL stability results, arXiv:1309.4358 for ultraproduct/M-ideal stability, and
the source arXiv:2007.10589, but no primary paper proving this implication.
Novelty confidence is moderate.

## Packet and visual checks

- `latexmk` completed with resolved references and no overfull boxes,
  underfull boxes, or final logged warnings.
- The final packet contains four A4 pages.
- Every final page was rendered at 150 DPI and inspected at original
  resolution.  The source excerpt is readable; formulas, ultrafilter notation,
  distance bins, margins, proof ending, references, and page numbers are
  clean; nothing is clipped.
- Text extraction confirms the functional construction, finite distance-bin
  step, and final conclusion that `L_infinity(mu,X)` is GL.

## SHA-256

```text
ae553ae3d6e4fb4bc63c87866b147c0e7aa0a6462262610f3d4311f863768996  solution_packet.pdf
0f0eadf59961d3b476297f7fe8db7fd1160e8ca9ee45d4ab3b3a1fc055b28de5  source_paper.pdf
e7e35e16908a68dcebd3b7b4e89824b5398980199937aae8c216eb86ffee739d  figures/open_question_crop.png
```

## Human-review recommendation

Check the quantifier order carefully: the Boolean ultrafilter and normalized
functional are fixed from `f` before `g` is chosen.  Then verify measurability
of the countably valued witness fields and the finite-bin estimate
`2+5 delta`; these are the only nonstandard steps.
