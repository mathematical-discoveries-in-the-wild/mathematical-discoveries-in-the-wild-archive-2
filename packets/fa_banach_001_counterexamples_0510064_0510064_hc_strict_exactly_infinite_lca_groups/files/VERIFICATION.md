# Verification Report

Candidate: arXiv:math/0510064, Problem 5.4.7.

## Claim Checked

For an LCA group `G`, the inclusion

`H_c(G) superset H(G) intersection W(G)`

is strict if and only if `G` is infinite. More generally, strictness holds for every infinite maximally almost periodic abelian topological group.

## Verdict

valid

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Source match | valid | Problem 5.4.7 asks exactly when the inclusion is strict and requests a function in the difference. |
| Finite-character neighborhoods | valid | For a finite character map, either its image is finite and the kernel is infinite, or its infinite precompact image has non-isolated identity. Hence every specified identity neighborhood has infinite preimage. |
| Recursive sum separation | valid | At each stage, every possible collision involving the new `x_n` or `y_n` excludes only one of finitely many values. Infinite neighborhoods leave an admissible choice. |
| Character separation | valid | The MAP hypothesis supplies a continuous character nontrivial on every nonzero difference of selected sums. Adding finitely many such characters at each stage separates all sums in the final countable product. |
| Null convergence | valid | Every fixed character is controlled from some stage onward, so both selected sequences converge to the identity in the metrizable product compactification. |
| Closure calculation | valid | After passing to a subsequence, the index pair is constant (giving a point of the support), the first index is constant while the second diverges (giving the corresponding first-sequence point), or both indices diverge (giving the identity). The closure is countable. |
| Hartman membership | valid | The characteristic function on the compactification is discontinuous only on a countable Haar-null set and is therefore Riemann integrable. Its support is meager and null, giving `f in H_0(G) subset H_c(G)`. |
| Non-WAP conclusion | valid | The translate matrix is exactly `1_{n<=m}`, whose two iterated limits are 1 and 0. Grothendieck's criterion rules out weak almost periodicity. |
| LCA classification | valid | Pontryagin duality makes every LCA group MAP. For finite groups every bounded function is continuous and almost periodic, so equality holds. |
| Computational smoke check | valid | `code/verify_z_instance.py` verifies 120 distinct two-term sums and an `8 x 8` upper-triangular translate matrix for an explicit Pell-denominator instance. |

## Counterexample Search

Small cases checked:

- Finite abelian groups: no contradiction; all bounded functions are almost periodic, agreeing with the equality half.
- The explicit `G=Z` construction was instantiated with a rapidly growing subsequence of convergent denominators for `sqrt(2)`.
- Possible collisions between lower- and upper-triangular sums were checked both symbolically in the proof and on the finite instance.

Result:
none found

## External Dependencies

- Continuous characters separate points of LCA groups (Pontryagin duality): standard and used only to pass from the MAP theorem to the LCA classification.
- Grothendieck's double-limit criterion: stated in the source itself.
- The source proves `H_0(G) subset H_c(G)` and gives the equivalent existential realization definition of `H_0(G)`.

## Gaps

No mathematical gap found. The code is only a finite smoke check; the proof of the general recursive construction and the countable-closure argument is analytic and combinatorial.

The classification is claimed only for LCA groups (and, more generally, the stated MAP abelian class), not for arbitrary nonabelian topological groups.

## Confidence

Score: 97/100.

The main review risk is notation transfer between the paper's multiplicative group convention and the additive notation used in the construction. The translate-matrix argument is invariant under that change.

## Human Review Recommendation

send to human

Check the finite-character-neighborhood lemma and the countable closure of the triangular support first; all remaining implications then follow directly from definitions and the source's double-limit criterion.
