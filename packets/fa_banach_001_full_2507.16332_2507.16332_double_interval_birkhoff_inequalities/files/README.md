# Hölder and Minkowski inequalities in the doubly interval-valued Birkhoff setting

Status: candidate_full_solution_likely_valid

This packet answers the conclusion question in arXiv:2507.16332, where both
the integrand F=[f_-,f_+] and the set function M=[nu_-,nu_+] are
interval-valued.

The key identity is an exact endpoint factorization:

    integral F dM = [integral f_- dnu_-, integral f_+ dnu_+].

Consequently, for positive conjugate exponents p,q>1, Hölder holds in the
weak interval order, and Minkowski holds for p>=1. For 0<p<1, Minkowski
reverses. These statements follow componentwise from the scalar theorems in
the source.

The reverse Hölder regime q=p/(p-1)<0 has an additional interval-arithmetic
obstruction. The naive natural interval q-gauge fails already on a one-atom
additive example: for p=1/2 and M=[1,4], the desired comparison would require
[1,4] to dominate [1/4,16]. The packet gives two sharp repairs:

- an unconditional endpointwise diagonal-hull reverse Hölder inequality;
- a natural-gauge inequality with optimal factor C^(1/q) whenever
  nu_+ <= C nu_-.

There is no positive width-independent natural-gauge factor.

Files:

- main.tex: full endpoint theorem, inequalities, counterexample, and sharp repair.
- solution_packet.pdf: rendered proof packet.
- source_paper.pdf: locally compiled arXiv:2507.16332 source.
- figures/open_problem_crop.png: the exact conclusion question.
- code/verify_finite_models.py: randomized finite-atomic and exact obstruction checks.
- tmp/: build and rendering intermediates.
