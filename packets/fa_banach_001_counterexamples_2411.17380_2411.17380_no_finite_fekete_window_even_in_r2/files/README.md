# No finite Fekete window, even in the Euclidean plane

Status: candidate full negative answer to Question 3.2 of arXiv:2411.17380,
likely valid pending expert review.

Kulikov and Shao ask whether, for a uniformly convex Banach space `X`, some
function `f:N->N` can force convergence of `v_n/n` when the vector-valued
Fekete inequality is assumed only for `n <= m <= f(n)`. The answer is no,
already for `X=R^2` with its Euclidean norm.

For an arbitrary proposed `f`, the construction divides the integers into
recursively separated finite blocks so every allowed pair lies in the same or
the next block. Directions rotate by the nonsummable increments `c/k`, while
the radii carry the summable slack `2c^2 sum_(j>=k) 1/j^2`. The radial slack
between adjacent blocks exactly dominates the quadratic cosine loss. Hence all
required inequalities hold, but `v_n/n` keeps rotating and cannot converge.

Files:

- `solution_packet.pdf`: complete review packet.
- `source_paper.pdf`: arXiv:2411.17380v1.
- `figures/open_problem_crop.png`: source screenshot of Question 3.2.
- `main.tex`: self-contained proof source.
- `verification.md`: proof audit, numerical scope, and novelty check.
- `code/verify_construction.py`: finite sanity checks for the block formula.

Human review recommendation: check the adjacent-block budget estimate and the
recursive quantifier step `m <= f(n) < N_(k+2)`. No external theorem beyond
elementary Euclidean geometry and divergence/convergence of the harmonic and
square-harmonic series is used.
