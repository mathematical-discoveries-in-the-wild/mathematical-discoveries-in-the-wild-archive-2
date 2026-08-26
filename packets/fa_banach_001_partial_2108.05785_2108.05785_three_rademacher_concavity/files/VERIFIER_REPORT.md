# Verifier report

Verdict: `likely valid`, pending independent human review.

## Formal proof audit

- The Jenkins--Tkocz Hessian identity has the stated weights
  `r_k r_l E[|S|^(p-2) epsilon_k epsilon_l]` after setting
  `r_k=x_k^(1/p)`.
- Direct enumeration of the eight signs gives the three formulas `(6)`.
- Ordering `r >= u >= v > 0` makes `P,Q` strictly positive, so the only bad
  edge can be `w_23`.
- Minimizing a weighted two-edge path over its middle potential gives the
  exact effective-conductance criterion `c <= ab/(a+b)`.
- In the cone `r >= u+v`, the inequalities `m <= P,Q` imply the criterion.
- In the triangle cone, both ratio inequalities `(8)` were expanded in both
  directions and reduce exactly to `(9)` and `(10)`.
- For `0<q<1`, differentiating at fixed `h` gives
  `d_a g = a^q[(1+t)^(q-1)(1+q+t)-(1+q)]`; its bracket is positive because
  its first term has derivative `q(1+t)^(q-2)(q+t)>0` and initial value
  `1+q`.
- The ratio inequalities sum to the effective-conductance bound precisely
  because `2r-u-v<r` is the triangle condition.
- Continuity extends concavity from the open to the closed positive orthant.

## Computational check

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2108.05785_three_rademacher_concavity/code/check_hessian.py
```

Output:

```text
tested=200000
worst_scaled_min_eigenvalue=-4.238e-16
worst_relative_formula_error=1.440e-13
result=no contradiction
```

This is only a finite contradiction check. The theorem rests on the symbolic
proof in `main.tex`.

## Priority for human review

Check the external Schechtman equivalence used for the corollary and whether
the three-variable theorem is already implicit in older Hanner literature.
