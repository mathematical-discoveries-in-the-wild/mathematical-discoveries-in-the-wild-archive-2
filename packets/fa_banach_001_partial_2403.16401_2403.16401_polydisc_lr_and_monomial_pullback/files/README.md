# Two positive results for the measurable polydisc Douglas--Rudin problem

Status: **candidate substantial partial result; likely valid; human review
recommended**

Source: P. Kumar, S. Rastogi, and D. Tripathi, *Douglas--Rudin Approximation
theorem for operator-valued functions on the unit ball of C^d*,
arXiv:2403.16401 (2024), concluding question on PDF page 10.

## Results

1. For every `d >= 1`, every finite `0 < r < infinity`, and every measurable
   unimodular `f` on `T^d`, quotients of rational polydisc inner functions are
   dense at `f` in `L^r`.  There is also a sequence of such quotients converging
   to `f` almost everywhere.

2. The full essential-supremum conclusion holds whenever

   `f(zeta) = product_j g_j(zeta^(a_j))`,

   where the product is finite, each `g_j:T->T` is arbitrary measurable, and
   each nonzero `a_j` lies in `N_0^d`.  This includes every coordinate-separable
   measurable phase.

The first theorem combines measure regularity with McDonald's uniform theorem
for continuous phases.  The second applies the classical one-variable
Douglas--Rudin theorem and observes that composing an inner function with the
analytic monomial `z -> z^a` produces a polydisc inner function.

## Scope

The arbitrary measurable essential-supremum problem is not settled.  It
reduces to approximating arbitrary two-valued signs `2 chi_E - 1`; neither
finite-`L^r` approximation nor finite analytic-character separation controls
that case.  Eight focused upgrade attempts are recorded in
`runs/fa_banach_001/attempts/2403.16401_measurable_polydisc_uniform_gap_attempts.md`.

## Files

- `main.tex`, `solution_packet.pdf`: complete theorem statements and proofs.
- `source_paper.pdf`: current arXiv source PDF.
- `figures/open_problem_crop.png`: exact source question on PDF page 10.
- `verification.md`: line-by-line proof and scope audit.
