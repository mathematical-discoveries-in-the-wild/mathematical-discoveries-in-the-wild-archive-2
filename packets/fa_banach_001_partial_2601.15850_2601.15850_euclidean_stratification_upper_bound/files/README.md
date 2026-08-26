# Euclidean stratification improves the Heisenberg-cylinder discrepancy upper bound

Status: `candidate_partial_likely_valid`.

Source: Luca Brandolini, Alessandro Monguzzi, and Matteo Monti, *Quadratic discrepancy estimates for probability measures on the Heisenberg group*, arXiv:2601.15850, page 3 (sharpness question after Theorem 2).

## Result

Let `Q=2n+2`. For normalized Lebesgue measure on a unit-volume Euclidean cube in `H^n`, the source proves a squared `L^2` discrepancy lower bound of order

`N^(1-1/(Q-2))`

and records an upper bound of order `N^(1-1/Q)`. The packet proves the improved upper bound

`N^(1-1/(Q-1))`.

The proof partitions the cube into equal-volume cells of Euclidean diameter `O(N^(-1/(Q-1)))` and samples one point per cell. A variance contribution can come only from a cell crossing the boundary of a test cylinder. Relevant left-translated Heisenberg cylinders are uniformly bounded affine shears of Euclidean cylinders, so their Euclidean boundary layers have volume `O(h)`. Hence only `O(Nh)` cells contribute.

This narrows, but does not close, the sharp-exponent gap:

`N^(1-1/(Q-2)) <= minimal squared discrepancy <= N^(1-1/(Q-1))`.

## Files

- `main.tex`: complete statement and proof.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: page-3 crop of the sharpness question.
- `tmp/`: LaTeX and rendering intermediates.

## Verification and review focus

The argument is deterministic after the probabilistic method and has no computational dependency. The main points for human review are:

1. uniform Euclidean `O(h)` boundary-layer content for all relevant sheared cylinders, including small radii;
2. compactness of the set of translation parameters for which a cylinder boundary can meet the fixed support;
3. whether the source's intended sharpness question restricts to a broader measure class than the Lebesgue subcase treated here.

Novelty confidence is moderate. The stratified-sampling mechanism is standard and close to Brandolini et al. (2019), but the exact `Q-1` dimensional application was not stated in the source and no exact later statement was found in searches through 11 August 2026.

Ledger: `runs/fa_banach_001/ledger/results/2601.15850_euclidean_stratification_upper_bound.json`.
