# Full-solution packet: power criterion for one-sided Drazin invertibility

Status: **candidate full resolution; likely valid; human review required**

Source: Kai Yan, *One-sided Drazin inverses in Banach algebras and
perturbations of B-Fredholm spectra*, arXiv:2402.13574.

## Question and result

Question 2.9 asks whether one-sided Drazin invertibility with index `n` is
equivalent to one-sided group invertibility of `a^n`.

For every `n >= 1`, the sharp statement is proved in every unital ring:

`a^n` is left group invertible if and only if `ind_L(a) <= n`,

and dually on the right. Equivalently, `a` admits a one-sided Drazin inverse
satisfying the defining equation at exponent `n`.

If “index `n`” means the minimal index is exactly `n`, the source statement is
literally false: `a=1` has index zero while every power is group invertible.
The printed `n=0` case is also false in general because `a^0=1` for every `a`.

## Proof mechanism

A left group inverse of `b=a^n` supplies an idempotent `e=xb`. Relative to
`e` and `p=1-e`, the element `a` is lower triangular with a left-invertible
upper block `A` and a nilpotent lower block `D`. An explicit finite Sylvester
sum removes the off-diagonal block by similarity. The left inverse of `A`,
extended by zero, then becomes a left Drazin inverse of `a` with exponent `n`.

## Files

- `main.tex`: self-contained ring-theoretic proof and index clarification.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_question_crop.jpg`: source page 8 crop with Question 2.9.
- `code/verify_block_conjugation.py`: exact symbolic verifier.
- `verification.md`: proof, source, novelty, and rendering audit.

Ledger: `runs/fa_banach_001/ledger/results/2402.13574_power_criterion_one_sided_drazin.json`.
