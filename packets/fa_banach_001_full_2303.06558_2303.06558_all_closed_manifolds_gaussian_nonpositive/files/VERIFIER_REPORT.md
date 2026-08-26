# Verifier report

## Mathematical audit

The proof has four independent checkpoints.

1. A positive-definite real kernel admits a real Hilbert feature map `Phi`.
2. On a sufficiently short interval of a unit-speed geodesic, ambient
   distance equals parameter distance.  Equality of local Gram matrices then
   gives a well-defined Hilbert isometry from the explicit line-Gaussian
   feature curve to `Phi o gamma`.
3. The explicit curve is entire as an `ell^2(C)`-valued map because the square
   norm of its complex extension is `exp(4 lambda (Im z)^2)`.  Thus the actual
   feature curve is locally real analytic, and its scalar correlations are
   real analytic on the whole parameter line.
4. Analytic continuation from a neighborhood of one time gives
   `<Phi(gamma(a)),Phi(gamma(t))>=exp(-lambda(t-a)^2)` for every real `t`.
   A positive period `L` makes the left side equal to `1` at `a+L`, while the
   right side is strictly smaller than `1`.

The argument never differentiates the Riemannian distance at a cut locus and
does not require the closed geodesic to minimize between distant points.

## Computational consistency check

`code/verify_gaussian_feature_curve.py` evaluates finite truncations of the
explicit feature series for several parameters and pairs of points.  It also
checks the exact squared separation

```text
||psi(0)-psi(L)||^2 = 2(1-exp(-lambda L^2)) > 0,
```

which contradicts any proposed period `L>0`.  All tests pass; exact output is
in `code/verification_output.txt`.

## Boundary

Lyusternik--Fet supplies a nonconstant closed geodesic on every
positive-dimensional closed Riemannian manifold.  Dimension zero is excluded:
finite metric spaces can have nonempty proper positivity ranges.  The result
settles the global qualitative conclusion but gives no quantitative bound on
the number or spacing of sample points needed to witness a negative Gram
eigenvalue at a prescribed bandwidth.
