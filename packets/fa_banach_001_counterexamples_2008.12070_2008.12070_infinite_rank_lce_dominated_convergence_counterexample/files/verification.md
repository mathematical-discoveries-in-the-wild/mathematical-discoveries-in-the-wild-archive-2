# Verification record

Date: 2026-08-12

## Source evidence

- Official source PDF: `figures/source_2008.12070.pdf`
- Exact question: PDF page 9, rendered as `figures/source_page9.png`
- The page says that DCT hypothesis (alpha), with one square-integrable
  dominator, remains open when `C_V` has infinite rank.

## Proof audit

1. Menshov's 1923 sharpness theorem with weight `W(n)=1` gives an ONS and
   square-summable coefficients whose partial sums diverge everywhere.
2. Multiplication by an independent symmetric sign makes the ONS mean-zero
   without changing orthonormality or divergence.
3. The disjoint-support tails converge pointwise and their pointwise supremum
   has squared integral equal to the coefficient `ell^2` norm.
4. In the half-weighted direct sum, projection onto the graph of an isometry
   maps `(f,0)` to `(f,Tf)/2`.
5. The coordinate variable `V=(2^{-n}s_n)` has covariance
   `diag(4^{-n})`, hence infinite rank, and its affine coordinate closure is
   exactly constants plus the graph.
6. The L2 Menshov tail equals the L2 sum minus the finite partial sum, so
   pointwise divergence of partial sums is exactly failure of the projected
   tails to converge to zero.

Run the finite-dimensional algebra check with:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2008.12070_infinite_rank_lce_dominated_convergence_counterexample/code/verify_graph_projection.py
```

The script checks graph orthonormality, weighted self-adjointness and
idempotence of the projection, the tail formula, and finite covariance rank.

## Highest-value review points

- Check the use of Menshov's exact Weyl-multiplier theorem at `W=1`.
- Check that representatives `r_k=F-S_{k-1}` correctly encode the L2 tails.
- Check the closure identity for bounded affine functions of `V`.

## Mechanical and visual checks

- `verify_graph_projection.py`: all finite graph-projection checks passed;
  graph Gram error and projection idempotence error were both exactly zero.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`: passed with
  no warnings, overfull boxes, or underfull boxes in the final log.
- Final packet: 5 letter-sized pages, all rendered at 140 dpi and visually
  inspected after the final edit; no clipping, overlap, illegible text, or
  malformed mathematics was found.
- Packet SHA-256:
  `fce1aea27c9ebb6356a8923888c73cde7f8b3127b2238361e687d90ceacd6278`.
- Official source PDF SHA-256:
  `470365444c9d410eeb21fa6308eaf38aaf6a02f6f664d470cdea22e0f071c5e1`.
