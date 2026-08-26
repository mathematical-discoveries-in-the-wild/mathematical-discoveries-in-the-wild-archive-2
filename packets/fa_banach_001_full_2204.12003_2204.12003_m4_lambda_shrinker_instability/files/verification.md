# Verification record

## Statement audited

For Chang's noncircular embedded convex lambda-shrinker `Gamma_m`, if `m` is
even and `m >= 4`, the centrally symmetric region bounded by `Gamma_m` cannot
minimize Gaussian perimeter at its Gaussian volume.  The same holds for
`Gamma_m x R^d`.

## Checks

1. **Source scope.** PDF page 4 of arXiv:2204.12003 explicitly isolates
   `m=2` and `m=4` as the cases for which instability was unclear.
2. **Jacobi field.** Rotational invariance gives
   `L <Qx,N> = 0`; the Gaussian mean is zero by the weighted divergence
   theorem.  Under central inversion the field is even.
3. **Phase equations.** With positive curvature `k` and
   `tau=<x,T>`, differentiation of
   `k=<x,N>+lambda` gives `k'=k tau`; the companion equation is
   `tau'=1+lambda k-k^2` (up to the harmless simultaneous orientation
   convention used by Chang).
4. **Zeros per phase period.** Chang's energy equation has exactly two
   curvature turning points on a nonconstant orbit.  Since `k>0`, these are
   exactly the two zeros of `tau`.  They are simple: a simultaneous zero of
   `tau` and `tau'` is the equilibrium, and ODE uniqueness would force the
   circle.
5. **Closure bookkeeping.** Chang imposes a turning-angle increment
   `2 pi/m` per full phase period.  Hence the closed `m`-fold curve contains
   `m` periods and the rotation field has `2m` nodal domains.  For `m=4`, the
   count is eight.
6. **Instability threshold.** The nodal-domain argument only needs more than
   four domains.  Eight qualifies.  For `m=2` the count is exactly four, so
   this packet makes no claim there.
7. **Products.** On `Gamma_m x R^d`, the rotation field depends only on the
   curve coordinate.  Its nodal domains are the curve domains times the
   connected factor `R^d`, so their number is unchanged; Gaussian integrals
   factor.

## Independent algebraic cross-check

In normal angle `theta`, the curvature satisfies

```text
k_{theta theta} + k = lambda + 1/k,
```

and the curve Jacobi operator becomes

```text
L f = f + k^2 (f_{theta theta} + f).
```

Differentiating the curvature equation shows directly that
`f=k_theta` lies in `ker L`.  Since `k_theta=k'/k=tau`, this agrees with the
rotation calculation and makes the two-zeros-per-period count transparent.

## Novelty check

- Cheap run indexes: no hit for arXiv:2204.12003 or the low-symmetry
  lambda-shrinker problem.
- Exact-title/arXiv searches: only the source paper.
- Focused arXiv searches for `m=4`, `Gamma_4`, four nodal domains, and
  Gaussian-perimeter instability: no later answer located.
- Closest sources checked: arXiv:1410.1782 (Chang construction) and
  arXiv:1705.06643 (Heilman's nodal criterion).

This was a bounded novelty search, not a claim of exhaustive bibliographic
coverage.

## Review risk

The proof is short because it corrects a count before invoking an existing
criterion.  The only material review risk is a convention mismatch in the
meaning of the integer `m`.  Chang's displayed turning-angle formula and
closure argument use precisely `m` full phase periods when
`Delta theta=2 pi/m`, which supports the packet's convention.

