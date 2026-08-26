# Verification report

Verdict: `candidate_partial_likely_valid`

## Formal audit

The proof was checked against the following possible failure points.

1. **Decay of the local scale.** For matrix entries
   `t_ij = <T e_j,e_i>`, the largest entry incident to vertex `i` is bounded
   by `max(||T e_i||, ||T* e_i||)`. Both terms tend to zero because `T` and
   `T*` are compact and `e_i` converges weakly to zero.
2. **No small denominators on support edges.** A proper finite coloring gives
   finitely many distinct rays. Their normalized pairwise separation is
   strictly positive even when the two radial lengths differ.
3. **Boundedness.** The divided matrix has at most `Delta` entries per row and
   column. The Schur test applies with a uniform row/column sum bound.
4. **Compactness.** Given a finite initial vertex set, its neighbor set is
   finite. After truncating beyond all those neighbors, every remaining
   matrix entry has both endpoints in the small local-scale tail. The same
   Schur estimate forces the norm of the discarded tail to zero.
5. **Exact identity.** Entrywise,
   `[A,B]_ij = (lambda_i-lambda_j)b_ij=t_ij`; both diagonals are zero.

No use is made of quasinilpotence in the theorem, so its absence from the
proof is deliberate. It enters only in identifying compact weighted shifts
as a nonnilpotent subcase of the source question.

## Computational regression

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2401.16916_bounded_degree_zero_diagonal_commutators/code/check_sparse_commutator.py
```

Result: 2,900/2,900 random sparse finite matrices passed.  The maximum
operator-norm residual in `T-[A,B]` was below `2e-15`, and every tested edge
satisfied the stated denominator lower bound and quotient upper bound.

This finite check is only a regression test for the algebraic construction.
The infinite-dimensional compactness conclusion is supplied by the formal
Schur-tail proof.

## Limit audit

The argument does **not** cover arbitrary compact quasinilpotents:

- without bounded support degree, row and column sums of the divided matrix
  need not be controlled;
- a change of basis producing zero diagonal can destroy sparsity;
- universal block-tridiagonalization has block sizes growing exponentially,
  so its scalar degrees are not uniformly bounded.

These limitations are stated in the theorem packet and README.
