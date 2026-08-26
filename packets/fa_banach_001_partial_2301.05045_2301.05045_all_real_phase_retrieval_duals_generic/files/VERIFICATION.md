# Verification report

Verdict: `candidate_partial_solution_likely_valid`.

## Mathematical checks

- Verified the synthesis-matrix convention: duals are exactly the affine
  solutions `G F^T = I_n`, and the canonical dual is
  `G_0=(F F^T)^(-1)F`.
- Checked directly that `G_0` does phase retrieval whenever `F` does, using
  self-adjointness and invertibility of the frame operator.
- Checked the complement-property certificate for every subset, including
  subsets with fewer than `n` elements (their maximal-minor sum is the empty
  sum, hence zero).
- Because each certificate is a sum of squares, its vanishing is exactly the
  simultaneous failure of both spanning alternatives; no sign or
  complex-zero issue enters.
- The product polynomial is strictly positive at the canonical dual, so its
  restriction to the affine dual space and to every line ending at the
  canonical dual is nonzero.
- A nonzero real polynomial on a finite-dimensional affine space has empty
  interior and Lebesgue-null zero set; a nonzero univariate polynomial has
  finitely many roots.

No unproved lemma or computational dependency remains beyond the standard
real complement-property characterization, cited explicitly in the packet.

## Novelty check

The run indexes had no exact hit. Official arXiv API searches on 2026-08-11
for each of the following returned only arXiv:2301.05045v1:

- `"phase retrieval dual frames"`;
- `"alternate dual frames" AND "phase retrieval"`;
- `"dual frames" AND "open and dense" AND "phase retrieval"`.

No arbitrary-redundancy theorem or radial finite-exception result was found.

## Packet and rendering checks

- `source_paper.pdf` opens and has 14 pages.
- The first crop contains the complete classification/density question and
  the source's statement that only some classes are handled.
- The second crop contains the whole statement of source Theorem 2.3 and its
  explicit `2n-1`-vector restriction.
- `main.tex` was compiled with all intermediates confined to `tmp/`.
- Every rendered page of `solution_packet.pdf` was visually inspected; no
  clipping, overlap, missing glyph, or blank-page defect was found.

