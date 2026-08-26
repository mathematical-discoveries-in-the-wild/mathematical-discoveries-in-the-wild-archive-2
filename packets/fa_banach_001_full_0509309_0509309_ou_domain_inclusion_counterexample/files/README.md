# Counterexample to the OU/drift generator-domain inclusion

This packet gives a candidate full negative answer to the question in Section 2
of arXiv:math/0509309: the generator domain of the Ornstein--Uhlenbeck
semigroup on `BUC^circ` need not be contained in the generator domain of the
associated drift semigroup.

The counterexample uses an outward OU semigroup on `ell_2`.  Gaussian-smoothed
indicators of homogeneous cones are OU-harmonic on finite coordinate blocks,
while their drift derivatives grow like the square root of the block
dimension.  A uniformly convergent weighted sum is fixed by the OU semigroup
but cannot have a bounded drift generator.

Files:

- `main.tex`: complete proof.
- `solution_packet.pdf`: rendered candidate full solution.
- `verification.md`: proof, source, novelty, and render audit.
- `source_paper.pdf`: locally compiled from the archived arXiv source TeX.

Status: candidate full counterexample, likely valid; independent expert review
is requested.
