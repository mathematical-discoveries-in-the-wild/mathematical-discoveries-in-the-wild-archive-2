# General isotropic polynomial L2 bound: negative literature answer

Status: `literature_already_answered (full negative answer to the unrestricted version)`

## Source question

Itay Glazer and Dan Mikulincer, *Anti-concentration of polynomials: dimension-free covariance bounds and decay of Fourier coefficients*, arXiv:2108.04268, page 4 after Theorem 2, asks whether its dimension-free lower bound

```text
integral f^2 dmu >= C_d coeff_d(f)^2
```

continues to hold for general isotropic log-concave measures, possibly after imposing suitable symmetries.

## Later answer

The same authors' later paper, *Anti-concentration of polynomials: L^p balls and symmetric measures*, arXiv:2603.22664, page 38, Section 5.1 and Proposition 5.1, gives a full negative answer without extra symmetry. Let `mu_n` be the product of two isotropic Euclidean-ball measures in `R^n`, and set

```text
f_n(x) = (sum_{i=1}^n x_i^2 - sum_{i=n+1}^{2n} x_i^2) / sqrt(2n).
```

Then `mu_n` is isotropic and log-concave, `f_n` is homogeneous quadratic with `coeff_2(f_n)=1`, but

```text
integral f_n^2 dmu_n = Var(f_n) = 4/(n+4) -> 0.
```

Thus no dimension-free positive constant exists for arbitrary isotropic log-concave measures.

## Scope

The vague symmetry-qualified direction in the 2021 question is not refuted. The 2026 paper formulates a precise `H_n`-invariant version as Conjecture 1.4 and proves low-degree cases; that conjecture remains separate. The run already has a partial packet for its parity-separated subcase.

## Files

- `main.tex`: compact identification note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:2108.04268.
- `supporting_paper_2603.22664.pdf`: the later counterexample paper.

Ledger: `runs/fa_banach_001/ledger/results/2108.04268_general_isotropic_polynomial_l2_counterexample_2603.22664.json`.
