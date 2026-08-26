# Verification Notes

Status: `candidate_counterexample_likely_valid`

## Checks completed

1. **Geometry.** The attachment intervals are disjoint because
   `r_j = exp(-j^2)` is much smaller than the spacing between `2^{-j}` and
   `2^{-(j+1)}`. The rooms and passages accumulate only at `(0,1)`, their
   heights tend to zero, and their total added boundary length is summable.
   Hence the boundary is a rectifiable Jordan curve.

2. **Neck scaling.** On a room of side `r` joined through a corridor of width
   `w` and length `r`, rescaling to side one gives aspect ratio
   `eta=w/r`. Anchoring at the inlet yields boundary constants of order
   `eta^{-1}`. Returning to physical scale gives exactly
   `(r/w) * inlet_mass + (r^2/w) * energy`.

3. **Critical interval factor.** The estimate
   `||v||_Lp <= C sqrt(p) ||v||_Hhalf` and Hölder with
   `p=2 log(e/delta)` give
   `int_I |v|^2 <= C delta log(e/delta) ||v||_Hhalf^2`.

4. **Trace tail.** With `w_j=r_j^2 log(j+1)`, the inlet contribution is
   bounded by `sum_{j>=J} r_j log(e/w_j)`, which tends to zero. The energy
   contribution is bounded by `1/log(J+1)` times total energy. Thus the trace
   outside a finite core has uniformly vanishing operator norm.

5. **Compactness.** On the square and any fixed finite collection of polygonal
   appendages, ordinary Lipschitz trace compactness applies. Finite-core
   compactness plus the uniform tail estimate proves global compactness.

6. **Min--max calculation.** The room function has energy
   `w_j/r_j=r_j log(j+1)`. Its external room boundary alone has length at
   least `3 r_j`, and the corridor sides add positive mass. Disjoint supports
   make both quadratic forms diagonal, giving
   `sigma_{N-1} <= log(N+3)`.

7. **Weyl contradiction.** At `tau_N=2 log(N+3)`, at least `N` eigenvalues lie
   below `tau_N`, whereas the two-dimensional Weyl law would give only
   `O(log N)`.

## No computational dependency

No finite search, numerical approximation, or symbolic computation is used
in the mathematical proof. PDF rendering and cropping are documentary only.

## Primary human-review focus

Check that the compact embedding is interpreted on exactly the natural
boundary Sobolev completion used in Section 2 of the source paper. The packet
proves the tail estimate first on the dense piecewise-smooth core and explains
its extension to the completion. This is the only technically delicate
functional-analytic passage.
