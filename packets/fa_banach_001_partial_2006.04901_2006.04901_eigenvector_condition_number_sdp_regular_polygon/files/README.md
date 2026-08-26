# 2006.04901 — exact SDP and regular-polygon condition numbers

Status: `candidate major partial result; likely valid; pending human review`

Source: Kelly Bickel, Pamela Gorkin, Anne Greenbaum, Thomas Ransford,
Felix L. Schwenninger, and Elias Wegert, *Crouzeix's Conjecture and Related
Problems*, arXiv:2006.04901, Question 1.1.

The packet gives an exact, ordering-free answer in optimization form for every
finite Blaschke product with distinct zeros. If `G` is the normalized
Szego-kernel Gram matrix of the zeros, then

`eta(M_Theta)^2 = min { t : P <= G <= tP for some positive diagonal P }`.

It also proves two closed-form consequences:

- for two distinct zeros at pseudohyperbolic distance `rho`, with
  `c=sqrt(1-rho^2)`, one has
  `eta=(1+c)/rho=sqrt((1+c)/(1-c))`;
- if the zeros form a regular pseudohyperbolic `n`-gon, equivalently they are a
  disk-automorphic image of `{r omega^j : 0<=j<n}`, then
  `eta=r^(-(n-1))`.

The degree-two formula also yields a sharp pairwise lower bound in every
degree. For the regular polygon, the source paper's sufficient test
`eta<=2` is therefore exact precisely when `r>=2^(-1/(n-1))`.

The packet does **not** give an elementary scalar formula for a generic zero
configuration; the exact remaining problem is diagonal semidefinite
equilibration of `G`.

Files:

- `main.tex`, `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: Question 1.1 on source page 4.
- `code/verify_condition_numbers.py`: numerical algebra checks.
- `verification.md`: proof, literature, build, and visual audit.
