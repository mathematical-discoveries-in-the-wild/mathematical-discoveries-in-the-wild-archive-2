# Verification record

## Mathematical checks

- The source question was checked against page 2 of arXiv:2002.05230v3.
- Pairwise commutation after finite-block truncation follows because distinct
  binary sequences occupy distinct tensor coordinates on every sufficiently
  late source block.
- Every finite signed Boolean word has nonzero range on every sufficiently
  late block; since there are infinitely many such blocks, its rank is
  infinite.
- Consequently the essential joint spectrum of the commuting projections is
  the full binary cube, and the binary series has spectrum and essential
  spectrum `[0,1]`.
- The only external structural input is the classical Weyl--von
  Neumann classification of bounded self-adjoint operators modulo compacts.
  Both compared operators have essential spectrum `[0,1]` and no isolated
  spectrum outside it, so its hypotheses match exactly.
- The weak-closure limitation is explicit: endpoint evaluation on
  `C([0,1])` has many state extensions to diffuse `L_infinity`, including
  nonmultiplicative convex mixtures.

## Computational check

`code/check_boolean_core.py` constructs small tensor-coordinate projection
models using exact integer ranks and rational dyadic sums.  It passed 1,534
checks covering all pairwise commutators, every signed Boolean word through
six generators, and all dyadic values through depth eight.

## Artifact checks

- `source_paper.pdf`: 11 pages.
- `source_question.pdf`: one extracted source page.
- `solution_packet.pdf`: three pages, compiled twice with `pdflatex` through
  `latexmk` with no warnings.
- The final PDF was rendered to RGB PNG at 170 dpi, and every rendered page
  was visually inspected after the last compilation.
