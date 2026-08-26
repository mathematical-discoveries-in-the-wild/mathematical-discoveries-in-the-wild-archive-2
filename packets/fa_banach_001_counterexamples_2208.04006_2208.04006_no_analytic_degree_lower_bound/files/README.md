# arXiv:2208.04006 — no analytic-degree lower bound from the Cauchy-weight degree

Status: `candidate_counterexample_likely_valid`

This packet gives a negative answer to the open statement at the end of
Section 6.2 of Armin Rainer, *Quantitative tame properties of differentiable
functions with controlled derivatives* (arXiv:2208.04006; Nonlinear Analysis
237 (2023), 113372).

For fixed `epsilon`, take the paper's Cauchy weight
`mu_j=C*j/epsilon`. Its degree `dfrak_{2mu}(epsilon)` is independent of the
function's distance from a constant. For the nonconstant entire functions
`f_delta(z)=1+delta*z`, however,

`d_fdelta(2epsilon) <= log((1+delta)/(1-delta))/log(4) -> 0`.

Thus no positive lower bound depending only on the Cauchy-weight degree can
hold, even after constants are excluded. Taking `epsilon_n=exp(-n)` makes the
weight degrees unbounded because they are at least `n`.

Files:

- `main.tex`: formal counterexample and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: printed page 25 containing the statement.
- `code/check_near_constant.py`: independent arithmetic check.
- `verification.md`: proof audit, novelty record, and review focus.

The counterexample addresses the question exactly as printed. A reverse
comparison might become possible after a quantitative nonconstancy
normalization or with a minimal function-adapted weight.
