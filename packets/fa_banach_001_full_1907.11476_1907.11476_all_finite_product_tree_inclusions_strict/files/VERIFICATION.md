# Verification notes

Status: candidate full solution, likely valid pending expert review.

## Logical audit

1. For `phi_t(0)=1`, `phi_t(1)=t`, and `phi_t(n)=0` for `n>=2`, the kernel
   matrix on a graph is entrywise exactly `I+tA`.
2. Kernel positivity is positivity of this quadratic form on every finitely
   supported vector. For locally finite products this is equivalent to
   positivity of the bounded self-adjoint operator `I+tA`.
3. The proof of `||A_(T_q)||<=2sqrt(q)` uses an explicit positive weight
   satisfying `Ah=2sqrt(q)h`; it does not assume the spectral formula.
4. The reverse inequality uses finitely supported radial vectors and computes
   their Rayleigh quotients explicitly.
5. On a product, the adjacency is the sum of the coordinate adjacencies. The
   triangle inequality gives the upper bound; tensor powers of the one-factor
   approximate extremizers give the matching lower bound.
6. Bipartite parity conjugates `A` to `-A`, so the lower spectral edge is the
   negative of the norm. Equivalently, parity-twisted approximate extremizers
   directly show failure above the threshold.
7. If `q'` or `N'` strictly increases, then
   `2N'sqrt(q') > 2Nsqrt(q)`, leaving a nonempty interval of separating `t`.
8. For `q'=infinity`, a center and `M` neighbors give eigenvalue
   `1-|t|sqrt(M)`, which is negative for large `M` whenever `t!=0`.
9. The source already proves `R_+(T_infinity^N)=R_+(T_infinity)` for all `N`,
   completing the equality side of the classification.

## Edge cases

- At `|t|=1/(2Nsqrt(q))`, the operator is positive semidefinite, although not
  bounded below; the upper Schur estimate proves the endpoint.
- Negative `t` has the same criterion by bipartite symmetry, but positive `t`
  alone suffices for separation.
- The theorem assumes `N,N'>=1` and `q,q'>=2` or infinity, exactly as in the
  source notation.

## Optional checker

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1907.11476_all_finite_product_tree_inclusions_strict/code/verify_sparse_witness.py
```

The script checks the exact Rayleigh-quotient formula for several finite
parameters, verifies convergence to `2Nsqrt(q)`, and verifies a negative finite
star eigenvalue in the infinite-degree case. These checks are not part of the
proof.

## Novelty status

The 2026-08-09 bounded search found no result settling all inclusions in the
source's equation (7). Confidence is moderate until a specialist checks the
operator-algebra/tree literature.
