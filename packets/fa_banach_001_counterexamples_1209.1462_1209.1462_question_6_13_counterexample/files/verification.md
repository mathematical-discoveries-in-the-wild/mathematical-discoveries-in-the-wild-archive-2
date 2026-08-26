# Verification record

Date: 2026-08-11

## Symbolic checks

- All six displayed vectors have `ell_1` norm one.
- Six thresholds `2/5` have total squared mass `24/25`.
- The geometric tail has squared mass
  `(3/25) * sum_{k>=1} 4^{-k} = 1/25`.
- At radius `1`, the fourth-root distance bound is
  `2-sqrt(2) < 16/25`, equivalent to `2 > (34/25)^2`.
- At radius `2/5`, the bound is
  `29/25-2sqrt(2)/5 < 16/25`, equivalent to
  `2 > (13/10)^2`.
- Convexity of `1+rho^2-sqrt(2)rho` puts the maximum on
  `[2/5,1]` at one of those endpoints.
- Multiplication by the dominant coordinate modulus `m<=1` only decreases
  the selected diagonal correlation.

## Mechanical checks

Run:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1209.1462_question_6_13_counterexample/code/verify_counterexample.py
```

The script checks the exact rational comparisons and samples a dense grid in
radius and angle as a diagnostic for the covering estimate.

## Source and render checks

- `source_paper.pdf` is the 35-page letter-sized arXiv PDF.
- Question 6.13 appears on source PDF page 33.
- The source question crop was visually inspected and is legible.
- The final packet is rendered from `main.tex`; all pages are visually
  inspected after compilation.
- Final SHA256:
  `a57131a89fa45e53fdae8ec543aa8d550ad85e9db0d0fded971d1e1185da98c1`.

## Scope guardrail

The packet answers Question 6.13 itself.  It makes no claim about the
separate weak-closedness conjecture for which the question was proposed as a
sufficient route.
