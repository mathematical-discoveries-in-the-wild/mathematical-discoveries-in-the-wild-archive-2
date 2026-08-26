# Verifier report

## Result checked

The packet claims a full affirmative resolution of Q2 in arXiv:1103.4691 for
the natural equal-weight, common-matrix self-affine class: if the invariant
measure is absolutely continuous and admits a Fourier frame, then the number
of digits equals the absolute determinant, the cylinders are essentially
disjoint, and the measure is normalized Lebesgue measure on a self-affine
tile.

## Mathematical verification

- Lai's Theorem 1.1 supplies constants `0 < m <= phi <= M < infinity`
  almost everywhere on the support from the Fourier-frame hypothesis.
- Absolute continuity and full IFS support imply that the attractor `K` has
  positive Lebesgue measure.  Subadditivity in
  `K = union_b R^{-1}(K+b)` then gives `q = |det R| <= N = #B`.
- A vector `u` can be chosen outside the countable union of hyperplanes
  `<u,R^{-j}(b-b')> = 0`.  At each level there is therefore a unique
  minimizing digit.  Every alternative address has a termwise nonnegative
  difference from the selected address and a strictly positive first changed
  term.  This verifies the unique exposed-address lemma for arbitrary
  invertible expansive `R`, including non-normal matrices.
- At every depth, the finitely many competing compact cylinders omit the
  exposed point, so a ball separates that point from all of them.  Because
  the point lies in `supp(mu)`, its intersection with `K` has positive
  `mu`-measure, hence positive Lebesgue measure.
- Changing variables in invariance gives
  `phi(x) = (q/N) sum_b phi(Rx-b)`.  On the exclusive depth-`n` set, only one
  summand survives after iteration.  Affine images and preimages preserve
  null sets, so the almost-everywhere bounds legitimately give
  `m <= (q/N)^n M` on a positive-measure subset for every `n`.
- If `q < N`, that inequality fails for large `n`; hence `q >= N`.  Together
  with the volume inequality this yields `q = N`.
- Equality in the finite-cover volume estimate makes the first-level
  cylinders an almost-everywhere partition.  Direct change of variables then
  shows normalized Lebesgue measure on `K` satisfies the equal-weight
  invariant equation.  Uniqueness of the invariant probability yields
  `mu = |K|^{-1} Lebesgue|_K`.
- With `RK = K+B`, positive measure, and `#B = |det R|`, `K` meets the
  Lagarias--Wang definition of a self-affine tile.  Their classical result
  gives a translation tiling of Euclidean space.

Verdict: the proof is complete for equal weights, one common expansive
matrix, and distinct translation digits.  The packet correctly does not
claim unequal weights or varying linear parts.  It also corrects the source's
probability normalization: the density is `|K|^{-1} chi_K`, literally
`chi_K` only when `|K| = 1`.

## Source verification

- `source_paper.pdf` is arXiv:1103.4691v2, Chun-Kit Lai, *On Fourier frame of
  absolutely continuous measures*.
- Source PDF page 13 contains Q2 and the immediately preceding text says the
  paper has treated equal-weight absolutely continuous self-similar measures.
- `figures/question_q2.png` is a readable crop of source PDF page 13
  containing the complete question and its conjectural lead-in.
- The density-bounds theorem used by the proof is Theorem 1.1 of the source.

## Literature and novelty verification

- Cheap run indexes were searched for arXiv:1103.4691, its exact title, and
  the core self-affine/Fourier-frame/density phrases; no duplicate packet or
  ledger answer was found.
- Bounded arXiv/web searches checked the exact question and related later
  works, including arXiv:1202.6028, arXiv:1502.03209, and the review
  arXiv:1602.04750.  They contain related uniformity, no-overlap, spectral,
  and frame-spectral results, but no located theorem states this resolution
  of Q2.
- Lagarias--Wang, *Self-Affine Tiles in R^n*, Advances in Mathematics 121
  (1996), supplies the standard tile terminology and translation-tiling
  implication, not the new determinant argument.
- Novelty is moderate and provisional because a more exhaustive citation
  search may locate the exposed-address argument under different language.

## Build and visual verification

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully.
- The final log has no LaTeX, package, overfull, underfull, or
  undefined-reference warnings.
- Poppler text extraction recovered the theorem, both determinant
  inequalities, exposed-address lemma, normalization, scope, and references.
- The final PDF has four letter-size pages.
- All four pages were rendered at 120 dpi and visually inspected.  The source
  crop is readable; there is no clipping, overlap, malformed mathematics,
  stray source syntax, or illegible text.

## Artifact hashes

- `solution_packet.pdf`: `95e48c8eb43b01f777afa34a1066389ee2ed2d9f5c9633e9c7a31d2a31c9c775`
- `source_paper.pdf`: `eb760d4192ecf1494dc6ad9526489c2d51500f936e6fd1f3f710048671aa32b2`
- `main.tex`: `8947206764ce2924f4c824bfbce67f445f9c5c0d18979b51faa501f40b483587`
- `README.md`: `4a624461f58a99839571d5d3583d46324306345a3f29b0b2e7ddbaf084304850`
- `figures/question_q2.png`: `090e7256895692f63f227c47aa3c8071c47a9b652c9faa222a4d7f090ccb9748`

## Human-review recommendation

Check that Q2 is intended to retain equal weights and a common affine linear
part from the class treated immediately before it.  Then verify the
term-by-term exposed-address argument, the positive-measure exclusive
neighborhood, and the iterated density factor `(q/N)^n`.  Finally confirm the
normalization correction and the Lagarias--Wang tile convention.
