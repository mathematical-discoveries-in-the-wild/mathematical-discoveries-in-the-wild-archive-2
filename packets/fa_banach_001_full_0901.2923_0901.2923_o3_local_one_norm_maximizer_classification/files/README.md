# All local one-norm maximizers on O(3)

This packet gives a candidate full solution to the concrete problem left on
page 8 of arXiv:0901.2923: compute all local maximizers of the entrywise
one-norm on the three-dimensional orthogonal group.

The answer is exact. There are 192 local maximizers, one for each nonsingular
3 by 3 sign matrix. They form a single class under signed row and column
permutations, represented by

\[
\frac13
\begin{pmatrix}
1&2&2\\
2&-2&1\\
2&1&-2
\end{pmatrix}.
\]

Every local maximizer is therefore global and has one-norm 5.

The proof converts the source's positivity criterion into a polar-factor
codebook and classifies the nonsingular 3 by 3 sign matrices by an elementary
binary-tail normalization. The PDF is the authoritative review artifact.

## Files

- solution_packet.pdf — complete expert-facing proof.
- main.tex — packet source.
- source_paper.pdf — locally compiled arXiv source.
- figures/source_problem_page8.png — complete source page containing the
  unresolved statement.
- code/verify_sign_orbits.py — exact enumeration and canonical-matrix checks.
- verification.md — proof, novelty, and render audit.
