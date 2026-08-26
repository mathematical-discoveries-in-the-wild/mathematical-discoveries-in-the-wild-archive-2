# Nonmonotone multidimensional Gamma-liminf and ridge recovery

Status: `candidate_partial_result_likely_valid`.

This packet gives a substantial partial answer to the higher-dimensional open
question on PDF page 3 of Brezis--Nguyen, arXiv:1909.02162.

Without assuming that the interaction law is nondecreasing, it proves:

- the full multidimensional Gamma-liminf for every target and every
  approximating sequence, with exact coefficient
  `(gamma_(d,p)/2) kappa`; and
- the matching Gamma-limsup at every ridge target `u(te+z)=g(t)` on every
  cylinder `I e + D`, for `p>1` and for `p=1`.

The full arbitrary-target Gamma-limsup remains open.  The packet isolates the
missing step as a monotonicity-free localization/fundamental estimate for a
universal scalar-cell postcomposition across changing affine gradients.

Contents:

- `main.tex` / `solution_packet.pdf`: theorem, proof, and limitations.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: original question on PDF page 3.
- `verification.md`: proof audit and constant checks.
- `novelty.md`: bounded duplicate and later-literature search.
- `code/verify_constants.py`: numerical checks of the transverse constant.

Ledger:
`runs/fa_banach_001/ledger/results/1909.02162_nonmonotone_multidimensional_liminf_ridge_recovery.json`.

Human review should focus on the factor `1/2` in the line decomposition, the
almost-everywhere sliced convergence extraction, and the BV zero-`kappa`
convention.
