# Two derivation obstructions for compact quasinilpotent generators

**Status:** candidate substantial partial result, likely valid; human review
requested.

Remark 2.3 of arXiv:1008.5241 asks whether a compact quasinilpotent operator
can be weakly amenable.  This packet does not settle the existence question,
but proves two general obstructions.  For

`A_T = closure span {T^n : n >= 1}`,

weak amenability forces both

`A_T = closure(A_T^2)` and `[B(H),T] intersect A_T = {0}`.

These criteria rule out every nonzero compact unilateral weighted shift and
every Riemann--Liouville fractional integration operator `J_(1/r)` on
`L^2(0,1)`, `r >= 1`.  In particular, the classical Volterra operator is not
weakly amenable, even though the source records it as character amenable.

Files:

- `solution_packet.pdf`: review-ready statements and proofs.
- `main.tex`: complete LaTeX source.
- `source_paper.pdf`: original arXiv paper.
- `supporting_paper_2309.13530.pdf`: later context on radical operator
  algebras.
- `figures/open_problem_crop.png`: source Remark 2.3 and Volterra context.
- `code/crop_source.py`: reproducible source-page crop.
- `tmp/`: LaTeX and rendered-page QA artifacts.

Exact-phrase and current-literature searches found no resolution of the full
question and no statement of these two criteria in this setting.  Novelty
confidence is moderate and provisional.

