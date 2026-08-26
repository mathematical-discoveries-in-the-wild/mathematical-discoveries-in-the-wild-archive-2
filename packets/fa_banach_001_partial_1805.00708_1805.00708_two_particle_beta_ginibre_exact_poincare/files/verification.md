# Verification record

## Statement audited

For the law on `C^2` with density proportional to

```text
exp(-a(|z1|^2+|z2|^2)) |z1-z2|^beta,
```

where `a>0` and `beta>=0`, the exact spectral gap is
`a(sqrt(beta^2+4)-beta)`.

## Mathematical checks

1. The map `u=(z1+z2)/sqrt(2)`, `v=(z1-z2)/sqrt(2)` is orthogonal on
   `R^4`, preserves the Dirichlet energy, and factors the law.
2. The center factor has planar Gaussian gap `2a`.
3. The relative generator in angular mode `m` is
   `d_rr + ((beta+1)/r-2ar)d_r - m^2/r^2`.
4. With `alpha_m(alpha_m+beta)=m^2` and `rho=ar^2`, its equation becomes
   the generalized Laguerre equation.
5. The exact relative eigenvalues are `4ak+2a alpha_m`.
6. Fourier completeness and Laguerre completeness exhaust the Friedrichs
   spectrum.  The negative indicial root is excluded by `L^2` or finite
   energy at the collision point.
7. The first nonzero eigenvalue is the `|m|=1,k=0` value
   `a(sqrt(beta^2+4)-beta)`, which is at most the center gap.
8. The corresponding eigenfunctions belong to the weighted form domain;
   collision cutoffs introduce energy tending to zero.

## Exact symbolic checks

`code/verify_spectrum.py` uses SymPy to verify the differential eigen-equation
for `m=0,...,3` and `k=0,1,2`, the reciprocal closed form, the Gaussian
limit, the `a=beta=2` specialization, and an independent gamma-integral
Rayleigh quotient for the proposed extremizer.

Command:

```bash
conda run --no-capture-output -n sandbox python code/verify_spectrum.py
```

Expected output:

```text
checked Laguerre eigen-equation for m=0..3 and k=0..2
gap = a*(-beta + sqrt(beta**2 + 4))
optimal Poincare constant = (beta + sqrt(beta**2 + 4))/(4*a)
source n=2, beta=2 gap = -4 + 4*sqrt(2)
source n=2, beta=2 constant = 1/4 + sqrt(2)/4
```

## Source and novelty audit

- Source PDF page 8 explicitly says that the beta-Ginibre Poincare and
  log-Sobolev constants are unclear.
- Cheap run indexes contain no prior result for arXiv:1805.00708 or this
  exact constant.
- Bounded searches covered the source title/id, beta-Ginibre Poincare and
  spectral-gap terms, two-particle planar Coulomb gases, radial weighted
  Gaussian gaps, and the exact square-root formula.
- The cited planar Coulomb-gas paper arXiv:1706.08776 proves existence and
  discusses bounds, not this exact two-particle diagonalization.

This was a bounded novelty search, not exhaustive bibliographic
certification.
