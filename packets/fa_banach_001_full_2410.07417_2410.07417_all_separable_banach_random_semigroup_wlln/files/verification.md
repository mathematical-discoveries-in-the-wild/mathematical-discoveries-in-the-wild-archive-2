# Verification report

Status: candidate full solution; analytic proof audited and finite-dimensional
noncommutative sanity checks passed, pending expert review.

## Formal proof checks

1. The exponential-to-Euler remainder is `O((t/n)^2)` per factor. A
   telescoping estimate using the common `exp(rho t/n)` norm bound gives the
   uniform deterministic product error
   `rho^2 T^2 exp(rho T)||x||/(2n)`.
2. In the ordered U-statistic lemma, every disjoint pair of index tuples is
   independent. Only `O_k(n^(2k-1))` of `O_k(n^(2k))` pairs overlap, so an
   indicator-kernel variance is `O_k(1/n)` after normalization.
3. The `L1` approximation error for a kernel replacement `h -> g` is at most
   `binom(n,k)n^-k E||h-g|| <= E||h-g||/k!`; the same `1/k!` controls the
   integral error.
4. Ordered composition is SOT-continuous on a common operator-norm ball. The
   coefficient kernel is therefore strongly measurable and bounded by
   `rho^k||x||`.
5. Both random and limiting coefficients are bounded by
   `rho^k||x||/k!`, so their time-weighted tails are dominated by a single
   exponential series, uniformly in `n` and `t in [0,T]`.

## Computational sanity check

Run from the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2410.07417_all_separable_banach_random_semigroup_wlln/code/verify_euler_ustat.py
```

The verifier uses a three-point distribution of noncommuting real `3 x 3`
matrices. It measures the sample mean of the uniform time-grid error for the
exact semigroup product, the exact-to-Euler replacement error, and the `L1`
errors of ordered coefficients `k=1,2,3`. Numerical evidence is not used in
the proof.

Observed output:

```text
distribution spectral-norm bound rho=0.537238
n  mean_sup_exact  mean_sup_exact_minus_euler  coeff_L1(k=1,2,3)
  4  1.356876e-01  1.543562e-02  1.095015e-01 1.580797e-02 1.320751e-03
  8  9.440303e-02  7.483782e-03  7.641810e-02 1.067172e-02 9.067826e-04
 16  6.853800e-02  3.626133e-03  5.509071e-02 7.321906e-03 7.567419e-04
 32  4.739264e-02  1.764998e-03  3.822648e-02 4.860893e-03 5.413422e-04
 64  3.275834e-02  8.953044e-04  2.679963e-02 3.445548e-03 3.247530e-04
128  2.249639e-02  4.391867e-04  1.820975e-02 2.353371e-03 2.738248e-04
```

## Review priority

The mathematical core is the ordered nonsymmetric U-statistic lemma and its
simple-kernel approximation. The main source-specific issue is terminological:
verify whether the source's bespoke scalar-observation definition of
independence is intended to mean ordinary independence of the operator random
elements. Under the ordinary interpretation, the proof is complete.
