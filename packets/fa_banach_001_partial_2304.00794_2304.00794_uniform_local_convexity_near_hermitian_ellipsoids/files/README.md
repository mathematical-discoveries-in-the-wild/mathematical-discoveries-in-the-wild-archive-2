# Uniform local convexity for complex L_p-intersection bodies

This packet gives a partial answer to the open question in arXiv:2304.00794.

For each complex dimension, one common `C^2` neighborhood of the Hermitian
ellipsoids has the following property: every `S^1`-invariant convex body in
that neighborhood has a convex complex `L_p`-intersection body for every
`-2<p<-1` and every admissible planar body `C`.

The proof normalizes the complex cosine transform by `Gamma(p+2)`, upgrades
the source's `C^0` endpoint convergence to `C^2` using unitary equivariance,
and applies the spherical curvature criterion uniformly on the compact
parameter interval `[-2,-1]`.

The result is partial because no uniform neighborhood covers an arbitrary
balanced convex body, and pseudoconvexity does not prevent one real curvature
from vanishing while its complex partner stays positive.

Build with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -jobname=solution_packet main.tex
```
