# Verification report

Verdict: `partial_result_likely_valid`

## Claim audited

For hyperplane-nondegenerate iid rows, exact Gaussian pairwise Hamming-distance
behavior on every finite set is equivalent to Haar-uniform projective row
direction.  A non-Haar law has a biased two-point set.  Isotropic bounded
subgaussian Rademacher rows already show that the usual linear-universality
hypotheses do not imply unshifted binary universality.

## Proof audit

1. **Projective reduction.** Multiplying a row by a nonzero scalar changes all
   signs by at most one common flip, so every pairwise disagreement indicator
   depends only on the unoriented row line.  This is exact.
2. **Haar sufficiency.** A Gaussian direction is uniform on the sphere, hence
   its line is projective Haar.  Equal projective row laws give equal
   distributions of each per-row cut pattern; iid products give equality of
   the full finite-sample distance array.
3. **Population conversion.** For an even signed measure difference `nu` of
   total mass zero, equality of separation probabilities is exactly
   `integral s_x s_y dnu=0` for all `x,y`.
4. **Odd harmonic recovery.** Funk--Hecke diagonalizes the hemisphere-sign
   transform.  The Rodrigues calculation in the packet proves its eigenvalue
   is nonzero in every odd degree for dimensions at least three.  The Fourier
   square-wave calculation covers dimension two; dimension one is trivial.
5. **Measure determination.** Replacing both sign functions by their integral
   representations shows that `nu` annihilates every product of odd
   harmonics.  For an even spherical polynomial `P`, the identity
   `P=sum_i u_i(u_iP)` writes it as a sum of such products after harmonic
   decomposition of the odd polynomials `u_iP`.  Density of even polynomials
   and evenness of `nu` then imply `nu=0`.
6. **Asymptotic failure.** A non-Haar law must therefore bias at least one
   pair.  The strong law applied to its Bernoulli separation indicators gives
   failure probability tending to one below half the bias.
7. **Rademacher example.** For `0<t<1`, direct sign calculation gives zero
   disagreements for `e_1` and `(e_1+t e_2)/sqrt(1+t^2)`, whereas their
   normalized angle is `arctan(t)/pi`.

No circular dependency or computationally supplied proof step was found.

## Computation

Run from the packet directory:

```bash
conda run --no-capture-output -n sandbox python code/check_gegenbauer_coefficients.py
```

The script checks dimensions 3 through 8 and odd degrees 1 through 9 for
nonzero Funk--Hecke integrals, and enumerates the four two-dimensional
Rademacher rows for several rational values of `t`.  All checks pass.  This is
only a finite sanity check; the Rodrigues and sign arguments in `main.tex` are
the proof.

## Scope and novelty audit

The source question is broader and informal.  The packet resolves only the
exact iid, unshifted formulation; dependent fast maps and rate-comparison
notions remain open.

A bounded search covered the four run indexes and arXiv/web phrases combining
“binary embedding”, “projective space”, “random hyperplane”, “universality”,
and “Funk--Hecke”.  It also checked arXiv:1608.06498 (Gaussian circulant
embeddings), arXiv:1801.08639 (structured quantized embeddings), and
arXiv:1805.09409 (non-Gaussian affine/dithered hyperplanes).  No exact
projective-direction characterization was located.  Novelty confidence is
therefore moderate, not conclusive.

## Human review recommendation

Recommend expert review as a substantial partial result.  Focus on the
Gegenbauer endpoint calculation and the polynomial-spanning step.  Do not
interpret the packet as settling the structured fast-transform part of the
source question.

