# Verification notes

Verdict: **likely valid claimed full counterexample**, pending expert review.

The proof was checked at three levels:

1. The source question and definitions were verified in arXiv:1201.4196v1,
   Definition 2.12 and Remark 2.13, page 10; the repeated question after the
   `L_infinity` example was verified on page 15.
2. The new generators were multiplied explicitly. They satisfy
   `T_j S_k = delta_jk I` and `sum_j S_j T_j = I`.
3. Disjoint supports of the standard insertions `V_j` give the exact norm
   identity for every mixed forward combination. The scaling factor vanishes
   only for the zero coefficient vector because the triangular coefficient
   matrix is invertible.

The decisive noncontractivity check is exact:

`T_2 = 2^(1/p) W_2`, so `||T_2|| = 2^(1/p) > 1`.

No computation is required. Human review should focus on the universal
Leavitt-algebra step and confirm that the source question has no implicit
extra hypothesis beyond Definition 2.12.

