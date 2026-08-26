# Entropy factorization on every `l_p` sphere

Candidate full solution to Conjecture 1 in arXiv:2407.13457.

The packet proves the conjectured arbitrary-block entropy factorization for
cone measure on `S_p^{n-1}` for every `p>0`. The proof is stronger: every
symmetrized Dirichlet law with arbitrary positive parameters satisfies the
same inequality with pair-coverage constant `theta_**`.

The key mechanism is an exact entropy-chain decomposition. The magnitudes are
Dirichlet and obey a 2011 Brascamp-Lieb/entropy inequality; the signs form an
independent product space and obey ordinary Shearer. Convexity of conditional
entropy fits those two estimates into each joint block update, eliminating the
regularization obstruction in the source paper.

## Files

- `solution_packet.pdf`: compiled proof packet.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: official arXiv PDF for arXiv:2407.13457.
- `supporting_paper_0907.2858.pdf`: decisive Dirichlet Brascamp-Lieb source.
- `figures/open_problem_crop.png`: readable crop of Conjecture 1 on page 16.
- `code/crop_source.py`: deterministic crop script.
- `code/verify_quadrature.py`: deterministic sign-dependent quadrature QA.
- `verification_report.md`: adversarial mathematical and artifact audit.

## Scope

The result proves the stated lower bound. It does not claim that the constant
is optimal for every `p` and every block-weight vector. Novelty remains
provisional pending expert review.
