# Malnormal contractions in every matrix dimension

Status: candidate full proof; likely valid; human review recommended.

The packet solves Problem 5.1 of arXiv:2009.11139.  Its quantitative padding
lemma sends a `kappa`-malnormal matrix in `M_m` to a uniformly controlled
malnormal matrix in `M_(m+1)` by the upper-triangular coupling

`[[A,v],[0,M+1]]`.

For contractions a fixed rescaling gives another contraction, with a positive
constant depending only on `kappa`.  Applying the operation at most twice to
the source's uniform `3m x 3m` family fills all sufficiently large dimensions;
nilpotent shifts handle the finite remainder.  The result is one contraction
in every dimension with a common positive malnormality constant.

Files:

- `solution_packet.pdf`: reviewable proof packet.
- `main.tex`: packet source.
- `source_paper.pdf`: official source PDF.
- `figures/problem_crop.png`: exact Problem 5.1 crop.
- `verification.md`: mathematical and presentation checks.
