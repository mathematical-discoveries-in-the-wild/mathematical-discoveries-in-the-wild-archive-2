# Verification Report

## Verdict

`candidate partial result - likely valid`

The proof removes the finite graph-theoretical restriction on the target for
compact domains. It proves existence, not uniqueness, for arbitrary complete
R-tree targets.

## Source-scope audit

Naor-Sheffield define a metric tree to be the realization of a finite
graph-theoretical tree. Immediately after Theorem 1 they conjecture both that
local compactness of the domain can be dropped and that the target can be a
bounded R-tree. The packet addresses the second direction only, under the
stronger domain hypothesis that `X` is compact. It actually permits an
unbounded complete R-tree because the boundary data generate a compact
subtree.

## Compact-hull audit

Let `A` be compact in a complete R-tree and let `C` be its closed convex hull.
For every epsilon, choose a finite epsilon-net `F` in `A`. The convex hull of
`F` is a finite union of compact geodesic segments. Every point of `conv(A)`
lies on a segment `[a,b]` with `a,b in A`. Replacing the endpoints by nearby
points of `F` moves the corresponding point on the segment by at most epsilon,
using Busemann convexity of R-trees. Thus `conv(A)` is totally bounded. Its
closure is complete because the ambient tree is complete, hence compact.

No properness or local compactness of the ambient R-tree is used.

## Finite-subtree approximation audit

Choose nested finite `1/n`-nets `F_n` in `C` and let `K_n=conv(F_n)`. Each
`K_n` is a finite metric tree. Its nearest-point projection `p_n:C->K_n` is
1-Lipschitz, and

```text
sup_{z in C} d(z,p_n(z)) <= 1/n.
```

Therefore `f_n=p_n o f` converges uniformly to `f` and has Lipschitz constant
at most `Lip(f)`. Applying the source theorem to `f_n` is legitimate because
`X` is a compact, hence locally compact, length space and `K_n` is a finite
metric tree.

## Equicontinuity audit

The finite-tree AMLE `u_n` can be taken with global Lipschitz constant at most
`Lip(f_n)`. This is also recoverable directly: finite trees are absolute
1-Lipschitz retracts, so an isometric extension competitor exists; applying
absolute minimality on `X\Y` controls the interior Lipschitz constant, and a
length-path argument controls pairs meeting `Y`.

Hence the maps `u_n:X->C` are uniformly Lipschitz. Compactness of both `X` and
`C` makes Arzela-Ascoli applicable and supplies a uniformly convergent
subsequence.

## Comparison audit

For `t in C`, let `q=p_n(t)`. The gate property of convex subtrees in an
R-tree gives

```text
d(t,z) = d(t,q) + d(q,z)   for every z in K_n.
```

The source theorem and its comparison characterization imply that
`x -> d(q,u_n(x))` satisfies comparison with distance functions from above.
Adding the constant `d(t,q)` preserves comparison, so `u_n` satisfies
comparison for every target point of the full tree `C`, not just points of
`K_n`.

Uniform limits preserve comparison: a boundary inequality for the limit is a
boundary inequality with an arbitrary additive epsilon for all sufficiently
large approximants. Pass the approximant inequality to the interior and then
let epsilon tend to zero.

Naor-Sheffield explicitly note that the comparison-implies-AMLE direction of
their Proposition 7 works for an arbitrary metric target. Consequently the
uniform limit is an AMLE as a `C`-valued map.

## Ambient-target audit

The compact subtree `C` is closed and convex, so the gate projection
`P_C:T->C` is 1-Lipschitz. If a `T`-valued competitor improves the limit on an
open set, composing it with `P_C` gives a `C`-valued competitor with no larger
Lipschitz constant and the same exterior values. This contradicts absolute
minimality in `C`. Thus the map is also an AMLE with ambient target `T`.

## Edge cases and limitations

- If `Y` is empty, a constant map is an AMLE; the theorem is stated for
  nonempty `Y` to avoid choosing an arbitrary target point.
- If `f` is constant, the construction and conclusion reduce to that constant
  extension.
- Completeness of `T` is used to make the closed, totally bounded convex hull
  compact.
- Compactness of `X` makes `f(Y)` compact and supplies global uniform
  convergence. The proof does not settle arbitrary non-locally-compact
  domains.
- The packet does not prove that every AMLE into an arbitrary R-tree satisfies
  the source's tree-comparison condition, so it does not claim uniqueness.

## Literature audit

The lightweight run indexes and bounded web/arXiv searches on 9 August 2026
found no exact prior statement. Search phrases and scope are recorded in the
README and packet. This is not an exhaustive citation review.
