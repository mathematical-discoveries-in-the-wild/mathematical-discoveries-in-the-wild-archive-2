# Vortex obstruction to openness of the density map

Status: `candidate_counterexample_full_likely_valid` for the unqualified
openness question in arXiv:1907.02024.

The source asks whether every sequence of square-root densities converging in
`H^1` to the density of a prescribed wave function can be lifted to wave
functions converging in `H^1`.  This packet gives a negative answer already in
the spinless one-particle sector, in every spatial dimension `d >= 2` (including
the physical case `d=3`).  For one particle the symmetric and antisymmetric
conditions are both vacuous, so the same example applies to both maps.

The base wave function is a normalized compactly supported degree-one vortex

```text
psi(x) = C (x_1 + i x_2) times real cutoffs.
```

Its modulus is approximated in `H^1` by normalized strictly positive cores
`sqrt(x_1^2+x_2^2+epsilon^2)` with the same cutoffs.  If corresponding wave
functions converged to `psi`, division by the positive core would produce
`H^1` circle-valued phases on a central disk.  Every such phase has degree zero
on almost every interior circle, because it has an `H^1` real lifting on the
disk.  Strong convergence on an annulus would instead force convergence to the
vortex phase, whose degree is one.  This is impossible.

The result disproves openness as formulated without an `N >= 2` restriction.
It does not decide the genuinely many-particle versions, where the conditional
phase takes values in an infinite-dimensional unit sphere and this degree
obstruction may disappear.  The main human-review issue is therefore scope:
confirm that `N=1` is included in the source/Lieb formulation being reviewed.

The source PDF and its page-2 open-question crop are included.  The proof is
analytic and uses no numerical computation.

