# Verification report

## Verdict

`candidate_substantial_partial_likely_valid_novelty_uncertain`

The proof closes the full one-dimensional missing range `beta>1`. It does not
claim the source's all-dimensional extension.

## Hypothesis audit

Let `I` be an open interval and `f=varphi^(-beta)` a probability density on
`I`, with `varphi>0` convex and `beta>1`.

- Affine rescaling of the variable preserves `h(f)+log ||f||_infinity` and
  puts `||f||_infinity=1`, equivalently `inf varphi=1` and
  `int varphi^(-beta)=1`.
- Finite normalization forces every finite sublevel set of `varphi` to have
  finite length. The layer-cake formulas used below are therefore legitimate.
- The logarithmic moment defining entropy is finite for `beta>1`; convexity
  forces at least linear growth on every unbounded end compatible with finite
  mass.

## Negative-moment lemma

Set `L(t)=|{x in I: varphi(x)<t}|` for `t>=1`.

- Convexity gives `(1-lambda)A_s+lambda A_t subset
  A_((1-lambda)s+lambda t)` for the sublevel intervals `A_t`.
- Length is affine under Minkowski addition of intervals, so `L` is
  nonnegative, nondecreasing, and concave.
- Every such `L` has
  `L(t)=c+a(t-1)+int min(t-1,s-1) nu(ds)` with `c,a>=0` and a positive measure
  `nu`; this follows by integrating its decreasing right derivative.
- Layer cake and Tonelli give exactly
  `(p-1)Z(p)=c(p-1)+a+int(1-s^(1-p))nu(ds)`, where
  `Z(p)=int varphi^(-p)`.
- With `x=p-1`, each `1-exp(-x log s)` is concave. Hence `(p-1)Z(p)` is
  positive concave, and therefore log-concave, on `p>1`.

## Entropy step

- Integrating the convexity inequality for `varphi` and differentiating at
  `t=1` gives `Z(beta+1)>=1-1/beta`.
- For `R(p)=log((p-1)Z(p))`, concavity yields
  `R'(beta)>=R(beta+1)-R(beta)>=0`.
- Since `Z(beta)=1`, this says
  `-Z'(beta)<=1/(beta-1)`.
- Finally `h(f)=-int f log f=-beta Z'(beta)`, giving the sharp bound
  `h(f)<=beta/(beta-1)` in the normalized case.
- Undoing the affine scaling gives
  `h(f)+log ||f||_infinity<=beta/(beta-1)`.

## Equality example

On `(0,infinity)`,

`f_beta(x)=(1+x/(beta-1))^(-beta)`

has total mass and supremum equal to one and entropy
`beta/(beta-1)`. This verifies sharpness for every `beta>1`.

## Computational stress test

`code/negative_moment_probe.py` samples concave piecewise-linear sublevel-radius
profiles in dimensions 2--4 and computes the normalized Mellin transform by
exact integration on every affine segment and tail. It found no numerical
failure in the strip `n<p<n+1`. This does not prove the higher-dimensional
claim and is included only to document the counterexample search.

## Remaining obstruction

For `n>=2`, Brunn--Minkowski only shows that `L(t)^(1/n)` is concave. Taking
its `n`th power destroys the direct positive-concavity representation used in
one dimension. A new inverse-Hölder/localization theorem is needed.
