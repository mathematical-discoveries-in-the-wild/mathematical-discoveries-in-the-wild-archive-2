# Verifier report

Date: 2026-08-13

Status: `all_sanity_checks_passed`

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2507.07256_endpoint_ritt_square_weak11_counterexample/code/verify_counterexample.py
```

Key output:

```text
PASS: exact s=1 target block masses exceed 1/8 for m=1,2
PASS: future interference bound 0.000002000002... leaves block margin >1/32
PASS: past interference is bounded by a convergent exp(-10^6 k) series
sample n=         1: multiplier variation=1.999998000000e-06 <= 2/e
sample n=   1000000: multiplier variation=7.357585144421e-01 <= 2/e
sample n=1000000000: multiplier variation=1.998001043866e-03 <= 2/e
PASS: sampled Ritt multiplier variations satisfy the analytic ceiling
PASS: the weak-type obstruction exponent is positive for every sampled s<2
ALL SANITY CHECKS PASSED
```

## What was checked

- High-precision evaluation of the exact geometric block mass for the first
  two lacunary levels at `s=1`.
- The analytic future-level interference bound and its margin over `1/32`.
- Sampled total variations of the Ritt multiplier coefficients at six time
  scales through `n=10^9`.
- Positivity of the growth exponent `1/s-1/2` at five points in `[1,2)`.

## What remains analytic

The checker is not the proof.  The packet proves operator-norm convergence on
the infinite product space, the variation estimates for every `n`, the block
lower bound for every real `1<=s<2`, the infinite interference bounds, and
the weak-type contradiction for arbitrary large `N`.

## Manual audit

- The martingale multiplier summation-by-parts identity was expanded at
  finite truncation before passing to operator norm limits.
- The coefficient sequence of `I-T^n` is decreasing, and that of
  `nT^n(I-T)` is unimodal; these are the exact hypotheses used in the
  bounded-variation estimates.
- The integer blocks are disjoint because `L_(m+1)=10^6 L_m`.
- Past levels decay exponentially in `delta_j/delta_m`; future levels sum as
  a geometric series.
- The pointwise lower bound holds on all of the probability space, so no
  exceptional-set estimate is hidden in the weak-type contradiction.

Human review recommendation: check Lemma 1 and equations (7)--(8) in the
packet first.  No computational or unproved conditional dependency remains.

