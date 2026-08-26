# Complex continuous normal convex-cyclic operator

Status: `literature_implied_answer (complex continuous-normal subproblem)`

Source: T. Bermudez, A. Bonilla, and N. Feldman, *On convex-cyclic
operators*, arXiv:1410.4664, Section 7, Question 2 (locally rendered page 17).

Supporting theorem: N. S. Feldman and P. J. McGuire, *A Convex
Stone-Weierstrass Theorem & Applications*, arXiv:1510.08878, Theorem 7.1
(locally rendered page 13).

The packet proves that multiplication by `ir` on complex
`L^2([a,b],mu)`, where `1<a<b` and `mu` is nonatomic, is normal,
continuous, and convex-cyclic. The vector `1` is convex-cyclic. Even powers
reduce to the later paper's real convex-polynomial theorem on
`[-b^2,-a^2]`; odd powers supply the imaginary direction.

This settles the continuous-normal existence alternative on a complex Hilbert
space. It does not settle the pure-hyponormal alternative or the other open
questions in Section 7.

Files:

- `solution_packet.pdf`: review packet
- `source_paper.pdf`: arXiv:1410.4664, rendered from the archived arXiv source
- `supporting_paper_1510.08878.pdf`: supporting theorem, likewise rendered
- `figures/open_problem_crop.png`: source Question 2
- `code/check_even_odd_reduction.py`: exact structural check

Human review: likely valid; verify the even/odd complexification and the
conservative literature-implied classification.
