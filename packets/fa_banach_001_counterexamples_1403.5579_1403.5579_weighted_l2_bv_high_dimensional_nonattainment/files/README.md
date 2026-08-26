# High-dimensional nonattainment for weighted L2--BV regularization

This packet gives a full counterexample to Theorem 2.8 of arXiv:1403.5579 in
every dimension `n >= 3`, and proves the repaired theorem for `n <= 2`.

## Contents

- `main.tex` — self-contained proof with Proof Intuition.
- `solution_packet.pdf` — compiled packet.
- `source_paper.pdf` — arXiv:1403.5579, SHA-256
  `d600210abe361fb1f9c56665a41a4d06504647592780363b707776f00e1a526e`.
- `references/source_crop_theorem_2_8.pdf` — exact source pages 7--8 containing
  Theorem 2.8 and the compactness step, SHA-256
  `c5857986835f64beaaac2e3a38a93349542913819b9227cde7155868a7ee6764`.
- `code/verify_scaling.py` — independent arithmetic and exponent check.
- `verification.md` — verification commands and outcomes.

## Result

On `B(0,R) subset R^n`, take

```text
theta(x) = 1 - |x|^(n-1),
g(x) = |x|^(-(n+2)/4),
Tu = integral g u,
v = 1.
```

Normalized characteristic functions of shrinking balls satisfy `Tu_r=1`,
while the weighted quadratic penalty is `O(r^(n/2))` and the weighted BV
penalty is `O(r^((n-2)/4))`.  Thus the infimum is zero.  It is unattained,
because zero weighted quadratic cost forces `u=0` almost everywhere, which
cannot fit `v=1`.

No supporting paper is used beyond the source itself and standard BV facts.
