# Counterexample to the unrestricted form of Conjecture 5.11

Status: `candidate counterexample; likely valid; human review requested`

Source: Eduard Roure-Perdices, *Extrapolation via Sawyer-type inequalities*, arXiv:2404.09351v1, Conjecture 5.11 on pp. 31--32.

## Result

The formulation of Conjecture 5.11 allowing every `varsigma > 0` is false. For every `q>1` and `varsigma>1`, set

```text
rho = 1 + varsigma(q-1),
u(x) = |x|^(q-1),
v(x) = 1,
f_N(x) = x^(-1) 1_[1,N](x).
```

Then `u^varsigma=|x|^(rho-1)` belongs to the endpoint restricted Muckenhoupt class `A_rho^R`, so both weight hypotheses hold (take `r=rho`). But the conjectured left side is bounded below by a constant times `(log N)^rho`, whereas the right side is bounded above by a constant times `(log N)^q`. Since `rho>q`, no weight-characteristic-dependent constant can make the estimate hold for all `N`.

This does **not** refute the parenthetical restricted formulation `0<varsigma<=1`; the logarithmic obstruction changes sign exactly at `varsigma=1`, which the source already records as true.

## Files

- `main.tex`, `solution_packet.pdf`: formal result and proof.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/open_problem_crop_page31.png` and `figures/open_problem_crop_page32.png`: the complete two-page statement.
- `verification.md`: independent algebraic and asymptotic audit.
- `code/check_growth.py`: reproducible finite-scale growth check (illustrative only).

Human-review focus: check the elementary endpoint inclusion `|x|^(p-1) in A_p^R` and the Lorentz normalization. Both are proved directly in the packet rather than imported from a classification theorem.
