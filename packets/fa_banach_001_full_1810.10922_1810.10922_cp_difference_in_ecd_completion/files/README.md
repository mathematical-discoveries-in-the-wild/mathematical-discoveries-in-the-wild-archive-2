# CP differences generate the Hermitian ECD completion

Status: `candidate_full_solution_likely_valid`.

This packet gives a candidate full affirmative proof of the conjecture on
page 23 of M. E. Shirokov, *On completion of the cone of CP linear maps with
respect to the energy-constrained diamond norm* (arXiv:1810.10922v2).

The result states that, for every positive discrete unbounded operator `G`,
each map `Phi` in `Y_G(A,B)` has a representation

```text
Phi = Psi_+ - Psi_-,   Psi_+, Psi_- in F_G^0(A,B).
```

The main device is the compact weight `R=(I+G/E_0)^(-1/2)`. The transform
`hat(Phi)(rho)=Phi(R rho R)` converts the ECD norm into the ordinary diamond
norm up to constants 1 and 2. Compactness of `R` gives finite spectral-corner
approximations. A summable telescoping sequence and normal Wittstock
decomposition produce summable positive and negative CP parts; conjugating
inside each finite corner lifts them to ordinary bounded CP maps. Their ECD
limits belong to `F_G^0` by the source paper's Theorem 1B.

Files:

- `main.tex` — self-contained proof packet source.
- `solution_packet.pdf` — final review artifact after verification.
- `source_paper.pdf` — local copy of arXiv:1810.10922v2.
- `figures/open_problem_crop.png` — source-page crop of the conjecture.
- `verification.md` — mathematical, build, and visual checks.
- `tmp/` — LaTeX and rendering intermediates only.

Review focus: the weighted reverse inequality, normality/norm control in the
Wittstock step, and injectivity of the weighted transform on `Y_G`.

Ledger:
`runs/fa_banach_001/ledger/results/1810.10922_cp_difference_ecd_completion.json`.
