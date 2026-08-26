# Literature-implied answers: both continuous-family questions are affirmative

Status: **literature_implied_answer (both open questions, affirmative)**

Source: Mohammed Berkani, *Index of continuous families of bounded linear
operators in Banach spaces and application*, arXiv:2010.07040, PDF page 4,
the two questions after Theorem 1.5.

## Identification

Question 1 follows immediately from the classical Bartle-Graves theorem.  The
quotient map `q:L(X)->L(X)/K(X)` has a continuous nonlinear right inverse
`s`; therefore `s o S` continuously lifts every continuous Calkin-valued
family `S`.  A supporting statement appears as Theorem 5.1 of Messerschmidt,
arXiv:1611.08435, PDF page 14.

Question 2 is also affirmative.  Compactness of the family image lets one
choose finitely many finite-rank approximants at each accuracy.  A single
finite-dimensional subspace containing their ranges and adjoint ranges gives
an orthogonal projection `P` for which the family `P K_x P` is continuous,
finite-rank, and uniformly close to `K_x`.

These are agent-identified implications; the supporting authors did not
explicitly discuss Berkani's questions.

## Files

- `main.tex`: compact status note with both arguments.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: source paper rebuilt from the locally archived arXiv source.
- `supporting_paper_1611.08435.pdf`: supporting Bartle-Graves paper rebuilt from its locally archived arXiv source.

Ledger: `runs/fa_banach_001/ledger/results/2010.07040_bartle_graves_and_uniform_compressions.json`.
