# LCA classification for bounded function convolvers

Status: **candidate partial result; likely valid; send to human review**.

Source: Brian E. Forrest, Nico Spronk, and Peter J. Wood, *Operator Segal
Algebras in Fourier Algebras*, arXiv:math/0601509v1; Studia Math. 179 (2007),
277--295.  The questions occur on source PDF page 8, at the end of Section 2.1.

## Result

For every locally compact abelian group `G`, the packet proves the two sharp
equivalences

1. `Conv^infty(G) subset L^2(G)` iff `G` is compact or discrete;
2. the operator-norm closure of `Lambda(Conv^infty(G))` in `VN(G)` is a
   star-subalgebra iff `G` is compact or discrete.

Thus the two elementary positive classes mentioned in the source paper are
exactly the positive classes among all LCA groups.

The proof uses the LCA structure theorem.  An open Euclidean factor is handled
by a quadratic chirp.  In the compact-open case, the construction places
distinct compact-subgroup characters on distinct quotient cosets.  A
fiber-averaging/Riemann--Lebesgue argument proves that the resulting product
projection remains operator-norm distance one from every bounded-function
convolver.

This is a partial result because the source asks about arbitrary locally
compact groups, and the separate question asking for a full description of
the closure is not answered.

## Files

- `solution_packet.pdf`: review packet with theorem and proof.
- `source_paper.pdf`: the original paper.
- `figures/open_problem_crop.png`: source PDF page 8 showing the questions.
- `verification_report.md`: adversarial proof audit.
- `novelty_search.md`: bounded novelty search and limitations.
- `../../../../attempts/0601509_lca_bounded_convolver_classification_attempt.md`:
  three-stage upgrade log.

No computation is used as proof.
