# Verification report

Verdict: **likely valid partial result; not a solution of the source question**

## Claim checked

Uniformly quasi-greedy, uniformly M-bounded finite-dimensional bases whose
best possible prefix-ordering constants tend to infinity yield, by an
`ell_2`-direct sum, a quasi-greedy Markushevich basis in a Banach space with no
Schauder reordering.

## Adversarial checks

1. **Markushevich property.** Each block is finite dimensional. The algebraic
   union of the blocks is dense in the `ell_2` sum, and the embedded block
   coordinate functionals separate points. Uniform normalization and the
   uniform dual bound make the union a semi-normalized M-bounded system.

2. **Greedy sets really localize.** If `A` is a global greedy set for
   `x=(x_j)`, then `A_j=A cap B_j` is a greedy set for `x_j` inside block `j`:
   every selected coefficient in that block dominates every unselected
   coefficient in the same block. Empty intersections contribute zero.

3. **The quasi-greedy constant does not accumulate across blocks.** The
   squared `ell_2` norm of the global greedy projection is the sum of the
   squared block-projection norms. Applying the common block constant before
   summing gives exactly the same constant `K`.

4. **Every reordering is caught.** A global permutation induces a finite
   permutation in each block. By the definition of `beta(B_j)`, one induced
   prefix has norm at least `beta(B_j)`. At the global position of the last
   coordinate of that prefix, the global initial projection restricted to
   `E_j` is exactly the bad block projection. Hence its operator norm is at
   least `beta(B_j)`.

5. **Schauder conclusion.** Since `beta(B_j) -> infinity`, the initial
   projection norms for every global permutation are unbounded. A fundamental
   minimal system with unbounded partial-sum projections is not a Schauder
   basis in that order.

6. **No hidden full claim.** The proof never constructs the required finite
   blocks. Their existence is precisely the remaining obstacle. No converse
   finite-to-infinite compactness statement is asserted.

7. **Literature status.** arXiv:2510.13693 gives a nonlocally convex
   quasi-Banach counterexample and explicitly leaves the Banach restriction
   open. Exact-phrase and close-variant searches found no statement matching
   this finite-dimensional reduction, but this is not a certified novelty
   determination.

## Reviewer focus

The central two-line estimate and the induced-prefix argument are elementary.
The most useful specialist review is therefore novelty review and assessment
of whether known finite-dimensional quasi-greedy constructions can make
`beta(B_j)` diverge while keeping the quasi-greedy and M-bounds uniform.
