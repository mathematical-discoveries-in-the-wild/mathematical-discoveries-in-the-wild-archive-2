# Parabolic counterexample to the Gaussian Neumann-to-Dirichlet condition

Status: `counterexample_likely_valid`.

Source: Alexander V. Kolesnikov and Emanuel Milman, *Sharp Poincare-type
inequality for the Gaussian measure on the boundary of convex sets*,
arXiv:1601.02925v2, Question 3.4 (page 11).

## Result

The answer to Question 3.4 is negative. There are compact `C-infinity`
strictly convex ellipses `K` in `R^2` and smooth Neumann data `f` for which
condition (3.2) fails with

`F(v)=1/v-(log I_gamma)'(v)`.

The ellipses can be chosen to have Gaussian measure `1/2`. For the associated
solution `Lu=1`, the questioned right-hand boundary expression equals

`integral_K (||Hess u||^2+|grad u|^2) d gamma_2 < 1/2`,

whereas the proposed lower bound is exactly `F(1/2)(1/2)^2=1/2`.

## Idea

Start from the sharp halfspace at Gaussian volume `1/2`. If
`w=Phi/phi` and `rho(y)=(1-y^2)/sqrt(2)`, then `L_x w'=2w'` while
`L_y rho=-2rho`. Thus the perturbation `w'(x)rho(y)` is `L`-harmonic and
can be added to a particular solution of `Lu=1`.

On the volume-preserving parabolic perturbation

`x<c(epsilon)+epsilon rho(y)`,

the optimized energy has the exact expansion

`1/2-(4-pi)^2 epsilon^2/(16pi)+o(epsilon^2)`.

The negative coefficient is the Cauchy-Schwarz defect that is absent in one
dimension. Large translated ellipses converge to the parabolic domain in
Gaussian volume and energy, so the strict deficit persists for finite compact
strictly convex ellipses.

## Files

- `main.tex`: complete proof and compactification argument.
- `VERIFICATION.md`: independent proof audit and verifier verdict.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:1601.02925v2.
- `figures/open_problem_crop.png`: source Question 3.4.
- `figures/condition_3_2_crop.png`: the condition referenced by the question.
- `code/check_second_variation_and_ellipses.py`: symbolic-constant and
  numerical ellipse checks; the proof does not depend on floating-point data.
- Ledger: `runs/fa_banach_001/ledger/results/1601.02925_gaussian_neumann_to_dirichlet_parabolic_counterexample.json`.

## Novelty Check

The run indexes were searched for arXiv:1601.02925, the exact title,
Gaussian Neumann-to-Dirichlet terminology, and the fixed-source Hessian-energy
formulation. Web and arXiv searches on 2026-08-09 used the exact question
title and close variants. They found the source paper but no later resolution
or this parabolic construction. The new arXiv:2608.05390 was also inspected
because it uses Gaussian Neumann Hessian-energy localization; it optimizes a
freely selected source and does not answer this fixed-constant-source question.
This was a bounded, not exhaustive, novelty search.

## Human Review

Recommended focus: verify the second-variation bookkeeping and the final
dominated-convergence passage from the unbounded parabola to volume-normalized
ellipses. The exact coefficient and several finite ellipses were independently
checked by the included script.
