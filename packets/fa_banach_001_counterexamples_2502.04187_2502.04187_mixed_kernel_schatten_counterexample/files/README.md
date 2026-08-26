# Mixed-kernel Schatten estimate fails below p=2

Result type: `counterexample`

Status: candidate counterexample, likely valid pending expert review.

Source paper:

- Dimitris Michail Gerontogiannis and Bram Mesland, “Ideal quantum metrics
  from fractional Laplacians,” arXiv:2502.04187v1 (2025).
- Open question: Remark 2.18, PDF page 20.
- Local source: `source_paper.pdf`.
- Source evidence: `figures/open_problem_crop.png`.

## Claimed contribution

For every `1 < p < 2`, the packet constructs a binary Ahlfors-regular
ultrametric Cantor space and a locally constant real function `h` whose
fractional commutator kernel violates the paper's displayed mixed-kernel
Schatten estimate (2.12).

The infinite-dimensional kernel reduces exactly to a 4x4 antisymmetric
matrix.  As the ultrametric ratio tends to zero, this matrix tends to the
matrix having every strict upper-triangular entry equal to one.  Its singular
values are `sqrt(2)+1` and `sqrt(2)-1`, each twice, and a one-variable
monotonicity argument proves strict failure for every exponent below two.

An additional Hadamard construction shows that for arbitrary real
antisymmetric kernels no replacement estimate with a dimension-free constant
depending only on `p` can hold.

## Scope caveat

The result disproves the exact constant-one inequality (2.12), including its
narrow fractional-commutator interpretation.  It does not disprove an estimate
with an additional constant depending on `p` and the geometry, and therefore
does not rule out the source's desired `ell=1` conclusion by a different
argument.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source page containing (2.12) and Remark
  2.18.
- `code/verify_counterexample.py`: finite-matrix checks; not part of the proof.
- `verification.md`: commands, outputs, and review priorities.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Literature and novelty check

A bounded local and web search on 17 August 2026 checked the current arXiv
record (still v1), the exact remark and equation, and ultrametric,
fractional-commutator, and mixed-norm Schatten variants.  No later resolution
or this special four-cylinder example was found.  Delgado--Ruzhansky's 2021
survey records classical below-two obstructions for general kernels, but not
the fractional-commutator construction here.  Novelty confidence is moderate
pending specialist review.

## Human review focus

Please check:

- the ultrametric cylinder distances and the six matrix entries;
- the finite-rank reduction and normalization by 4;
- the interpretation of “inequality (2.12)” as the exact displayed
  constant-one estimate rather than an estimate up to an unspecified factor.

