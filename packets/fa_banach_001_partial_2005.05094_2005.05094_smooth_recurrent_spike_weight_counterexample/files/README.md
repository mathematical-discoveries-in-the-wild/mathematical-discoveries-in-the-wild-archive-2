# Smooth recurrent-spike obstruction for the weighted boundary embedding

## Status

`candidate_partial_result_likely_valid`

For the open weight-characterization problem in arXiv:2005.05094, this packet
constructs a nonnegative smooth weight `omega` such that

- `omega(t) -> 0` as `|t| -> infinity`;
- `omega` belongs to every `L^q(R)`, `1 <= q <= infinity`; but
- the critical-line embedding of the Hardy space of Dirichlet series into
  `L^2(omega dt)` is unbounded.

Thus the necessary condition `L^1 cap L^infinity` is not sufficient. In
addition, the symmetric decreasing rearrangement of the bad weight is
admissible by the source paper's positive lemma, so admissibility is not a
rearrangement-invariant property.

## Files

- `solution_packet.pdf`: theorem, proof intuition, rigorous construction,
  and limitations.
- `source_paper.pdf`: arXiv:2005.05094.
- `code/verify_peak_bounds.py`: numerical checks of the normalized truncated
  zeta peak estimate and parameter scaling.
- `verification.md`: provenance and QA record.
