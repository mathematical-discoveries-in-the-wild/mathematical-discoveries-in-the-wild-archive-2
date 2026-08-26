# Verification record

## Claim under review

The first question in Remark 3.3 of arXiv:1912.13057 has a negative answer:
eventual norm continuity cannot replace analyticity in Theorem 3.1's
implication `(i) => (iii)`.

## Decomposed mathematical checks

1. **Nilpotent shift.**  For
   `S(t)g(x)=g(x+t)` when `x+t<=1` and `0` otherwise, direct substitution gives
   `S(s)S(t)=S(s+t)`, strong continuity on `L2(0,1)`, and `S(t)=0` for `t>=1`.

2. **Empty spectrum of its generator.**  The generator is
   `Gg=g'`, with `D(G)={g in H1(0,1):g(1)=0}`.  For every complex `lambda`,
   
   `((lambda-G)^(-1)h)(x)=integral_x^1 exp(lambda(x-s))h(s) ds`.
   
   The integral operator is bounded on `L2`, maps into `D(G)`, and direct
   differentiation verifies both inverse identities.  Thus `rho(G)=C` and
   `sigma(G)` is empty.  Scaling by `2` preserves empty spectrum.

3. **Hilbert decomposition.**  The averaging map `P f=(integral f)1` is a
   real rank-one projection.  Its kernel `F` is a real-invariant separable
   infinite-dimensional Hilbert space, so a complex-linear unitary
   `J:L2(0,1)->F` can be chosen to map real functions to real functions (choose
   real orthonormal bases and complexify).

4. **Semigroup law.**  Relative to `E=span{1} direct-sum F`, the two families
   are `1 direct-sum S(t)` and `1 direct-sum S(2t)`, up to unitary conjugacy.
   Hence they are real `C0`-semigroups.  They equal `P` for `t>=1` and
   `t>=1/2`, respectively.

5. **Distinctness.**  For `g=1` and `h=Jg in F`, at `t=1/4` the complementary
   components are the images under `J` of `1_(0,3/4)` and `1_(0,1/2)`, so the
   two semigroups differ.

6. **Generator spectra and poles.**  The generators are unitarily similar on
   the decompositions to `0 direct-sum G` and `0 direct-sum 2G`.  Their spectra
   are therefore exactly `{0}`.  Near zero their resolvents are
   `lambda^(-1)P` plus an operator-valued entire function, making `0` a simple
   pole in each case.  Hence both spectral bounds equal zero.

7. **Smoothing and positivity.**  With `u=1`, `E_u=L-infinity(0,1)`.  At the
   common time `t0=1`, both ranges are `P E=span{1} subset E_u`.  For every
   nonzero `f>=0`, `P f=(integral f)u` and the integral is strictly positive.
   Thus the first semigroup is uniformly eventually positive and the second
   is uniformly eventually strongly positive with respect to `u`.

8. **Domination versus spectral bound.**  For every `0<f` and every `t>=1`,
   `T_B(t)f=T_A(t)f=Pf>=0`; source assertion (i) holds with the common time
   `1`.  Since both spectral bounds are zero, assertion (iii) fails.

9. **Exact weakened regularity.**  Both semigroups are constant in operator
   norm on `[1,infinity)`, hence eventually norm continuous.  They are not
   analytic: their positive-time operators have nontrivial kernels once the
   shift dies, while a nonzero analytic semigroup is injective at every
   positive time.

## Source and novelty checks

- Exact question visually checked in `figures/open_question_crop.png` against
  source PDF page 9.
- Cheap indexes and the local parsed full-source corpus were searched for the
  arXiv id, exact wording, eventual norm continuity, eventual domination,
  eventual equality, nilpotent shifts, and empty-spectrum/rank-one variants.
- Official arXiv/web searches were run for the same close phrases.  They found
  the source and arXiv:2204.00146, but no exact answer or construction.
- arXiv:2204.00146 Section 4 was inspected directly.  Proposition 4.2 avoids
  smoothing of the dominating semigroup only by assuming a single positive
  orbit lower bound valid for all late times; it does not settle the second
  source question under the original weaker definition.

## Deep-upgrade attempts

1. The tail-equality step in the published proof was isolated.  A Baire
   argument can make the tail time common across the positive cone, but without
   injectivity it cannot recover earlier times.  This exposed the finite-time
   erasure mechanism used in the counterexample.
2. A purely nilpotent example would violate the source's nonempty-spectrum
   assumption.  Adding a common strongly positive rank-one fixed component
   repairs exactly that defect and also supplies the smoothing and positivity
   hypotheses.
3. The second Remark 3.3 question was attacked via strong spectral convergence,
   gauge-norm lower bounds, Baire-category uniformization, and the later
   Proposition 4.2.  The missing implication is precisely from pointwise late
   strong positivity to a time-uniform order constant without `B`-smoothing;
   neither the proof nor a semigroup-compatible spike counterexample closed.

## Build and render checks

- `latexmk -pdf -interaction=nonstopmode -halt-on-error
  -jobname=solution_packet main.tex` completed successfully.
- Final log contains no warnings, undefined references, overfull boxes, or
  underfull boxes.
- `pdfinfo` reports a four-page A4 PDF.
- All four pages were rendered at 150 dpi and inspected individually.  The
  source crop is legible; equations, theorem boundaries, page breaks,
  bibliography, and margins are clean; no clipping or overlap was observed.
- SHA-256 of `solution_packet.pdf`:
  `0a42c571a9f17360f8143c7acdd661bf02618d0d7df1c16f1348dc1f22a26bdd`.
- SHA-256 of `source_paper.pdf`:
  `dc70f7b2cc872afcebf019a8bbd61204df2526c3274f9cbad5d86ee1faab40d6`.
- SHA-256 of `figures/open_question_crop.png`:
  `ff025a452b2adc0d3cd10efea42c42311083e658b1841acdf0a56bc9279f2050`.
