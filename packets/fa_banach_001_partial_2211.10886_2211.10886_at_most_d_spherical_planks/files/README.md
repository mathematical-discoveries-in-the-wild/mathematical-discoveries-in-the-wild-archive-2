# At most d spherical planks

Status: `candidate_substantial_partial_result_likely_valid_needs_human_review`

This packet proves Conjecture 1.15 of arXiv:2211.10886 when the number `N` of
planks is at most the ambient dimension `d`. More generally, it proves the
conjectured total-width bound whenever the plank normals span a proper
subspace of `R^d`.

The key theorem is stronger than the numerical width conclusion: under either
hypothesis, any finite plank cover of the unit sphere automatically covers the
whole unit ball. Bang's plank theorem then gives total width at least `2`.

Contents:

- `solution_packet.pdf`: review packet with the theorem and elementary proof.
- `source_paper.pdf`: local copy of arXiv:2211.10886.
- `figures/source_conjecture_1_15.png`: source Conjecture 1.15 on PDF page 5.
- `code/make_open_problem_crop.py`: reproducible source-statement crop.
- `verification.md`: proof, scope, novelty, and rendering audit.

The unrestricted case remains open. In particular, `d+1` signed halfspaces
can bound a simplex-like complement cell, so the common recession-ray argument
need not extend beyond `N=d`.
