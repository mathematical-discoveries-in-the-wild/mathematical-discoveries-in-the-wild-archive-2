# Verification report

Status: candidate counterexample, likely valid.

## Symbolic audit

1. With `theta_1=s<p`, `theta_2=...=theta_n=p`, and all
   `beta_j=rho`, the source formulas give
   `1/theta=(1/n)(1/s+(n-1)/p)` and
   `1/q_rho=1/p-rho/n`.
2. Thus `theta<p` and
   `1/theta-1/p=(1/n)(1/s-1/p)=Gamma>0`.
3. For `a=1/p+epsilon`, `0<epsilon<Gamma`, the radial witness has
   gradient density comparable to
   `r^{-1}[log(e/r)]^{-ap}`.  It is integrable because `ap>1`.
4. The Sobolev translation inequality and the trivial large-translation bound
   give, for every finite `r>=1`,
   `(1-rho)^{1/r}||f||_{b_{p,r;j}^rho}=O(1)` uniformly as `rho->1`.
5. Near zero,
   `f*(t)>=c t^{-1/p*}[log(C/t)]^{-a}`.  Since
   `1/q_rho-1/p*=(1-rho)/n`, the Lorentz norm dominates
   `integral exp[-theta(1-rho)u/n]u^{-a theta}du`.
6. Because `a theta<1`, this integral is comparable to
   `(1-rho)^{a theta-1}`.  Therefore the Lorentz norm grows like
   `(1-rho)^{-(Gamma-epsilon)}` while the proposed right side is bounded.

## Computational check

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2306.13938_subp_fine_index_uniform_extension_counterexample/code/check_asymptotic_integral.py
```

The script evaluates the exact incomplete-Gamma expression for the lower-bound
integral in the concrete case `(n,p,s,a)=(3,2,1,7/12)`.  The ratio to the
predicted power converges to a positive constant.  This is a regression check,
not part of the proof.

## Scope audit

The result refutes a constant bounded as `rho->1`.  It intentionally makes no
claim that the embedding fails for a fixed `rho<1`; the source itself notes
that the unnormalized fixed-parameter estimate is known for all fine indices.

## Reviewer focus

The main interpretive point is the uniformity implicit in the source's sharp
factors.  Mathematically, check the rearrangement asymptotic and the change of
variables `u=log(C/t)`; the remaining estimates are standard one-line Sobolev
translation bounds.

