# Verification report

Verdict: candidate full solution, likely valid, suitable for expert review.

## Exact source match

- Source PDF page 3, Remark 1.1: no known W2 estimate for `k<n` under the hypotheses of Theorem 1.1.
- Packet theorem retains those hypotheses without an added regularity, moment, product, or coordinate assumption.
- Conclusion gives the requested product with the actual orthogonal marginal of `mu` and an explicit W2 bound.

## Proof audit

1. Caffarelli: the Brenier Jacobian `A` is symmetric and `0 <= A <= I`; hence `B=I-A` is a positive contraction and `B^2 <= I-A^2`.
2. Coupling marginals: for `G=Y+Z` and independent `Y'`, the vector `p+Y+P_perp T(Y'+Z)` has first marginal `gamma_{p,E}`, second marginal `(P_perp)#mu`, and independent components.
3. Coupling cost: vector Gaussian Poincare bounds the plane displacement by `delta_E`; conditional Gaussian Poincare after resampling bounds the orthogonal displacement by `2 delta_E`. Orthogonality of the blocks gives total squared cost `<=3 delta_E`.
4. Near first chaos: `Var(v_i)=1`, `grad v_i=A q_i`, and energy `<=1+epsilon` imply `E|B q_i|^2<=epsilon`. The Hermite decomposition gives residual gradient energy `<=2epsilon` and `1-epsilon<=|w_i|^2<=1`.
5. Direction error: in the small regime `epsilon<=1/(36k)`, Minkowski gives `||q_i-hat w_i||_2^2<7epsilon` and `||B hat w_i||_2^2<14epsilon`.
6. Conditioning: gradient orthogonality makes the `q_i` mutually orthogonal in vector-valued L2 and Poincare gives each norm at least one. Thus the synthesis map `W` of the `hat w_i` has least singular value at least `1-sqrt(7k epsilon)>1/2`.
7. Trace step: `W W* >= P_E/4`, so positivity gives `delta_E=E tr(B^2 P_E) <=4 sum_i E|B hat w_i|^2 <56k epsilon`.
8. Constants: small regime gives `W2^2<168k epsilon`; large regime uses the universal `W2^2<=3k`. Both imply `W2<=13k sqrt(epsilon)`.
9. Edge cases: `epsilon=0`, `k=1`, and `k=n` are included. The proof's target is strongest where requested, namely `k<n`.

## Computational sanity check

Run:

```text
conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/full/1807.09845_bakry_emery_w2_gaussian_splitting/code/check_constants.py
```

The script verifies the numerical inequalities used in the two epsilon regimes and tests the finite-dimensional PSD contraction/trace inequalities on deterministic and randomized matrices. This is only a sanity check, not part of the proof.

## Reviewer focus

- Confirm the vector-valued conditional Gaussian Poincare step for the resampled orthogonal block.
- Confirm the trace monotonicity `WW*>=P_E/4 => tr(B^2 WW*)>=tr(B^2 P_E)/4` without requiring `B` to preserve `E`.
- Confirm the usual smooth approximation suffices for Sobolev `u_i` and the almost-everywhere Brenier Jacobian.

No hidden conditional dependency was found.
