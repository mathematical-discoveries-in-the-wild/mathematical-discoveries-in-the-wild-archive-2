# A nodal Gaussian obstruction to the adaptive fixed-point equation

This packet gives an exact counterexample to universal well-posedness of the implicit adaptation equation in arXiv:1805.00703 and a substantial partial answer to its open classification problem.

For the admissible Schwartz function

`f(x) = x exp(-a x^2/2)`, `a > 0`,

the proposed iteration at `x=0`, written in the squared variable `s_n = mu_n(0)^2`, is exactly

`s_(n+1) = 3a/2 + (3 lambda^2/2) s_n`.

Consequently, the implicit equation has a positive solution and this pointwise iteration converges from every positive start exactly when `lambda^2 < 2/3`. At and above `lambda^2 = 2/3`, there is no positive solution at the node. This includes `lambda=1`, inside the paper's empirically favorable interval `[0.6,1.2]`.

The packet generalizes the calculation to every Gaussian monomial `x^m exp(-a x^2/2)`, obtaining the sharp nodal threshold

`lambda^2 < (4m-2)/(4m-1)`.

It also proves that for the first nodal Gaussian, below `2/3`, the implicit equation has a unique positive solution at every spatial point. Convergence of the raw iteration at every nonzero spatial point is not claimed.

Files:

- `main.tex`, `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: arXiv:1805.00703.
- `figures/open_problem_crop.png`: the source's fixed-point iteration and open-problem remark on PDF page 13.
- `code/verify_gaussian_monomial.py`: exact symbolic verification of the core recurrence.
- `tmp/`: build and rendering artifacts.

Novelty confidence is moderate. Bounded primary-source searches found no later analysis of this exact obstruction.
