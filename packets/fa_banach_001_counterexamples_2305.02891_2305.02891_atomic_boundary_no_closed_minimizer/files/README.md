# Atomic-boundary minimizer with no closed representative

Status: candidate_counterexample_likely_valid

Source: Jesse Koivu, Danka Lučić, and Tapio Rajala, *Approximation by
BV-extension sets via perimeter minimization in metric spaces*,
arXiv:2305.02891, Question 5.2.

## Result

Question 5.2 asks whether a Borel minimizer of either

- M_lambda(A) = Per(A) + lambda m(Omega minus A), or
- Mtilde_lambda(A) = Per(A) + lambda m(Omega Delta A)

must have a closed representative.

The answer is no for both functionals. Take

X = R, m = Lebesgue + delta_0 + delta_1, Omega = (0,1), and any
lambda at least 2.

The interval has perimeter exactly two. Every positive-Lebesgue-measure set
which excludes both endpoint atoms has perimeter at least two: any Lipschitz
relaxation must rise from value zero at the atom at 0 to nearly one at an
interior point, then fall back to zero at the atom at 1. All remaining
competitors pay fidelity at least lambda. Thus Omega minimizes both
functionals.

Yet Omega has no closed representative. A closed representative must omit
0 and 1 because the atoms there have positive mass; omitting 0 while remaining
closed forces omission of a whole interval (0,r), which has positive
Lebesgue measure.

## Scope and novelty

The counterexample lies outside the PI class, as allowed by Question 5.2. The
source already gives a positive result for the symmetric-difference
functional in PI-spaces.

A bounded search of the run indexes, exact question wording, the published
IMRN article, and arXiv:2503.15716 found no later answer. Novelty confidence is
bounded, not definitive.

## Packet contents

- main.tex, solution_packet.pdf: complete counterexample and proof.
- source_paper.pdf: arXiv:2305.02891.
- figures/open_problem_crop.png: Question 5.2 on PDF page 17.
- VERIFICATION.md: mathematical and rendering audit.

Human review should focus on the relaxed-perimeter lower bound.
