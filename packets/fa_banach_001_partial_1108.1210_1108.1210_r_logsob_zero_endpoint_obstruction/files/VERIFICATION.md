# Verification report

Verdict: `likely valid candidate partial result`.

## Claim checked

For every fixed `0<r<1` and fixed degree `d>=3`, the optimal normalized
`r`-logSob constant of a connected `d`-regular `n`-vertex graph is bounded
below by `c(r,d) log n` for all sufficiently large `n`.  Combined with the
bounded `0`-logSob constants of bounded-degree spectral expanders, this rules
out every equivalence interval in Open Problem (I) that contains zero and a
positive point.

## Independent step check

| Step | Status | Notes |
| --- | --- | --- |
| Source scope | valid | Open Problem (I) is on official PDF page 27; Section 12.2 treats only the `0` versus `1` separation. |
| Exponent choice | valid | With `s=r/2`, both `s` and `s'=s/(s-1)` lie in the admissible interval of source Proposition 6.1. |
| Time conversion | valid | `(C/4) log((1-s')/(1-s))=-(C/2)log(1-s)`. |
| Two-function bound | valid | Reverse Holder and Proposition 6.1 yield `E[f T_t g]>=||f||_s||g||_s`. |
| Singleton normalization | valid | Uniform stationarity gives `E[1_u T_t1_v]=P_t(u,v)/n`, hence exponent `1-2/s=1-4/r`. |
| Distance bound | valid | The standard maximum-degree ball count forces diameter `Omega_d(log n)`. |
| Poisson obstruction | valid | The `I-P` walk has Poisson(`t`) jumps; reaching distance `D` requires at least `D` jumps and the quoted Chernoff bound applies when `t<D`. |
| Expander corollary | valid | Source Lemma 3.1 equates the `0`-logSob and Poincare inequalities up to the displayed factor. |

The proof does not settle intervals contained strictly inside `(0,1)`.

## Computation and render audit

The command

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/1108.1210_r_logsob_zero_endpoint_obstruction/code/verify_expander_algebra.py
```

rechecks the conjugate-exponent, time, singleton exponent, and Chernoff
constant algebra for 15 `(r,d)` pairs.  This is regression evidence only.

`main.tex` was rebuilt from scratch.  Every page of the resulting PDF was
rendered and visually inspected on 2026-08-21; the source crop is full-width
and readable, and no clipping, overlap, missing glyph, or placeholder remains.
