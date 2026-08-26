# Verification report

Verdict: `partial_result_likely_valid`

## Mathematical checks

1. The source conjectures are transcribed from page 10 and the crop shows both
   the bounded and compact formulations.
2. The Sarason condition used is only a necessary condition for a bounded
   symbol, which is all the contradiction argument requires.  Both
   `k_zeta^I` and `Ih` lie in `H^2`, so the strip-growth lemma applies to
   their sum.
3. An analytic `H^2` function with essentially bounded boundary real part has
   bounded harmonic real part in the disk.  Carathéodory's derivative
   inequality and radial integration give logarithmic growth with no endpoint
   BMO projection assumption.
4. The `H^2` point-evaluation estimate is
   `|h(z)| <= ||h||_2 / sqrt(1-|z|^2)`.  This makes the correction term
   negligible under the stated small-value hypothesis.
5. For the Blaschke sequence, `1-|a_n|^2` is comparable to
   `exp(-sqrt(n))` and `|1-a_n|` to `1/n`.  Therefore every Ahern--Clark/Cohn
   sum is bounded by a convergent exponential-times-polynomial series.
6. At each Blaschke zero the correction vanishes exactly, and the tangential
   product is `(1/n)(1+sqrt(n))`, which tends to zero.
7. The singular measure has finite mass and satisfies the same finite-power
   moment estimates.  At `z_n=(1-c_n^2)xi_n`, the Poisson contribution of the
   matching atom alone is at least `1/c_n`, so the inner function is
   superexponentially small compared with the `H^2` evaluation loss.
8. The two rank-one operators are compact.  Since every `I C(T)` symbol is
   bounded, lack of any bounded symbol also rules out an `I C(T)` symbol.
9. Membership of the kernels in every finite `H^p` confirms that the examples
   are not detected by the known theorem requiring failure at one fixed
   finite `p>2`.

## Upgrade attempts and obstruction audit

- Attempt 1 compared `C_1(I^2)=C_2(I^2)` with Aleksandrov's equality-of-all-
  exponents characterization.  The boundary two-exponent identity does not
  supply a justified extrapolation to all disk embedding classes.
- Attempt 2 tested normalized point masses, two-point measures, and Clark
  measures.  The strongest elementary estimates reduce to the reproducing-
  kernel/Clark isometry and do not force Bessonov's neighbor-mass conditions.
- Attempt 3 converted Sarason's rank-one criterion into the strip-growth
  theorem.
- Attempt 4 supplied the Blaschke example whose kernel lies in every finite
  Hardy class.
- Attempt 5 deepened this to the zero-free atomic singular example.
- Attempt 6 explored products and orthogonal model-space decompositions as a
  route to a non-one-component inner function satisfying the full bounded-
  symbol property.  The required decomposition at the `H^1` endpoint was not
  bounded, so no counterexample to the universal conjecture resulted.
- The remaining unhandled class includes non-one-component meromorphic inner
  functions with discrete Clark measures and only slowly deteriorating
  geometry.  No credible path from the present strip obstruction to that
  full class remained.

## Novelty and literature bounds

- Searches were run through 2026-08-13 for the exact conjecture, source title,
  bounded/compact symbol equivalence, one-component inner functions, rank-one
  TTO bounded symbols, weak factorization, and Carleson embedding classes.
- arXiv:0909.0131 gives the known fixed-`p` kernel obstruction and examples
  failing some finite `H^p` test.
- arXiv:1009.5123 gives the equivalent Carleson-class and weak-factorization
  conditions and explicitly leaves the one-component converse open.
- The 2016 survey and later expert sources located in the bounded search still
  list the converse as open.  No later paper found states the logarithmic
  strip obstruction or either example with kernel membership in every finite
  `H^p`.
- Novelty is provisional and should be checked by a specialist in truncated
  Toeplitz operators and model spaces.

## Artifact checks

- `source_paper.pdf` opens and has 12 pages.
- `figures/open_problem_crop.png` is readable and shows both source
  conjectures.
- The final five-page LaTeX build is warning-free.
- All five final packet pages were rendered at 170 dpi and visually inspected;
  no clipping, overlap, unreadable crop, or broken reference remains.
