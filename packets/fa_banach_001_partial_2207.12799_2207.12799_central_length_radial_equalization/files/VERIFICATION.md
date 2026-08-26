# Verification

Status: `candidate_full_solution_central_length_subcase_likely_valid; general_noncommutative_problem_open`

## Mathematical checks

- The source uses the standard **left** module convention `<x,y> = sum_i x_i y_i^*`; every scalar multiplication and cross term in the packet follows that convention.
- Near equality makes every `p_j` positive and invertible because `0 < epsilon < 1`.
- Functional calculus directly verifies `<c p_j^(-1/2) tau_j, c p_j^(-1/2) tau_j> = d/n`.
- Inserting `c^2 p_j^(-1)` between `<x,tau_j>` and its adjoint gives the stated frame bounds by C*-order.
- Expanding the candidate's squared displacement gives exactly `(p_j^(1/2)-c)^2`; the spectral interval for `p_j` gives both displayed quantitative bounds.
- For a central `p_j`, C*-module Cauchy--Schwarz gives a contraction `q_j`; central multiplication preserves `q_j+q_j^* <= 2`, yielding the claimed positive-element lower bound for every equal-length competitor.
- No uniqueness claim is made, and no centrality-free optimality claim is made.

## Source and novelty checks

- arXiv:2207.12799, Definition 2.5 and Problem 2.10, contain the exact near-equal hypothesis and closest-frame question used here.
- Cheap-run indexes and exact-phrase/title/arXiv searches found no existing packet or later paper answering Problem 2.10.
- The appendix restricted-invertibility conjectures and the literally printed modular Johnson--Lindenstrauss statement are deliberately excluded: they are already handled by the run's GPT5.6 packet for arXiv:2208.05223.
- Eight materially distinct upgrade routes are recorded in `attempts/2207.12799_central_length_equalization_upgrade.md`.

## Reproducibility and presentation

- The official source PDF and a crop containing Definitions 2.5--2.7 and Problem 2.10 are included.
- `main.tex` was compiled twice with `pdflatex` without errors or layout diagnostics.
- The final PDF was text-extracted, rasterized, and visually inspected page by page.
