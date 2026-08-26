# Verification report

Status: candidate full answer, likely valid.

## Symbolic checks

1. Under cone measure, `X_i^p=Y_i/S` with independent
   `Y_i~Gamma(1/p,1)` and `S~Gamma(n/p,1)`.
2. The best `m`-term error in `ell_infinity` is exactly
   `sigma_m(X)_infinity=X^*_{m+1}`.
3. The upper union bound is
   `P(Y_k^*>u)<=binom(n,k)P(Y_1>u)^k`; its logarithm is
   `k log(en/k)-Theta_p(k u)`.
4. In the lower construction, `Y_i in [B t^p,2B t^p]` for `i<=k` and
   `sum_{i>k}Y_i<=D n`.  Taking `B=4D` and `k t^p/n<=1/8` yields
   `nY_i/S>=2t^p`, so the desired strict threshold holds.
5. Fixed Gamma interval probabilities are bounded below by
   `exp(-C_p t^p)`; Gamma Chernoff bounds give both required radial-sum tails.
6. For `p=infinity`, conditioning on the unique maximum of a uniform cube
   vector leaves `n-1` independent uniform coordinate ratios, giving the
   exact binomial formula.

## Computational check

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1009.1751_cone_measure_mterm_concentration/code/check_concentration_scaling.py
```

The script samples normalized Gamma vectors for `p=1/2,1,2`, several `n`, and
several positive `m`.  It reports quantiles of
`X_k^*/[log(en/k)/n]^{1/p}`.  Stable order-one quantiles across dimensions are
the expected regression signature.  This is not part of the proof.

## Novelty bounds

Cheap run indexes and bounded exact-title, arXiv-id, best-m-term
concentration, cone-measure order-statistic, and kth-coordinate searches were
performed through 2026-08-11.  No matching later resolution was found.
General independent-order-statistic concentration results were found, but not
the normalized cone-measure theorem or the matching two-sided exponent above.
Novelty confidence is moderate and requires specialist citation review.

