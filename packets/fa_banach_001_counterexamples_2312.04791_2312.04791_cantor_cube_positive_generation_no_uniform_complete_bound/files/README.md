# Cantor-cube function-system counterexample

Status: `candidate_counterexample_likely_valid`

Question 7.3 of the published version of Adam Humeniuk, Matthew Kennedy, and
Nicholas Manor, *An extension property for noncommutative convex sets and
duality for operator systems* (arXiv:2312.04791; JFA 289 (2025), 111153), asks
whether every positively generated function system is completely
`alpha`-generated for some uniform `alpha > 0`.

The packet gives a negative answer. Let `K={0,1}^N` and

`S={epsilon -> sum_k epsilon_k z_k : z in ell^1} subset C(K)`.

This is a closed, selfadjoint function system because its supremum norm is
equivalent to the `ell^1` norm. It is positively generated because its scalar
positive cone is the coordinatewise positive cone. At every matrix level,
singleton points of the Cantor cube show that the positive cone is likewise
coordinatewise.

The coefficient map from `S` to the matrix ordered space `MIN(ell^1)` in the
source's Example 8.6 is therefore a complete order isomorphism. Both sides are
minimal operator spaces, so scalar norm equivalence makes this a completely
bounded isomorphism. Example 8.6 proves that the target has no finite uniform
complete positive-generation constant. Such a constant would transfer through
the coefficient map, so `S` has none either.

Files:

- `solution_packet.pdf`, `main.tex`: full proof and review note.
- `source_paper.pdf`: exact PDF compiled from the stored arXiv source.
- `figures/open_problem_crop.png`: real crop of source PDF page 24.
- `code/verifier.py`: finite-coordinate norm and cone sanity checks.
- `VERIFIER_REPORT.md`: verification summary and human-review focus.

The construction is nonunital, as permitted by the source's definition of a
function system. It does not address any strengthened unital variant.
