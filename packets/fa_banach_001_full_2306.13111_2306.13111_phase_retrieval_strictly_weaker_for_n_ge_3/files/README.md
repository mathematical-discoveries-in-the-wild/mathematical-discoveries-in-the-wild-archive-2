# Phase retrieval is strictly weaker than universal sorting for n at least 3

This packet gives a candidate full implication-level answer to the open
relationship question in the conclusion of arXiv:2306.13111.

## Result

For every n at least 2, injectivity of the sorting encoder beta_A implies real
phase retrieval by alpha_A.  The implication preserves every admissible pair
of bi-Lipschitz constants through an explicit scaled-isometric slice.

For every d at least 2 and n at least 3, the converse is false.  More strongly,
every real phase-retrieval frame with the minimal 2d-1 columns fails to be a
universal sorting key.  Therefore every universal key in this regime requires
at least 2d templates.

Together with the source theorem, this gives the exact logical relationship:
equivalence for n=2 (and trivially for d=1), but strict one-way implication
for n at least 3 and d at least 2.

## Proof mechanism

The one-way implication inserts x as the antipodal row cloud
(x,-x,0,...,0).  Both the quotient metric and the encoder norm acquire the
same factor sqrt(2).

For strictness, partition a full-spark 2d-1 frame into blocks of sizes
d-1,d-1,1.  Normals to the first two blocks are scaled into three nonzero
vectors r1,r2,r3 summing to zero, with every frame vector orthogonal to one of
them.  The clouds {r1,r2,r3} and {-r1,-r2,-r3} consequently have identical
sorted projections but are not row permutations.

## Files

- main.tex: theorem, proof intuition, complete proof, literature comparison,
  scope, and novelty audit.
- solution_packet.pdf: compiled expert-facing packet.
- verification.md: proof, computation, source, and render audits.
- source_paper.pdf: source paper arXiv:2306.13111.
- supporting_2510.22186.pdf: 2026 follow-up whose numerical section observed
  the minimal-frame failure in dimensions 2, 3, and 4 without proving it.
- code/verify_switching_construction.py: exact symbolic checks on Vandermonde
  full-spark frames in dimensions 2 through 8 and checks of the metric slice.

Status: candidate full result, likely valid.  Independent human review is
requested, especially for the universal minimal-frame switching construction
and the interpretation of the source's broad relationship question.
