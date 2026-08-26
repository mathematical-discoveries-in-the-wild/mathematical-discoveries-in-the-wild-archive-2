# Verification report

Status: candidate full proof; likely valid; human review required.

## Exact target

The passage on source PDF page 4 asks whether `ND[0,1]` is
`(1,c)`-spaceable. The theorem in the packet proves `(n,c)`-spaceability for
every finite positive integer `n`, so it answers the exact question.

## Source theorem check

Hencl, Proposition 2, accepts every continuous increasing
`phi:[0,infinity)->[0,infinity)` with `phi(0)=0`. It supplies a Cantor set `K`
and a linear isometry `T:C(K)->C[0,1]`. For every nonzero input, every point,
and every positive integer `m`, the set on which the increment divided by
`phi(distance)` exceeds `m` has upper density one. The proposition explicitly
includes right-upper density at `0` and left-upper density at `1`.

The proof uses only `m=1` and only the consequence that the density-one set
contains points arbitrarily close to the base point. This is valid at interior
points and at both endpoints.

## Common modulus

For a finite-dimensional `E`, its closed unit ball is compact. A finite
epsilon-net plus uniform continuity of finitely many net points proves uniform
equicontinuity, hence `Omega_E(t)->0`.

The intermediate-point argument proves subadditivity. Therefore
`|Omega_E(s)-Omega_E(t)| <= Omega_E(|s-t|)`, which gives continuity.

Every nonzero member of `E` is nowhere differentiable, so any unit vector in
`E` is nonconstant. Partitioning an interval on which that vector changes by
`delta>0` gives `Omega_E(t) >= delta*t/(L+t)`. Hence `Omega_E(t) >= c*t`
near zero.

## Scale domination

With `phi=sqrt(Omega_E)`, both needed limits are exact:

    Omega_E(t)/phi(t) = sqrt(Omega_E(t)) -> 0,
    phi(t)/t >= sqrt(c)/sqrt(t) -> infinity.

For a fixed `e in E`, the coefficient `||e||` is harmless because
`||e||*Omega_E(t)/phi(t)->0`.

## No cancellation

At a fixed point `z`, select `y_j->z` from Hencl's set for `m=1`. For large
`j`, the prescribed-space increment is at most half the Hencl threshold.
The reverse triangle inequality gives an increment of the sum at least
`phi(|y_j-z|)/2`. Its difference quotient tends to infinity. Thus no finite
derivative exists at `z`. The endpoint density clauses give the identical
one-sided conclusion.

This statement holds for every nonzero Hencl input and every fixed `e in E`.
It also forces the Hencl range to intersect `E` only at zero: otherwise a
nonzero Hencl vector plus its negative in `E` would be the zero function while
the no-cancellation statement would declare it nowhere differentiable.

## Closedness and dimension

The Hencl range `Y` is closed because `T` is an isometry. If `q` is the
quotient by `Y`, then `q(E)` is finite-dimensional and closed, so
`Y+E=q^{-1}(q(E))` is closed. The intersection is zero, hence the sum is
direct.

`C(K)` for a Cantor set has Hamel dimension `c`; therefore the direct sum also
has dimension `c`. Every nonzero direct-sum vector is covered either by the
no-cancellation statement or by the original hypothesis on `E`.

## Novelty bounds

The local run indexes and exact/close web searches found no prior
`(n,c)`-spaceability theorem for `ND[0,1]`. Ribeiro's 2024 thesis was
downloaded and text-searched: its pointwise-spaceability result concerns a
different set, while its ND result is the negative obstruction for infinite
starting dimension. arXiv:2607.15749 (17 July 2026) proves only
`(n,aleph_0)`-lineability by an algebraic construction. It does use a uniform
finite-dimensional modulus, but does not produce a closed subspace, continuum
dimension, or the Hencl perturbation used here.

No computational experiment is part of the proof. Novelty confidence is
moderate pending a specialist review of non-indexed literature.
