# Full-solution packet: projection span with no rank-one matrix

Status: **candidate full solution; likely valid; human review required**

Source: Jameson Cahill, Peter G. Casazza, Jesse Peterson, and Lindsey
Woodland, *Phase Retrieval By Projections*, arXiv:1305.6226.

## Question and result

Problem 5.9 asks for phase-retrieving subspaces whose associated projection
span is not the span of any equally large family of rank-one projections.

The packet supplies seven explicit two-dimensional subspaces of `R^4`. Their
rank-two orthogonal projections span a seven-dimensional subspace `S` of
`Sym_4(R)` that contains no nonzero rank-one matrix at all. The orthogonal
complement `K=S^perp` is a three-dimensional Clifford space in which every
nonzero matrix has rank four. Therefore a difference `xx^T-yy^T` in the
measurement kernel, whose rank is at most two, must vanish; this proves phase
retrieval.

## Files

- `main.tex`: self-contained construction and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.jpg`: source page 16 crop containing Problem 5.9.
- `code/verify_matrices.py`: exact symbolic verifier.
- `verification.md`: source, proof, novelty, and rendering audit.

## Review focus

Check the identification of the projection span with `K^perp` and the
rank-one exclusion via the Hopf identity. Both are also checked exactly by
the accompanying script.

Ledger: `runs/fa_banach_001/ledger/results/1305.6226_clifford_projection_span_no_rank_one.json`.
