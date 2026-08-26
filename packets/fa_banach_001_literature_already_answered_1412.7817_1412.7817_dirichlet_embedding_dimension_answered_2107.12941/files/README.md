# Dirichlet embedding dimension: explicit later answer

Run: `fa_banach_001`

Agent: `agent_lane_14`

Status: `literature_already_answered (full Dirichlet-space subcase)`

## Original question

Section 7.5 on PDF pages 26--27 of Salomon--Shalit, *The isomorphism
problem for complete Pick algebras: a survey*, arXiv:1412.7817, asks for the
least `d` such that an irreducible complete Pick algebra is isomorphic to
`M_V` for a variety `V` in the `d`-ball, and says the answer is unknown even
for the multiplier algebra of the classical Dirichlet space.

## Explicit later answer

Hartz, *Embedding dimension of the Dirichlet space*, arXiv:2107.12941,
explicitly says that it answers the Salomon--Shalit Section 7.5 question.
Theorem 4.2 on PDF page 16 proves that there are no finite `d` and no subset
`V` of the `d`-ball for which `Mult(D)` is algebraically isomorphic to
`Mult(H^2_d|_V)`.  The universal complete-Pick representation supplies an
infinite-dimensional realization, so the least dimension for the Dirichlet
multiplier algebra is exactly `infinity`.

This answers the Dirichlet-space case completely.  It does not give a general
formula for the embedding dimension of every irreducible complete Pick
algebra.

## Files

- `main.tex`: compact identification note.
- `solution_packet.pdf`: rendered status packet.
- `source_paper.pdf`: arXiv:1412.7817.
- `supporting_paper_2107.12941.pdf`: explicit later answer.
