# Verification report

Verdict: `likely valid candidate counterexample`.

## Symbolic audit

1. The norm is equivalent to `ell_1` because the weighted Hilbertian term lies between zero and `||x||_1`.
2. The weighted Hilbertian term is strictly convex because all weights are positive. Equality in the midpoint inequality for the sum norm would force positive collinearity, and equal unit norms then force equality.
3. The `ell_1` distance from `(e_n+e_m)/2` to any basis vector is either 1 or 2. Hence the sites are positively separated; tail indices show the infimum is exactly 1.
4. Both sites have distance 1 from zero by sending their indices to infinity.
5. On `||x||_*<1/2`, every coordinate has absolute value below `1/2`. This validates the two piecewise-linear `ell_1` formulas in the proof.
6. With `n` fixed and `m` tending to infinity, `x_m` and `2^{-m}` both tend to zero. The limiting `P` radicand is smaller than the `A` radicand by exactly `2^{-n}(3/4-x_n)>0`.
7. The comparison holds for every `n`, so taking the infimum gives `d(x,P)<=d(x,A)` throughout the ball.
8. The origin is therefore an interior equality point, which violates the exact boundary and interior conclusions in the source theorem.

No hidden attainment assumption is used. In fact, the nonattainment of both distance-one infima at zero is the mechanism that lets a strict norm emulate the flat `ell_1` geometry asymptotically.

## Computational sanity check

`code/verifier.py` uses only the Python standard library. It tests 12,000 finite dominance comparisons, 500 random strict-midpoint inequalities, and the finite site-separation formula with seed `13034733`.

The numerical check is not a proof. Its purpose is to catch sign, factor-of-two, and indexing mistakes in the displayed coordinate identities.

## Human-review focus

The highest-value review is to recompute the two squared Hilbertian distances and confirm that their difference is `2^{-n}(3/4-x_n)`. The second check is the logical passage from the pointwise comparison for each basis vector to the infimum defining `d(x,A)`.
