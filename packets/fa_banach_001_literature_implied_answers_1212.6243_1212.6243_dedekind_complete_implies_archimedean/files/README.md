# Dedekind completeness makes the Archimedean hypothesis redundant

Status: `literature_implied_answer (full answer to the local question)`

Source: D. V. Rutsky, *Remarks on the Riesz--Kantorovich formula*,
arXiv:1212.6243.

## Result

After Proposition 18 the source asks whether Archimedeanness of the codomain
`Y` is necessary. It is not: the proposition already assumes that `Y` is a
Dedekind complete vector lattice, and every such lattice is Archimedean.

If `n y <= x` for every positive integer `n`, then
`n y^+ = (n y)^+ <= x^+`. Let `s = sup_n n y^+`. The tail of this increasing
sequence has the same supremum, and translation preserves suprema, so
`s = y^+ + s`. Therefore `y^+=0`, hence `y<=0`.

Thus the explicit Archimedean assumption can be deleted from Proposition 18
and from the corresponding second case of Theorem 24, without changing their
conclusions.

The result is classified as literature-implied because the only ingredient is
the standard implication “Dedekind complete vector lattice implies
Archimedean.” The paper's broader operator-supremum problem is distinct and is
already recorded elsewhere in this run as answered negatively by Elliott
(2019).

## Files

- `main.tex` and `solution_packet.pdf`: complete proof and scope note.
- `source_paper.pdf`: locally compiled source paper.
- `figures/source_question.jpg`: the exact source question.
- `verification.md`: independent proof audit.

