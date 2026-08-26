# Dense metrizable core forced in every zero-dimensional model

Status: `substantial_partial_likely_valid`, pending human review.

Source: Grzegorz Plebanek, *Musing on Kunen's compact L-space*,
arXiv:2012.01849, final paragraph of Section 4 (source PDF page 10).

## Result

Let `K` be either connected compact `L`-space produced by Construction 3.3
of the source, including the countable-Maharam-type version singled out in
the open question. If `L` is zero-dimensional and `C(K)` is isomorphic to
`C(L)`, then `L` has a dense open metrizable cozero subspace `O`.
Consequently, `F=L\O` is a nowhere-dense zero-set and

`0 -> C_0(O) -> C(L) -> C(F) -> 0`

is exact with `C_0(O)` separable. Thus every possible nonmetrizability of a
zero-dimensional model is confined to the boundary `F`.

The proof is a general ccc localization lemma. The source's isomorphism
theorem and its zero-dimensional reflection theorem give a pi-base of `L`
whose members have metrizable closures. A maximal disjoint subfamily is
countable by ccc and has dense union. Each member is an open F-sigma set,
so their union is cozero as well as metrizable.

## Scope

This does not answer whether such an `L` exists. The remaining obstruction is
the nowhere-dense zero-set boundary, and an arbitrary Banach-space isomorphism
does not preserve the order/normal-measure structure needed to eliminate it.
Six focused full-upgrade attempts and their obstructions are recorded in the
associated attempt note.

## Files

- `main.tex`: theorem, proof, upgrade audit, limitations, and references.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: source reconstructed from the cached arXiv TeX.
- `figures/open_problem_crop.png`: exact final-paragraph source crop.
- `verification.md`: proof and artifact verification.

Ledger: `runs/fa_banach_001/ledger/results/2012.01849_dense_metrizable_core_for_zero_dimensional_models.json`.
