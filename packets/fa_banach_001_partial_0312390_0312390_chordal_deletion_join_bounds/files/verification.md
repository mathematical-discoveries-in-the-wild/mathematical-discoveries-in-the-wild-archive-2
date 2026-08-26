# Verification notes

Status: `partial_result_likely_valid`

1. **Upper bound.** If `S` is a chordal deletion set and `A` is partial
   positive on `G`, the restriction to `G-S` has a positive semidefinite
   completion by the chordal completion theorem. Retaining all specified
   entries involving `S` and choosing the remaining free entries arbitrarily
   produces a Hermitian completion of `A`. Adding `|S|` rows and columns to a
   PSD principal submatrix creates at most `|S|` negative eigenvalues by
   repeated Cauchy interlacing.

2. **Lower-bound construction remains partial positive.** On each induced
   nonchordal block use the standard partial positive obstruction. Put `1` on
   every unused diagonal and `0` on every other specified edge. Every clique
   principal matrix is a direct sum of clique restrictions of the obstruction
   matrices and scalar `1` blocks, hence is PSD.

3. **Additivity is forced, not assumed.** Pairwise complete adjacency means
   every cross-block entry is specified. Setting those entries to zero makes
   the completed principal submatrix on the union exactly block diagonal.
   Each diagonal block is a completion with at least one negative eigenvalue;
   their negative indices therefore sum. Interlacing transfers the lower
   bound to the full completion.

4. **Exact completion-number-one class.** A nonchordal graph has joined-
   obstruction number at least one. If one vertex deletion makes it chordal,
   the upper bound is at most one, so both bounds equal one.

5. **Computational sanity check.** `code/check_graph_families.py` verifies
   chordal vertex-deletion number one for small cycles. It also verifies that
   the join of two four-cycles has deletion number three, not two. This caught
   and removed a false proposed exact-join corollary before promotion.

The analytic proof does not depend on the checker. The final PDF and source
crop were rendered and visually inspected page by page.
