# Verification note

Verdict: literature-implied answers to all three source problems.

Checks performed:

1. The source PDF is arXiv:1008.0780v2; page 11 contains all three problems.
2. Abels–Manoussos arXiv:1108.1123, Table 3 on PDF page 11, lists `2n` for
   complex `n x n` Toeplitz matrices and `n+1` for real Toeplitz matrices.
3. Singular generators cannot reduce these numbers because every product
   containing a singular triangular Toeplitz matrix has last coordinate zero;
   a dense orbit restricted to `{x_n != 0}` therefore comes entirely from the
   invertible subtuple.
4. The invertible Toeplitz group acts simply transitively on `{x_n != 0}` via
   `A -> A e_n`, so dense semigroup generators give a hypercyclic tuple.
5. For Problem 3, the common complex eigenvector exists by successively
   restricting the commuting family to invariant eigenspaces. Its real and
   imaginary parts give a nonzero invariant real subspace of dimension at
   most two, proper for `n >= 3`.

Human review should focus on items 3–4, which are the identification needed
to pass from the supporting paper's invertible Toeplitz group to the source's
unrestricted matrix tuples.
