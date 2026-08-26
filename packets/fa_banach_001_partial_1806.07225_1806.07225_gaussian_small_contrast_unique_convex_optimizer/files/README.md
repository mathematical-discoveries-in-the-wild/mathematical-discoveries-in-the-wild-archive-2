# Gaussian small-contrast uniqueness and convexity

Status: `partial_result_likely_valid`

Source: Braxton Osting and Brian Simanek, *A maximal energy pointset
configuration problem*, arXiv:1806.07225, Conjecture 3.8 on PDF page 10.

## Result

Let `Omega` be a bounded convex body, fix a Gaussian bandwidth and a desired
high-density volume fraction `theta` in `(0,1)`, and set

    rho_- = |Omega|^{-1} - theta epsilon,
    rho_+ = |Omega|^{-1} + (1-theta) epsilon.

For all sufficiently small positive `epsilon`, the source's continuous energy
problem has exactly one maximizing density (up to null sets), and its
high-density set is convex.  Thus both conclusions of Conjecture 3.8 hold in
the full-dimensional Gaussian small-contrast regime, for every fixed volume
fraction.

The proof uses the strict curvature of level sets of the Gaussian container
potential and a contraction estimate for the KKT threshold map in the
symmetric-difference metric.

## Scope

- Arbitrary density contrast remains open.
- Kernels beyond the Gaussian are not claimed, although the same proof works
  whenever the reference container potential has a uniformly strictly convex
  selected level and the kernel gives a uniform `C^2` perturbation bound.
- The source explicitly lists the Gaussian, but its written complete-
  monotonicity condition is phrased in `r` rather than `r^2`; this formulation
  mismatch is highlighted in the packet.

## Verification

See `VERIFICATION.md`.  The scripts under `code/` record failed numerical
counterexample reconnaissance only and are not used as proof.
