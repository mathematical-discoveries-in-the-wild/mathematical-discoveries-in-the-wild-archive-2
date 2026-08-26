# Bounded spectral complexity gives rank-metric stability

This packet proves a dimension-free partial affirmative answer to Remark 2 of
arXiv:1708.05338.  For a fixed number of matrices and a fixed bound `M` on the
number of distinct eigenvalues of each normal matrix, pairwise almost
commutation in normalized rank implies proximity to an exactly commuting
tuple.  The result also holds when all but a sufficiently small rank fraction
of every spectrum is concentrated on at most `M` values.

The proof interpolates the adjoint as a polynomial of degree at most `M-1`,
controls polynomial commutators by a telescoping rank estimate, and invokes
the source's star-closed Theorem 6.  An exact normal `4 x 4` example shows why
the more direct adjoint-commutator rank identity does not extend from the
unitary/self-adjoint cases.

Status: `candidate_partial_likely_valid`, pending human review.

Files:

- `main.tex`: exact statement and proof.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: official source PDF.
- `supporting_rank_stability_2024.pdf`: primary later source confirming the
  unrestricted question remained open in 2024.
- `figures/open_problem_crop.png`: Remark 2 on source PDF page 3.
- `code/verify_rank_bounds.py`: exact symbolic checks.
- `VERIFICATION.md`: mathematical, literature, build, visual-QA, and hash
  record.

