# Positive non-atomic minimal extrapolations are never unique

Status: `candidate_full_likely_valid` for the explicit uniqueness questions in
Examples 3.8 and 3.9 of arXiv:1601.05761.

## Result

If `Lambda` is finite and contains the zero frequency, no positive non-atomic
measure can be the unique total-variation-minimal extrapolation of its Fourier
data on `Lambda`.  A finite-dimensional real kernel produces a nonzero bounded
density perturbation `h`; the distinct positive measures `(1+h)mu` and
`(1-h)mu` have the same sampled Fourier coefficients and the same optimal norm.

This fully answers both source examples negatively:

- the positive Cantor measure in Example 3.8 is not unique for any finite
  `Lambda` containing zero;
- for the two surface measures in Example 3.9, an explicit second minimal
  extrapolation is obtained by replacing Haar measure on each horizontal
  circle by uniform mass on the five points `j/5`, `j=0,...,4`.

The five-point construction matches the source data for every frequency with
`|m1|<=2`, so it covers both the printed frequency set and the symmetric set
apparently intended by the source's displayed `Gamma`.

## Verification

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1601.05761_surface_measure_minimal_extrapolation_nonunique_full/code/verify_five_point_extrapolation.py
```

The script numerically checks the elementary roots-of-unity identity over a
larger frequency rectangle.  The proof itself is exact and independent of the
script.

Human review should focus on the finite real linear system for `h` and the
scope: the result fully settles the two explicit source uniqueness questions,
while signed or complex singular-continuous measures remain outside the
general theorem.
