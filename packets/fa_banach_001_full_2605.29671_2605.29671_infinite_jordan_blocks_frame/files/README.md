# Infinitely many nontrivial root blocks in a Parseval operator-orbit frame

Status: **candidate full solution, likely valid; specialist review required**.

This packet answers the open question on PDF page 17 of Eva A.
Gallardo-Gutiérrez and Jonathan R. Partington, *Frame constructions associated
with operator orbits*, arXiv:2605.29671 (2026).

For every fixed integer `m>=2`, it constructs an interpolating Blaschke
product `b` with infinitely many zeros and puts `theta=b^m`. The canonical
orbit

`{S_theta^n k_0^theta : n>=0}`

is a Parseval frame for the model space `K_theta`. Meanwhile the normalized
derivative kernels at the zeros, through order `m-1`, form a Riesz basis of
generalized eigenvectors of `S_theta^*`. The biorthogonal basis gives a Riesz
basis of generalized eigenvectors of `S_theta` itself. Hence there are
infinitely many nontrivial root blocks, all of length `m`.

The proof's main device is a finite upper-triangular cross-Gram operator
between the derivative kernels and the standard model-space Riesz basis
`{b^r e_j}`. Uniform separation of the zeros makes every diagonal block
invertible.

Files:

- `main.tex` and `solution_packet.pdf`: theorem and proof.
- `source_paper.pdf`: local copy of the source paper.
- `figures/open_question_crop.png`: the source question.
- `VERIFICATION.md`: mathematical, source, layout, and novelty checks.

Important scope note: the packet proves nontrivial root blocks and a Riesz
basis of root vectors. It does not claim a uniformly bounded similarity to a
direct sum of canonical unit-superdiagonal Jordan matrices; the normalized
within-block weights tend to zero in this construction.
