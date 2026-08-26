# Verification report

## Result and source

- Source: Benoit R. Kloeckner, *A geometric study of Wasserstein spaces:
  ultrametrics*, arXiv:1304.5219.
- Exact signal: PDF page 21, final paragraph.
- Claimed result: for every finite `D > 0`, one compact countable ultrametric
  `X_D` has upper Minkowski dimension `D` and
  `crit_P(W_p(X_D)) = 0` for every `p >= 1`.
- Classification: candidate full counterexample to the strongest conjecture;
  likely valid.

## Proof audit

1. **Metric and compactness.**  Distinct points have distance equal to the
   larger of their radii from the accumulation point.  This is ultrametric.
   Radii tend to zero, so every tail lies in one arbitrarily small ball.
2. **Upper Minkowski dimension.**  Between consecutive radii, all points in
   the first `k` blocks are isolated and the tail is one ball.  The covering
   number is exactly `S_k + 1`; `log S_k = D A_k + o(A_k)`.
3. **Tail collapse.**  Moving all tail mass to the accumulation point has
   explicit transport cost at most `R_(k+1)^p`.
4. **Finite simplex net.**  Rounding `n-1` coordinates downward on a mesh
   `delta=(r/2)^p/n` changes total variation by at most `(r/2)^p`; a maximal
   coupling therefore has `W_p` cost at most `r/2`.
5. **Gauge comparison.**  At `rho_k=exp(-sqrt(A_(k+1)))`, the logarithm of
   the net size is at most single exponential in `A_k`, whereas
   `(2 rho_k)^(-s)` is double exponential for every fixed `s>0`.  The total
   `exp(-diam^(-s))` cover cost tends to zero.
6. **Quantifiers.**  The construction depends on `D` but not on `p`; the net
   estimate is valid separately for every finite `p >= 1`.

No computational experiment is used as proof.

## Upgrade-attempt log

- Route 1 tested whether sparse branching bursts might fail because finite
  Wasserstein simplexes are individually finite-dimensional.
- Route 2 replaced a general tree-selection problem by an explicit ultrametric
  comb of finite equilateral blocks and derived exact covering numbers.
- Route 3 converted the scale-gap heuristic into a Hausdorff-gauge upper bound
  using tail collapse and a finite-simplex rounding net.
- Deep upgrade: the first `D=1`, fixed-`p` construction was generalized to
  every prescribed finite `D>0`, with the same `X_D` working for all `p>=1`.
- A further attempt to attack the possible lower-Minkowski bound was stopped:
  the scale gaps essential to this proof force lower Minkowski dimension zero,
  and removing those gaps destroys the cheap-cover mechanism.

## Novelty audit

Bounded searches through 2026-08-11 covered the exact conjectural formula,
title/citation combinations, and the terms *Wasserstein*, *power-exponential
critical parameter*, *upper Minkowski dimension*, and *ultrametric*.  No later
paper explicitly resolving the conjecture was found.  The abstract/search
record for arXiv:2607.18525, *Regular ultrametric skeletons*, concerns regular
skeletons and controlled balls; it did not disclose this result.  Novelty
confidence is moderate because no exhaustive citation graph was available.

## Source and render audit

- `source_paper.pdf` was compiled locally from the archived arXiv source and
  has 22 pages.
- The source question was visually confirmed on source PDF page 21.
- `figures/open_problem_crop.png` includes the full page width and the complete
  question paragraph.
- The final packet has 5 pages, was compiled with `latexmk`, rendered
  page-by-page with Poppler, and every page was visually inspected after the
  last material edit; no clipping, overlap, broken glyph, or unreadable crop
  was found.
- Final packet SHA-256:
  `bdcf663f1dfa53284d5f4f6ec8bdb73b37b96074fded68a170106b083df4bf87`.
- Source PDF SHA-256:
  `084715eccaea81c94bfbeaa6730763e50714f8dd25ffcb8472819cd309c6b619`.

## Human verifier focus

Check the ball-radius/cover-diameter convention in the Hausdorff gauge,
the exact finite-simplex net cardinality, and the asymptotic comparison between
`log Q_k` and `(2 rho_k)^(-s)`.  Also confirm that the source's `M-dim` denotes
upper Minkowski dimension in the quoted strongest conjecture.
