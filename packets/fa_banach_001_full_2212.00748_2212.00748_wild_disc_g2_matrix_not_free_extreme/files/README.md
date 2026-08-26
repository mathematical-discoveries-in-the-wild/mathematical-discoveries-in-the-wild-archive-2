# Exact non-free matrix extreme point for the two-variable wild disc

Status: **candidate full result, likely valid; novelty cautious; human review
requested**.

This packet settles the specific conjecture in Section 5.3 of the current
manuscript associated with arXiv:2212.00748. It constructs real symmetric
`8 x 8` matrices `(X,Y)` in the wild disc such that `(X,Y)` is matrix extreme
but not free extreme.

The construction is exact:

- `X` and a rank-three defect factor `Z` are rational;
- the second coordinate `Y` is a symmetric solution in a certified rational
  ball of `Y^2 = I-X^2-Z^T Z`;
- a contraction argument proves that `Y` exists;
- an exact rational inverse-residual certificate proves that a fixed
  `108 x 108` minor of the matrix-extreme system remains invertible at `Y`;
- the Arveson system has 15 equations in 16 unknowns, so the point is not
  Arveson extreme and therefore not free extreme.

Floating point is used only to propose rational approximate inverses. Every
proof-critical residual and inequality is recomputed using Python integers and
`Fraction` arithmetic. The final rank-stability product is below `9.824e-7`.

Files:

- `main.tex`: self-contained construction and proof.
- `solution_packet.pdf`: compiled five-page review packet.
- `source_paper.pdf`: authors' January 24, 2024 manuscript.
- `figures/open_problem_page17.png`: readable source evidence showing the
  open problem, exact wild-disc formulation, and conjecture.
- `code/verify_wild_disc_certificate.py`: exact certificate builder/checker.
- `code/verification_output.txt`: output of the successful exact run.
- `verification.md`: mathematical, computational, source, and rendering audit.
- `tmp/`: LaTeX and rendering intermediates.

Reproduce the exact certificate from the repository root with:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2212.00748_wild_disc_g2_matrix_not_free_extreme/code/verify_wild_disc_certificate.py
```

Human review should prioritize the translation of the source paper's Theorem
2.6 into the three block equations, the max-norm perturbation bound
`2176/21`, and an independent certificate run. A specialist citation-database
search is also appropriate before any novelty claim is circulated.
