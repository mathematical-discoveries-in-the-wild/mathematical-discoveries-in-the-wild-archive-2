# Verification report

Verdict: `candidate_full_likely_valid`

## Formal audit

1. **Coordinate response bound.** Transport-information for `mu_i^*` and
   combined Fisher-smoothness give
   `e_i(new) <= sum_{j != i}(L_ij/lambda_i)e_j(input)`.
2. **Sequential bookkeeping.** In a systematic sweep, coordinates `j<i`
   are new and `j>i` are old, so
   `e^{k+1} <= A_- e^{k+1} + A_+ e^k`.
3. **Positive triangular inverse.** `A_-` is nilpotent and nonnegative;
   therefore `(I-A_-)^{-1}=sum_{r=0}^{m-1} A_-^r` is nonnegative and the
   preceding inequality yields `e^{k+1}<=G e^k`.
4. **Perron weighting.** For `rho(G)<q<1`,
   `w=(I-G/q)^{-1}1>0` and `Gw=q(w-1)<=qw`. The weighted maximum norm thus
   contracts by `q`.
5. **Local invariance.** An initial weighted ball strictly inside the product
   neighborhood stays inside it during every hybrid partial sweep; the same
   row inequality closes induction over coordinates and sweeps.
6. **Parallel variant.** Jacobi updates contain only old errors, yielding
   `e^{k+1}<=Ae^k` and the same spectral argument with `A`.
7. **Two-block reduction.** For update order 1 then 2,
   `G=[[0,a12],[0,a21*a12]]`; its spectral radius is the source's product
   `L12*L21/(lambda1*lambda2)`.
8. **Scope.** The proof uses combined multiblock Fisher-smoothness, not merely
   separate pairwise relative-Fisher estimates with changing reference
   measures. This distinction is explicit in the packet.

## Computational regression

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2605.30253_multiblock_cavi_gauss_seidel/code/check_multiblock_contraction.py
```

The script checks random nonsymmetric nonnegative interaction matrices,
direct sequential sweeps, Perron weights, and the two-block identity. It is a
regression for matrix orientation and constants, not a proof.

Result: 25,000/25,000 matrix cases, 100,000/100,000 error-vector cases, and
20,000/20,000 two-block reductions passed. The maximum sequential-recursion
residual was `8.327e-17`; the maximum two-block spectral-radius residual was
`1.421e-14`.

## Novelty and scope audit

- Exact source and keyword searches were performed on 2026-08-17.
- Existing multiblock CAVI papers found in the source's citation neighborhood
  use strong log-concavity/block-smoothness and relative-entropy convergence.
- No direct multiblock Fisher-smoothness plus transport-information theorem
  with the Gauss--Seidel Wasserstein comparison matrix was found.
- The packet does not cover random scan, nonsmooth blocks, or derivation of
  the combined smoothness constants in a concrete model.
- Human review should focus first on whether a proposed application satisfies
  the exact combined smoothness inequality.
