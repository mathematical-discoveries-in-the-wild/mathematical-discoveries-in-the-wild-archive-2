# Sparse zero-diagonal compact operators are compact commutators

Status: `candidate_partial_likely_valid`

Source: Sasmita Patnaik and Rahul Sethi, *On Simultaneous
Triangularization of Matrices and Quasinilpotency of Commutator of Compact
Operators*, arXiv:2401.16916, unnumbered Question on PDF page 2.

## Result

This packet proves that a compact operator `T` is a single commutator of two
compact operators whenever, in some orthonormal basis,

1. `T` has zero diagonal, and
2. the undirected graph joining `i` and `j` when either matrix entry
   `t_ij` or `t_ji` is nonzero has uniformly bounded degree.

The first factor is an explicitly constructed compact diagonal operator; the
second has the same sparse support as `T`.  Consequently every compact
finite-band zero-diagonal matrix, every compact unilateral or bilateral
weighted shift, and the stated uniformly finite block-sparse extension is a
compact--compact commutator.  Compact weighted shifts are quasinilpotent, and
when all weights are nonzero they need not be nilpotent, so this gives a
genuine nonnilpotent subcase of the source question.

## Scope

The source asks whether **every** compact quasinilpotent operator is a
commutator of compact operators.  That remains open.  Universal
block-tridiagonal forms have growing block sizes, hence unbounded scalar
support degree; the uniform Schur estimate in this proof then collapses.
Quasinilpotence also does not by itself provide a zero diagonal in a sparse
basis.

## Evidence and verification

- `source_paper.pdf`: arXiv source paper.
- `figures/open_problem_crop.png`: full-width crop of PDF page 2.
- `main.tex`, `solution_packet.pdf`: proof packet.
- `code/check_sparse_commutator.py`: 2,900 finite random regression cases for
  the exact factorization and the denominator estimate.
- `VERIFICATION.md`: independent proof audit and command/results log.

The run indexes and bounded web/arXiv searches on 2026-08-17 used the exact
source question and the phrases `zero diagonal commutator of compact
operators`, `bounded degree sparse matrix compact commutator`, and `compact
weighted shift commutator compact`.  They found the general Pearcy--Topping
literature and classical weighted-shift commutator statements, but no exact
bounded-support-degree compact-factor theorem.  Novelty confidence is
moderate pending expert review.

Human review should focus on the compactness passage for the second factor
and on whether the sparse theorem already appears under different
terminology in the older commutator literature.
