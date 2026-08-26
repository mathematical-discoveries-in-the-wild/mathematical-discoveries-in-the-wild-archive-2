# Verification report

Status: `candidate_counterexample_likely_valid`

The proof was checked in three independent forms:

1. rank-one projector algebra with `u=(1,0,0)^T`, `v=(1,1,1)^T`, and
   `J=diag(1,1,-1)`;
2. direct entrywise multiplication in the proof packet;
3. exact symbolic evaluation by `code/verify_counterexample.py`.

The symbolic audit confirms:

- `A` and `B` are `J`-Hermitian idempotents;
- `BA` satisfies all four indefinite Penrose equations for `AB`;
- `(AB)^[dagger]=BA=B^[dagger]A^[dagger]`;
- `A^[*]ABB^[*]=AB` is not range Hermitian;
- both identities in Theorem 3.5(iv) fail;
- the two sides of the source rank hypothesis have ranks 1 and 2.

No floating-point computation is used. The only substantive reviewer check is
that the common-weight specialization `M=N=L=J` matches the source's adjoint
convention; it does.

