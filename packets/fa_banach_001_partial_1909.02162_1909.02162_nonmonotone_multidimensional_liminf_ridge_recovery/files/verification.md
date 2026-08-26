# Verification audit

Status: proof audited; no computational contradiction found.

## Constants

The exact energy slicing formula has a factor `1/2` because the
one-dimensional double integral counts both orientations.  The transverse
kernel marginal is

`integral_(R^(d-1)) (h^2+|q|^2)^(-(d+p)/2)dq
 = pi^((d-1)/2) Gamma((p+1)/2)/Gamma((d+p)/2) |h|^(-p-1)`.

Direct sphere integration gives

`gamma_(d,p)=2 pi^((d-1)/2) Gamma((p+1)/2)/Gamma((d+p)/2)`.

Hence the lower-bound and ridge-recovery constants both equal
`c_(d,p)=gamma_(d,p)/2`.

`code/verify_constants.py` numerically checks representative dimensions and
exponents against direct quadrature.

## Slicing audit

- A subsequence realizes the global liminf.
- Integrated sliced `L^p` errors equal the sphere measure times the global
  `L^p` error, so a summable further subsequence converges on almost every
  line.
- Each open line section is a countable union of intervals.  Nonnegative
  cross-component terms may be discarded, the source one-dimensional
  Gamma-liminf applies componentwise, and monotone convergence sums the
  components.
- Fatou is applied only to nonnegative line energies.
- Sobolev/BV slicing gives the exact averaged directional seminorm.  When
  `kappa=0`, the source convention makes the limiting functional identically
  zero, so no false regularity inference is made.

## Ridge audit

- The lifted sequence converges because
  `||u_delta-u||_Lp(I x D)^p=|D| ||g_delta-g||_Lp(I)^p`.
- Enlarging one transverse integration from `D` to all of `R^(d-1)` is valid
  because the integrand is nonnegative.
- The resulting upper bound is exactly `|D| c_(d,p)` times the
  one-dimensional energy.
- The global lower bound applies to arbitrary multidimensional perturbations,
  so the matching value is not merely a restricted-ridge liminf.

## Unresolved verifier focus

No general Gamma-limsup is claimed.  In particular, the packet does not assume
a fundamental estimate for nonmonotone `phi`; that is explicitly identified
as the remaining obstruction.
