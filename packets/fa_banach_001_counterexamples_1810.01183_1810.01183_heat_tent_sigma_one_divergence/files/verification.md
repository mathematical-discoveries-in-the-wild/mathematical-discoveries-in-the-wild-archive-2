# Verification report

status: likely valid candidate full counterexample

## Proof-critical checks

1. Identity coefficients are included in the source setting and give
   `Gamma(t,0)=exp(t Delta)`.
2. The source explicitly states
   `T_sigma^{2,2}=L2(R_+ x R^d, dt dx/t^(1+sigma))`.
3. The factor `sqrt(t)` therefore changes the squared weight to
   `t^(-sigma)dt`.
4. For nonzero Schwartz `f`, `grad exp(t Delta)f -> grad f` in `L2`, and
   `||grad f||_2>0`; hence the time integral diverges for `sigma>=1`.
5. The left side is finite for every `sigma>=0` on Schwartz inputs.
6. For `0<=sigma<1`, Tonelli and Plancherel give the exact constant
   `2^(sigma-1) Gamma(1-sigma)` multiplying the squared Sobolev seminorm.

## Mechanical sanity check

Run from this directory:

```sh
conda run --no-capture-output -n sandbox python code/verify_heat_threshold.py
```

It checks the exact subcritical gamma integral and the predicted logarithmic
or power divergence of the truncated scalar time factor at and above one.
The proof is analytic and does not depend on the script.

## Literature and novelty check

A bounded search on 13 August 2026 used the exact displayed formula, paper
title, and tent/Sobolev terminology. It found the arXiv and published source
(DOI `10.1007/s40072-019-00134-w`), both with the same question, but no later
record of this endpoint correction. The novelty claim is only “apparently new
within the bounded search.”

## Recommended human focus

Check the exponent after inserting `sqrt(t)` into the source's definition of
`T_sigma^{2,2}`. Once it is `t^(-sigma)`, the threshold is immediate.

## Packet QA

- `pdflatex` completed twice with no remaining warnings, undefined references,
  or overfull/underfull boxes.
- Both pages of the final PDF were rendered at 150 dpi and visually inspected;
  the source excerpt, equations, margins, and page break are clean.
- The verification script returned `PASS`, and the result ledger parsed as
  valid JSON with model `GPT5.6`.
- Final packet SHA-256:
  `cc89fa1039960a0bc361aeb8d35eb33029a196cad9dd747afc48fd42b8f89a30`.
