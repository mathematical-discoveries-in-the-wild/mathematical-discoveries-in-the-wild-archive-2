# Verification report

status: likely valid candidate full counterexample

## Proof-critical checks

1. The balls of radius `a_n/4` around `+/- a_n e_n` are pairwise disjoint.
2. On the `n`th bump pair, the `k`th derivative is bounded by a constant
   times `r_n a_n^(1-k)=(log(n+1))^(k-1)/sqrt(n)`, which tends to zero for
   each fixed `k`. All derivative jets therefore extend continuously by zero
   at the unique accumulation point.
3. The first derivative is globally bounded, so the resulting Frechet
   `C^infinity` map is globally Lipschitz; every higher derivative is also
   globally bounded.
4. For `p_n=2^(1-n)`, `P(X=+/-a_n e_n)=p_n/2` is a probability law with
   compact support closure `{0} union {+/-a_n e_n}`, and
   `C_XX e_n=lambda_n e_n` with `lambda_n=p_n a_n^2>0`.
5. For `Y=f(X)`, the scalar-response cross-covariance vector is
   `b=sum lambda_n r_n e_n`; hence `C_XY C_YX=b tensor b`.
6. Testing a proposed domination on
   `x^(N)=sum_(n=2)^N (r_n/lambda_n)e_n` forces
   `sum_(n=2)^N 1/n<=beta`, contradicting divergence of the harmonic series.
7. Independent centered noise has zero cross-covariance with `X`, so it does
   not change the obstruction.

## Mechanical sanity check

Run from this directory:

```sh
conda run --no-capture-output -n sandbox python code/verify_atomic_covariance.py
```

The script checks normalization, finite support-separation samples, derivative
envelopes, and the exact finite-dimensional quadratic-form ratios. It is a
sanity check; the all-`n` statements are proved analytically in the packet.

## Literature and novelty check

A bounded search on 13 August 2026 used the exact paper title, the displayed
covariance inequality, and the terms covariance bounds, range inclusion, and
nonlinear infinite-dimensional regression. It found the source and nearby
operator-learning papers but no later resolution of this question or this
smooth atomic counterexample. The novelty claim is therefore only
“apparently new within the bounded search.”

## Packet QA

`solution_packet.pdf` has three pages. It was compiled twice after the final
source edit with no LaTeX warnings, rendered at 150 dpi, and every page was
visually inspected. SHA-256:
`99744c449a08fc76fa8df5f72f0720757730d67bb3f001fedbb283956f751aa7`.

## Recommended human focus

Check the removable-singularity argument for the infinite family of smooth
bumps and the covariance orientation. The packet also gives a direct
finite-support quadratic-form contradiction independent of pseudoinverses.
