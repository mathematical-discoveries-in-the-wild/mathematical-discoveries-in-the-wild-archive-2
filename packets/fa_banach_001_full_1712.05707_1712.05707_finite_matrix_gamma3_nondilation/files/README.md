# Finite matrix Gamma_3-contractions without unitary dilation

## Status

`candidate_full_solution_likely_valid`

The source asks whether every `Gamma_n`-contraction consisting of commuting
matrices has a `Gamma_n`-unitary dilation. This packet gives a negative answer
for `n=3`.

Finite sections of Pal's known infinite-dimensional non-dilating
`Gamma_3`-contraction remain scalar `Gamma_3`-contractions because all products
of two tuple components vanish. If all finite sections dilated, their complete
spectral-set inequalities would pass to the strong limit, contradicting the
known non-dilation of that limit. In fact, one fixed matrix-polynomial norm gap
shows that every sufficiently large finite section fails to dilate.

The resulting matrices have size `8m x 8m`. The proof is existential in the
threshold `m_0`, but the family itself is completely explicit.

## Files

- `solution_packet.pdf`: theorem, explicit family, and full proof.
- `source_paper.pdf`: arXiv:1712.05707.
- `supporting_paper_1610.00425.pdf`: the published infinite-dimensional
  counterexample used as the limiting obstruction.
- `code/verify_finite_sections.py`: exact/numerical checks of the finite matrix
  relations and compression compatibility.
- `verification.md`: provenance, literature search, and QA record.
