# arXiv:2210.10728 — all finite-band oscillatory Toeplitz matrices have PBF

Status: `candidate_full_solution`, pending expert review.

Source: Amílcar Branquinho, Ana Foulquié-Moreno, and Manuel Mañas,
*Positive bidiagonal factorization of tetradiagonal Hessenberg matrices*,
arXiv:2210.10728, question on printed page 21.

## Result

Every oscillatory pentadiagonal Toeplitz–Hessenberg matrix admits a positive
bidiagonal factorization (PBF), answering the exact source question
affirmatively.  More strongly, every oscillatory lower Hessenberg Toeplitz
matrix with any fixed finite number of subdiagonals admits the prescribed
ordered PBF.

Edrei–Schoenberg writes the Toeplitz generating polynomial as a product of
positive linear factors.  This initially gives the bidiagonal factors in the
wrong order.  A quotient–difference exchange moves the upper factor past each
lower factor.  Its diagonal after `m` exchanges is
`h_{n+1}(beta_1,...,beta_m)/h_n(beta_1,...,beta_m)`, where `h_n` is complete
homogeneous.  The defining recurrence for `h_n` proves the exchange identity,
and every resulting bidiagonal parameter is strictly positive.

## Files

- `solution_packet.pdf`: rendered proof packet.
- `main.tex`: self-contained packet source.
- `source_paper.pdf`: official arXiv source paper.
- `figures/open_problem_crop.png`: full-width source screenshot of the question.
- `verification.md`: mathematical and novelty audit.
- `code/verify_pbf.py`: exact rational verifier for multiple bandwidths.

Associated attempt: `attempts/2210.10728_toeplitz_qd_refactorization_full.md`.
