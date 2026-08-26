# Verifier report

Verdict: **candidate full proof, likely valid; promote for expert review.**

## Exact claim

The packet proves both inequalities conjectured at the end of
arXiv:2201.13050 for every `1<r<=2<=q<infinity`, `0<kappa<1`, and every
exponent pair in the two displayed regions.

## Proof audit

1. On a fixed wave annulus away from the cone vertex, the characteristic set
   has `d-2` nonzero principal curvatures. Substituting
   `alpha_bar=1-kappa` into the source's Theorem 4 gives exactly the wave
   region.
2. On a fixed parabolic annulus, the Schrödinger paraboloid has `d-1`
   nonzero principal curvatures. The same substitution gives exactly the
   Schrödinger region.
3. Equality in the curvature thresholds is permitted by the source theorem
   because `alpha_bar<1`, the two vanishing orders differ, and
   `0<kappa<1`.
4. The wave scaling is isotropic with homogeneous dimension `d`; the
   Schrödinger scaling is parabolic with homogeneous dimension `d+1`. In
   both cases the conjectured equality makes the annular constant uniform.
5. For `q>=2`, the output square function is bounded by the `ell2` sum of
   annular Lq norms. Sequence Hölder separates the factors.
6. For `r<=2`, 2-concavity bounds the `ell2` sum of annular Lr norms by the
   Lr square function, which Littlewood–Paley theory bounds globally.
7. The flat `d=2` wave cone is not silently passed through the curved theorem;
   it is treated separately using the one-dimensional normal GN inequality
   and tangential vector-valued Bernstein.

## Adversarial checks

- Ordinary rather than parabolic annuli would not make the Schrödinger
  constants uniform; the proof uses the correct parabolic system.
- The proof does not use endpoint square-function theory at `r=1` or
  `q=infinity`; those exponents are explicitly outside the conjecture.
- Homogeneous decompositions reconstruct Schwartz functions in all relevant
  finite Lp spaces; no zero-frequency polynomial survives.
- Regions away from the characteristic sets are covered by Bernstein plus a
  smooth inverse multiplier.
- Symbolic curvature/scaling and randomized sequence checks pass.

## Human-review focus

Check the use of Theorem 4 and Remark 1(d) of the source on finitely many
unit-annulus pieces, particularly uniformity at equality in the curvature
thresholds. Check the standard anisotropic Littlewood–Paley theorem for the
parabolic dilation. No candidate-specific unproved lemma remains after those
standard inputs.

Bounded searches through 2026-08-13 found no later answer; novelty is not
certified.
