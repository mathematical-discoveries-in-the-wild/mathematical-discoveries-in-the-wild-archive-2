# Literature-Implied Answer (Partial Subcase): Optimal Type-I so-Paving

Status: `literature_implied_answer (partial subcase)`.

Source paper: Sorin Popa and Stefaan Vaes, *Paving over arbitrary MASAs in von
Neumann algebras*, arXiv:1412.0631v3 (2015).

Supporting paper: Mohan Ravichandran and Nikhil Srivastava,
*Asymptotically Optimal Multi-Paving*, arXiv:1706.03737v2 (2017).

## Identified question

Conjecture 2.8(2), page 8 of the source PDF, asks for a universal sharp-order
bound `n_s(x, epsilon) <= C epsilon^-2` for so-paving over arbitrary MASAs.
The source proves in Section 3 that every MASA in a type-I von Neumann algebra
with separable predual is so-pavable, but its matrix-paving input gives only
`O(epsilon^-4)` blocks.

## Literature-implied answer

Ravichandran--Srivastava Theorem 1, page 1, gives a common one-sided paving of
`k` zero-diagonal Hermitian contractions into at most
`18 k epsilon^-2` blocks. Applying it to `T` and `-T` gives two-sided paving
with at most `36 epsilon^-2` blocks. Substituting this result into the source
paper's measurable-selection and finite-compression argument yields, for every
type-I von Neumann algebra `M` with separable predual, every MASA `A subset M`,
every self-adjoint `x`, and `0 < epsilon < 1`,

`n_s(A subset M; x, epsilon) <= ceil(144 epsilon^-2)`.

The factor `4` accounts for centering: the relevant zero-diagonal compression
has norm at most `2||x||`, so the matrix theorem is used at tolerance
`epsilon/2`. The order `epsilon^-2` is optimal uniformly over this class
because it is already necessary for the diagonal MASA.

This is an agent-identified implication. The supporting authors cite
Popa--Vaes in their discussion of multi-paving, but they do not explicitly
state the type-I so-paving consequence above.

## Scope

This settles the quantitative conjecture only for type-I algebras with
separable predual. It does not prove so-paving for an arbitrary MASA in a
non-type-I von Neumann algebra, nor the universal `C epsilon^-2` bound in that
generality. A bounded search on 2026-08-13 found no later resolution of the
general conjecture.

## Files

- `main.tex`: compact theorem, proof of the implication, and scope statement.
- `solution_packet.pdf`: rendered status packet.
- `source_paper.pdf`: arXiv:1412.0631v3.
- `supporting_paper_1706.03737.pdf`: arXiv:1706.03737v2.
- `verification_report.md`: mathematical and rendering checks.

Ledger: `runs/fa_banach_001/ledger/results/1412.0631_optimal_typeI_so_paving.json`.

