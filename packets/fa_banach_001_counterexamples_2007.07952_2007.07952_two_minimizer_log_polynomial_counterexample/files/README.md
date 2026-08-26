# Two minimizing log-polynomials in every even degree at least eight

Status: `candidate full negative answer (likely valid; human review requested)`

Source/open question:

- David Alonso-Gutiérrez, Bernardo González Merino, and Rafael Villa,
  *Best approximation of functions by log-polynomials*, arXiv:2007.07952,
  Journal of Functional Analysis 280 (2021), 108999.
- On PDF page 4, after Theorem 1.1, the authors say that uniqueness in
  Problem 1 is not known in general and that they know no example with a
  nonunique minimization point.

Candidate result:

The answer is negative. For every even `d >= 8`, the packet constructs an even,
normalized, integrable log-concave function `f` on `R^2` for which Problem 1
has exactly two minimizing pairs `(t,g)`.

The construction starts from two rotated degree-`d` polynomial norms

`p_+^d = rho^d(1 + epsilon cos(d theta))`,

`p_-^d = s^d rho^d(1 - epsilon cos(d theta))`,

where `s=((1+epsilon)/(1-epsilon))^(1/d)`. Their dual unit balls are joined by
a nested piecewise-Minkowski family and realized as the sublevel sets of the
convex conjugate of `-log f`. Dihedral symmetry reduces each fixed-height
Lasserre optimizer to `A+B cos(d theta)`. Concavity of a power mean identifies
the optimizer exactly, and a uniform second-order expansion shows that the
weighted volume is strictly larger between the two endpoints when `d>=8` and
`epsilon` is sufficiently small. Outside that segment it is strictly
monotone. The endpoints therefore give exactly two global minimizers.

Novelty check:

A bounded search on 2026-08-13 covered the run registry/attempt/solution
indexes, the exact arXiv id and title, and arXiv/web searches combining the
title, authors, `d-Lasserre-Löwner`, log-polynomial, uniqueness, and
nonunique-minimizer phrases. It found the source paper and adjacent Lasserre
work, but no later answer or counterexample. This does not prove novelty;
specialist review is still required.

Files:

- `solution_packet.pdf`: self-contained proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source-page image containing the question.
- `code/verify_expansion.py`: symbolic and numerical sanity checks (not used as
  proof).

Human review recommendation: focus on the realization lemma for the nested
polar family, the invariant-polynomial reduction, the endpoint-chord
optimality, and the uniform division of the analytic remainder by
`lambda(1-lambda)`.

