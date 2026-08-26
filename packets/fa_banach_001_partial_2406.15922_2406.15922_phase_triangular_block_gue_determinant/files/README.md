# Phase-triangular block-GUE determinant limit

Status: `candidate_partial_result_likely_valid`.

This packet gives a substantial partial answer to Conjecture 1 of Mai--Speicher,
arXiv:2406.15922 (PDF page 17).

The full conjectured determinant limit is proved when fixed left/right changes
of basis make all coefficient matrices upper triangular and every diagonal
coefficient vector is a common complex phase times a real vector.  This covers
the scalar case, all real simultaneously triangularizable pencils, and
non-diagonal triangular systems.  In this class the random block determinant
factors exactly into finitely many scalar GUE determinants.  The packet also
proves, for arbitrary coefficients, convergence of every fixed regularized
determinant and identifies the remaining full-problem obstruction as uniform
logarithmic integrability at the hard edge.

Contents:

- `main.tex` / `solution_packet.pdf`: theorem, proof, reduction, and scope.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source Conjecture 1.
- `verification.md`: line-by-line audit and computational scope.
- `novelty.md`: bounded index/literature search.
- `code/make_open_problem_crop.py`: source-image renderer.
- `code/verify_identities.py`: finite determinant and change-of-basis sanity checks.
- `code/verify_packet.py`: mechanical packet gate.

Ledger:
`runs/fa_banach_001/ledger/results/2406.15922_phase_triangular_block_gue_determinant.json`.

Human review should focus on the affiliated-operator triangular
Fuglede--Kadison determinant lemma and on the exact GUE log-determinant
normalization.

