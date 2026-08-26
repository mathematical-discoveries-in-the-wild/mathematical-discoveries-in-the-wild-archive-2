# Strictly positive ground state for arXiv:2109.05465

Status: `candidate_full_affirmative_answer_likely_valid`

Laptev and Schimmer ask whether the lowest eigenfunction of
`W_V(b)=2 cosh(bP)-V` can be chosen strictly positive when
`0 <= V in L^1(R)` and the whole discrete spectrum lies in `[-2,2)`.

The packet answers yes and proves more: the lowest eigenvalue is simple, and
its eigenspace is spanned by a continuous function that is strictly positive
at every real point. At the lowest eigenvalue, the compact Birman--Schwinger
operator has spectral radius one by eigenvalue counting. Its kernel is
strictly positive throughout the allowed energy band, including the endpoint
`-2`, so an elementary Perron argument gives a unique positive eigenvector.
Resolvent reconstruction then produces the desired eigenfunction.

Contents:

- `solution_packet.pdf` — proof packet for review;
- `source_paper.pdf` — locally compiled cached arXiv source;
- `figures/open_problem_crop.png` — exact question on source PDF page 9;
- `main.tex` — packet source;
- `verification.md` — line-by-line audit and reviewer focus.

Bounded local and external searches through 11 August 2026 found no later
paper explicitly answering the question. Novelty confidence is moderate; the
packet does not claim priority.
