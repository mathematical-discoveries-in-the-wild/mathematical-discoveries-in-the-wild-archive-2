# Counterexample to Conjecture 1.1 of arXiv:2105.13356

Status: `candidate_counterexample_likely_valid_needs_human_review`

The packet gives exact integer positive-definite `4 x 4` matrices `A,B` and
`t=15/16` for which

`s(A^t (A #_t B) B^(1-t))` is **not** log-majorized by `s(AB)`.

The decisive comparison is

`s_min(A^t (A #_t B) B^(1-t)) < 235.716 < 235.8 < s_min(AB)`.

Since the two matrices have the same determinant, this reverses the required
prefix-product inequality at `k=3`.  Positivity of `A` and `B`, the lower bound
for `s_min(AB)`, and the matrix-power error bounds are certified by exact
rational arithmetic in `code/certify_counterexample.py`; arbitrary precision
floating point is used only to choose rational ball centers.

Contents:

- `solution_packet.pdf`: review packet with the theorem and proof.
- `source_paper.pdf`: local copy of arXiv:2105.13356.
- `figures/open_problem_crop.png`: Conjecture 1.1 on source PDF page 3.
- `code/certify_counterexample.py`: exact rational ball certificate.
- `code/search_counterexample.py`: reproducible heuristic discovery search.
- `verification.md`: mathematical, computational, literature, and rendering
  audit.

The packet does not claim that dimension four is minimal.  The strict gap also
implies failure for all `t` in some open neighborhood of `15/16`, but no
explicit maximal interval is claimed.

