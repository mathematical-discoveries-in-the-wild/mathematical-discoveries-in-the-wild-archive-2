# Gaussian-section obstruction to common depth

**Status:** candidate partial result, likely valid, pending human review.

**Source target:** Omar Antolín Camarena and Jaime Calles Loperena, *A Center
Transversal Theorem for mass assignments*, arXiv:2401.15095, Problem 2.3,
PDF page 4.

## Result

Let `E -> B` be a rank-`k` Euclidean vector bundle. If
`E^(direct-sum (m-1))` has a nowhere-zero section, then there is no positive
universal simultaneous Tukey-depth bound for `m` mass assignments on `E`.
More precisely, for every `eta>0` there are `m` continuous fiberwise Gaussian
mass assignments such that, at every `b in B` and every `x in E_b`, at least
one of the `m` measures has depth below `eta` at `x`.

For the source's tautological bundle `nu_i` over
`Fl(n_1,...,n_r)`, put

```text
n = n_1 + ... + n_r,
k = n_1 + ... + n_i.
```

The smallest `q` for which `nu_i^(direct-sum q)` has a nowhere-zero section
is exactly `n-k+1`. Consequently, Problem 2.3 has a negative answer in the
strongest uniform-depth sense whenever

```text
m >= n-k+2.
```

## Proof mechanism

Choose a nowhere-zero section `(s_2,...,s_m)` and normalize it so the sum of
the squared fiber norms is one. Use `0,s_2,...,s_m` as the centers of
isotropic Gaussians of variance `sigma^2`. At each fiber, some two centers are
at least `1/sqrt(m-1)` apart, so every candidate point is at distance at least
`1/(2 sqrt(m-1))` from one center. The Tukey depth of a spherical Gaussian at
distance `d` from its center is exactly `Phi(-d/sigma)`, which tends uniformly
to zero as `sigma` tends to zero.

For `nu_i`, project an orthonormal basis of any fixed
`(n-k+1)`-dimensional subspace of `R^n` onto `V_i`. Those projections cannot
all vanish because `dim(V_i^perp)=n-k`. This gives the required section. The
matching lower bound for the number of summands follows from the nonzero class
`w_k(nu_i)^(n-k)`, pulled back from the Grassmannian.

## Scope and novelty

This supplies a broad necessary/negative parameter range and an exact
sectional threshold for the Gaussian-center obstruction. It does not classify
the intermediate range `2 <= m <= n-k+1`, where the source's characteristic-
class existence theorems give some positive cases.

A bounded run-index and arXiv/web search on 2026-08-17 used the source id and
phrases involving mass assignments, Tukey depth, Gaussian centers,
nowhere-zero sections, and `n-k+2`. It found the source and related positive
mass-partition theorems, but no exact negative theorem above. Novelty
confidence is moderate.

## Review focus

The proof is analytic/topological and uses no computation. A reviewer should
check the exact Gaussian halfspace-depth formula, continuity of the Gaussian
assignments in bundle charts, and the pullback/nonvanishing assertion for
`w_k(nu_i)^(n-k)`.

Ledger:
`runs/fa_banach_001/ledger/results/2401.15095_gaussian_section_depth_obstruction.json`.
