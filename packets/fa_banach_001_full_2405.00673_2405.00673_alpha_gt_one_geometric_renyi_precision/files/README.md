# Optimal precision for geometric Rényi quasi-entropy when alpha > 1

Status: `candidate_full_solution_likely_valid`; `human_review_recommended`.

Source: Nana Liu, Qisheng Wang, Mark M. Wilde, and Zhicheng Zhang,
*Quantum algorithms for matrix geometric means*, arXiv:2405.00673; npj
Quantum Information 11 (2025), Article 101.  The open problem appears after
Lemma 20 on source PDF page 24.

## Result

For every fixed `alpha in (1,2]`, any quantum algorithm that estimates the
geometric Rényi relative quasi-entropy

```text
Fhat_alpha(rho,sigma) = Tr(sigma #_alpha rho)
```

to additive error `epsilon` from purification oracles requires
`Omega_alpha(1/epsilon)` queries, even for commuting qubit states satisfying
`rho,sigma >= I/4`.  This matches the source's
`O-tilde_alpha(1/epsilon)` upper bound and answers its open problem
affirmatively, including the endpoint `alpha=2`.

The same hard pair gives two strengthenings:

- estimating the logarithmic geometric Rényi entropy also requires
  `Omega_alpha(1/epsilon)` queries;
- estimating either quantity from copies alone requires
  `Omega_alpha(1/epsilon^2)` copies.

## Proof mechanism

The source already uses the Bernoulli pair
`rho_t=diag((1+t)/2,(1-t)/2)` and `rho_2t`, together with the fixed state
`eta=diag(1/4,3/4)`, for `alpha<1`.  On this commuting family the target is a
scalar function `g_alpha(t)`.  Its derivative at zero is nonzero for every
`alpha != 1`.  For `alpha>1` its sign is the reverse of the sign used in the
source, but a query lower-bound reduction only needs absolute separation.
Reversing the decision threshold yields a linear output gap while the two
purification oracles remain only `O(t)` apart in Hellinger distance.

## Novelty boundary

The current arXiv revision and the published 2025 article still state the
`alpha in (1,2]` case as open.  Searches of the run indexes, exact problem
wording, title citations, and geometric-Rényi quantum-query terminology found
no later solution through 17 August 2026.  Because the repair is elementary
and close to the source proof, expert novelty and model-convention review is
recommended despite the strong bounded search.

## Files

- `main.tex` and `solution_packet.pdf`: self-contained proof packet.
- `source_paper.pdf`: source paper compiled from the cached arXiv source.
- `figures/open_problem_crop.png`: source PDF page 24 crop.
- `code/check_hard_instance.py`: finite numerical derivative and gap check.

Run the numerical check with:

```sh
python3 code/check_hard_instance.py
```

Build the packet with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
```

