# Verification report

Verdict: `likely valid candidate counterexample`.

## Statement match

- Source: arXiv:2404.09351v1, Conjecture 5.11, pp. 31--32.
- Refuted scope: the formulation allowing all `varsigma>0`.
- Preserved scope: the alternative restriction `0<varsigma<=1` and the separate Section 8.2 conjecture are not claimed solved.

## Algebra audit

For `rho=1+varsigma(q-1)`, `u=|x|^(q-1)`, and `f_N=x^(-1)1_[1,N]`,

```text
(-q + (q-1)(1-varsigma))/rho
= (-1-varsigma(q-1))/rho
= -1.
```

Thus the maximal input is exactly `x^(-1)1_[1,N]`.

## Weight audit

`u^varsigma=|x|^(rho-1)`. The packet proves directly from

```text
sup_I sup_(E subset I) |E|/|I| * (w(I)/w(E))^(1/p) < infinity
```

that `|x|^(p-1) in A_p^R` for every `p>1`. The interval cases are exhaustive:

1. the interval meets 0;
2. it lies on one side with distance to 0 smaller than its length;
3. it lies on one side with distance at least its length.

The rearrangement lower bound is

```text
integral_E |x|^(p-1) dx >= |E|^p/(p 2^(p-1)).
```

Taking `p=rho` establishes both hypotheses, with the second exponent `r=rho` and `v=1`. The weight characteristics do not depend on `N`.

## Norm audit

- On `[0,N]`, the interval `[0,N]` gives `M(x^(-1)1_[1,N]) >= log(N)/N`.
- The target weight mass is `integral_0^N x^(rho-1) dx=N^rho/rho`.
- Therefore the target weak norm to power `rho` is at least `(log N)^rho/(2^rho rho)`.
- The source distribution bound gives

```text
||f_N||_(L^(q,1)(u)) <= q^(1-1/q)(1+log N).
```

Hence the conjecture would imply `(log N)^rho <= C(1+log N)^q`. Since

```text
rho-q=(varsigma-1)(q-1)>0,
```

this is impossible.

## Stress tests

- `q=2`, `varsigma=2` gives the concrete instance `rho=3`, `u=|x|`: cubic logarithmic growth versus quadratic.
- The mechanism is exactly neutral at `varsigma=1`, agreeing with source Remark 5.12.
- Log-power and nontrivial-`v` variants were explored; neither produced a justified extension to `varsigma<=1`.

## Artifact checks

- `latexmk` completed without errors, warnings, overfull boxes, or underfull boxes.
- The final PDF has 4 A4 pages and parses successfully with Ghostscript.
- All four pages were rendered at 170 dpi and inspected at original detail; no clipping, overlap, broken glyphs, or unreadable evidence crops were found.
- `git diff --check` and ledger JSON validation passed.
- `solution_packet.pdf` SHA-256: `8b41d22b1de281f6e7550f0e87384bcd027648020ba57e7087605d55ba6780c0`.
- `source_paper.pdf` SHA-256: `148bf368a783e59a733b270d759ba5d5e86ac948b3bb7ee6e5efcc3fe14663df`.
