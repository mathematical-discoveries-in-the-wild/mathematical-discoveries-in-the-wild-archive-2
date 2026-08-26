# Multiblock CAVI contracts by a Gauss--Seidel interaction matrix

Status: `candidate_full_likely_valid`

Source: Rocco Caprio, Adrien Corenflos, and Sam Power, *Wasserstein
Contraction of Coordinate Ascent Variational Inference*, arXiv:2605.30253,
future-work statement on source PDF page 5.

## Result

The source proves a two-block Wasserstein contraction theorem from
Fisher-smoothness and transport-information inequalities, then leaves the
multi-block dynamics for future work.

This packet supplies the systematic-scan extension. If `L_ij` are combined
cross-Fisher smoothness constants and `lambda_i` are the fixed-point
transport-information constants, put `a_ij=L_ij/lambda_i`, split the
nonnegative interaction matrix as `A=A_-+A_+` into strict lower/upper parts,
and set

`G=(I-A_-)^{-1}A_+`.

If `rho(G)<1`, every full sequential sweep contracts a weighted maximum of
the blockwise Wasserstein errors at any rate `q` strictly between `rho(G)`
and one. The theorem includes a local invariant-neighborhood statement and a
parallel-update corollary with comparison matrix `A`. For two blocks,
`rho(G)=L_12 L_21/(lambda_1 lambda_2)`, exactly recovering the source result.

## Evidence and verification

- `source_paper.pdf`: locally rendered canonical arXiv source.
- `figures/open_problem_crop.png`: the source's multiblock future-work line.
- `main.tex`, `solution_packet.pdf`: complete proof packet.
- `code/check_multiblock_contraction.py`: randomized comparison-matrix
  regression.
- `VERIFICATION.md`: proof, scope, and novelty audit.

Eight focused upgrades are recorded in
`attempts/2605.30253_multiblock_cavi_upgrade_attempts.md`.

Bounded run-index and web/arXiv searches on 2026-08-17 found multiblock CAVI
results under strong log-concavity and block smoothness, but no direct
Wasserstein contraction theorem under the source's functional-inequality
framework. Novelty confidence is moderate-high pending expert review.
