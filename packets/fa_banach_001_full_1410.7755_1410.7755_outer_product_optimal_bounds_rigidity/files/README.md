# arXiv:1410.7755 — rigidity of optimal outer-product Riesz bounds

Status: `candidate_full_solution`, pending expert review.

## Result

For a unit-norm frame of `M>N>1` vectors in `F^N`, let `A,B` be the
optimal lower and upper Riesz bounds of the induced rank-one outer products.
The source proves

`A <= M(N-1)/(N(M-1))` and `B >= M/N`

and asks whether frames other than equiangular tight frames can attain the
optimal bounds.  The packet proves that equality in the lower bound alone
forces an equiangular tight frame.  Equivalently, the simultaneous optimal
pair and the minimum possible gap `B-A` are attained exactly by equiangular
tight frames.

Upper-bound equality alone is deliberately not overclaimed: it characterizes
all unit-norm tight frames.

## Files

- `solution_packet.pdf`: rendered candidate full proof.
- `main.tex`: packet source.
- `source_paper.pdf`: source paper compiled verbatim from the run's archived
  arXiv source.
- `figures/source_question_crop.png`: exact crop containing the open question.
- `figures/source_bounds_crop.png`: exact crop containing the source's sharp
  lower-bound argument and ETF equality statement.
- `verify_constants.py`: exact rational audit of the constants and spectra.
- `verification.md`: proof, provenance, novelty, and rendering QA.

The associated result ledger is
`ledger/results/1410.7755_outer_product_optimal_bounds_rigidity.json`.

