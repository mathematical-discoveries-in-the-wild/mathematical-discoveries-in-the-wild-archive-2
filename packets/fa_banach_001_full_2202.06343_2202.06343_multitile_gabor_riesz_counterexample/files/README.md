# A three-cell multi-tile generating a critical Gabor Riesz basis

Candidate new full counterexample for Problems 6.1 and 6.2 of arXiv:2202.06343.

Take

```text
Omega = [0,2) union [3,4),  Lambda = Gamma = Z.
```

Then `Omega` multi-tiles `R` by `Z` at level three but does not tile at level
one. Nevertheless, `G(chi_Omega, Z x Z)` is a Riesz basis for `L^2(R)`. Its
Zak multiplier is `1+z+z^3`, and its exact squared-modulus bounds are

```text
(47-14*sqrt(7))/27 <= |1+z+z^3|^2 <= 9,  |z|=1.
```

This answers Problem 6.2 positively (even with a lattice frequency set) and
the intended tiling-necessity question in Problem 6.1 negatively. It also
contradicts Theorems 1.3 and 1.4 of the source as stated; the packet identifies
the failed continuity inference in their proof.

## Files

- `main.tex`: self-contained proof and audit.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: official arXiv source paper PDF.
- `figures/open_problem_crop.png`: exact Problems 6.1 and 6.2 from page 20.
- `verify_counterexample.py`: independent symbolic/numerical checks.

## Reproduce

From the repository root:

```bash
conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/full/2202.06343_multitile_gabor_riesz_counterexample/verify_counterexample.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=runs/fa_banach_001/solutions/full/2202.06343_multitile_gabor_riesz_counterexample/tmp runs/fa_banach_001/solutions/full/2202.06343_multitile_gabor_riesz_counterexample/main.tex
```

Human review is strongly recommended because the counterexample also reveals
an error in stated theorems of the source preprint.
