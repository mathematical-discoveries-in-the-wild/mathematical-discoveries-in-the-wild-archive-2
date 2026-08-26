# Verification report

## Source audit

- The archived arXiv TeX for math/0509309 was compiled locally because the
  environment declined a fresh network PDF download after its approval quota
  was exhausted.
- The locally compiled source has 14 pages; text extraction locates the exact
  question on PDF page 4, in Section 2.
- The exact question appears immediately after the generator-domain
  characterization in Section 2: the authors state that they do not know
  whether `D(L_(P^circ))` is always contained in `D(L_(R^circ))`.
- The source proves just before the question that the strong-continuity
  subspaces for `P` and `R` in `BUC(E)` coincide.  This is the only source
  theorem needed to place the fixed witness in the common `BUC^circ(E)`.

## Construction audit

1. `E` is an `ell_2`-sum of finite-dimensional blocks of dimensions
   `d_n=2^(4n)` and is a real separable Hilbert space.
2. `A=I` generates `S(t)=exp(t)I`.  The block covariance eigenvalues
   `q_n=2^(-6n)` satisfy `sum d_n q_n=sum 2^(-2n)<infinity`, so `Q` is
   positive trace class and every `Q_t=(exp(2t)-1)Q/2` is a Gaussian Radon
   covariance.
3. On a block, the cone `C_d={z_1>=norm(z')}` is invariant under every
   positive dilation.
4. If `Y~N(0,qI/2)` and the OU step noise has covariance
   `(exp(2t)-1)qI/2`, their independent sum has the law of `exp(t)Y`.
   This proves that the Gaussian-smoothed cone indicator is exactly
   `P`-harmonic.
5. Along the first axis its radial profile is
   `E Phi(r/sigma-T)`, with `T` chi-distributed in `d-1` dimensions.
   Differentiation is justified by the bounded normal density.
6. Gaussian Poincare gives `Var(T)<=1`, hence
   `(E T)^2=(d-1)-Var(T)>=d-2`.
7. Chebyshev gives probability at least `3/4` that
   `|T-E T|<=2`; on this event the normal density is at least `phi(2)`.
   Therefore the radial drift derivative is at least
   `(3/4)phi(2)sqrt(d-2)`.
8. The weighted series with coefficients `2^(-n)` converges uniformly, so
   its sum is bounded uniformly continuous.  Every term is fixed by `P`,
   and contractivity permits passage of `P(t)` through the uniform sum.
9. If a bounded drift generator existed, evaluating its forced pointwise
   derivative on a vector supported in block `n` would give a value at least
   `2^(-n)c sqrt(2^(4n)-2)`, which diverges.  This contradiction excludes
   drift-domain membership.

No logical gap was found in the construction.

## Literature and scope audit

- Cheap run indexes contained no result or attempt for math/0509309.
- Exact-phrase, title, drift-domain, and generator-domain searches were run.
  A citation-metadata query located four later citing works, including the
  2018 and 2020 OU surveys and the 2020 paper on time regularity of generalized
  Mehler semigroups.  Inspection of locally archived primary-source TeX where
  available found use of the source's norm-discontinuity results, not a stated
  answer to this domain question.
- The counterexample settles the unrestricted inclusion negatively.  It does
  not address positive versions under finite-dimensional, elliptic, analytic,
  or maximal-regularity assumptions.
- Because citation databases can be incomplete and the construction is
  elementary once the cone block is identified, novelty confidence is
  moderate rather than high.

## File hashes

- Locally compiled source PDF SHA-256:
  `31f5f5d9ddc4e22b3876bf6fc7a14c57a6df8955cdb90ed4e2eddd51ebe37c54`.
- Final solution packet SHA-256:
  `fb2a057a7c1823371093e60086ab90f431e2f2df1824056ab17ec623fb68ca66`.

## PDF and render audit

- Final packet: 4 letter-size pages.
- Latexmk reached a stable build with no warnings, undefined references,
  overfull boxes, or underfull boxes in the final log.
- The bundled `pypdf` runtime reopened the final PDF and extracted nonempty
  text from all four pages.
- All four pages were rendered with bundled Poppler at 144 dpi after the final
  citation edit and inspected individually.  The status banner, cone formulas,
  covariance calculation, derivative lower bound, block construction,
  theorem, references, and page boundaries are legible.  No clipping, overlap,
  broken glyph, or malformed spacing was found.
