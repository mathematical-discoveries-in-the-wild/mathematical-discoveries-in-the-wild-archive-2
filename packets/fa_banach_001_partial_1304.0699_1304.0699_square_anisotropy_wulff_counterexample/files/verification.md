# Verification record

## Mathematical checks

- Translation of the square at the boundary point `(1,t)` gives exactly
  `[-2,0] x [-1-t,1-t]`.
- In curvature differences the singular local half-space terms cancel.
- Differentiating the moving horizontal endpoints gives
  `H_s'(t)=2 integral_[−2,0](k(x,1−t)−k(x,1+t)) dx > 0` for `0<t<1`.
- A smooth right-side graph variation with zero-integral normal velocity
  preserves area exactly and has negative first energy derivative when mass
  is moved outward near the side midpoint and inward nearer a corner.
- Simultaneous affine covariance of the set and anisotropy was checked,
  including the factor `|det A|^2` in the energy.
- The rectangle covariogram and layer-cake formula were derived independently.
- Symbolic differentiation gives the stated derivative. Its sign reduces to
  `G_s(1)=0` and
  `G_s'(q)=2s(s+1)q^(2s−1)(2q^2−1)>0`.
- Numerical quadrature at `s=0.2,0.5,0.8` and aspect ratios
  `q=1,1.1,1.5,2,3` confirmed strict increase after correcting for the full
  square rather than quadrant layer-cake normalization.

## Literature checks

- The source's exact statement that minimizer determination remains open was
  verified on printed page 4.
- Kreuml (2021) gives an unconditional star-body structural result under
  strict convexity, not a full equality-case classification.
- Cai, arXiv:2510.05279 (2025), explicitly says little is known and derives a
  necessary condition for convex optimizers.
- Bounded exact-phrase, title, square/cube, parallelogram, Wulff-shape,
  optimizer, and nonlocal-curvature searches found no matching all-s square
  nonstationarity or rectangle-restriction theorem.

## Packet QA

- `source_paper.pdf` has 19 pages and the evidence page was visually checked.
- `solution_packet.pdf` compiled with `latexmk` without fatal errors.
- All packet pages were rendered and visually inspected.
- Extracted text was checked for both theorem statements, the curvature
  derivative, the rectangle derivative, limitations, and references.

## Checksums

- Raw arXiv source download: `5d4f2ca00d1ec046a67ad10a6ea8f6b8d7ccd13f5ba4ebaa31e6e59607e7716d`
- Compiled source paper: `90541c8f8e5343c1f1db3ff73228cf6fae21c31f3575c0ac325eccb9ed8d4466`
- Open-problem evidence crop: `b9ace6158d91a260fcba537a92b2fdb4b6f465714d80336f1df48f460c503865`
- Final solution packet: `87bef34aa44d108d21bd998237048bb695b978a685406c06b7ad759fce56a097`
